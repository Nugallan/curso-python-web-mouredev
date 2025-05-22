import os
import dotenv
# pip install configcat-client
import configcatclient
import json

class ConfigCatAPI:
    
    dotenv.load_dotenv()
    
    CONFIGCAT_SDK_KEY = os.environ.get("CONFIGCAT_SDK_KEY")

    def __init__(self) -> None:
        if self.CONFIGCAT_SDK_KEY != None:
            self.configcat: configcatclient.get(self.CONFIGCAT_SDK_KEY) # type: ignore

    def schedule(self) -> dict:
        response = self.configcat.get_value("live_schedule", "") # "live_schedule" is el nombre de proyecto de ConfigCat
        schedule = json.loads(response)
        print(type(schedule))
        return schedule

        