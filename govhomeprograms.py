# create model for govhomeprogam here

class GovHomeProgXpathModel:
    # Home Type
    dropdown_home_type = "//select[@id='homeType']"

    # Credit Type
    dropdown_credit_type = "//select[@id='creditType']"

    # Loan Type
    dropdown_loan_type = "//select[@id='creditType']"

    # ZIP
    input_zip = "//input[@id='zipCode']"

    # Home Purchase Year
    dropdown_purc_year = "//select[@id='homePurchasedYear']"

    # Home worth
    dropdown_home_worth = "//select[@id='estimatedHomeValue']"

    # Household income
    dropdown_income = "//select[@id='yearlyIncome']"

    # Mortgage Interest Rate
    dropdown_int_rate = "//select[@id='mortgage1InterestRate']"

    # Mortgage Balance
    dropdown_mort_bal = "//select[@id='mortgage1Balance']"

    # Monthly Payment
    dropdown_monthly_pay = "//select[@id='monthlyMortgagePayment']"

    # Mortgage Lender
    dropdown_lender = "//select[@id='currentLender']"

    # Type of Rate
    input_fixed = "//input[@id='FIXED']"
    input_adjustable = "//input[@id='VARIABLE']"

    # Credit Card Debt
    input_yes = "//input[@id='true']"
    input_no = "//input[@id='false']"

    # Borrow Additional Cash
    dropdown_add_cash = "//select[@id='cashOut']"

    # Age
    dropdown_age = "//select[@id='age']"

    # Employment Status
    dropdow_emp_status = "//select[@id='occupationalStatus']"

    # Purpose of Cash Out
    dropdown_cash_out = "//select[@id='purposeOfCashOut']"

    # Bankruptcy
    input_bankruptcy_yes = "//div[@class='radio-button__container']/input[@id ='true' and @name = 'isBankruptcy']"
    input_bankruptcy_no = "//div[@class='radio-button__container']/input[@id ='false' and @name = 'isBankruptcy']"

    # FHA Loan
    input_fha_yes = "//div[@class='radio-button__container']/input[@id ='true' and @name = 'hasFHA']"
    input_fha_no = "//div[@class='radio-button__container']/input[@id ='false' and @name = 'hasFHA']"
    input_fha_idk = "//div[@class='radio-button__container']/input[@id ='other' and @name = 'hasFHA']"

    # Pay for PMI
    input_pmi_yes = "//div[@class='radio-button__container']/input[@id ='YES' and @name = 'privateMortgageInsurance']"
    input_pmi_no = "//div[@class='radio-button__container']/input[@id ='NO' and @name = 'privateMortgageInsurance']"
    input_pmi_idk = "//div[@class='radio-button__container']/input[@id ='I_DO_NOT_KNOW' and @name = 'privateMortgageInsurance']"

    # Number Mortgage Payment
    dropdown_mort_pay_number = "//select[@id='isMortgageLate']"

    # Property Address
    input_property_street = "//input[@id='propertyAddress1']"
    input_property_city = "//select[@id='propertyCity']"

    # Email address
    input_email = "//input[@id='email']"

    # Current Occupation
    dropdown_curr_occupation = "//select[@id='currentOccupation']"

    # Previous military service
    input_mil_yes = "//div[@class = 'radio-button__container']/input[@id='true' and @name = 'isVeteran']"
    input_mil_no = "//div[@class = 'radio-button__container']/input[@id='false' and @name = 'isVeteran']"

    # VA Loan
    input_va_yes = "//div[@class = 'radio-button__container']/input[@id='true' and @name = 'isVALoan']"
    input_va_no = "//div[@class = 'radio-button__container']/input[@id='false' and @name = 'isVALoan']"

    # First Name
    input_first = "//input[@id='firstName']"

    # Last Name
    input_last = "//input[@id='lastName']"

    # Primary Residence
    input_prim_street = "//input[@id='mailingAddress1']"
    dropdown_prim_state = "//select[@id='mailingState']"
    input_prim_city = "//input[@id='mailingCity']"
    input_prim_zip = "//input[@id='mailingZip']"

    # Primary Phone Number
    input_prim_area = "//input[@id='dayPhoneArea']"
    input_prim_prefix = "//input[@id='dayPhonePrefix']"
    input_prim_suffix = "//input[@id='dayPhoneSuffix']"

    # Secondary Phone Number
    input_sec_area = "//input[@id='evePhoneArea']"
    input_sec_prefix = "//input[@id='evePhonePrefix']"
    input_sec_sufffix = "//input[@id='evePhoneSuffix']"

    # Continue Button
    btn_continue = "//div[@class ='step-submit__button']"

    # Calculate Button
    btn_calculate = "//input[@class ='submit-button undefined']"


class GovHomeProgInputModel:
    def __init__(self,
                 home_type: str,
                 credit_score: str,
                 loan_type: str,
                 zip_code: str,
                 purchase_year: str,
                 home_worth: str,
                 household_inc: str,
                 mort_int: str,
                 mort_bal: str,
                 monthly_payment: str,
                 mort_lender: str,
                 rate_type: str,
                 credit_debt: str,
                 additional_cash: str,
                 age: str,
                 employment_status: str,
                 cash_out: str,
                 bankruptcy: str,
                 fha_loan: str,
                 pmi: str,
                 mort_payment_num: str,
                 property_street: str,
                 property_city: str,
                 email: str,
                 curr_occupation: str,
                 mil_service: str,
                 va_loan: str,
                 first_name: str,
                 last_name: str,
                 prim_street: str,
                 prim_state: str,
                 prim_zip: str,
                 prim_city: str,
                 prim_phone_area_code: str,
                 prim_phone_prefix: str,
                 prim_phone_suffix: str,
                 sec_phone_area_code: str,
                 sec_phone_prefix: str,
                 sec_phone_suffix: str
                 ):
        self.home_type = home_type
        self.credit_score = credit_score
        self.loan_type = loan_type
        self.zip_code = zip_code
        self.purchase_year = purchase_year
        self.home_worth = home_worth
        self.household_inc = household_inc
        self.mort_int = mort_int
        self.mort_bal = mort_bal
        self.monthly_payment = monthly_payment
        self.mort_lender = mort_lender
        self.rate_type = rate_type
        self.credit_debt = credit_debt
        self.additional_cash = additional_cash
        self.age = age
        self.employment_status = employment_status
        self.cash_out = cash_out
        self.bankruptcy = bankruptcy
        self.fha_loan = fha_loan
        self.pmi = pmi
        self.mort_payment_num = mort_payment_num
        self.email = email
        self.curr_occupation = curr_occupation
        self.mil_service = mil_service
        self.va_loan = va_loan
        self.first_name = first_name
        self.last_name = last_name
        self.prim_street = prim_street
        self.prim_state = prim_state
        self.prim_zip = prim_zip
        self.prim_city = prim_city
        self.prim_phone_area_code = prim_phone_area_code
        self.prim_phone_prefix = prim_phone_prefix
        self.prim_phone_suffix = prim_phone_suffix
        self.sec_phone_area_code = sec_phone_area_code
        self.sec_phone_prefix = sec_phone_prefix
        self.sec_phone_suffix = sec_phone_suffix
