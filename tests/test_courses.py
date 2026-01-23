import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage

from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()

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
