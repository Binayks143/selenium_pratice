from callhub.campaign_page_class import campaign_page
from callhub.helper_class import HelpertestStatus
from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def OneTimeSetup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.callhub.io/")
    driver.implicitly_wait(2)
    # Attach the driver to the class so that it is accessible in tests
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("OneTimeSetup")
class TestCampaign:
    # test data
    __userName="binay.tite@gmail.com"
    __password="Binay123@"
    __selectCampaign="Call Center Campaign"


    @pytest.fixture(autouse=True)
    def launchSetup(self,OneTimeSetup):
        self.ts=HelpertestStatus(self.driver)
        self.camp=campaign_page(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.camp.enter_username(self.__userName)
        self.camp.click_on_next_button()
        self.camp.enter_password(self.__password)
        self.camp.click_on_sign_in_button()

        result=self.camp.login_check()
        self.ts.markFinal("Valid Login Check",result,"User is able to logged in successfully")

    @pytest.mark.run(order=2)
    def test_checkCreateCampaignLink(self):
        self.camp.create_campaign_link_click()
        result=self.camp.compaign_type_check_popup()
        self.ts.markFinal("Check Create campaign link functionality",result,
                          "user is able to click on Create Campaign link and 'Select Campaign "
                          "Type' pop up is displaying")


    @pytest.mark.run(order=3)
    def test_select_call_centre_Campaign(self):
        self.camp.select_campaign_option(self.__selectCampaign)
        result=self.camp.check_selected_campaign()
        self.ts.markFinal("Campaign Selected test",result,"User is able to select the campaign")

    @pytest.mark.run(order=4)
    def test_validate_new_ccc(self):
        self.camp.click_campaign_next_button()
        result=self.camp.check_new_ccs_form()
        self.ts.markFinal("Selecting campaign and confirming selected option",result,
                          "User is able to land in New Call Center Campaign page")











