from selene.support.shared import browser
from selene.support.conditions import have
from tests.helpers import resourses
from tests.helpers.users import olga


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def choose_gender(self, gender):
        browser.all('.custom-radio').element_by(have.text(gender)).click()

    def fill_mobile(self, mobile):
        browser.element("#userNumber").type(mobile)

    def fill_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(olga.date_of_birth.strftime('%B'))
        browser.element('.react-datepicker__year-select').send_keys(olga.date_of_birth.year)
        browser.element(f'.react-datepicker__day--0{olga.date_of_birth.strftime("%d")}').click()

    def fill_subject(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def choose_hobbies(self):
        browser.element('div.col-md-9.col-sm-12 > div:nth-child(2) > [for="hobbies-checkbox-2"]').click()

    def upload_picture(self, picture):
        browser.element("#uploadPicture").send_keys(resourses.path(picture))

    def fill_current_address(self, current_address):
        browser.element("#currentAddress").type(current_address)
        browser.execute_script("window.scrollTo(0, 500)")

    def fill_state(self, state):
        browser.element("#state").click().all('[id^="react-select-3-option"]').element_by(
            have.exact_text(state)
        ).click()

    def fill_city(self, city):
        browser.element("#city").click().all('[id^="react-select-4-option"]').element_by(
            have.exact_text(city)
        ).click()

    def submit(self):
        browser.element("#userNumber").press_enter()

    def text_should_successful(self, text):
        browser.element(".modal-title").should(
            have.exact_text(text)
        )

    def registration(self):
        self.open()
        self.fill_first_name(olga.full_name[0])
        self.fill_last_name(olga.full_name[1])
        self.fill_email(olga.email)
        self.choose_gender(olga.gender)
        self.fill_mobile(olga.mobile)
        self.fill_date_of_birth()
        self.fill_subject(olga.subject)
        self.choose_hobbies()
        self.upload_picture(olga.picture)
        self.fill_current_address(olga.current_address)
        self.fill_state(olga.state)
        self.fill_city(olga.city)
        self.submit()

    def should_registered_user(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f"{olga.full_name[0]} {olga.full_name[1]}",
                             f"{olga.email}",
                             f"{olga.gender}",
                             f"{olga.mobile}",
                             '{0} {1},{2}'.format(
                                 olga.date_of_birth.strftime("%d"), olga.date_of_birth.strftime("%B"),
                                 olga.date_of_birth.strftime("%Y")),
                             f"{olga.subject}",
                             f"{olga.hobbies}",
                             f"{olga.picture}",
                             f"{olga.current_address}",
                             f"{olga.state} {olga.city}"))
