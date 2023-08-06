from .stat_interface import StatInterface

class Max(StatInterface):

    def update(self, value):
        if value > self.value:
            self.value = value
            self.check_if_value_updated()
