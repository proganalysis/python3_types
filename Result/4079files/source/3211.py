from src.util.bunk_user import BunkUser

class Vote:
    def __init__(self, value: str, user: BunkUser):
        self.value = value
        self.user = user