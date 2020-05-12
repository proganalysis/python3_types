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
import itertools
from xml.etree import ElementTree

import pytest

from jenkins_job_linter.linters import (
    CheckColumnConfiguration,
    CheckEnvInject,
    CheckForEmptyShell,
    CheckJobReferences,
    CheckShebang,
    EnsureTimestamps,
    EnsureWorkspaceCleanup,
    Linter,
    LintResult,
)
from jenkins_job_linter.models import LintContext, RunContext

from .mocks import get_config

FAILING_SHEBANG_ARGS = ['e', 'u', 'x'] + list(itertools.combinations('eux', 2))
PASSING_SHEBANG_ARGS = itertools.permutations('eux')


def _elementtree_from_str(xml_string: str) -> ElementTree.ElementTree:
    return ElementTree.ElementTree(ElementTree.fromstring(xml_string))


class ShellTest:

    _xml_template = '''\
        <project>
            <builders>
                {builders}
            </builders>
        </project>'''

    _shell_builder_template = '''\
        <hudson.tasks.Shell>
            <command>{shell_script}</command>
        </hudson.tasks.Shell>'''

    def test_non_project_skipped(self):
        tree = _elementtree_from_str('<not_project/>')
        linter = CheckForEmptyShell(LintContext({}, None, tree))
        result, text = linter.check()
        assert result is LintResult.SKIP
        assert text is None


class TestCheckShebang(ShellTest):

    @pytest.mark.parametrize('expected,shell_string', [
        (LintResult.PASS, 'no-shebang-is-fine'),
        (LintResult.FAIL, '#!/bin/sh -lolno'),
        (LintResult.FAIL, '#!/bin/zsh'),
        (LintResult.PASS, '#!/usr/bin/env python'),
        (LintResult.PASS, ''),
    ] + [(LintResult.FAIL, '#!/bin/sh -{}'.format(''.join(args)))
         for args in FAILING_SHEBANG_ARGS] +
        [(LintResult.PASS, '#!/bin/sh -{}'.format(''.join(args)))
         for args in PASSING_SHEBANG_ARGS]
    )
    def test_project_with_shell(self, expected, shell_string):
        xml_string = self._xml_template.format(
            builders=self._shell_builder_template.format(
                shell_script=shell_string))
        tree = _elementtree_from_str(xml_string)
        linter = CheckShebang(
            LintContext(get_config()['job_linter:check_shebang'], None, tree))
        result, _ = linter.check()
        assert result is expected

    def test_project_with_no_shell_part_skipped(self):
        tree = _elementtree_from_str('<project/>')
        linter = CheckShebang(LintContext({}, None, tree))
        result, _ = linter.actual_check()
        assert result is LintResult.SKIP

    @pytest.mark.parametrize('expected,shebangs', (
        (LintResult.PASS, ('#!/bin/sh -eux', '#!/usr/bin/env python3')),
        (LintResult.FAIL, ('#!/bin/sh -eux', '#!/bin/sh')),
        (LintResult.FAIL, ('#!/bin/sh', '#!/bin/sh -eux'))
    ))
    def test_multiple_shell_parts(self, expected, shebangs):
        builders = ''.join(
            self._shell_builder_template.format(shell_script=shebang)
            for shebang in shebangs)
        tree = _elementtree_from_str(self._xml_template.format(
            builders=builders))
        linter = CheckShebang(
            LintContext(get_config()['job_linter:check_shebang'], None, tree))
        result, _ = linter.check()
        assert result is expected

    def test_allow_default_shebang_false(self):
        tree = _elementtree_from_str(
            self._xml_template.format(
                builders=self._shell_builder_template.format(
                    shell_script='just some code')))
        config = configparser.ConfigParser()
        config.read_dict({
            'job_linter:check_shebang': {'allow_default_shebang': 'false'}})
        linter = CheckShebang(
            LintContext(config['job_linter:check_shebang'], None, tree))
        result, _ = linter.check()
        assert result == LintResult.FAIL

    @pytest.mark.parametrize('expected,required,shell_string', [
        (LintResult.PASS, '', '#!/bin/sh'),
        (LintResult.FAIL, 'e', '#!/bin/sh'),
        (LintResult.FAIL, 'e', '#!/bin/sh not options'),
        (LintResult.PASS, 'e', '#!/bin/sh -e'),
        (LintResult.PASS, 'ex', '#!/bin/sh -ex'),
        (LintResult.PASS, 'ex', '#!/bin/sh -xe'),
        (LintResult.PASS, 'ex', '#!/bin/sh -xeu'),
    ])
    def test_required_shell_options(self, expected, required, shell_string):
        xml_string = self._xml_template.format(
            builders=self._shell_builder_template.format(
                shell_script=shell_string))
        config = configparser.ConfigParser()
        config.read_dict({
            'job_linter:check_shebang': {'required_shell_options': required}})
        tree = _elementtree_from_str(xml_string)
        linter = CheckShebang(
            LintContext(config['job_linter:check_shebang'], None, tree))
        result, _ = linter.check()
        assert result is expected


class TestCheckForEmptyShell(ShellTest):

    @pytest.mark.parametrize('expected,script', (
        (LintResult.FAIL, ''), (LintResult.PASS, '...')))
    def test_linter(self, expected, script):
        tree = _elementtree_from_str(
            self._xml_template.format(
                builders=self._shell_builder_template.format(
                    shell_script=script)))
        linter = CheckForEmptyShell(LintContext({}, None, tree))
        result, _ = linter.check()
        assert result is expected


class TestEnsureTimestamps:

    @pytest.mark.parametrize('expected,xml_string', (
        (LintResult.SKIP, '<not_a_project/>'),
        (LintResult.FAIL, '<project/>'),
        (LintResult.PASS, '''\
            <project>
                <buildWrappers>
                    <hudson.plugins.timestamper.TimestamperBuildWrapper />
                </buildWrappers>
            </project>''')))
    def test_linter(self, expected, xml_string):
        tree = _elementtree_from_str(xml_string)
        linter = EnsureTimestamps(LintContext({}, None, tree))
        result, _ = linter.check()
        assert result is expected


class TestEnsureWorkspaceCleanup:

    @pytest.mark.parametrize('expected,xml_string', (
        (LintResult.SKIP, '<not_a_project/>'),
        (LintResult.FAIL, '<project/>'),
        (LintResult.PASS, '''\
            <project>
                <buildWrappers>
                    <hudson.plugins.ws__cleanup.PreBuildCleanup />
                </buildWrappers>
            </project>''')))
    def test_linter(self, expected, xml_string):
        tree = _elementtree_from_str(xml_string)
        linter = EnsureWorkspaceCleanup(LintContext({}, None, tree))
        result, _ = linter.check()
        assert result is expected


class TestCheckJobReferences:

    _trigger_builder_template = """\
<project>
    <builders>
        <hudson.plugins.parameterizedtrigger.TriggerBuilder>
            <configs>
                {}
            </configs>
        </hudson.plugins.parameterizedtrigger.TriggerBuilder>
    </builders>
</project>"""

    _config_template = """\
<hudson.plugins.parameterizedtrigger.BlockableBuildTriggerConfig>
    <projects>{}</projects>
</hudson.plugins.parameterizedtrigger.BlockableBuildTriggerConfig>"""

    @pytest.mark.parametrize('expected,configured_projects,object_names', (
        (LintResult.PASS, ['existent-project'], ['existent-project']),
        (LintResult.PASS, ['one', 'two'], ['one', 'two']),
        (LintResult.PASS, ['one', 'two'], ['zero', 'one', 'two', 'three']),
        (LintResult.PASS, ['one,two'], ['zero', 'one', 'two', 'three']),
        (LintResult.PASS, ['one, two'], ['zero', 'one', 'two', 'three']),
        (LintResult.FAIL, ['non-existent-project'], ['existent-project']),
        (LintResult.FAIL, ['exists', 'doesnt'], ['exists']),
        (LintResult.FAIL, ['doesnt', 'exists'], ['exists']),
        (LintResult.FAIL, ['doesnt,exists'], ['exists']),
        (LintResult.FAIL, ['doesnt, exists'], ['exists']),
    ))
    def test_linter(self, expected, configured_projects, object_names):
        configs = ''.join(self._config_template.format(project)
                          for project in configured_projects)
        tree = _elementtree_from_str(
            self._trigger_builder_template.format(configs))
        linter = CheckJobReferences(
            LintContext({}, RunContext(object_names), tree))
        result, _ = linter.check()
        assert result is expected

    def test_completely_empty_projects_node(self):
        config = """\
<hudson.plugins.parameterizedtrigger.BlockableBuildTriggerConfig>
    <projects/>
</hudson.plugins.parameterizedtrigger.BlockableBuildTriggerConfig>"""
        tree = _elementtree_from_str(
            self._trigger_builder_template.format(config))
        linter = CheckJobReferences(
            LintContext({}, RunContext(['object']), tree))
        result, _ = linter.check()
        assert result is LintResult.FAIL


class TestCheckColumnConfiguration:

    @pytest.mark.parametrize('expected,xml_string', (
        (LintResult.SKIP, '<not_a_view/>'),
        (LintResult.SKIP, '<project/>'),
        (LintResult.PASS, '''\
            <hudson.model.ListView>
                <columns>
                    <something/>
                </columns>
            </hudson.model.ListView>'''),
        (LintResult.FAIL,
         '<hudson.model.ListView><columns /></hudson.model.ListView>'),
        (LintResult.FAIL, '<hudson.model.ListView/>'),
    ))
    def test_linter(self, expected, xml_string):
        tree = _elementtree_from_str(xml_string)
        linter = CheckColumnConfiguration(LintContext({}, None, tree))
        result, _ = linter.check()
        assert result is expected


class TestCheckEnvInject:

    _template = '''\
<project>
  <properties>
    <EnvInjectJobProperty>
      <info>
        <propertiesContent>{}</propertiesContent>
      </info>
    </EnvInjectJobProperty>
  </properties>
</project>'''

    @pytest.mark.parametrize('expected,required_environment_settings', (
        (LintResult.SKIP, ''),
        (LintResult.FAIL, 'SOME=thing'),
    ))
    def test_no_properties_configured(
            self, expected, required_environment_settings):
        tree = _elementtree_from_str('<project/>')
        config = get_config()
        config['job_linter:check_env_inject'][
            'required_environment_settings'] = required_environment_settings
        linter = CheckEnvInject(
            LintContext(config['job_linter:check_env_inject'], None, tree))
        result, _ = linter.check()
        assert result is expected

    @pytest.mark.parametrize(
        'expected,properties_content,required_environment_settings', (
            (LintResult.FAIL, '', 'SOME=thing'),
            (LintResult.PASS, 'SOME=thing', 'SOME=thing'),
            (LintResult.PASS, '\n'.join(['FIRST=thing', 'SOME=thing',
                                         'LAST=thing']),
             'SOME=thing'),
            (LintResult.PASS, '\n'.join(['FIRST=thing', 'SOME=thing',
                                         'LAST=thing']),
             'SOME=thing, LAST=thing'),
            (LintResult.FAIL, 'FIRST=thingSOME=thing', 'SOME=thing'),
        ))
    def test_linter(
            self, expected, properties_content, required_environment_settings):
        tree = _elementtree_from_str(self._template.format(properties_content))
        config = get_config()
        config['job_linter:check_env_inject'][
            'required_environment_settings'] = required_environment_settings
        linter = CheckEnvInject(
            LintContext(config['job_linter:check_env_inject'], None, tree))
        result, _ = linter.check()
        assert result is expected


class TestLinter:

    class LintTestSubclass(Linter):

        description = 'test description'
        root_tag = 'test_tag'

        def actual_check(self):
            return self._ctx.config['_mock_result']

    def test_check_and_text_passed_through(self, mocker):
        tree = _elementtree_from_str('<test_tag/>')
        mock_result = mocker.sentinel.result, mocker.sentinel.text
        linter = self.LintTestSubclass(
            LintContext({'_mock_result': mock_result}, None, tree))
        assert mock_result == linter.check()

    def test_wrong_root_tag_is_skipped_without_check(self, mocker):
        tree = _elementtree_from_str('<not_right/>')
        linter = self.LintTestSubclass(LintContext({}, None, tree))
        linter.actual_check = mocker.Mock()
        result, text = linter.check()
        assert result == LintResult.SKIP
        assert text is None
        assert 0 == linter.actual_check.call_count
