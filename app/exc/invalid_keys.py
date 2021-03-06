class InvalidKeys(Exception):
    def __init__(self, data: dict) -> None:
        self.message = {
        "required_key": "name",
        "received_keys": self.wrong_key(data)
    }

    @classmethod
    def wrong_key(cls, data: dict) -> list:
        return [key for key in data.keys()]

class EmpytKey(Exception):
    def __init__(self) -> None:
        self.message = {
        "error": "Category name is required"
    }

class InvalidUpdatedKeys(Exception):
    def __init__(self, data: dict) -> None:
        self.message = {
        "available_keys": ["name", "description"],
        "received_keys": self.wrong_key(data)
    }

    @classmethod
    def wrong_key(cls, data: dict) -> list:
        return [key for key in data.keys() if key not in ["name", "description"]]

class InvalidValues(Exception):
    def __init__(self, data: dict) -> None:
        self.message = {
        "available_value": [{"importance": "1 or 2", "urgency": "1 or 2"}],
        "received_values": [data]
    }

available_keys = ["name", "description", "duration", "importance", "urgency", "categories"]
class InvalidTasksKeys(Exception):
    def __init__(self, data: dict) -> None:
        self.message = {
        "available_keys": available_keys,
        "received_keys": self.wrong_key(data)
    }

    @classmethod
    def wrong_key(cls, data: dict) -> list:
        return [key for key in data.keys() if key not in available_keys]
