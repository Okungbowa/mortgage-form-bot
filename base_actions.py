from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expectation
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class BaseActions:
    @staticmethod
    def launch(driver, url: str):
        driver.get(url)

    @staticmethod
    def wait(driver, timeout, xpath):
        element = Wait(driver, timeout).until(
            Expectation.element_to_be_clickable((By.XPATH, xpath)))
        return element

    @staticmethod
    def click_button(driver, timeout, xpath):
        button = Wait(driver, timeout).until(
            Expectation.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    @staticmethod
    def read_text(driver, timeout, xpath) -> str:
        element = Wait(driver, timeout).until(
            Expectation.visibility_of_element_located((By.XPATH, xpath)))
        text = element.text
        return text

    @staticmethod
    def move_slider_bar(driver, timeout, bar_xpath: str, direction: str, pixels: int):
        action = ActionChains(driver)
        bar_element = Wait(driver, timeout).until(
            Expectation.element_to_be_clickable((By.XPATH, bar_xpath)))
        if direction.upper() == "RIGHT":
            action.drag_and_drop_by_offset(bar_element, abs(pixels), 0)
        elif direction.upper() == "LEFT":
            action.drag_and_drop_by_offset(bar_element, -abs(pixels), 0)
        action.perform()
        action.reset_actions()

    @staticmethod
    def answer_yes_no(driver, timeout, yes: bool, yes_btn_xpath: str, no_btn_xpath: str):
        try:
            if yes:
                button = Wait(driver, timeout).until(
                    Expectation.element_to_be_clickable((By.XPATH, yes_btn_xpath)))
            else:
                button = Wait(driver, timeout).until(
                    Expectation.element_to_be_clickable((By.XPATH, no_btn_xpath)))
            button.click()
        except Exception as e:
            raise e

    @staticmethod
    def enter_text(driver, timeout, xpath, text) -> str:
        element = Wait(driver, timeout).until(
            Expectation.visibility_of_element_located((By.XPATH, xpath)))
        element.send_keys(text)

    @staticmethod
    def choose_dropdown_option(self, driver, timeout, drop_xpath, value):
        try:
            dropdown = self.wait(driver, timeout, drop_xpath)
            select = Select(dropdown)

            # select by visible text
            select.select_by_visible_text(value)
        except Exception as e:
            raise e