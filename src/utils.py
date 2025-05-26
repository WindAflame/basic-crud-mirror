import json
import os


class Utils:
    
    @staticmethod
    def load_from_json_file(path: str) -> any:
        if not os.path.isfile(path):
            raise FileNotFoundError("File path not found : " + path)
        return json.load(open(path))
