import os
from selene import browser
from selene.support.conditions import have


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def choose_gender(self):
        browser.element(
            'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="gender-radio-2"]'
        ).click()

    def fill_mobile(self, mobile):
        browser.element("#userNumber").type(mobile)

    def fill_date_of_birth(self, date_of_birth):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().all("option").element_by(
            have.exact_text("April")
        ).click()
        browser.element(".react-datepicker__year-select").click().all("option").element_by(
            have.exact_text("1995")
        ).click()
        browser.element(f'[aria-label="Choose Sunday, {date_of_birth}"]').click()

    def fill_subject(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def choose_hobbies(self):
        browser.element(
            'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="hobbies-checkbox-2"]'
        ).click()

    def upload_picture(self, picture):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"helpers/{picture}"))

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

    def should_registered_user(self, full_name, email, gender, mobile, date_of_birth, subject,
                               hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile,
                date_of_birth,
                subject,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )
        return self