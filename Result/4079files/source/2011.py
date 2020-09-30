import smtplib
from email.mime.text import MIMEText


class GmailHandler():
	"""
	IMPORTANT NOTE:
	in order to access a gmail account with this handler,
	your account needs 'foreign-access' enabled (follow these steps):
	login to the account
	go here--> https://accounts.google.com/b/0/DisplayUnlockCaptcha
	press 'Continue'
	Done.
	"""

	def __init__(self, gmail, password):
		self.gmail = gmail
		self.password = password

	def send_mail(self, receivers, subject, text):

		if not isinstance(receivers, list):
			receivers = [receivers]

		# Send the message via our own SMTP server, but don't include the envelope header
		smtp = smtplib.SMTP("smtp.gmail.com", 587)
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(self.gmail, self.password)

		for receiver in receivers:

			msg = MIMEText(text)
			msg['Subject'] = subject
			msg['From'] = self.gmail
			msg['To'] = receiver
			smtp.sendmail(self.gmail, receiver, str(msg))

		smtp.quit()