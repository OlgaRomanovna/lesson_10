import dataclasses


@dataclasses.dataclass
class User:
    full_name: list[str]
    email: str
    mobile: int
    date_of_birth: str
    subject: str
    picture: str
    current_address: str
    state: str
    city: str



olga = User(full_name=['Olga', 'N'], email='super+admin@gmail.com', mobile=9999999999,
            date_of_birth="April 9th, 1995", subject="B", picture="cat.jpeg", current_address="Krasnodar",
            state="Haryana", city="Karnal")
