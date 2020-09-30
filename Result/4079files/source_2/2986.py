from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial', app_label='library')


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]