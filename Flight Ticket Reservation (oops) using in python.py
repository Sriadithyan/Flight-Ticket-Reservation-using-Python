#Login Process:
class Login:
    def __init__(self):
        self.Name = input("Enter UserName:")
        self.Number = input("Enter Your Number:")
        self.Email=input("Enter Your Email:")
        self.password = input("Enter Your Password:")
        print("\t\t", "*"*54)
        print("\t\t\t", "Login Please Wait for a Minute")
        print("\t\t", "*"*54)
        print()
        print("\t\t\t", "Please Wait")
        print()

    def s(self):
        
        if self.Name.isalpha() and len(self.Name) <= 15:
            print("Name:", self.Name)
        if len(self.Number) <= 10:
            print("Number:", int(self.Number))
        if '@' in self.Email and '.' in self.Email and self.password:
            print("Email", self.Email)
        if self.password.isdigit() and len(self.password)<=10:
            print("Your Password Successfully Created")
            print()
            print("\t\t", "*"*46)
            print("\t\t\t", "Successfully Completed")
            print("\t\t", "*"*46)
            print()
            
        else:
            print('Your Details Not Corret, Please Check')
            return self.__init__()
            return self.s()

# ii)flight Availability:

class Flight():
    def z(self):
        self.flights = [
            {"departure": "New York", "arrival": "London", "date": "2024-03-15", "fare": 2800, "seats": 100,'Id':1},{"departure": "London", "arrival": "Paris", "date": "2024-03-16", "fare": 1600, "seats": 117,'Id':2},{"departure": "India", "arrival": "Australia", "date": "2024-03-17", "fare": 3450, "seats": 138,'Id':3}]
        print(self.flights)

    def q(self):
        destination = input("Enter destination: ")
        found_flights = []
        f=False
        for flight in self.flights:
            if flight["arrival"] == destination:
                found_flights.append(flight)
                f=True
        if not f:
            print("Destination Wrong")
            return self.q()
            
        if found_flights:
            print("Flights to:", destination)
            for flight in found_flights:
                print(flight)
        else:
            print("No flights found to", destination)
    
        print()
        print()
   
#Seats Availability and Fare:     

    def e(self):
        seat = int(input("Enter the number of seats: "))
        fare1 = int(input("Enter the fare per seat: "))
        f = False
        
        for i in self.flights:
            if i['seats'] >= seat:
                print()
                print("Sufficient seats available")  
                if i['fare'] == fare1:
                    print()
                    print("Fare matches")  
                    f = True
                    break
        if not f:
            print(" Fare Invalid")
            return self.e()


#Cashier Login:

class Cash():
    def p(self):
        self.c= [{"Name":"Cashier1","Password": "Cashier_1234"},{"Name":"Cashier2","Password":"Cashier_5678"}]
        
        self.username = input("Enter Cashier username: ")
        self.password = input("Enter Cashier password: ")
        f=False
        
        for i in self.c:
            if i['Name']==self.username and i['Password']==self.password:
                print("Login successful")
                f=True
                break
        if not f:
            print("Check Your Username or Password, Please Try again")
            return self.p()

#Cashier Approve and Issue in the Cash or Ticket:

    def i(self):
        
        Departure = input("Enter the Departure: ")
        Id = int(input("Enter ID: "))

        f= False
        for flight in self.flights:
            if flight['Id'] == Id and flight['departure'] == Departure:
                print("Id Confirmed")
                f= True
                break
        if not f:
            print("Id Wrong")
            return self.i()
    
    def r(self):    
        amount=0
        seat = int(input("Enter the number of seats: "))
        fare1 = int(input("Enter fare: "))
        f= False
        for flight in self.flights:
            if flight['fare'] == fare1:
                print("Cash Approved")
                amount = seat * fare1
                print("Please Wait a Minute")
                print("Total Amount:", amount)
                print("\t\t", "*"*67)
                print("\t\t\t\t","Successfully Paid a cash")
                print("\t\t\t\t\t","Enjoy Your Ride")
                print("\t\t", "*"*67)
                f= True
                break

        if not f:
            print("Issue in the cash or seat")
            return self.r()

#Passenger Logout:
class Return(Login, Flight, Cash):

    def t(self):
        f=False
        z=input("Do you want to Change the flight (Yes/No:)")
        if z=="yes" or  z=="Yes":
            return self.z(),self.q(),self.e()
            f=True
        if not f:
            print("None")
            
                
#Cashier Logout:

    def h(self):
        c = input("Please Login to change the Ticket and Fare Enter (Yes) or Enter (exit) logout: ")
        if c=="Yes"or c=="yes":
            return self.p(),self.i()
        else:
            print("Logout.......")
            

                
a=Return()
a.s()
a.z()
a.q()
a.e()
a.p()
a.i()
a.r()
a.t()
a.h()

