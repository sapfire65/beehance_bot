import pytest
from base.base_page import BasePage
from pages.start_page import StartPage
from pages.searching_results import SerchResults
from pages.user_profile import UserProfile
from pages.content_page import ContentPage


class TestBase:
    base_page: BasePage
    start_page: StartPage
    searching_results: SerchResults
    user_profile: UserProfile
    content_page: ContentPage

    @pytest.fixture(autouse=True)
    def setup(self, request, chrome_driver):
        request.cls.chrome_driver = chrome_driver

        request.cls.base_page = BasePage(chrome_driver)
        request.cls.start_page = StartPage(chrome_driver)
        request.cls.searching_results = SerchResults(chrome_driver)
        request.cls.user_profile = UserProfile(chrome_driver)
        request.cls.content_page = ContentPage(chrome_driver)
