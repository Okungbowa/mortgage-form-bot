from selenium import webdriver
from home_equity_model import HomeEqInputModel as HEQInput
from home_equity_actions import HomeEquityActions as HEQActions
from govhomeprogram_actions import GovhomeActions
import time

# proxy_status = 'ON'
# # # initialise the driver
# if proxy_status == 'ON':
#
#     PROXY = "169.57.1.85:8123"  # IP:PORT or HOST:PORT
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--proxy-server=%s' % PROXY)
#     driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver', options=chrome_options)
#
# elif proxy_status == 'OFF':
#
#     driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')


# driver.get("https://whatismyipaddress.com/")


data = HEQInput(
    house_type="SINGLE FAMILY",
    credit_score="GOOD",
    property_value="200000",
    mort_balance="150000",
    mort_intr_rate="5",
    loan_type="FIXED OR ADJUSTABLE",
    second_mort=False,
    addtional_cash="12000",
    bankruptcy=False,
    late_payments="ONE",
    military_spouse=True,
    home_improvements=True,
    address="4024 Chardonnay Drive",
    zip_code="90210",
    first_name="John",
    last_name="Doe",
    email_address="john.doe@email.com",
    phone_area_code="646",
    phone_prefix="960",
    phone_line_num="3305",
    scd_mort_bal="15000",
    scd_mort_intr="4",
    verify_income=True
)


def main():
    # Initialise Home Equity Quiz Actions
    driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')

    # Launch HEQ
    # action = HEQActions(driver)
    # action.launch(driver, "http://tr4ckme.com/?a=41&c=60&s1=")
    # time.sleep(5)
    # home_equity_quiz_steps(action)

    action = GovhomeActions(driver)
    action.launch(driver, "https://tr4ckme.com/?a=41&c=9&s1=")
    time.sleep(5)
    govhomeprog_steps(action)


def govhomeprog_steps(action):
    action.select_block_push()
    time.sleep(2)

    action.select_own_home()
    time.sleep(2)






def home_equity_quiz_steps(action):
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


if __name__ == '__main__':
    main()
