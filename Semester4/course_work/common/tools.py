from datetime import datetime


class Tools:
    datetime_format = '%Y-%m-%d %H:%M:%S'
    
    @staticmethod
    def datetime_to_string(datetime: datetime | None) -> str | None:
        if not datetime:
            return
        return datetime.strftime(Tools.datetime_format)
    
    @staticmethod
    def string_to_datetime(string: str | None) -> datetime | None:
        if not string:
            return
        return datetime.strptime(string, Tools.datetime_format)

    @staticmethod
    def generate_secret_key(login: str, password: str) -> str:
        return login + password