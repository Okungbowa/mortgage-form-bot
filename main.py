from selenium import webdriver
from home_equity_model import HomeEqXpathModel as HEQXpath, HomeEqInputModel as HEQInput
from home_equity_actions import HomeEquityActions as HEQActions
import time

# initialise the driver
driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')

data = HEQInput(
    house_type="SINGLE FAMILY",
    credit_score="GOOD",
    property_value="200000",
    mort_balance="150000",
    mort_intr_rate="5",
    loan_type="FIXED OR ADJUSTABLE",
    second_mort=False,
    addtional_cash="",
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
    scd_mort_bal="",
    scd_mort_intr="",
    verify_income=True
)


def main():
    # Initialise Home Equity Quiz Actions
    action = HEQActions(driver)

    # Launch HEQ
    action.launch(driver, "http://tr4ckme.com/?a=41&c=60&s1=")
    time.sleep(5)

    # Select Refinance
    action.select_refinance()

    # select house type
    action.select_house_type(data.house_type)

    # select credit score
    action.select_estimated_credit(data.credit_score)

    # slider selection - REVISIT
    action.adjust_prop_val_slider(data.property_value)
    action.click_continue()
    time.sleep(2)

    # slider selection - REVISIT
    action.adjust_mort_bal_slider(data.mort_balance)
    action.click_continue()
    time.sleep(2)

    # slider selection - REVISIT
    action.adjust_mort_intr_slider(data.mort_intr_rate)
    action.click_continue()
    time.sleep(2)

    # select loan type
    action.select_loan_type(data.loan_type)

    # select second mortgage
    action.answer_second_mort(data.second_mort)

    if data.second_mort:
        # slider selection
        action.click_continue()
        time.sleep(2)

    # slider selection - REVISIT
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
