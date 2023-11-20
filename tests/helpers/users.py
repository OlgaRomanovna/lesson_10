import dataclasses
import datetime


@dataclasses.dataclass
class User:
    full_name: list[str]
    email: str
    gender: str
    mobile: int
    date_of_birth: datetime.date
    subject: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str


olga = User(full_name=['Olga', 'N'], email='o.romanovna@gmail.com', gender='Female', mobile=9999999999,
            date_of_birth=datetime.date(day=9, month=4, year=1995), subject="Biology", hobbies="Reding", picture="cat.jpeg",
            current_address="Krasnodar", state="Haryana", city="Karnal")
