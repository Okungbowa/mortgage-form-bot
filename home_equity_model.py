from enum import Enum


class HomeEquityQuizXpathModel():
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

    btn_under_contr = "//button[@id='time_now']"
    btn_immediately = "//button[@id='time_immediate']"
    btn_currently_shopping = "//button[@id='time_30_days']"
    btn_soon = "//button[@id='time_60_days']"
    btn_not_sure = "//button[@id='time_unspecified']"
