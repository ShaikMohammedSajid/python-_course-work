data = {
    123456:{"pin":1234,"balance":7000,"history":[]}
    234561:{"pin":1234,"balance":5000,"history":[]}
    345612:{"pin":1234,"balance":6000,"history":[]}
    456123:{"pin":1234,"balance":9000,"history":[]}
}
def menu():
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdrwal")
    print("[v]iew transactions")
    print("[E]xit")

def login():
    global acc_num
    acc_num =(int(input("enter the account number :")))
    pin = int(input("enter your pin"))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False
def check_balance():
    print("current balance :" data[acc_num]["balance"])
def deposite():
                 
        
