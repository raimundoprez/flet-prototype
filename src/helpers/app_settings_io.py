import json
import os

from common.app_globals import refs
from common.utils import pretty_exception
from helpers.app_settings import AppSettings

class AppSettingsIO:
    def __init__(self, settings_file: str):
        self.settings_file = settings_file

    def read_settings(self, **default_kwargs) -> AppSettings:
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, "r", encoding="utf-8") as file:
                    data = json.load(file) # read json file and create a python dict from it
                    return AppSettings.schema().load({**default_kwargs, **data}) # return an instance with the data we just extracted from the file
        except OSError as e:
            refs["logger"].error(pretty_exception("Operating system error while trying to read the settings file", e))
        except Exception as e:
            refs["logger"].error(pretty_exception("Unknown exception while trying to read the settings file", e))
            
        return AppSettings(**default_kwargs)

    def write_settings(self, app_settings: AppSettings):
        try:
            with open(self.settings_file, "w", encoding="utf-8") as file:
                data = app_settings.to_dict()
                json.dump(data, file, indent=4)
        except OSError as e:
            refs["logger"].error(pretty_exception("Operating system error while trying to write into the settings file", e))
        except Exception as e:
            refs["logger"].error(pretty_exception("Unknown exception while trying to write into the settings file", e))