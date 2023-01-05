import time, csv
from uuid import uuid1
from typing import List
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import date

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lib.page import LoginPage, HomePage, CreateClient, ClientName, AddClient, SearchClient, EditClient, CreateClientFromCampaign
from lib.resources import LoginResources, ClientModuleResource, SearchClientResource, EditClientResource, CreateClientFromCamResource

USER_Name = "Usman_AU_Testing"
PASS_Word = "Usman@112"


Client_name = "hcaxzn12167"
Client_name1 = "hsdvsdvaxn1213"
Client_name2 = "haasdvsxsxan12"


def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = 'w' if new else 'a'
    with open(filename, mode, newline='') as f:
        f.writelines(data)
        

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

# Login Page===

    login_page = LoginPage(driver)
    login_page.enter_username(LoginResources.USERNAME, USER_Name)
    login_page.enter_password(LoginResources.PASSWORD, PASS_Word)
    url_a = (driver.current_url)
    success = login_page.click_login_btn(LoginResources.LOGIN_BTN)
    make_csv('Client Report.csv', 'Client Module Report\n')
    today = date.today()
    make_csv('Client Report.csv', f'Test Case,Scenario,Detailed Results\n', new=False)
    make_csv('Campaign Report.csv', '\n', new=False)
    make_csv('Client Report.csv', f'Date:{today}\n', new=False)
    if success:
        make_csv('Client Report.csv', f'Login Page,Login With Correct Username & Password,Login Successfull,{url_a}\n', new=False)
    else:
        make_csv('Client Report.csv', 'Login Page,Login With Correct Username & Password,Invalid Credentials\n', new=False)

# Click on the client module====

    Home_Mod = HomePage(driver)
    Home_Mod.click_client_btn(ClientModuleResource.Client_Module)
    url_b = (driver.current_url)
    make_csv('Client Report.csv', f'Client Module,Click on Client Button,Successfull,{url_b}\n', new=False)
 
 # Click on the Create lient module====   

    CreateClient_Mod = CreateClient(driver)
    CreateClient_Mod.Click_Create_Client_btn(ClientModuleResource.Create_Client)
    url_c = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Click on Create Client Button,Successfull,{url_c}\n', new=False)

# Check Special Chracter and Limtation while creating Client ==== 
 
    Client_Mod = ClientName(driver)
    time.sleep(1)
    Client_Mod.enter_Client_Name(ClientModuleResource.CLIENTNAME, "@#!$%^&*")
    url_d = (driver.current_url)
    Pop_nam = driver.find_element(By.XPATH, "//*[@class='mt-2 text-danger warning-text']").text
    make_csv('Client Report.csv', f'Create Client,Check Special Chracters are not allowed,{Pop_nam},{url_d}\n', new=False)
    time.sleep(.5)
    
    Name_Clear = driver.find_element(By.XPATH,"//*[@id='client_name']").clear()
    
    time.sleep(.5)
    
    Client_Mod1 = ClientName(driver)
    time.sleep(.5)
    Client_Mod1.enter_Client_Name(ClientModuleResource.CLIENTNAME, "vosdfihvcbiudspvjhkldzsjvkluzdxghbvhjzcxhkdxvbhkdsvbhdsbvjshcbvsdhbvhjzxbvgxjhzcbkxcbjkbzhbjnvhfbghdc")  
    Pop_nam1 = driver.find_element(By.XPATH, "//*[@class='mt-2 text-danger warning-text']").text
    url_e = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Check 100 Chracters limitation,{Pop_nam1},{url_e}\n', new=False)
    time.sleep(.5)
    
    Name_Clear1 = driver.find_element(By.XPATH,"//*[@id='client_name']").clear()
    
    time.sleep(.5)
    
    Client_Mod2 = ClientName(driver)
    time.sleep(.5)
    Client_Mod2.enter_Client_Name(ClientModuleResource.CLIENTNAME, Client_name)
    url_f = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Enter Correct Client Name,Successfull,{url_f}\n', new=False)
    time.sleep(.5)
    
    Add_Client = AddClient(driver)
    Add_Client.add_client_Btn(ClientModuleResource.ADDCLIENT)
    Create_clientt = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "popUpMessage"))
    )
    Pop_namee = driver.find_element(By.ID, "popUpMessage").text
    url_g = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Click on ADD Client Button,{Pop_namee},{url_g}\n', new=False)
    time.sleep(3)
    
# Search Client on front end====

    Client_Mod3 = SearchClient(driver)
    time.sleep(.5)
    Client_Mod3.Search_Client_Name(SearchClientResource.Search_Bar, Client_name) 
    Create_clien1t = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='compaign-holder-name']"))
    )
    time.sleep(5)
    Pop_namwe = driver.find_element(By.XPATH, f'//*[contains(normalize-space(),"{Client_name}")][@class="compaign-holder-name"]').text 
    url_h = (driver.current_url)
    make_csv('Client Report.csv', f'Search Client,Search Client on front End,{Pop_namwe},{url_h}\n', new=False)
    time.sleep(3)

# Edit client===
   
    Edit_Client = EditClient(driver)
    Edit_Client.Edit_Client_1(EditClientResource.edit_client1)
    time.sleep(1)
    
    Edit_Client = EditClient(driver)
    Edit_Client.Edit_Client_2(EditClientResource.edit_client2)
    time.sleep(1)
    url_i = (driver.current_url)
    make_csv('Client Report.csv', f'Edit Client,Edit Client after search new created client,Successfull,{url_i}\n', new=False)
    time.sleep(1)
   
    Edit_Client_102 = driver.find_element(By.XPATH, "//*[@id='client_name-edit-id']").clear()
    time.sleep(0.5) 
    
    Edit_Client = EditClient(driver)
    time.sleep(.5)
    Edit_Client.Edit_Client_Name(EditClientResource.EDITCLIENTNAME, Client_name1) 
    url_j = (driver.current_url)
    make_csv('Client Report.csv', f'Edit Client,Enter new client name,Successfull,{url_j}\n', new=False)
    time.sleep(0.5)
    
    Edit_Client = EditClient(driver)
    time.sleep(.5)
    Edit_Client.Edit_CLient_btn(EditClientResource.EDITCLIENT_BTN)
    url_k = (driver.current_url)
    Create_clien2t = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "popUpMessage"))
    )
    Pop_namvt = driver.find_element(By.ID, "popUpMessage").text
    make_csv('Client Report.csv', f'Edit Client,Click on Edit Client Button,{Pop_namvt},{url_k}\n', new=False)
    time.sleep(2)

# Seach Client after edit on front end===
 
    Client_Mod3 = SearchClient(driver)
    time.sleep(.5)
    url_l = (driver.current_url)
    Client_Mod3.Search_Client_Name(SearchClientResource.Search_Bar, Client_name1)
    Create_clien9t = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='compaign-holder-name']"))
    )
    time.sleep(5)
    Pop_nampz = driver.find_element(By.XPATH, f'//*[contains(normalize-space(),"{Client_name1}")][@class="compaign-holder-name"]').text 
    make_csv('Client Report.csv', f'Search Client,Search Client on front end after edit client,{Pop_nampz},{url_l}\n', new=False)
    make_csv('Client Report.csv', 'Create Client,Create Client From Campaign Module,Creating new client\n', new=False)
    time.sleep(3)
    
    
 # # """"""""""""Create Client From Campaign Module"""

# Click on campaign button to create new client
 
    Cam_module = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_module.click_Campaign(CreateClientFromCamResource.campaign_btn)  
    url_m = (driver.current_url)
    make_csv('Client Report.csv', f'Campaign Module,Click on Campaign Button,Successfull,{url_m}\n', new=False)
    time.sleep(2)

# Click on Create campaign button to create new client
   
    Cam_Module1 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_Module1.Click_Create_cam_btn(CreateClientFromCamResource.Create_campaign_btn)
    url_n = (driver.current_url)  
    make_csv('Client Report.csv', f'Create Campaign,Click on Create Campaign Button,Successfull,{url_n}\n', new=False)
    time.sleep(1)
    
# Click on Create client button in create campain page
    
    Cam_module2 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_module2.Create_Client_from_cam(CreateClientFromCamResource.Create_client_btn) 
    url_o = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Click on Create Client button in campaign creation page,Successfull,{url_o}\n', new=False)
    time.sleep(2)

# Check 100 chracter and specail chracter while creating client from create campaign page==
   
    Cam_Module3 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_Module3.add_client_nam(CreateClientFromCamResource.Add_client_name, "@#$@%#^#@%@%")
    Pop_nammt = driver.find_element(By.XPATH, "//*[@id='edit-campaign-client']").text 
    url_p = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Check Special Chracters are not allowed while creating client,{Pop_nammt},{url_p}\n', new=False)  
    time.sleep(1)
    
    Clear_name1 = driver.find_element(By.XPATH,"//*[@id='campaign-client-name-cam']").clear()
    
    
    Cam_Module3 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_Module3.add_client_nam(CreateClientFromCamResource.Add_client_name, "vosdfihvcbiudspvjhkldzsjvkluzdxghbvhjzcxhkdxvbhkdsvbhdsbvjshcbvsdhbvhjzxbvgxjhzcbkxcbjkbzhbjnvhfbghdc")  
    Pop_nam7 = driver.find_element(By.XPATH, "//*[@id='edit-campaign-client']").text
    url_q = (driver.current_url)
    make_csv('Client Report.csv', f'Create Client,Check 100 Chracters limitation while creating client,{Pop_nam7},{url_q}\n', new=False)
    time.sleep(1)
    
    Clear_name2 = driver.find_element(By.XPATH,"//*[@id='campaign-client-name-cam']").clear()
    
    Cam_Module3 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_Module3.add_client_nam(CreateClientFromCamResource.Add_client_name, Client_name2)
    url_r = (driver.current_url) 
    make_csv('Client Report.csv', f'Create Client,Enter Correct Client Name while creating client from campaign creation page,Successfull,{url_r}\n', new=False)
    time.sleep(1)
    
    Cam_module5 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    url_s = (driver.current_url)
    Cam_module5.add_client_btn1(CreateClientFromCamResource.add_client_btn) 
    Create_clien19t = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "popUpMessage"))
    )
    Pop_namcg = driver.find_element(By.ID, "popUpMessage").text
    make_csv('Client Report.csv', f'Create Client,Click on Add Client Button while creating client from campaign creation page,{Pop_namcg},{url_s}\n', new=False)
    time.sleep(3)

# Click on client module button 
  
    Cam_module18 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Cam_module18.client_btn12(CreateClientFromCamResource.Client_mod14) 
    url_t = (driver.current_url) 
    make_csv('Client Report.csv', f'Client module,Click on Client module Button,Successfull,{url_t}\n', new=False)
    time.sleep(2)

# Search client on front end 
 
    Search_Client12 = CreateClientFromCampaign(driver)
    time.sleep(.5)
    Search_Client12.Search_new_client(CreateClientFromCamResource.Search_Bar1, Client_name2)
    url_u = (driver.current_url)
    Create_clien15t = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='compaign-holder-name']"))
    )
    time.sleep(5)
    Pop_namxp = driver.find_element(By.XPATH, f'//*[contains(normalize-space(),"{Client_name2}")][@class="compaign-holder-name"]').text 
    make_csv('Client Report.csv', f'Search Client,Search client on front end after create client from campaign creation page ,{Pop_namxp},{url_u}\n', new=False)
    make_csv('Client Report.csv', f'Login Credentials,Username:{USER_Name},Password:{PASS_Word}\n', new=False) 
    
    
    time.sleep(5)
if __name__ == '__main__':
    main()