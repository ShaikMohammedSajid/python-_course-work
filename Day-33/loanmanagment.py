from abc import ABC,abstractmethod
class customer:
    def __init__(self,coustomer_id,name,email,phonenumber,age,income,credit_score):
        self.coustomer_id = coustomer_id
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.age = age
        self.income = income
        self.credit_score = credit_score
    def check_eligibilty(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 25000:
            return False   
        return True 
    def display_coustomer(self):
        print("\n coustomer details")
        print("---------------------------")
        print("coustomer_id", self.coustomer_id)
        print("Name",self.name)       
        print("email",self.email)       
        print("phone number",self.phonenumber)       
        print("age",self.age)       
        print("income",self.income)       
        print("credit_score",self.credit_score)       
sajid = customer(1,"sajid","shaiaksajid@gamil.com",98765432121,21,50000,750)
sajid.display_coustomer()    
print(sajid.check_eligibilty())

class Loan(ABC):
    def __init__(self,loan_id,customer,loan_amount,intrest_rate,tenure):
        self.loan = loan_id
        self.coustome = customer
        self.loan_amount = loan_amount
        self.intrest_rate = intrest_rate
        self.tenure = tenure
        self.__balance = loan_amount
        self.repayment_history = []
        self.status = "Applied"
    @abstractmethod
    def caluclate_emi(self):
        pass
    def check_loan_eligibilty(Self):
        if not self.customer.check_eligibilty:
            self.status = "Rejected"
            return False
        return True 
    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application is Rejected")
            return
        if not self.check_loan_eligibilty():
            print("Customer is not eligible for loan")
            return
        self.status = "Sanctioned"
        print("/nLoan Sanctioned Sucessfully")
    def repay(Self,amount):
        if self.status != "Sanctioned":
            print("Repayment is not allowd")
            print("Loan ststus :",self.status)
        if amount <= 0:
            print("Invalid repayment amount")
            return
        if amount > self.__balance:
            print("Repayment amount is greater than outsatanding Balance")
            return
        self.__balance -= amount  
        self,__total_paid += amount
        self.repayment_history.append(amount)

        print("\nRepayment Succesfull")
        print("Amount paid      : ",amount)
        print("Outstanding Balance       :",self.__balance)

        if self.__balance = 0:
            self.sttus = "Closed"
            print("Loan is closed sucessfully")
    def get_balance(self):
        return self.__balance
    def get_loan_amount(self):
        return self.loan_amount
    def get_total_paid(self):
        return self.__total_paid

    def display_statment(self):
        print("\n")
        print("=" * 40)
        print("LOAN STATMENT")
        print("=" * 40)

        print("Loan ID                    :", self.loan_id)
        priint("Customer name             :", self.customer.name)        
        priint("Loan Amount               :", self.__loan_amount )        
        priint("Intrest Rate              :", self.intrest_rate)        
        priint("Tenure                    :", self.tenure)        
        priint("Outstanding balance       :", self.__balance)        
        priint("Loan status               :", self.self.status)

        print("\n Repayment History")

        if not self.repayment_history:
            print("No Repaymennts Made")
        else:
            for i in range(len(self.repayment_history)):
                print(f"payment {i+1}        :{self.repayment_history[i]}")
        print("=" * 40)
    def __str__(self):
        return (
            f"Loan ID : {self.loan_id},"   
            f"Custromer : {self.customer.name}, "
            f"Loan amount : {self.__loan_amount}, "  
            f"Outstanding : {self.__balance},"
            f"status : {self.status}"
        )  
sajid = customer(1,"sajid","shaiaksajid@gamil.com",98765432121,21,50000,750)
sajid.display_coustomer()    
print(sajid.check_eligibilty())                         
            



     