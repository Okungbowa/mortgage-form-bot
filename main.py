from selenium import webdriver
from home_equity_model import HomeEqXpathModel as HEQXpath, HomeEqInputModel as HEQInput
from home_equity_actions import HomeEquityActions as HEQActions

# initialise the driver
driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')

data = HEQInput(
    house_type="SINGLE FAMILY",
    credit_score="GOOD",
    property_value=0,
    mort_balance="",
    mort_intr_rate="",
    loan_type="",
    second_mort="",
    addtional_cash="",
    bankruptcy="",
    late_payments="",
    military_spouse=True,
    home_improvements=True,
    address="",
    zip_code="",
    first_name="",
    last_name="",
    email_address="",
    phone_area_code="",
    phone_prefix="",
    phone_line_num="",
    scd_mort_bal="",
    scd_mort_intr=""
)


def main():
    # Initialise Home Equity Quiz Actions
    action = HEQActions(driver)

    # Launch HEQ
    action.launch(driver, "http://tr4ckme.com/?a=41&c=60&s1=")

    # Select Refinance
    action.select_refinance()

    # select house type
    action.select_house_type(data.house_type)

    # select credit score
    action.select_estimated_credit(data.credit_score)

    #slider selection - REVISIT
    action.click_continue()

    # slider selection - REVISIT
    action.click_continue()

    # slider selection - REVISIT
    action.click_continue()

    action.select_loan_type(data.loan_type)





if __name__ == '__main__':
    main()
