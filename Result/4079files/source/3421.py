from config.api import IntranetAPI


class Context:
    """
    Context
    Provide : API
    """

    def __init__(self, a_p_i: IntranetAPI, options: dict) -> object:
        if not isinstance(a_p_i, IntranetAPI):
            raise TypeError("API must be an instance of IntranetAPI")
        self.api = a_p_i
        self.options = options

    def get_api(self):
        return self.api

    def is_verbose(self) -> bool:
        return self.options.get("verbose", True)

    def display(self):
        print("Context: ")
        print("Api host: " + self.api.get_host())
        print("Api format: " + self.api.get_format())
        print("verbose mode: " + self.is_verbose().__str__())
        print("options" + self.options.__str__())
