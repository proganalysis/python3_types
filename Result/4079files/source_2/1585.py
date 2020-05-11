"""Integration tests for each command.

Copyright © 2017-2018 Garrett Powell <garrett@gpowell.net>

This file is part of codot.

codot is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

codot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with codot.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
import builtins
import textwrap
import subprocess
from typing import NamedTuple

import pytest

import codot
from codot import CONFIG_EXT, CONFIG_DIR, TEMPLATES_DIR, HOME_DIR
from codot.exceptions import InputError
from codot.utils import rm_ext, add_ext
from codot.user_files import UserConfigFile, Role, TemplateFile
from codot.container import ProgramData
from codot.commands.add_template import AddTemplateCommand
from codot.commands.rm_template import RmTemplateCommand
from codot.commands.role import RoleCommand
from codot.commands.sync import SyncCommand

real_open = builtins.open

FakeFilePaths = NamedTuple(
    "FakeFilePaths", [
        ("role", Role), ("config", UserConfigFile), ("template", TemplateFile)
    ])


@pytest.fixture
def copy_config(fs):
    """Copy the template config file to the fake filesystem."""
    config_path = os.path.join(
        os.path.dirname(codot.__file__), "../docs/config/settings.conf")
    with real_open(config_path) as real_file:
        fs.CreateFile(
            os.path.join(sys.prefix, "share/codot/settings.conf"),
            contents=real_file.read())


@pytest.fixture
def fake_files(fs, copy_config) -> FakeFilePaths:
    """Create fake files for testing."""
    files = FakeFilePaths(
        Role("color_scheme", CONFIG_DIR),
        UserConfigFile(os.path.join(CONFIG_DIR, "desktop.conf")),
        TemplateFile(".config/i3/config", TEMPLATES_DIR))

    # Create config files.
    fs.CreateFile(
        os.path.join(files.role.dir_path, "solarized.conf"),
        contents=textwrap.dedent("""\
            ForegroundColor=#93a1a1
            BackgroundColor=#002b36
            Font=NotoSans
            """))
    fs.CreateFile(
        os.path.join(files.role.dir_path, "zenburn.conf"),
        contents=textwrap.dedent("""\
            ForegroundColor=#ffffff
            BackgroundColor=#000000
            Font=Roboto
            """))
    fs.CreateFile(
        files.config.path, contents=textwrap.dedent("""\
            Font=DejaVuSans
            FontSize=12
            """))
    os.symlink(
        files.role.get_configs()[0].path, files.role.symlink_path)

    # Create template files.
    fs.CreateFile(
        files.template.path, contents=textwrap.dedent("""\
            {{Font}}
            {{FontSize}}
            {{ForegroundColor}}
            {{BackgroundColor}}
            """))

    # Create source files.
    fs.CreateFile(os.path.join(
        HOME_DIR, os.path.relpath(files.template.path, TEMPLATES_DIR)))

    return files


class TestAddTemplateCommand:
    @pytest.fixture
    def patch_editor(self, monkeypatch):
        def edit_text_file(filepath):
            with open(filepath, "a") as file:
                file.write("{{AccentColor}}")
            return 0

        monkeypatch.setattr(
            "codot.commands.add_template.open_text_editor", edit_text_file)

    def test_add_new_template(self, fake_files, patch_editor):
        """New template files can be created from source files."""
        cmd = AddTemplateCommand(
            [fake_files.template.source_path], revise=False)
        cmd.main()

        with open(fake_files.template.path) as file:
            assert file.read() == "{{AccentColor}}"

    def test_add_revised_template(self, fake_files, patch_editor):
        """Template files can be revised."""
        cmd = AddTemplateCommand(
            [fake_files.template.source_path], revise=True)
        cmd.main()

        expected_output = textwrap.dedent("""\
            {{Font}}
            {{FontSize}}
            {{ForegroundColor}}
            {{BackgroundColor}}
            {{AccentColor}}""")

        with open(fake_files.template.path) as file:
            assert file.read() == expected_output


class TestRmTemplateCommand:
    def test_nonexistent_template(self, fake_files):
        """Specifying a nonexistent template raises an exception."""
        os.remove(fake_files.template.path)
        with pytest.raises(InputError):
            cmd = RmTemplateCommand([fake_files.template.source_path])
            cmd.main()

    def test_remove_template_file(self, fake_files):
        """The template file is removed."""
        cmd = RmTemplateCommand([fake_files.template.source_path])
        cmd.main()

        assert not os.path.isfile(fake_files.template.path)

    def test_remove_unused_options(self, fs, fake_files):
        """Unused options are removed from the config files."""
        new_template = TemplateFile(".Xresources", TEMPLATES_DIR)
        fs.CreateFile(new_template.source_path)
        fs.CreateFile(
            new_template.path, contents=textwrap.dedent("""\
                {{FontSize}}
                {{ForegroundColor}}
                {{BackgroundColor}}
                """))

        cmd = RmTemplateCommand([fake_files.template.source_path])
        cmd.main()

        solarized_output = textwrap.dedent("""\
            ForegroundColor=#93a1a1
            BackgroundColor=#002b36
            """)
        zenburn_output = textwrap.dedent("""\
            ForegroundColor=#ffffff
            BackgroundColor=#000000
            """)
        desktop_output = textwrap.dedent("""\
            FontSize=12
            """)

        with open(fake_files.role.get_configs()[0].path) as file:
            assert file.read() == solarized_output
        with open(fake_files.role.get_configs()[1].path) as file:
            assert file.read() == zenburn_output
        with open(fake_files.config.path) as file:
            assert file.read() == desktop_output


class TestRoleCommand:
    def test_no_role_specified(self):
        """Not specifying a role returns None."""
        cmd = RoleCommand(None, None)
        assert cmd.main() is None

    def test_no_config_specified(self, fake_files):
        """Not specifying a config returns None."""
        cmd = RoleCommand(fake_files.role.name, None)
        assert cmd.main() is None

    def test_role_nonexistent(self, fake_files):
        """Specifying a role that doesn't exist raises an exception."""
        cmd = RoleCommand("foo", None)
        with pytest.raises(InputError):
            cmd.main()

    def test_config_nonexistent(self, fake_files):
        """Specifying a config that doesn't exist raises an exception."""
        cmd = RoleCommand(fake_files.role.name, "foo")
        with pytest.raises(InputError):
            cmd.main()

    @pytest.mark.parametrize("extension", ["", CONFIG_EXT])
    def test_symlink_created(self, fs, fake_files, extension):
        """A symlink is created for the role."""
        config_name = add_ext(fake_files.role.get_configs()[1].name, extension)

        cmd = RoleCommand(fake_files.role.name, config_name)
        cmd.main()

        symlink_path = fake_files.role.symlink_path
        assert os.path.islink(symlink_path)
        assert (
            fake_files.role.selected.path
            == fake_files.role.get_configs()[1].path)


class TestSyncCommand:
    @pytest.mark.parametrize("overwrite", [True, False])
    def test_overwrite_source_files(self, fs, fake_files, overwrite):
        """Modified source files are ignored unless otherwise specified."""
        # Add the source file to the info file.
        cmd = SyncCommand(overwrite=overwrite)
        cmd.main()

        # Truncate the file so that its mtime is more recent that the time of
        # the last sync in the info file.
        open(fake_files.template.source_path, "w").close()
        cmd.main()

        if overwrite:
            assert os.stat(fake_files.template.source_path).st_size > 0
        else:
            assert os.stat(fake_files.template.source_path).st_size == 0

    def test_missing_identifiers(self, fs, fake_files):
        """Identifiers not found in a config file raise an exception."""
        os.remove(fake_files.role.symlink_path)

        cmd = SyncCommand()
        with pytest.raises(InputError):
            cmd.main()

    def test_missing_source_files(self, fs, fake_files):
        """Template files without corresponding source files are ignored."""
        os.remove(fake_files.template.source_path)

        cmd = SyncCommand()
        cmd.main()

        assert not os.path.exists(fake_files.template.source_path)

    @pytest.mark.parametrize("id_format", ["{{%s}}", "__%s__", "${%s}"])
    def test_propagate_config_changes(
            self, fake_files, monkeypatch, id_format):
        """Values can be propagated with different identifier formats."""
        identifiers = ["Font", "FontSize", "ForegroundColor", "BackgroundColor"]
        template_contents = "\n".join(
            id_format.replace("%s", identifier) for identifier in identifiers)

        with open(fake_files.template.path, "w") as file:
            file.write(template_contents)

        cmd = SyncCommand()
        monkeypatch.setattr(cmd.data, "read", cmd.data.generate)
        monkeypatch.setattr(type(cmd.data), "id_format", id_format)
        cmd.main()

        expected_content = textwrap.dedent("""\
            NotoSans
            12
            #93a1a1
            #002b36""")
        with open(fake_files.template.source_path, "r") as file:
            assert file.read() == expected_content
