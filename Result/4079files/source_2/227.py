# Copyright (C) 2017  Daniel Watkins <daniel@daniel-watkins.co.uk>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import inspect
import json
import os
import socket
import subprocess
import time
from collections import namedtuple
from glob import iglob

import pytest
import yaml


def get_available_port():
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


def _generate_jjb_config(url=None, password='XXX'):
    if url is None:
        url = 'http://0.0.0.0:{}/'.format(get_available_port())

    return '''\
[job_builder]
ignore_cache=True

[jenkins]
url={}
user=admin
password={}
'''.format(url, password)


class IntegrationTestRunner:

    def run_test_command(self, command):
        success = True
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            output = exc.output
            success = False
        return success, output.decode('utf-8')


class ActualJenkinsRunner(IntegrationTestRunner):

    def __init__(self, image_name):
        self.container_id = None
        self.image_name = image_name

    def check_docker_output(self, args):
        return subprocess.check_output(
            ['docker'] + args).decode('utf-8').strip()

    def do_retry(self, func):
        start_time = time.time()
        while time.time() < start_time + 30:
            try:
                return func()
            except subprocess.CalledProcessError:
                time.sleep(1)
        else:
            self.check_docker_output(['logs', self.container_id])
            raise Exception('Retrying failed')

    def _run_test_without_cleanup(self, tmpdir, config):
        # Set up Jenkins running in a Docker container
        self.container_id = self.check_docker_output(
            ['run', '-d', self.image_name])
        inspect_output = json.loads(
            self.check_docker_output(['inspect', self.container_id]))
        url = 'http://{}:8080'.format(
            inspect_output[0]['NetworkSettings']['IPAddress'])

        password = self.do_retry(
            lambda: self.check_docker_output(
                ['exec', self.container_id,
                 'cat', '/var/jenkins_home/secrets/initialAdminPassword']))

        # Write out a config file pointing to our Docker Jenkins
        conf_file = tmpdir.join('config.ini')
        config = '\n'.join(
            [_generate_jjb_config(url=url, password=password),
                config or ''])
        conf_file.write(config)

        # Update the running Jenkins from our job configuration
        config_args = ['--conf', str(conf_file)]

        self.do_retry(
            lambda: subprocess.check_output(
                ['jenkins-jobs'] + config_args + ['update', tmpdir]))

        # Lint the jobs from the running Jenkins
        return self.run_test_command(
            ['jenkins-job-linter'] + config_args
            + ['lint-jenkins', '--jenkins-url', url,
               '--jenkins-username', 'admin',
               '--jenkins-password', password])

    def run_test(self, tmpdir, config):
        if not subprocess.call(['which', 'docker']) == 0:
            pytest.fail(
                'Docker not installed, but is required for integration tests')
        try:
            return self._run_test_without_cleanup(tmpdir, config)
        finally:
            if self.container_id is not None:
                self.check_docker_output(['kill', self.container_id])


class DirectRunner(IntegrationTestRunner):

    def run_test(self, tmpdir, config):
        output_dir = os.path.join(tmpdir, 'output')
        subprocess.check_call([
            'jenkins-jobs', 'test', os.path.join(tmpdir), '-o', output_dir])
        config_args = []
        if config is not None:
            conf_file = tmpdir.join('config.ini')
            conf_file.write(config)
            config_args = ['--conf', str(conf_file)]
        return self.run_test_command(
            ['jenkins-job-linter'] + config_args + ['lint-directory',
                                                    output_dir])


class JJBSubcommandRunner(IntegrationTestRunner):

    def run_test(self, tmpdir, config):
        conf_file = tmpdir.join('config.ini')
        config = '\n'.join([_generate_jjb_config(), config or ''])
        conf_file.write(config)
        return self.run_test_command([
            'jenkins-jobs', '--conf', str(conf_file),
            'lint', os.path.join(tmpdir)])


@pytest.fixture(params=[
    pytest.param('actual_jenkins', marks=pytest.mark.docker),
    'direct',
    'jjb_subcommand',
])
def runner(request):
    runners_to_skip = request.getfixturevalue(
        'integration_testcase').runners_to_skip
    if runners_to_skip and request.param in runners_to_skip:
        pytest.skip('unsupported runner')
    runner_funcs = {
        'actual_jenkins': ActualJenkinsRunner(
            request.session.config.getvalue('jenkins_docker')),
        'direct': DirectRunner(),
        'jjb_subcommand': JJBSubcommandRunner(),
    }
    return runner_funcs[request.param]


def test_integration(runner, tmpdir, integration_testcase):
    tmpdir.join('jobs.yaml').write(integration_testcase.jobs_yaml)
    success, output = runner.run_test(tmpdir, integration_testcase.config)
    assert integration_testcase.expected_output == output
    assert integration_testcase.expect_success == success


IntegrationTestcase = namedtuple(
    'IntegrationTestcase',
    ['test_name', 'jobs_yaml', 'expected_output', 'expect_success', 'config',
     'runners_to_skip'])


def _get_case_item(key, case_dict, defaults, required=True):
    value = case_dict.get(key, None)
    if value is not None:
        return value
    if required:
        return defaults[key]
    return defaults.get(key, None)


def _parse_case(case_dict, defaults):
    if 'description' not in case_dict:
        raise Exception('Test {} has no description'.format(case_dict['name']))
    return IntegrationTestcase(
        case_dict['name'],
        _get_case_item('jobs.yaml', case_dict, defaults),
        _get_case_item('expected_output', case_dict, defaults),
        _get_case_item('expect_success', case_dict, defaults),
        _get_case_item('config', case_dict, defaults, required=False),
        _get_case_item('runners_to_skip', case_dict, defaults, required=False),
    )


def _parse_testcases(filenames):
    names = set()
    for filename in filenames:
        with open(filename) as f:
            data = yaml.safe_load(f)
        defaults = data.get('defaults', {})
        for case_dict in data['cases']:
            testcase = _parse_case(case_dict, defaults)
            if testcase.test_name in names:
                raise Exception(
                    'Duplicate test name: {}'.format(testcase.test_name))
            names.add(testcase.test_name)
            yield testcase


def pytest_generate_tests(metafunc):
    test_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    test_cases = _parse_testcases(iglob(os.path.join(test_dir, 'test_*.yaml')))
    if 'integration_testcase' in metafunc.fixturenames:
        metafunc.parametrize('integration_testcase', test_cases,
                             ids=lambda testcase: testcase.test_name)
