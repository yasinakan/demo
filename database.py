class Database:
    _instance = None

    def __init__(self):
        Database._instance = self

    @classmethod
    def get_instance(cls):
        return cls._instance