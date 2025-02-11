import re
from datetime import datetime


class TextHelper:
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def format_date(date_str):
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return None

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?\d{10,15}$"
        return bool(re.match(pattern, phone))
