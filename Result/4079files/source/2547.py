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
import configparser

import pytest

from jenkins_job_linter.config import (
    _filter_config,
    _get_default_linter_configs,
)
from jenkins_job_linter.linters import Linter

from .mocks import create_mock_for_class


class TestGetDefaultLinterConfigs:

    def test_no_linters_returns_empty_dict(self, mocker):
        mocker.patch('jenkins_job_linter.config.LINTERS', {})
        assert {} == _get_default_linter_configs()

    def test_with_linters(self, mocker):
        default_config = {'key': 'value', 'other_key': ['some', 'values']}
        linter_with_config = create_mock_for_class(
            Linter, default_config=default_config)
        mocker.patch('jenkins_job_linter.config.LINTERS', {
            'no_config': create_mock_for_class(Linter),
            'some_config': linter_with_config,
        })
        assert {
            'job_linter:no_config': {},
            'job_linter:some_config': default_config,
        } == _get_default_linter_configs()


class TestFilterConfig:

    def test_filter_by_prefix(self, mocker):
        mocker.patch('jenkins_job_linter.config.GLOBAL_CONFIG_DEFAULTS', {})
        mocker.patch('jenkins_job_linter.config.LINTERS', {})
        config = configparser.ConfigParser()
        wont_filter = ['job_linter', 'job_linter:linter', 'job_linter-thing']
        will_filter = ['jenkins', 'jenkins_jobs', 'whatever-else']
        config.read_dict({k: {} for k in wont_filter + will_filter})
        filtered_config = _filter_config(config)
        assert set(wont_filter) == set(filtered_config.sections())

    @pytest.mark.parametrize('expected,option_content', (
        ([], ''),
        (['eggs'], 'eggs'),
        (['eggs', 'spam'], 'eggs,spam'),
        (['eggs', 'spam'], 'eggs, spam'),
        (['eggs', 'spam'], '   eggs, spam   '),
        (['eggs', 'spam'], '   eggs,\nspam   '),
    ))
    def test_returned_configparser_getlist(
            self, expected, mocker, option_content):
        mocker.patch('jenkins_job_linter.config.GLOBAL_CONFIG_DEFAULTS', {})
        mocker.patch('jenkins_job_linter.config.LINTERS', {})
        config = configparser.ConfigParser()
        config.read_dict({'job_linter': {'opt': option_content}})
        filtered_config = _filter_config(config)
        assert expected == filtered_config.getlist('job_linter', 'opt')

    def test_sectionproxy_getlist(self, mocker):
        mocker.patch('jenkins_job_linter.config.GLOBAL_CONFIG_DEFAULTS', {})
        mocker.patch('jenkins_job_linter.config.LINTERS', {})
        config = configparser.ConfigParser()
        config.read_dict({'job_linter': {'opt': 'content'}})
        filtered_config = _filter_config(config)
        assert ['content'] == filtered_config['job_linter'].getlist('opt')
