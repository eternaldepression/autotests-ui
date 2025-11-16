from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        empty_icon_element = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon_element).to_be_visible()

        no_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_block).to_be_visible()
        expect(no_results_block).to_have_text('There is no results')

        results_from_the_load_test = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_from_the_load_test).to_be_visible()
        expect(results_from_the_load_test).to_have_text('Results from the load test pipeline will be displayed here')
