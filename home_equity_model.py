from enum import Enum


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

    # est property value
    slider_propt_val = "//div[@id = 'EST_VAL_SLIDER']/child::span"
    slder_display = "//div[@id = 'EST_VAL_DISPLAY_SMALL']"

    # mortgage balance slider
    slider_mort_bal = "//div[@id = 'BAL_ONE_SLIDER']/child::span"

    # Fixed Score
    btn_fixed = "//button[@id='fixed-btn']"
    btn_adjust = "//button[@id='adjust-btn']"
    btn_fix_adjust = "//button[@id='fixed-or-adjust-btn']"


class HomeEqInputModel:
    def __init__(self,
                 house_type: str,
                 credit_score: str,
                 property_value: int,
                 mort_balance: str,
                 mort_intr_rate: str,
                 loan_terms: str,
                 second_mort: bool,
                 addtional_cash: str,
                 bankruptcy: str,
                 verify_income: str,
                 late_payments: str,
                 military_spouse: str,
                 home_improvements: bool,
                 address: str,
                 zip_code: str,
                 first_name: str,
                 last_name: str,
                 email_address: str,
                 phone_area_code: str,
                 phone_prefix: str,
                 phone_line_num: str,
                 scd_mort_bal: str = "",
                 scd_mort_intr: str = ""
                 ):
        self.house_type = house_type
        self.credit_score = credit_score
        self.property_value = property_value
        self.mort_balance = mort_balance
        self.mort_intr_rate = mort_intr_rate
        self.loan_terms = loan_terms
        self.second_mort = second_mort
        self.addtional_cash = addtional_cash
        self.bankruptcy = bankruptcy
        self.verify_income = verify_income
        self.late_payments = late_payments
        self.military_spouse = military_spouse
        self.home_improvements = home_improvements
        self.address = address
        self.zip_code = zip_code
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_area_code = phone_area_code
        self.phone_prefix = phone_prefix
        self.phone_line_num = phone_line_num
        self.scd_mort_bal = scd_mort_bal
        self.scd_mort_intr = scd_mort_intr
