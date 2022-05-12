from govhomeprogram_actions import GovhomeActions
from input_data_model import BotInputModel as InputModel
from home_equity_actions import HomeEquityActions as HEQActions
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
from selenium.webdriver.chrome.options import Options



def initialise_driver_proxy(city: str, state: str):
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
    return driver


data = InputModel(
    house_type="single_family",
    credit_score="GOOD",
    property_value="200000",
    mort_balance="150000",
    mort_intr_rate="5",
    loan_type="fha",
    addtional_cash="12000",
    bankruptcy="no",
    late_payments="ONE",
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
)


def main():
    # Initialise Home Equity Quiz Actions
    driver = initialise_driver_proxy(data.city, data.state)

    if data.url == "https://tr4ckme.com/?a=41&c=9&s1=":
        # Launch Govhomeprog
        action = GovhomeActions(driver)
        govhomeprog_steps(action)
    elif data.url == "http://tr4ckme.com/?a=41&c=60&s1=":
        action = HEQActions(driver)
        home_equity_quiz_steps(action)


def govhomeprog_steps(action):
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


def home_equity_quiz_steps(action):
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


if __name__ == '__main__':
    main()
    # runbot()
