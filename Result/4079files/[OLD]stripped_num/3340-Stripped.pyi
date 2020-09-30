# (generated with --quick)

import email.mime.multipart
import email.mime.text
from typing import Any, Type, TypeVar, Union

MIMEMultipart: Type[email.mime.multipart.MIMEMultipart]
MIMEText: Type[email.mime.text.MIMEText]
RPi: Any
dbman: module
logging: module
smtplib: module
var: Any

_T1 = TypeVar('_T1')

def check_sensor_alert_limits(alert_results, alert_flag: _T1) -> Union[bool, _T1]: ...
def reset_email_sent_flag_if_alerts_clear(alert_results, email_sent) -> Any: ...
def send_email(alert_readings, address) -> None: ...
