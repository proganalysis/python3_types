from modules.models import Module

class Sera(Module):

    def has_action(self, action):
        return action == "diga_ola_para"

    def diga_ola_para(self, para):
        print("Ola, %s" % para)
        return "Ola, %s" % para


class Vish(Module):

    def has_action(self, action):
        return action == "vish_vish"

    def vish_vish(self, para):
        print("Vish, %s" % para)
        return "Vish, %s" % para