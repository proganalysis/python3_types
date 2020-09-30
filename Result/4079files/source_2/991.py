# -*- coding: utf-8 -*-
"""Predict cashflow for pigjar database.

**Copyright 2014, 2016 Stephen Rigden.**
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
import copy
import decimal
import heapq
from typing import List, Mapping, Sequence, Tuple

import chrono
import collections

import account
import pig


class Cashflow:
    """A cashflow prediction based on a 'snapshot' of accounts, pigs,
    and events.

    A pinch point occurs on a day when the net worth is at low point. It's
    severity is determined by a ratio. The ratio is calculated as the total of
    amounts between the start and the pinch point divided by the number of days
    to the pinch point. Pinch points do not include the start date.
    """
    def __init__(self) -> None:
        """Attributes.
            cashflow: Stores a running total of spend, Running total of
                saving, Spend delta, Spend plus saving delta.
                Deltas are stored as currency units/day e.g. £/day.
            pinch_points_spend: Stores a sorted list of spending pinch points, worst first.
            pinch_points_svg: Stores a sorted list of spend plus saving pinch points,
                worst first.
            start_date_totals: Stores the total spend from accounts and pigs, Total savings
                from pigs.
        """
        self.cashflow = {}  # type: Mapping[chrono.Date, Sequence]
        self.pinch_points_spend = []  # type: List[chrono.Date]
        self.pinch_points_svg = []  # type: List[chrono.Date]
        self.start_date_totals = None, None  # type: Tuple[decimal.Decimal]

    def __str__(self) ->str:
        return "{}".format(self.__class__.__name__)

    def __repr__(self) ->str:
        return "{}()".format(self.__class__.__name__)

    def predictor(self, accs: List['account.Account'], pigs: List['pig.Pig'],
                  start_date: chrono.date.Date = None,
                  end_date: chrono.date.Date = None, pinch_count: int = 4) -> None:
        """Create a cashflow prediction and identify pinch points.

        Args:
            accs: List of Account objects
            pigs: List of Pig objects
            start_date: Start date for evt_total accumulation.
            end_date: End date for cashflow accumulation.
            pinch_count: Maximum number of pinch points.
        """
        if start_date:
            start_date = chrono.Date(start_date)
        else:
            start_date = chrono.Date(True)  # Today
        if end_date:
            end_date = chrono.Date(end_date)
        else:
            end_date = copy.deepcopy(start_date)
            end_date.year += 1  # chrono can handle Feb 29th.
            end_date.day -= 1

        self._events_total(pigs, start_date, end_date)
        if self.cashflow:
            date_str = chrono.Date(start_date).format("$0year$0month$0day")
            self.cashflow[date_str][0] += sum(a.balance for a in accs)
            self.start_date_totals = (self.cashflow[date_str][0],
                                      self.cashflow[date_str][1])
            self._locate_pinch_points(pinch_count)

    def _events_total(self, pigs: List['pig.Pig'], start_date: chrono.date.Date,
                      end_date: chrono.date.Date) -> None:
        """Total the spend and savings for pigs and events.

        Args:
            pigs: The pigs whose events will be totalled.
            start_date: The earliest date in the returned dictionary.
            end_date: The end date for totalling.

        If the date of the pig is earlier than the start date the pig.spend
            and pig.svg will be included in the values for the earliest date. If
            any events occur before the start date their spend and saving
            amounts will also be included in the values for the first date.
        """

        self.cashflow = {}
        for p in pigs:
            cfgen = p.iter_event()
            while True:
                try:
                    date, e_amt, e_svg = next(cfgen)
                except StopIteration:
                    break
                if date > end_date:
                    break
                date = date if date >= start_date else start_date
                date_str = chrono.Date(date).format("$0year$0month$0day")
                if date_str in self.cashflow:
                    self.cashflow[date_str][0] += e_amt
                    self.cashflow[date_str][1] += e_svg
                else:
                    self.cashflow[date_str] = [e_amt, e_svg, date.get_julian() -
                                               start_date.get_julian()]

    def _locate_pinch_points(self, pinch_count: int) -> None:
        """Locate the pinch points.

        Args:
            pinch_count: Number of pinch points.
        """

        spendq = []
        svgq = []
        self.cashflow = collections.OrderedDict(
            sorted(self.cashflow.items(), key=lambda t: t[0]))
        last_k = None
        for k in self.cashflow.keys():
            spend, svg, days = self.cashflow[k]
            if last_k:  # Calculate running totals
                spend += self.cashflow[last_k][0]
                svg += self.cashflow[last_k][1]

            try:  # Calculate and save spending and saving deltas
                spend_d = spend / days
                svg_d = (spend + svg) / days
            except (decimal.InvalidOperation, decimal.DivisionByZero):
                spend_d = svg_d = 0
            self.cashflow[k] = [spend, svg, spend_d, svg_d]

            heapq.heappush(spendq, (spend_d, k))
            heapq.heappush(svgq, (svg_d, k))
            last_k = k

        self.pinch_points_spend = heapq.nlargest(pinch_count, spendq)
        self.pinch_points_spend = [item[1] for item in self.pinch_points_spend]
        self.pinch_points_svg = heapq.nlargest(pinch_count, svgq)
        self.pinch_points_svg = [item[1] for item in self.pinch_points_svg]
