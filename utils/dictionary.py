class Dictionary:
    def __init__(self):
        self.name = "first_name()"
        self.address = "address()"
        self.email = "email()"
        #automotive
        self.license_plate = "license_plate()"
        self.vin = "vin()"
        self.bank = "bank()"
        self.barcode = "barcode()"
        self.color = "color()"
        self.company = "company()"
        self.credit_card = "credit_card()"
        self.currency = "currency()"
        self.date_time = "date_time()"
        self.emoji = "emoji()"
        self.file = "file()"
        self.geo = "geo()"
        self.internet = "internet()"
        self.isbn = "isbn()"
        self.job = "job()"
        self.lorem = "lorem()"
        self.misc = "misc()"
        self.passport = "passport()"
        self.person = "person()"
        self.phone_number = "phone_number()"
        self.profile = "profile()"
        self.sbn = "sbn()"
        self.ssn = "ssn()"
        self.user_agent = "user_agent()"

    def get(self, var: str) -> str:
        if hasattr(self, var):
            return getattr(self, var)
        else:
            raise Exception("Data Type not Valid!")

