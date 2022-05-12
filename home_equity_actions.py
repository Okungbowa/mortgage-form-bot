from home_equity_model import HomeEqXpathModel as HEQXpath
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
            if house_type.upper() == "SINGLE_FAMILY":
                self.click_button(self.driver, self.timeout_m, self.btn_sgl_property)
            elif house_type.upper() == "MULTI_FAMILY":
                self.click_button(self.driver, self.timeout_m, self.btn_multi_property)
            elif house_type.upper() == "CONDO":
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

    def select_rate_type(self, rate_type: str):
        try:
            if rate_type.upper() == "FIXED":
                self.click_button(self.driver, self.timeout_m, self.btn_fixed)
            elif rate_type.upper() == "ADJUST":
                self.click_button(self.driver, self.timeout_m, self.btn_adjust)
            elif rate_type.upper() == "FIXED_ADJUST":
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
            self.answer_yes_no(self.driver, self.timeout_m, military_spouse, self.btn_military_yes,
                               self.btn_military_no)
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

    def adjust_prop_val_slider(self, value: int):
        try:
            self.adjust_money_slider(value, self.slider_propt_val, self.label_propt_val, 8, '$50,001 - $55,000', "")
        except Exception as e:
            raise e

    def adjust_mort_bal_slider(self, value: int):
        try:
            self.adjust_money_slider(value, self.slider_mort_bal, self.label_mort_bal, 16, '$50,001 - $55,000', "")
        except Exception as e:
            raise e

    def adjust_mort_intr_slider(self, value: int):
        try:
            self.adjust_percentage_slider(value, self.slider_mort_intr, self.label_mort_intr, 15, "3% or lower",
                                          "Over 10%")
        except Exception as e:
            raise e

    def adjust_additional_cash_slider(self, value: int):
        try:
            self.adjust_money_slider(value, self.slider_add_cash, self.label_add_cash, 90, '$0',
                                     '$45,001 - $50,000')
        except Exception as e:
            raise e

    def wait_for_last_screen(self):
        try:
            self.wait_for_element(self.driver, self.timeout_xl, self.input_first)
        except Exception as e:
            raise e

    def adjust_money_slider(self, value, bar_xpath, display_xpath, pixels, start_text, end_text):
        max_i = 500
        i = 0
        first_loop = True
        while i < max_i:
            display_val = self.read_text(self.driver, self.timeout_m, display_xpath)
            display_num = display_val.replace('$', '').replace(',', '').replace(' ', '').split('-')
            if first_loop and display_val == start_text:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "RIGHT", pixels)
                first_loop = False
            elif first_loop and display_val == end_text:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "LEFT", pixels)
                first_loop = False
            elif int(display_num[0]) <= int(value) <= int(display_num[1]):
                break
            elif display_val.__contains__(start_text) and int(value) <= 55000:
                break
            elif display_val.__contains__(end_text) and int(value) >= 2000000:
                break
            elif int(value) < int(display_num[0]):
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "LEFT", pixels)
            elif int(value) > int(display_num[1]):
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "RIGHT", pixels)
            i += 1

    def adjust_percentage_slider(self, value, bar_xpath, label_xpath, pixels, start_text, end_text):
        max_i = 100
        i = 0
        first_loop = True
        while i < max_i:
            display_val = self.read_text(self.driver, self.timeout_m, label_xpath)
            display_num = float(display_val.replace('%', '').replace(' ', ''))
            if first_loop and display_val == start_text:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "RIGHT", pixels)
                first_loop = False
            elif first_loop and display_val == end_text:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "LEFT", pixels)
                first_loop = False
            elif display_val == int(value):
                break
            elif display_val.__contains__(start_text) and float(value) <= 3:
                break
            elif display_val.__contains__(end_text) and float(value) >= 10:
                break
            elif float(value.replace(' ', '')) < display_num:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "LEFT", pixels)
            elif float(value.replace(' ', '')) > display_num:
                self.move_slider_bar(self.driver, self.timeout_m, bar_xpath, "RIGHT", pixels)
            i += 1
