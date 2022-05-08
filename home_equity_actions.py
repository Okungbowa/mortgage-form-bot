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

