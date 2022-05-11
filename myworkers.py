from selenium import webdriver
from home_equity_model import HomeEqXpathModel as HEQXpath, HomeEqInputModel as HEQInput
from home_equity_actions import HomeEquityActions as HEQActions
import time

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
