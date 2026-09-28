from pages.base_page import BasePage
from playwright.sync_api import Page
class LoginPage(BasePage):

    def __init__(self,page:Page):
       super().__init__(page)

       self.email_input = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
       self.password_input = page.get_by_role("textbox", name="Password")
       self.login_btn = page.get_by_role("button", name="Login")
       self.name=page.get_by_role("textbox",name="name")

       #new user
       self.name_input= page.get_by_role ("textbox", name ="name")
       self.email_input=page.locator ("form").filter(has_text="signup").get_by_placeholder("Email Address")
       self.signup_btn=page.get_by_role("button",name="signup")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_btn.click()

    def New_user(self, name:str, email:str,):
         self.signup_btn.click()
         self.email_input.fill(email)
         self.name_input.fill(name)