import sys
sys.path.insert(0, '/Users/joshuaokungbowa/PycharmProjects/HomeEquityBot')
from selenium.webdriver.common.by import By
import json
from govhomeprogram_actions import GovhomeActions
from home_equity_actions import HomeEquityActions as HEQActions
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
from selenium.webdriver.chrome.options import Options
import requests
from input_data_model import BotInputModel


def main(data):
    # Initialise Home Equity Quiz Actions

    run = 1
    include_city = True
    while run <= 50:
        try:
            run += 1
            if include_city:
                driver, json_ip = setup_driver_proxy(data.city, data.state)
            else:
                driver, json_ip = setup_driver_proxy("", data.state)
            json_object = json.loads(json_ip)
            ip = json_object['ip']
            if not ip.__contains__(data.last_ip):
                break
            else:
                driver.quit()
        except Exception as e:
            include_city = False
            driver.quit()

    if data.url == "https://tr4ckme.com/?a=41&c=9&s1=":
        # Launch Govhomeprog
        action = GovhomeActions(driver)
        govhomeprog_steps(action, data)
    elif data.url == "http://tr4ckme.com/?a=41&c=60&s1=":
        action = HEQActions(driver)
        home_equity_quiz_steps(action, data)

    r = requests.post("https://arlo.tycoonmach.net/api/logip", data={'url': data.url, 'ip': ip})
    if not r.status_code == 200:
        raise Exception()


def govhomeprog_steps(action, data):
    action.launch(action.driver, "https://tr4ckme.com/?a=41&c=9&s1=")
    time.sleep(5)

    action.select_block_push()
    time.sleep(2)

    action.select_own_home()
    time.sleep(2)

    action.enter_zipcode(data.zip_code)
    time.sleep(2)
    action.click_next()
    time.sleep(2)

    if data.military_spouse.upper() == "YES":
        action.answer_military_spouse(True)
    else:
        action.answer_military_spouse(False)
    time.sleep(2)

    action.select_estimated_credit(data.credit_score)
    time.sleep(2)

    action.select_house_type(data.house_type)
    time.sleep(2)

    action.adjust_prop_val_slider(data.property_value)
    time.sleep(2)

    action.adjust_mort_bal_slider(data.mort_balance)
    time.sleep(2)

    action.click_next()
    time.sleep(2)

    if data.addtional_cash == "0":
        action.answer_add_cash(False)
    else:
        action.answer_add_cash(True)
    time.sleep(2)

    action.select_future_plan(data.use_money)
    time.sleep(2)

    action.adjust_mort_intr_slider(data.mort_intr_rate)
    time.sleep(2)
    action.click_next()
    time.sleep(2)

    action.select_loan_type(data.loan_type)
    time.sleep(2)

    action.select_lender(data.lender)
    action.click_next()
    time.sleep(2)

    if data.employed.upper() == "YES":
        action.select_employment_status("EMPLOYED")
    else:
        action.select_employment_status("UNEMPLOYED")
    time.sleep(2)

    action.enter_address(data.address)
    action.click_next()
    time.sleep(2)

    action.enter_details(data.first_name, data.last_name, data.email_address, data.phone)
    time.sleep(2)

    action.click_see_results()
    time.sleep(2)

    action.wait_for_last_screen()
    time.sleep(10)

    action.driver.quit()


def home_equity_quiz_steps(action, data):
    action.launch(action.driver, "http://tr4ckme.com/?a=41&c=60&s1=")
    time.sleep(5)

    # Select Refinance
    action.select_refinance()
    time.sleep(2)
    # select house type
    action.select_house_type(data.house_type)
    time.sleep(2)
    # select credit score
    action.select_estimated_credit(data.credit_score)
    time.sleep(2)
    # Set estimated property value
    action.adjust_prop_val_slider(data.property_value)
    action.click_continue()
    time.sleep(2)
    # Set mortgage balance for first house
    action.adjust_mort_bal_slider(data.mort_balance)
    action.click_continue()
    time.sleep(2)
    # Set mortgage interest on first house
    action.adjust_mort_intr_slider(data.mort_intr_rate)
    time.sleep(2)

    action.click_continue()
    time.sleep(2)
    # select loan type
    action.select_rate_type(data.rate_type)
    time.sleep(2)
    # select second mortgage
    action.answer_second_mort(False)
    time.sleep(2)

    action.adjust_additional_cash_slider(data.addtional_cash)
    time.sleep(2)

    action.click_continue()
    time.sleep(2)

    # select bankruptcy
    if data.bankruptcy == "YES":
        action.answer_bankruptcy(True)
    else:
        action.answer_bankruptcy(False)
    time.sleep(2)

    # Answer verify income question
    action.answer_verify_income(True)

    # answer late payments question
    action.select_late_payment("none")

    # Answer Military wife question
    if data.military_spouse == "YES":
        action.answer_military_spouse(True)
    else:
        action.answer_military_spouse(False)
    time.sleep(2)

    if data.home_improvements == "YES":
        action.answer_home_improve(True)
    else:
        action.answer_home_improve(False)
    time.sleep(2)

    action.enter_address(data.address, data.zip_code)
    time.sleep(2)
    action.click_continue()
    time.sleep(2)

    action.enter_details(data.first_name,
                         data.last_name,
                         data.email_address,
                         data.phone[0:3],
                         data.phone[3:6],
                         data.phone[6:10]
                         )
    time.sleep(2)

    action.click_continue()
    time.sleep(2)

    action.wait_for_last_screen()
    time.sleep(10)

    action.driver.quit()


def setup_driver_proxy(city: str, state: str):
    manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""
    if city == "":
        user = "lum-customer-c_dffa1e0f-zone-arlo1-country-us-state-" + state.lower()
    else:
        user = "lum-customer-c_dffa1e0f-zone-arlo1-country-us-state-" + state.lower() + "-city-" + city.lower()
    background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "zproxy.lum-superproxy.io",
            port: parseInt(22225)
          },
          bypassList: ["foobar.com"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "m0m1od8d15v3"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (user)
    pluginfile = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    co = Options()
    co.add_argument("--start-maximized")
    co.add_extension(pluginfile)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=co)
    driver.get('https://api.ipify.org?format=json')
    json_ip = driver.find_element(By.XPATH,"//pre").text
    return driver, json_ip


test_model = BotInputModel(
    house_type="single_family",
    credit_score="GOOD",
    property_value="200000",
    mort_balance="150000",
    mort_intr_rate="5",
    loan_type="fha",
    addtional_cash="12000",
    bankruptcy="no",
    military_spouse="yes",
    home_improvements="yes",
    address="4024 Chardonnay Drive",
    zip_code="90210",
    first_name="John",
    last_name="Doe",
    email_address="john.doe@email.com",
    phone="6469603305",
    use_money="debt",
    dob="01/03/1985",
    url="https://tr4ckme.com/?a=41&c=9&s1=",
    refinance_purpose="cashout",
    rate_type="fixed",
    state="WY",
    city="Cheyenne",
    lender="Citi",
    employed="yes",
    last_ip="0.0.0.0"
)

if __name__ == '__main__':
    main(test_model)
    # runbot()


# initialise the driver
driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')


def HomeEquityQuizForm(data):
    # Initialise Home Equity Quiz Actions
    action = HEQActions(driver)

    # Launch HEQ
    action.launch(driver, "http://tr4ckme.com/?a=41&c=60&s1=")
    time.sleep(5)

    # Select Refinance
    action.select_refinance()
    time.sleep(2)

    # select house type
    action.select_house_type(data.house_type)
    time.sleep(2)

    # select credit score
    action.select_estimated_credit(data.credit_score)
    time.sleep(2)

    # Set estimated property value
    action.adjust_prop_val_slider(data.property_value)
    action.click_continue()
    time.sleep(2)

    # Set mortgage balance for first house
    action.adjust_mort_bal_slider(data.mort_balance)
    action.click_continue()
    time.sleep(2)

    # Set mortgage interest on first house
    action.adjust_mort_intr_slider(data.mort_intr_rate)
    action.click_continue()
    time.sleep(2)

    # select loan type
    action.select_loan_type(data.loan_type)
    time.sleep(2)

    # select second mortgage
    action.answer_second_mort(data.second_mort)

    # if data.second_mort:
    # slider selection
    # action.adjust_scd_mort_bal(data.scd_mort_bal)
    # time.sleep(2)
    # action.adjust_scd_mort_intr(data.scd_mort_intr)
    # action.click_continue()
    # time.sleep(2)

    # slider selection - REVISIT
    action.adjust_additional_cash_slider(data.addtional_cash)
    action.click_continue()
    time.sleep(2)

    # select bankruptcy
    action.answer_bankruptcy(data.bankruptcy)

    # Answer verify income question
    action.answer_verify_income(data.verify_income)

    # answer late payments question
    action.select_late_payment(data.late_payments)

    # Answer Military wife question
    action.answer_military_spouse(data.military_spouse)

    action.answer_home_improve(False)

    action.enter_address(data.address, data.zip_code)
    action.click_continue()

    action.enter_details(data.first_name,
                         data.last_name,
                         data.email_address,
                         data.phone_area_code,
                         data.phone_prefix,
                         data.phone_line_num
                         )
    action.click_continue()
