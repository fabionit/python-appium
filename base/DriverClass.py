from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 3 API 29'
        desired_caps['app'] = ('/Users/fabian.onit/PythonProjects/Appium/thomann.apk')
        desired_caps['appPackage'] = 'de.thomann'
        desired_caps['appActivity'] = 'de.thomann.android.MainActivity'
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver
