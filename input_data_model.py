

class BotInputModel:
    def __init__(self,
                 house_type: str,
                 credit_score: str,
                 property_value: int,
                 mort_balance: str,
                 mort_intr_rate: str,
                 loan_type: str,
                 addtional_cash: str,
                 bankruptcy: str,
                 military_spouse: str,
                 home_improvements: bool,
                 address: str,
                 zip_code: str,
                 first_name: str,
                 last_name: str,
                 email_address: str,
                 phone: str,
                 use_money: str,
                 rate_type: str,
                 refinance_purpose: str,
                 url: str,
                 dob:str,
                 state: str,
                 city: str,
                 lender: str,
                 employed: str,
                 last_ip:str
                 ):
        self.dob = dob
        self.url = url
        self.refinance_purpose = refinance_purpose
        self.rate_type = rate_type
        self.state = state
        self.city = city
        self.house_type = house_type
        self.credit_score = credit_score
        self.property_value = property_value
        self.mort_balance = mort_balance
        self.mort_intr_rate = mort_intr_rate
        self.loan_type = loan_type
        self.addtional_cash = addtional_cash
        self.bankruptcy = bankruptcy
        self.military_spouse = military_spouse
        self.home_improvements = home_improvements
        self.address = address
        self.zip_code = zip_code
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone = phone
        self.use_money = use_money
        self.lender = lender
        self.employed = employed
        self.last_ip = last_ip

