class ATM(object):
    """
        Blueprint for ATM
    """
    
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def CashWithdrawl(self):
        print("Cash has been withdrawled")
    
    def BalanceEnquiry(self):
        print("Balance Enquiry is: ")

    def AccountBalance(self):
        print("Account is balanced")
        "Checking account balance functionality here"

atm = ATM(1010, 2121)
print(atm.CashWithdrawl())