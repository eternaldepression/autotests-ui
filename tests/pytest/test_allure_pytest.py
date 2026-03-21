import allure


@allure.step('Opening browser')
def open_browser():
    ...


@allure.step('Creating course')
def create_course():
    ...


@allure.step('Closing browser')
def close_browser():
    ...


def test_feature():
    open_browser()
    create_course()
    close_browser()
