from home_equity_model import HomeEqXpathModel as HEQXpath, HomeEqInputModel as HEQInput
from base_actions import BaseActions


class HomeEquityActions(BaseActions, HEQXpath):
    def __init__(self, driver):
        self.driver = driver
        self.timeout_xs = 0.5
        self.timeout_s = 1
        self.timeout_m = 3
        self.timeout_l = 5
        self.timeout_xl = 10

    def select_refinance(self):
        try:
            self.click_button(self.driver, self.timeout_xl, self.btn_refi)
        except Exception as e:
            raise e

    def select_house_type(self, house_type: str):
        try:
            if house_type.upper() == "SINGLE FAMILY":
                self.click_button(self.driver, self.timeout_m, self.btn_sgl_property)
            elif house_type.upper() == "MULTI FAMILY":
                self.click_button(self.driver, self.timeout_m, self.btn_multi_property)
            elif house_type.upper() == "TOWNHOUSE":
                self.click_button(self.driver, self.timeout_m, self.btn_town_property)
            elif house_type.upper() == "CONDOMINIUM":
                self.click_button(self.driver, self.timeout_m, self.btn_condo_property)
        except Exception as e:
            raise e

    def select_estimated_credit(self, est_cred: str):
        try:
            if est_cred.upper() == "EXCELLENT":
                self.click_button(self.driver, self.timeout_m, self.btn_excellent_score)
            elif est_cred.upper() == "GOOD":
                self.click_button(self.driver, self.timeout_m, self.btn_good_score)
            elif est_cred.upper() == "AVERAGE":
                self.click_button(self.driver, self.timeout_m, self.btn_town_property)
            elif est_cred.upper() == "FAIR":
                self.click_button(self.driver, self.timeout_m, self.btn_condo_property)
            elif est_cred.upper() == "POOR":
                self.click_button(self.driver, self.timeout_m, self.btn_condo_property)
        except Exception as e:
            raise e

    def click_continue(self):
        try:
            self.click_button(self.driver, self.timeout_m, self.btn_continue)
        except Exception as e:
            raise e

    def select_loan_type(self, loan_type: str):
        try:
            if loan_type.upper() == "FIXED":
                self.click_button(self.driver, self.timeout_m, self.btn_fixed)
            elif loan_type.upper() == "ADJUSTABLE":
                self.click_button(self.driver, self.timeout_m, self.btn_adjust)
            elif loan_type.upper() == "FIXED OR ADJUSTABLE":
                self.click_button(self.driver, self.timeout_m, self.btn_fix_adjust)
        except Exception as e:
            raise e

    def answer_second_mort(self, second_mortgage: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, second_mortgage, self.btn_second_yes, self.btn_second_no)
        except Exception as e:
            raise e

    def answer_bankruptcy(self, bankruptcy: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, bankruptcy, self.btn_bankruptcy_yes, self.btn_bankruptcy_no)
        except Exception as e:
            raise e

    def select_late_payment(self, late_payment: str):
        try:
            if late_payment.upper() == "NONE":
                self.click_button(self.driver, self.timeout_m, self.btn_late_none)
            elif late_payment.upper() == "ONE":
                self.click_button(self.driver, self.timeout_m, self.btn_late_one)
            elif late_payment.upper() == "TWO OR MORE":
                self.click_button(self.driver, self.timeout_m, self.btn_late_two_or_more)
        except Exception as e:
            raise e

    def answer_verify_income(self, verify_income: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, verify_income, self.btn_verify_yes, self.btn_verify_no)
        except Exception as e:
            raise e

    def answer_military_spouse(self, military_spouse: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, military_spouse, self.btn_military_yes, self.btn_military_no)
        except Exception as e:
            raise e

    def answer_home_improve(self, home_improve: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, home_improve, self.btn_improv_yes, self.btn_improv_no)
        except Exception as e:
            raise e

    def enter_address(self, address: str, zipcode: str):
        try:
            self.enter_text(self.driver, self.timeout_m, self.input_address, address)
            self.enter_text(self.driver, self.timeout_m, self.input_zip, zipcode)
        except Exception as e:
            raise e

    def enter_details(self, firstname: str, lastname: str, email: str, num_1: str, num_2: str, num_3: str):
        try:
            self.enter_text(self.driver, self.timeout_m, self.input_first, firstname)
            self.enter_text(self.driver, self.timeout_m, self.input_last, lastname)
            self.enter_text(self.driver, self.timeout_m, self.input_email, email)
            self.enter_text(self.driver, self.timeout_m, self.input_primary_p1, num_1)
            self.enter_text(self.driver, self.timeout_m, self.input_primary_p2, num_2)
            self.enter_text(self.driver, self.timeout_m, self.input_primary_p3, num_3)
        except Exception as e:
            raise e