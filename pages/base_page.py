from playwright.sync_api import Page


class BasePage:
    def __int__(self,page:Page):
        self.page=page
        self.base_url="https://automationexercise.com"
    def navigate (self,endpoint:str=""):
        url=f"{self.base_url}/{endpoint}"if endpoint else self.base_url
        self.page.goto(url)


       #get the cutrent title
    def get_current_title(self):
            return self.page.title()

    def wait_for_url(self,endpoint:str):
        self.page.wait_for_url(f"{self.base_url}/{endpoint}")
























