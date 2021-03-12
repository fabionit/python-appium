import unittest
import pytest
from AppiumFramework.pages.HomePage import HomePage
import time


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class HomePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_openHomePage(self):
        time.sleep(30)
        registerDisplayed = self.hp.openRegisterFrom()
        assert registerDisplayed == True
        loginFailed = self.hp.login()
        print('login failed', loginFailed)
        assert loginFailed == True