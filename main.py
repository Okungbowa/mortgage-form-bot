from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as Expect
from webdriver_manager.chrome import ChromeDriverManager
from home_equity_model import HomeEqXpathModel as HEQXpath, HomeEqInputModel as HEQInput

home_equity_quiz_url = "http://tr4ckme.com/?a=41&c=60&s1="

driver = webdriver.Chrome('/Users/joshuaokungbowa/Downloads/chromedriver')

timeout_xs = 0.5
timeout_s = 1
timeout_m = 3
timeout_l = 5
timeout_xl = 10


def main():
    driver.get(home_equity_quiz_url)

    data = HEQInput(
        "",
        "",
        0,
        "",
        "",
        "",
        True,
        "",
        "",
        "",
        "",
        "",
        True,
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    )

    select_loan_type("refinance")


def select_loan_type(loan_type: str):
    try:
        if loan_type == "refinance":
            btn_refinance = wait(driver, timeout_m).until(Expect.element_to_be_clickable((By.XPATH, HEQXpath.btn_refi)))
        else:
            btn_refinance = wait(driver, timeout_m).until(Expect.element_to_be_clickable((By.XPATH, HEQXpath.btn_refi)))
        btn_refinance.click()
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
