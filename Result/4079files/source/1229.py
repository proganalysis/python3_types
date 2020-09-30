import datetime
import logging
import os
import re
import webbrowser

from dateutil import parser
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys

from helpers import format_dt
from pages.datepicker import JqueryUIDatePicker
from pages.helpers import wait_for, elem_has_class
from pages.timepicker import BasicTimePicker, TimeNotBookableError


logger = logging.getLogger(__name__)


class RestaurantPageAvailabilityForm:
	date_input_selector = 'diningAvailabilityForm-searchDate'
	date_input_real_selector = 'input[name="searchDate"]'
	date_input_id = 'diningAvailabilityForm-searchDate'
	time_select_selector = 'select#diningAvailabilityForm-searchTime'
	time_select_id = 'diningAvailabilityForm-searchTime'
	party_size_select_selector = 'select#partySize'
	party_size_id = 'partySize'
	availability_check_submit_selector = 'button#finderForm-findTableButton'
	loading_overylay_selector = '.pepLoadingOverlay'

	def __init__(self, url: str, browser, implicit_wait: int = 10):
		self.url = url
		self.browser = browser
		self.browser.implicitly_wait(implicit_wait)

		self.has_fetched = False

		self._submitted_at = None

	@property
	def name(self):
		self.check_has_fetched()
		return self.browser.find_element_by_css_selector('meta[property="og:title"]').get_attribute('content')

	def get_datepicker(self) -> JqueryUIDatePicker:
		self.check_has_fetched()
		return JqueryUIDatePicker(self.browser, self.date_input_selector)

	def set_time(self, dt: datetime.datetime):
		self.check_has_fetched()
		tp = BasicTimePicker(self.browser)
		try:
			tp.select_closest_time(dt)
		except TimeNotBookableError:
			return

	def set_breakfast(self):
		self.check_has_fetched()
		tp = BasicTimePicker(self.browser)
		tp.select_breakfast()

	def set_lunch(self):
		self.check_has_fetched()
		tp = BasicTimePicker(self.browser)
		tp.select_lunch()

	def set_dinner(self):
		self.check_has_fetched()
		tp = BasicTimePicker(self.browser)
		tp.select_dinner()

	@property
	def date_input_element(self):
		return self.browser.find_element_by_css_selector(self.date_input_real_selector)

	@property
	def current_date(self):
		current = self.date_input_element.get_attribute('value')
		return datetime.datetime.strptime(current, '%m/%d/%Y')

	def set_date(self, dt: datetime.datetime):
		self.check_has_fetched()
		value = dt.strftime('%m/%d/%Y')
		i = self.date_input_element
		# self.browser.execute_script('document.getElementById("{}").value="{}"'.format(self.date_input_id, value))
		i.send_keys(Keys.LEFT_CONTROL, 'a')
		i.send_keys(value)
		i.send_keys(Keys.TAB)
		i.send_keys(Keys.TAB)
		self._form_nudge(self.date_input_id)

	def set_partysize(self, size: int):
		self.check_has_fetched()
		self.browser.execute_script('document.getElementById("{}").value="{}"'.format(self.party_size_id, size))
		self._form_nudge(self.party_size_id)

	def _form_nudge(self, trigger_selector):
		self.browser.find_element_by_id('checkAvailability').click()
		try:
			clickme = self.browser.find_element_by_css_selector(
				'#partySizeid-base')
		# clickme = self.browser.find_element_by_css_selector(
		# 	'div.select-toggle[aria-owns="diningAvailabilityForm-searchTime-dropdown-list"]')
		except NoSuchElementException:

			self.browser.save_screenshot('what.png')
			with open('fail_source.html', 'w') as f:
				f.write(self.browser.page_source)
				webbrowser.open('file://{}'.format(os.path.realpath('./fail_source.html')))
			raise

		def clickable():
			try:
				clickme.click()
			except WebDriverException:
				return False
			return True

		wait_for(clickable, 2)
		self.browser.find_element_by_id('checkAvailability').click()

	# self.browser.execute_script('$(arguments[0]).change()', trigger_selector)

	@property
	def loading_overlay_displayed(self):
		self.check_has_fetched()
		overlay = self.browser.find_element_by_css_selector(self.loading_overylay_selector)
		return overlay.is_displayed() and not elem_has_class(overlay, 'hidden')

	@property
	def availability_submit(self):
		self.check_has_fetched()
		return self.browser.find_element_by_css_selector(self.availability_check_submit_selector)

	def check_has_fetched(self):
		assert self.has_fetched, "Call `.get()` before trying to access elements."

	def get(self):
		self.browser.get(self.url)
		self.has_fetched = True

	def submit_availability_check(self):
		self._submitted_at = datetime.datetime.now()
		logger.debug('Submitting availability check.')
		self.availability_submit.click()

		wait_for(lambda: self.loading_overlay_displayed, 8,
		         on_failure=lambda: self.browser.save_screenshot('error.png'))
		wait_for(lambda: not self.loading_overlay_displayed, 30,
		         on_failure=lambda: self.browser.save_screenshot('error.png'))

	@property
	def available_times(self):
		assert self._submitted_at, "Can't get available times until form is submitted."

		try:
			availability_div = self.browser.find_element_by_css_selector('div.ctaAvailableTimesContainer')
			logger.debug("Found available times div")
		except NoSuchElementException:
			try:
				availability_div = self.browser.find_element_by_css_selector('div.ctaNoAvailableTimesContainer')
				logger.debug("Found no available times div.")
			except NoSuchElementException:
				logger.error("No available times information div found.")
				return []

		available_times = availability_div.find_elements_by_css_selector('div.availableTime')

		times = []
		for at in available_times:
			time = at.text
			time = re.search('((\d{1,2}:\d\d )(AM|PM))', time)
			if time:
				time = time.groups()[0]
			assert re.match('((\d{1,2}:\d\d )(AM|PM))', time), "'{}' is not a time.".format(time)

			dt = parser.parse(time)

			current_dt = self.current_date
			fixed_dt = dt.replace(year=current_dt.year, month=current_dt.month, day=current_dt.day)
			logger.info("Found available time '{}' at '{}'".format(format_dt(fixed_dt), self.name))
			times.append(fixed_dt)

		return times

	def find_availability_for(self, dt: datetime.datetime, party_size: int, breakfast=False, lunch=False, dinner=False, any_time=False):
		self.get()
		self.set_date(dt)

		periods = [('breakfast', breakfast), ('lunch', lunch), ('dinner', dinner)]
		period_text = ", ".join([x[0] for x in periods if x[1]])

		self.set_partysize(party_size)

		info = {'restaurant': self.name,
		        'party_size': party_size,
		        'searched_at': datetime.datetime.now(),
		        'looking_for': {'datetime': dt, 'period': period_text},
		        'available_times': []}

		if not any_time:
			if breakfast:
				self.set_breakfast()
				logger.info("Checking '%s' for 'breakfast'.", self.name)
				self.submit_availability_check()
				info['available_times'].extend(self.available_times)
			if lunch:
				self.set_lunch()
				logger.info("Checking '%s' for 'lunch'.", self.name)
				self.submit_availability_check()
				info['available_times'].extend(self.available_times)
			if dinner:
				self.set_dinner()
				logger.info("Checking '%s' for 'dinner'.", self.name)
				self.submit_availability_check()
				info['available_times'].extend(self.available_times)

		if not breakfast and not lunch and not dinner and not any_time:
			self.set_time(dt)
			self.submit_availability_check()
			info['available_times'].extend(self.available_times)

		if any_time:
			self.check_has_fetched()
			tp = BasicTimePicker(self.browser)
			for sv in tp.selectable_values:
				if sv.lower() not in [x[0] for x in periods]:
					sv_dt = parser.parse(sv)
					sv_dt = sv_dt.replace(year=dt.year, month=dt.month, day=dt.day)
					tp.select_exact_time(sv_dt)
					logger.info("Checking '%s' for %s.", self.name, sv_dt)
					self.submit_availability_check()
					info['available_times'].extend(self.available_times)



		return info