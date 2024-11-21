import logging

from callhub.selenium_base_class import SeleniumDriver
from callhub.custom_logger import customLogger as cl


class campaign_page(SeleniumDriver):
    log = cl(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    username = "id_user"  # id
    next_button = 'change-btn-text'  # id
    password_field = "password"  # name
    sign_in_button = '//button[@id="change-btn-text"]'  # xpath
    user_login_icon = '//span[contains(text(),"Binay")]'  # xpath
    create_campaign = "Create Campaign"  # linktext
    compaign_type_check = '//h3[contains(text(),"Select Campaign Type")]'  # xpath
    select_campaign = "campaignType"  # id
    selected_campaign = '//h4[contains(text(),"Call Center Campaign")]'  # xpath
    campaign_next_button = "createCampaign"  # id
    new_ccc_page = "#cc-script"  # css

    def enter_username(self, username):
        self.sendKeys(username, self.username, "id")

    def click_on_next_button(self):
        self.elementClick(self.next_button)

    def enter_password(self, password):
        self.sendKeys(password, self.password_field, "name")

    def click_on_sign_in_button(self):
        self.elementClick(self.sign_in_button, "xpath")

    def login_check(self):
        return self.isElementPresent(self.user_login_icon, "xpath")

    def create_campaign_link_click(self):
        self.elementClick(self.create_campaign, "linktext")

    def compaign_type_check_popup(self):
        return self.isElementPresent(self.compaign_type_check, "xpath")

    def select_campaign_option(self, data):
        self.selectDropdownOption(self.select_campaign, "id", "visibleText", data)

    def check_selected_campaign(self):
        return self.isElementPresent(self.selected_campaign, "xpath")

    def click_campaign_next_button(self):
        self.elementClick(self.campaign_next_button)

    def check_new_ccs_form(self):
        return self.isElementPresent(self.new_ccc_page, "css")
