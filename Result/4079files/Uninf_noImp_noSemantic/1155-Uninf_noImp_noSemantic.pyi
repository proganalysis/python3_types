from africastalking.AfricasTalkingGateway import AfricasTalkingGateway as AfricasTalkingGateway
from sms_log_handler.providers.base import SMSProviderBase

class AfricasTalkingProvider(SMSProviderBase):
    def send(self, phone_numbers: str, message: str) -> None: ...
