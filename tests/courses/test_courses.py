import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_courses_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_courses_page.create_course_form_component.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_courses_page.create_course_exercises_toolbar_view_component.check_visible()
        create_courses_page.check_visible_exercises_empty_view()
        create_courses_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_courses_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_courses_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        create_courses_page.create_course_exercises_toolbar_view_component.click_create_exercise_button()

        create_courses_page.create_course_toolbar_view_component.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    def test_edit_course(self, create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_courses_page.create_course_form_component.fill(
            title="Pytest",
            estimated_time="9 weeks",
            description="Pytest",
            max_score="99",
            min_score="9"
        )
        create_courses_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_courses_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Pytest",
            max_score="99",
            min_score="9",
            estimated_time="9 weeks"
        )
        courses_list_page.courses_view_menu.click_edit(index=0)
        create_courses_page.create_course_form_component.fill(
            title="Java",
            estimated_time="6 days",
            description="Java",
            max_score="66",
            min_score="6"
        )
        create_courses_page.create_course_toolbar_view_component.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Java",
            max_score="66",
            min_score="6",
            estimated_time="6 days"
        )
