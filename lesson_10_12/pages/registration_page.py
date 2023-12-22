import allure
from selene.support.conditions import have
from selene.support.shared import browser
from tests.helpers.resources import path


class RegistrationPage:

    def open(self):
        with allure.step("Открытие браузера"):
            browser.open("/automation-practice-form")

    def fill_first_name(self, first_name):
        with allure.step("Заполнение поля Имя"):
            browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_name):
        with allure.step("Заполнение поля Фамилия"):
            browser.element("#lastName").type(last_name)

    def fill_email(self, email):
        with allure.step("Заполнение поля Электронная почта"):
            browser.element("#userEmail").type(email)

    def choose_gender(self):
        with allure.step("Выбор радиобаттона Пол"):
            browser.element(
            'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="gender-radio-2"]'
        ).click()

    def fill_mobile(self, mobile):
        with allure.step("Заполнение поля Мобильный телефон"):
            browser.element("#userNumber").type(mobile)

    def fill_date_of_birth(self, date_of_birth):
        with allure.step("Выбор в календаре Даты рождения"):
            browser.element("#dateOfBirthInput").click()
            browser.element(".react-datepicker__month-select").click().all("option").element_by(
            have.exact_text("April")
        ).click()
            browser.element(".react-datepicker__year-select").click().all("option").element_by(
            have.exact_text("1995")
        ).click()
            browser.element(f'[aria-label="Choose Sunday, {date_of_birth}"]').click()

    def fill_subject(self, subject):
        with allure.step("Заполнение поле Субъект"):
            browser.element("#subjectsInput").type(subject).press_enter()

    def choose_hobbies(self):
        with allure.step("Выбор чекбокса Хобби"):
            browser.element(
            'div.col-md-9.col-sm-12 > div:nth-child(2) > [for="hobbies-checkbox-2"]'
        ).click()

    def upload_picture(self, picture):
        with allure.step("Загрузка Фото"):
            browser.element("#uploadPicture").send_keys(path(picture))

    def fill_current_address(self, current_address):
        with allure.step("Заполнение поля Адреса"):
            browser.element("#currentAddress").type(current_address)
            browser.execute_script("window.scrollTo(0, 500)")

    def fill_state(self, state):
        with allure.step("Заполнение поля Штат"):
            browser.element("#state").click().all('[id^="react-select-3-option"]').element_by(
            have.exact_text(state)
        ).click()

    def fill_city(self, city):
        with allure.step("Заполнение поля Город"):
            browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        with allure.step("Нажатие на кнопку Submit"):
            browser.element("#userNumber").press_enter()

    def text_should_successful(self, text):
        with allure.step("Проверка Заголовка алерта"):
            browser.element(".modal-title").should(
            have.exact_text(text)
        )

    def should_registered_user(self, full_name, email, gender, mobile, date_of_birth, subject,
                               hobbies, picture, current_address, state_and_city):
        with allure.step("Проверка заполненной формы"):
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