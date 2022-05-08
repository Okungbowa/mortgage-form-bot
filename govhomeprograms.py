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
dropdown_home_worth = = "//select[@id='estimatedHomeValue']"

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
input_bankruptcy_no ="//div[@class='radio-button__container']/input[@id ='false' and @name = 'isBankruptcy']"

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
input_street = "//input[@id='propertyAddress1']"
input_city = "//select[@id='propertyCity']"

# Email address
input_email = "//input[@id='email']"

# Current Occupation
dropdown_occ = "//select[@id='currentOccupation']"

# Previous military service
input_mil_yes = "//div[@class = 'radio-button__container']/input[@id='true' and @name = 'isVeteran']"
input_mil_no = "//div[@class = 'radio-button__container']/input[@id='false' and @name = 'isVeteran']"

# VA Loan
input_va_yes = "//div[@class = 'radio-button__container']/input[@id='true' and @name = 'isVALoan']"
input_va_no = "//div[@class = 'radio-button__container']/input[@id='false' and @name = 'isVALoan']"

# First Name
input_first = "//input[@id='firstName']"

# Last Name
input_first = "//input[@id='lastName']"

# Primary Residence
input_street = "//input[@id='mailingAddress1']"
dropdown_state = "//select[@id='mailingState']"
input_city = "//input[@id='mailingCity']"
input_zip = "//input[@id='mailingZip']"

# Primary Phone Number
input_prim_area = "//input[@id='dayPhoneArea']"
input_prim_prefix = "//input[@id='dayPhonePrefix']"
input_prim_suffix = "//input[@id='dayPhoneSuffix']"

# Secondary Phone Number
input_sec_area = "//input[@id='evePhoneArea']"
input_sec_prefix = "//input[@id='evePhonePrefix']"
input_sec_sufffix = "//input[@id='evePhoneSuffix']"

#Continue Button
btn_continue = "//div[@class ='step-submit__button']"

#Calculate Button
btn_calculate = "//input[@class ='submit-button undefined']"

class GovHomeProgInputModel:
  def __init__(self,
               home_type:  str,
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
               rate_type: 
               
               
               
               
