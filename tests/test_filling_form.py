from lesson_10.pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()
    registration_page.registration()
    registration_page.should_registered_user()






