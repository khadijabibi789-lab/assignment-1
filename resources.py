institute_name = "CS Technologies"
course_name = "AI"


def greet(name):
    print("Welcome", name)
    print("You are at", institute_name, "in", course_name, "class")

class hccda:
    def __init__(self, name, age, gender, max_edu):
        self.name = name
        self.age = age
        self.gender = gender
        self.max_edu = max_edu

    def check_qualified(self):
        if (self.age>18 and self.age<40):
            if (self.max_edu >= 16):
                print("You are eligibile for this course")
            else:
                print("Sorry we need 16 years of education for enrollment")
        else:
            print("Sorry your are in not good fit for this course")

 
 
 # oop master class
class bank_account:
    # class attributes
    bank_name = "CS Banking System"
    t_fee = 20

    def __init__(self, title, acc_num, balance = 0):
        self.title = title
        self.acc_num = acc_num
        self.__balance = balance

    def deposit(self, amount):
        if (amount > 0):
            self.__balance += amount
            print("deposit success")
        else:
            print("please enter legal amount")

    def withdraw(self, amount):
        if(self.__balance + self.t_fee > amount):
            self.__balance -= amount
            self.__transaction_fee()
            print("Withdraw success")
        else:
            print("Please enter valid amount")
            self.print_slip()
    def __transaction_fee(self):
        self.__balance -= self.t_fee

    def print_slip(self):
        print('-'*40)
        print(f"Hello{self.title} This is {self.bank_name}")
        print('-'*40)
        print("Your account number is", self.acc_num)
        print("Your balance is ", self.__balance)
        print('-'*40)

    def transfer(self, amount, receiver):
        if(self.__balance + self.t_fee > amount):
            self.__balance -= amount
            self.__transaction_fee()
            receiver.__balance += amount
            print("Transaction success")
        else:
            print("Invalid amount")
            self.print_slip()
    

    @classmethod
    def update_t_fee(cls, amount):
        cls.t_fee = amount
        print("updated to", amount)

    @staticmethod
    def greet():
        print("Hellos this is static method")


    #@magic function
    #def __del__(self):
    #    print("your account have been deleted successfully")
    
    def __str__(self):
        return f'Your account balance is {self.__balance}