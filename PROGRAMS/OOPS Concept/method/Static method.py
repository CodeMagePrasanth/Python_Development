  # bank example

class Bank:
    BankName = 'ABCD'
    BranchName = 'XYZ'
    IFSCcode = 'ABC001'
    Roi = 0.32
    def __init__(self, Name, ACCNO, Balance, Mno,Pin):
        self.Name = Name
        self.ACCNO = ACCNO
        self.Balance = Balance
        self.Mno = Mno
        self.Pin = Pin
    def Checkbal(self):
        if (self.Pin == self.Getpin()):
            print('Available Balance i : {}'.format(self.pin))
        else:
            print('Incorrect Pin')
    def deposite(self):
        if (self.Pin == self.Getpin()):
            amt= int(input('Enter Amount to be Deposited: '))
            self.Balance = self.Balance + amt
            print('Amount Deposited Successfulluy !!')
        else:
            print('Incorrect Pin')
    def widthdraw(self):
        if (self.Pin == self.Getpin()):
            amt = int(input('Enter ther amout to be debited;'))
            if(self.Balance >= amt):
                self.Balance = self.Balance - amt
                print('Amount Debited successfully!!')
            else:
                print('Incorrect pin')
    @staticmethod
    def Getpin():
        return int(input('Enter 4 Digits Pin :'))

ob1 = Bank('ravi',245245245,2000,4524525262,2452)
ob1.widthdraw()
ob1.deposite()
