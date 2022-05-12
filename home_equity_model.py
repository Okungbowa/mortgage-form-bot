# create the same model for the other site, the InputModels are identical, you'll need to go through the other
# govhomeprog site to get all the xpaths for the xpath model

class HomeEqXpathModel:
    # Loan Type
    btn_refi = "//button[@id='refi-button']"
    btn_mort = "//button[@id='mortgage-button']"

    # House Type
    btn_sgl_property = "//button[@id='single_prop']"
    btn_multi_property = "//button[@id='multiple_prop']"
    btn_town_property = "//button[@id='townhouse_prop']"
    btn_condo_property = "//button[@id='condo_prop']"

    # Credit Score
    btn_poor_score = "//button[@id='poor_grade']"
    btn_fair_score = "//button[@id='fair_grade']"
    btn_average_score = "//button[@id='average_grade']"
    btn_good_score = "//button[@id='good_grade']"
    btn_excellent_score = "//button[@id='excellent_grade']"

    # Found home
    btn_found_home_yes = "//button[@id='spec-home-yes-btn']"
    btn_found_home_no = "//button[@id='spec-home-no-btn']"

    # Purchase Contract
    btn_purchase_cont_yes = "//button[@id='purchase-contract-yes-btn']"
    btn_purchase_cont_no = "//button[@id='purchase-contract-no-btn']"

    # searching status
    btn_under_contr = "//button[@id='time_now']"
    btn_immediately = "//button[@id='time_immediate']"
    btn_currently_shopping = "//button[@id='time_30_days']"
    btn_soon = "//button[@id='time_60_days']"
    btn_not_sure = "//button[@id='time_unspecified']"

    # Type Of Property
    btn_primary_residence = "//div[@id='primary-prop-button-group']/button"
    btn_vacation_property = "//div[@id='vacation-prop-button-group']/button"
    btn_investment_property = "//div[@id='investment-prop-button-group']/button"

    # est property value
    slider_propt_val = "//div[@id = 'EST_VAL_SLIDER']/child::span"
    label_propt_val = "//div[@id = 'EST_VAL_DISPLAY_SMALL']"

    # mortgage balance slider
    slider_mort_bal = "//div[@id = 'BAL_ONE_SLIDER']/child::span"
    label_mort_bal = "//div[@id='BAL_ONE_DISPLAY_SMALL']"

    # Fixed Score
    btn_fixed = "//button[@id='fixed-btn']"
    btn_adjust = "//button[@id='adjust-btn']"
    btn_fix_adjust = "//button[@id='fixed-or-adjust-btn']"

    # Bankruptcy
    btn_bankruptcy_yes = "//div[@id='fha-yes-btn-group']/button"
    btn_bankruptcy_no = "//div[@id='fha-no-btn-group']/button"

    # Verify Income
    btn_verify_yes = "//div[@id='verifiable-yes-btn-group']/button"
    btn_verify_no = "//div[@id='verifiable-no-btn-group']/button"

    # Late Payment
    btn_late_none = "//div[@id='late-none-btn-group']/button"
    btn_late_one = "//div[@id='late-one-btn-group']/button"
    btn_late_two_or_more = "//div[@id='late-two-or-more-btn-group']/button"

    # Military
    btn_military_yes = "//div[@id='va-stat-yes-btn-group']/button"
    btn_military_no = "//div[@id='va-stat-no-btn-group']/button"

    # Home Improvement
    btn_improv_yes = "//div[@id='ha-pro-yes-btn-group']/button"
    btn_improv_no = "//div[@id='ha-pro-no-btn-group']/button"
    dropdown_project_sort = "//div[@class='input-body']/select[@id='TASK']"

    # Project Phase
    btn_planning = "//button[@id='ha-status-no-btn']"
    btn_ready_to_hire = "//button[@id='ha-status-yes-btn']"
    dropdown_start_phase = "//div[@class='input-body']/select[@id='TIMELINE']"

    # Current Address
    input_address = "//div[@class='input-body']/input[@id='ADDRESS']"
    input_zip = "//div[@class='input-body centered']/input[@id='ZIP']"

    # Personal Information
    input_first = "//div[@class='input-body']/input[@id='FNAME']"
    input_last = "//div[@class='input-body']/input[@id='LNAME']"
    input_email = "//div[@class='input-body']/input[@id='EMAIL']"
    input_primary_p1 = "//div[@class='input-body']/input[@id='PRI_PHONE-p1']"
    input_primary_p2 = "//div[@class='input-body']/input[@id='PRI_PHONE-p2']"
    input_primary_p3 = "//div[@class='input-body']/input[@id='PRI_PHONE-p3']"

    # Remaining 1st mortgage slider
    slider_remain_first_mort = "//div[@id ='BAL_ONE_SLIDER']/child::span"

    # 1st mortgage interest slider
    slider_mort_intr = "//div[@id ='MTG_ONE_INT_SLIDER']/child::span"
    label_mort_intr = "//div[@id='MTG_ONE_INT_DISPLAY_SMALL']"

    # Second Mortgage
    btn_second_yes = "//div[@id ='mortgage-two-yes-btn-group']/button"
    btn_second_no = "//div[@id ='mortgage-two-no-btn-group']/button"
    slider_second_mort_bal = "//div[@id ='BAL_TWO_SLIDER']/child::span"
    slider_second_int_bal = "//div[@id ='MTG_TWO_INT_SLIDER']/child::span"
    label_second_mort_bal = "//div[@id ='BAL_TWO_DISPLAY_SMALL']"
    label_second_int_bal = "//div[@id ='MTG_TWO_INT_DISPLAY_SMALL']"

    # Additional Cash to borrow
    slider_add_cash = "//div[@id ='ADD_CASH_SLIDER']/child::span"
    label_add_cash = "//div[@id = 'ADD_CASH_DISPLAY_SMALL']"

    # Continue Button
    btn_continue = "//button[@id='continue_button']"

    #Last screen
    div_rows = "//div[@id = 'max-rows']"


class HomeEqInputModel:
    def __init__(self,
                 house_type: str,
                 credit_score: str,
                 property_value: int,
                 mort_balance: str,
                 mort_intr_rate: str,
                 loan_type: str,
                 addtional_cash: str,
                 bankruptcy: str,
                 late_payments: str,
                 military_spouse: str,
                 home_improvements: bool,
                 address: str,
                 zip_code: str,
                 first_name: str,
                 last_name: str,
                 email_address: str,
                 phone: str,
                 use_money: str,
                 rate_type: str,
                 refinance_purpose: str,
                 url: str,
                 dob:str,
                 state: str,
                 city: str,
                 lender: str,
                 employed: str
                 ):
        self.dob = dob
        self.url = url
        self.refinance_purpose = refinance_purpose
        self.rate_type = rate_type
        self.state = state
        self.city = city
        self.house_type = house_type
        self.credit_score = credit_score
        self.property_value = property_value
        self.mort_balance = mort_balance
        self.mort_intr_rate = mort_intr_rate
        self.loan_type = loan_type
        self.addtional_cash = addtional_cash
        self.bankruptcy = bankruptcy
        self.late_payments = late_payments
        self.military_spouse = military_spouse
        self.home_improvements = home_improvements
        self.address = address
        self.zip_code = zip_code
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone = phone
        self.use_money = use_money
        self.lender = lender
        self.employed = employed
