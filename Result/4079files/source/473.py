#!/usr/bin/env python
# -*- coding: utf-8 -*-
""".. module:: test_guisupport

**Copyright 2014, 2015, 2017 Stephen Rigden.**
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import functools
import tkinter
import unittest
import unittest.mock as mock

import chrono

import guisupport
from test.mixins import MockMixin


class TestAutoScrollBar(unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self) -> None:
        with mock.patch('guisupport.super'):
            self.scrollbar = guisupport.AutoScrollbar()

    def test_str(self):
        self.assertEqual("{} <id {}>".format(self.scrollbar.__class__.__name__,
                                             id(self.scrollbar)),
                         str(self.scrollbar))

    def test_grid_called(self):
        self.scrollbar.grid = mock.MagicMock(name='mock grid')
        with mock.patch('guisupport.super'):
            self.scrollbar.set('0.2', '0.8')
        # noinspection PyUnresolvedReferences
        self.scrollbar.grid.assert_called_with()

    def test_grid_remove_called(self):
        self.scrollbar.grid_remove = mock.MagicMock(name='mock grid_remove')
        with mock.patch('guisupport.super'):
            self.scrollbar.set('-0.2', '1.8')
        # noinspection PyUnresolvedReferences
        self.scrollbar.grid_remove.assert_called_with()

    def test_set_called(self) -> None:
        self.scrollbar.grid = mock.MagicMock(name='mock grid')
        with mock.patch('guisupport.super') as cm:
            self.scrollbar.set('0.2', '0.8')
        cm().set.assert_called_with('0.2', '0.8')

    def test_pack_raises_exception(self):
        with self.assertRaises(tkinter.TclError):
            self.scrollbar.pack()

    def test_place_raises_exception(self):
        with self.assertRaises(tkinter.TclError):
            self.scrollbar.place()


class EntryUpdateObserver(MockMixin, unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self):
        super().setUp()
        self.mock_widget = self.mock_patch('registermenu.ttk.Entry')
        self.value = 'new value'
        guisupport.entry_update_observer(self.mock_widget, self.value)

    def test_widget_delete_called(self):
        self.mock_widget.delete.assert_called_with(0, 'end')

    def test_widget_insert_called(self):
        self.mock_widget.insert.assert_called_with(0, self.value)


class LabelUpdateObserver(MockMixin, unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self):
        super().setUp()
        self.mock_widget = self.mock_patch('registermenu.ttk.Label')
        self.value = 'new value'
        guisupport.label_update_observer(self.mock_widget, self.value)

    def test_widget_updated(self):
        self.mock_widget.config.assert_called_with(text=self.value)


class WidgetEnableObserver(MockMixin, unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self):
        self.mock_ttk = self.mock_patch('guisupport.ttk')
        self.mock_widget = self.mock_patch('guisupport.ttk.Entry')

    def test_enable_calls_widget_state(self):
        observer = functools.partial(guisupport.entry_observer,
                                     self.mock_widget)
        observer(True)
        self.mock_widget.state.assert_called_with(['!disabled'])

    def test_disable_calls_widget_state_and_widget_delete(self):
        observer = functools.partial(guisupport.entry_observer,
                                     self.mock_widget)
        observer(False)
        self.mock_widget.delete.assert_called_with(0, tkinter.END)
        self.mock_widget.state.assert_called_with(['disabled'])


class ChangeMenuItemState(MockMixin, unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self):
        self.menu = self.mock_patch('guisupport.tk.Menu')

    def test_menu_item_enabled(self):
        guisupport.menu_item_enable_observer(self.menu, 42, True)
        self.menu.entryconfig.assert_called_with(42, state='normal')

    def test_menu_item_disabled(self):
        guisupport.menu_item_enable_observer(self.menu, 42)
        self.menu.entryconfig.assert_called_with(42, state='disabled')


class CleanupIntStr(unittest.TestCase):
    def test_empty_string_returns_str_zero(self):
        self.assertEqual('0', guisupport.cleanup_int_str(''))

    def test_non_empty_string_returns_integer(self):
        self.assertEqual(9, guisupport.cleanup_int_str('9'))


class FormatDate(MockMixin, unittest.TestCase):
    # noinspection PyMissingOrEmptyDocstring
    def setUp(self):
        self.date = chrono.Date('1/15/20')

    def test_date_formatted_with_supplied_format(self):
        format_ = "$weekdayname $day & $shortmonthname $year"
        result = guisupport.format_date(self.date, format_)
        self.assertEqual('Wednesday 15 & Jan 2020', result)

    def test_date_formatted_with_default_format(self):
        self.mock_config = self.mock_patch('guisupport.config')
        self.mock_config.config_static.get.return_value = 'Year: $year, Week: $week'
        result = guisupport.format_date(self.date)
        self.assertEqual('Year: 2020, Week: 3', result)


class CalendarPeriods(MockMixin, unittest.TestCase):
    def test_calendar_periods_returned(self):
        expected = {'Day': 'day', 'Week': 'week', 'Month': 'month', 'Year': 'year'}
        mock_config = self.mock_patch('guisupport.config')
        mock_config.config_static.get.return_value = 'Day, Week, Month, Year'
        result = guisupport.calendar_periods()
        self.assertEqual(expected, result)


class CalendarPeriodInternal(MockMixin, unittest.TestCase):
    def test_internal_period_returned(self):
        expected = 'month'
        config_period = 'Month'
        mock_periods = self.mock_patch('guisupport.calendar_periods')
        mock_periods.return_value = {'Day': 'day', 'Week': 'week', 'Month': 'month',
                                     'Year': 'year'}
        result = guisupport.calendar_period_internal(config_period)
        self.assertEqual(expected, result)


class CalendarPeriodConfig(MockMixin, unittest.TestCase):
    def test_config_period_returned(self):
        expected = 'Month'
        internal_period = 'month'
        mock_periods = self.mock_patch('guisupport.calendar_periods')
        mock_periods.return_value = {'Day': 'day', 'Week': 'week', 'Month': 'month',
                                     'Year': 'year'}
        result = guisupport.calendar_period_config(internal_period)
        self.assertEqual(expected, result)

    def test_invalid_period_logs_and_raises_error(self):
        mock_logging = self.mock_patch('guisupport.logging')
        internal_period = 'garbage'
        mock_periods = self.mock_patch('guisupport.calendar_periods')
        mock_periods.return_value = {}
        with self.assertRaises(IndexError) as cm:
            guisupport.calendar_period_config(internal_period)
        msg = "internal_period not found in calendar_periods().items()."
        mock_logging.error.assert_called_with(msg)
        self.assertEqual(msg, cm.exception.args[0])
