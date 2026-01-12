import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage

from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_icon_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_icon_element).to_be_visible()

    no_results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_block).to_be_visible()
    expect(no_results_block).to_have_text('There is no results')

    results_from_the_load_test = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_from_the_load_test).to_be_visible()
    expect(results_from_the_load_test).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_courses_page.check_visible_create_course_title()
    create_courses_page.check_disabled_create_course_button()
    create_courses_page.check_visible_image_preview_empty_view()
    create_courses_page.check_visible_image_upload_view()
    create_courses_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_courses_page.check_visible_exercises_title()
    create_courses_page.check_visible_create_exercise_button()
    create_courses_page.check_visible_exercises_empty_view()
    create_courses_page.upload_preview_image('./testdata/files/image.png')
    create_courses_page.check_visible_image_upload_view()
    create_courses_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_courses_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
