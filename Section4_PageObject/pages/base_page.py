class BasePage(object):

    def __init__(self, browser, url):
        self.brower = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)




