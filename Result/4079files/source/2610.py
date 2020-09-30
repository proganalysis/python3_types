import os.path

from psycopg2 import DatabaseError
from yoyo import read_migrations
from yoyo.connections import exceptions

from misc.deploy import Application
from microservice import components


class Microservice(Application):

    def _check(self):
        """
        We need config file to run the app. Should be probably provisioned by Puppet or sth like that.
        :return: None
        """
        current_dir = os.path.dirname(__file__)
        if not os.path.isfile(os.path.join(current_dir, 'config', 'config.yaml')):
            raise RuntimeError('config/config.yaml is missing.')

    def _after_deploy(self):
        """
        Runs build after deploying. Make clean is run to prune all env, pyc, pyo and other files.
        Code should be probably pulled by git. Or not?
        :return: None
        """
        version_path = os.path.join(self._get_app_path(), 'releases', self._version)
        self._perform_ssh_command('cd {} && make clean && make'.format(version_path))
        self._do_migrations()

    def _after_promote(self):
        """
        Creates symlink to the last deploy. Also restarts gunicorn.
        :return: None
        """
        current_path = os.path.join(self._get_app_path(), 'releases', 'current')
        pid_file = os.path.join(self._get_app_path(), 'releases', 'gunicorn.pid')
        self._perform_ssh_command(
            'kill -HUP $(cat {} 2>>/dev/null)  2>>/dev/null || '
            '(cd {}; ./env/bin/gunicorn microservice.main:application -D -p {})'.
            format(pid_file, current_path, pid_file))

    @staticmethod
    def _do_migrations():
        current_dir = os.path.dirname(__file__)
        migrations_dir = os.path.join(current_dir, 'migrations')
        conn = components.get_psql()
        exceptions.register(DatabaseError)
        migrations = read_migrations(conn, 'pyformat', migrations_dir)
        migrations.to_apply().apply()
        conn.commit()

if __name__ == '__main__':
    print('Deploy started, brace yourselves.')
    microservice = Microservice('127.0.0.1', 'microservice', 'chmelda')
    microservice.process()
    microservice.close()
    print('Done.')
