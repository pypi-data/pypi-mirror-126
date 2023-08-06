from abc import ABC, abstractmethod
import uuid
from .stats.stats import Stats

class ChannelInterface(ABC):
    def __init__(self, config, hardware_serial_no=None, serial_no=uuid.uuid4(), channel_stats=None, **kwargs):
        self.serial_no = serial_no
        self.hardware_serial_no = hardware_serial_no
        self.stats = Stats(channel_stats)
        if 'keep_statistics' in config:
            self.keep_statistics = config['keep_statistics']
        else:
            self.keep_statistics = False

    def update_stats(self,value):
        if self.keep_statistics:
            self.stats.update(value)
            self.stats.update_on_server()

    async def run(self):
        value = await self.get_raw_data()
        if self.keep_statistics:
            self.update_stats(value)
        return value


    @abstractmethod
    async def get_raw_data(self):
        pass
