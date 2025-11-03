from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_input_registration = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input_registration.fill('user.name@gmail.com')

    username_input_registration = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input_registration.fill('username')

    password_input_registration = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input_registration.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
