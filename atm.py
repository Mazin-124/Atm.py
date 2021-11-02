class Atm:
    def __init__(self, cardnumber , pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceEnquiry(self):
        print('Your balance is 100$')

    def cashWithDrawl(self, amount):
        new_amount = 100 - amount
        print('You withdrawed: ' + str(amount) + "Remaining amount is: " + str(new_amount))


def main():
    name = input('What is your name?')
    print('Hi ' + name)

    cardnumber = input('Enter your card number: ')
    pin = input('Enter your pin: ')

    new_user = Atm(cardnumber, pin)

    print('Choose any of these activities')
    print('1.Cash Withdrawal')
    print('2.Balance Enquiry')
    activities = int(input('Enter your choice: '))

    if (activities == 1):
        new_user.cashWithDrawl()
    elif(activities == 2):
        new_user.balanceEnquiry()
    else:
        print('Enter a valid number')

if __name__ == '__main__':
    main()
    