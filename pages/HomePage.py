from AppiumFramework.base.BasePage import BasePage
import time


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _register = 'Register' # text
    _firstName = 'First Name' #text
    _customerCentre = 'Customer Centre'
    _searchButton = 'android.widget.EditText' #class
    _categories = 'Categories' #desc
    _emailAddressField = 'Email Address' #text
    _yourPassword = 'Your Password' #text
    _loginButton = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'

    def openCategories(self):
        print('id customer centre present', self.isDisplayed(self._categories, 'des'))
        self.waitForElement(self._categories, 'des')
        self.clickElement(self._categories, 'des')

    def openRegisterFrom(self):
        self.waitForElement(self._customerCentre, 'text')
        self.clickElement(self._customerCentre, 'text')
        return self.isDisplayed(self._register, 'text')

    def login(self):
        self.waitForElement(self._emailAddressField, 'text')
        self.sendText('blabla@gmail.com', self._emailAddressField, 'text')
        self.waitForElement(self._yourPassword, 'text')
        self.sendText('dummypassword', self._yourPassword, 'text')
        self.clickElement(self._loginButton, 'xpath')
        return self.isDisplayed(self._loginButton, 'xpath')
