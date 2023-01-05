from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    url = "https://staging.brandsignals.io/"
    
        
    def enter_username(self, xpath: str, username: str):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, xpath).send_keys(username)
        
    def enter_password(self, xpath: str, password: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(password)

    def click_login_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        return 'Invalid Credentials' not in self.driver.page_source

class HomePage(BasePage):
    
    def click_client_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()

class CreateClient(BasePage):
    
    def Click_Create_Client_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
class ClientName(BasePage):
    
    def enter_Client_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
        
class AddClient(BasePage):
    
    def add_client_Btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
class SearchClient(BasePage):
    
    def Search_Client_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
    
class EditClient(BasePage):
    
    def Edit_Client_1(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
    def Edit_Client_2(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
    def Edit_Client_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
    
    def Edit_CLient_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
class CreateClientFromCampaign(BasePage):
    
    def click_Campaign(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
    def Click_Create_cam_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
    def Create_Client_from_cam(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
    def add_client_nam(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname) 
    
    def add_client_btn1(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
    def client_btn12(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
    
    def Search_new_client(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)