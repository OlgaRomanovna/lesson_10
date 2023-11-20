from lesson_10.pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name("Olga")
    registration_page.fill_last_name("N")
    registration_page.fill_email("olgaN@mail.ru")
    registration_page.choose_gender()
    registration_page.fill_mobile("9999999999")
    registration_page.fill_date_of_birth("April 9th, 1995")
    registration_page.fill_subject("B")
    registration_page.choose_hobbies()
    registration_page.upload_picture("cat.jpeg")
    registration_page.fill_current_address("Krasnodar")
    registration_page.fill_state("Haryana")
    registration_page.fill_city("Karnal")
    registration_page.submit()
    registration_page.text_should_successful("Thanks for submitting the form")
    registration_page.should_registered_user("Olga N",
                                             "olgaN@mail.ru",
                                             "Female",
                                             "9999999999",
                                             "09 April,1995",
                                             "Biology",
                                             "Reading",
                                             "cat.jpeg",
                                             "Krasnodar",
                                             "Haryana Karnal")






