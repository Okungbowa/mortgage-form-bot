from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expectation


class BaseActions:
    @staticmethod
    def launch(driver, url: str):
        driver.get(url)

    @staticmethod
    def click_button(driver, timeout, xpath):
        button = Wait(driver, timeout).until(
            Expectation.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    @staticmethod
    def read_text(driver, timeout, xpath) -> str:
        element = Wait(driver, timeout).until(
            Expectation.visibility_of_element_located((By.XPATH, xpath)))
        text = element.getText()
        return text

    @staticmethod
    def move_slider_bar(driver, timeout, bar_xpath: str, direction: str, pixels: int):
        bar_element = Wait(driver, timeout).until(
            Expectation.element_to_be_clickable((By.XPATH, bar_xpath)))
        # if direction.upper()

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