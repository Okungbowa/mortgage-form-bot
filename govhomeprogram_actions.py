from govhomeprograms_model import GovHomeProgXpathModel as GovXpath
from base_actions import BaseActions


class GovhomeActions(BaseActions, GovXpath):
    def __init__(self, driver):
        self.driver = driver
        self.timeout_xs = 0.5
        self.timeout_s = 1
        self.timeout_m = 3
        self.timeout_l = 5
        self.timeout_xl = 10

    def select_block_push(self):
        try:
            self.click_button(self.driver, self.timeout_xl, self.btn_block_push_not)
        except Exception as e:
            raise e

    def select_own_home(self):
        try:
            self.click_button(self.driver, self.timeout_xl, self.label_own_home)
        except Exception as e:
            raise e

    def enter_zipcode(self, zipcode: str):
        try:
            self.enter_text(self.driver, self.timeout_m, self.input_zip, zipcode)
        except Exception as e:
            raise e

    def select_house_type(self, house_type: str):
        try:
            if house_type.upper() == "SINGLE_FAMILY":
                self.click_button(self.driver, self.timeout_m, self.label_house_sgl_family)
            elif house_type.upper() == "MULTI_FAMILY":
                self.click_button(self.driver, self.timeout_m, self.label_house_townhouse)
            elif house_type.upper() == "MOBILE":
                self.click_button(self.driver, self.timeout_m, self.label_house_trailer)
            elif house_type.upper() == "CONDO":
                self.click_button(self.driver, self.timeout_m, self.label_house_townhouse)
        except Exception as e:
            raise e

    def select_employment_status(self, employment_status: str):
        try:
            if employment_status.upper() == "EMPLOYED":
                self.click_button(self.driver, self.timeout_m, self.label_employed)
            elif employment_status.upper() == "SELF-EMPLOYED":
                self.click_button(self.driver, self.timeout_m, self.label_self_employed)
            elif employment_status.upper() == "UNEMPLOYED":
                self.click_button(self.driver, self.timeout_m, self.label_unemployed)
            elif employment_status.upper() == "RETIRED":
                self.click_button(self.driver, self.timeout_m, self.label_retired)
        except Exception as e:
            raise e

    def select_estimated_credit(self, est_cred: str):
        try:
            if est_cred.upper() == "EXCELLENT":
                self.click_button(self.driver, self.timeout_m, self.label_credit_excellent)
            elif est_cred.upper() == "GOOD":
                self.click_button(self.driver, self.timeout_m, self.label_credit_good)
            elif est_cred.upper() == "AVERAGE":
                self.click_button(self.driver, self.timeout_m, self.label_credit_average)
            elif est_cred.upper() == "FAIR":
                self.click_button(self.driver, self.timeout_m, self.label_credit_below_avrg)
            elif est_cred.upper() == "POOR":
                self.click_button(self.driver, self.timeout_m, self.label_credit_poor)
        except Exception as e:
            raise e

    def click_next(self):
        try:
            self.click_button(self.driver, self.timeout_m, self.btn_next)
        except Exception as e:
            raise e

    def click_see_results(self):
        try:
            self.click_button(self.driver, self.timeout_m, self.btn_submit)
        except Exception as e:
            raise e

    def select_loan_type(self, loan_type: str):
        try:
            if loan_type.upper() == "FHA":
                self.click_button(self.driver, self.timeout_m, self.label_FHA)
            elif loan_type.upper() == "VA":
                self.click_button(self.driver, self.timeout_m, self.label_VA)
            else:
                self.click_button(self.driver, self.timeout_m, self.label_other_loan)
        except Exception as e:
            raise e

    def select_lender(self, value):
        no_option = False
        try:
            self.choose_dropdown_option(self.driver, self.timeout_m, self.dropdown_lender, value)
        except Exception as e:
            no_option = True
        finally:
            if no_option:
                try:
                    self.choose_dropdown_option(self.driver, self.timeout_m, self.dropdown_lender, "Other")
                except Exception as e:
                    raise e



    def wait_for_last_screen(self):
        try:
            self.wait_for_element(self.driver,self.timeout_xl, self.btn_submit)
        except Exception as e:
            raise e

    def answer_military_spouse(self, military_spouse: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, military_spouse, self.label_yes_vet_house,
                               self.label_no_vet_house)
        except Exception as e:
            raise e

    def enter_address(self, address: str):
        try:
            self.enter_text(self.driver, self.timeout_m, self.input_address, address)
        except Exception as e:
            raise e

    def enter_details(self, firstname: str, lastname: str, email: str, phone: str):
        try:
            self.enter_text(self.driver, self.timeout_m, self.input_first_name, firstname)
            self.enter_text(self.driver, self.timeout_m, self.input_last_name, lastname)
            self.enter_text(self.driver, self.timeout_m, self.input_email, email)
            self.enter_text(self.driver, self.timeout_m, self.input_phone, phone)
        except Exception as e:
            raise e

    def adjust_prop_val_slider(self, value: int):
        try:
            self.adjust_money_slider(
                value, self.slider_prop_val, self.display_prop_val, 8, '$105,000 - $110,000', "Over $2,000,000")
        except Exception as e:
            raise e

    def adjust_mort_bal_slider(self, value: int):
        try:
            self.adjust_money_slider(
                value, self.slider_mort_bal, self.display_mort_bal, 8, '$85,000 - $90,000', "Over $2,000,000")
        except Exception as e:
            raise e

    def answer_add_cash(self, add_cash: bool):
        try:
            self.answer_yes_no(self.driver, self.timeout_m, add_cash, self.btn_add_cash_yes, self.btn_add_cash_no)
        except Exception as e:
            raise e

    # due to be decided
    def select_future_plan(self, plan: str):
        try:
            if plan.upper() == "OTHER":
                self.click_button(self.driver, self.timeout_m, self.label_other_use)
            elif plan.upper() == "NOT_SAY":
                self.click_button(self.driver, self.timeout_m, self.label_pref_not_say)
            elif plan.upper() == "DEBT":
                self.click_button(self.driver, self.timeout_m, self.label_debt_cons)
        except Exception as e:
            raise e

    def adjust_mort_intr_slider(self, value: int):
        try:
            self.adjust_percentage_slider(value, self.slider_interest_rate, self.display_intr_rate, 15, "2.75%",
                                          "8%")
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
