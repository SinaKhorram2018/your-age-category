# Program to determine your age category
while True:
    try:    
        age = int(input("Enter your age : "))
        
        while age :
            if age <= 11:
                print("You are a" , age, "years old child ! \n")
                age = int(input("Enter your age : "))
                
            elif (age >= 12 and age <= 18 ):
                print("You are a" , age, "years old teenager ! \n")
                age = int(input("Enter your age : "))
                
            elif age == 19:
                print("You are of legal age and You are a" , age, "years old teenager ! \n")
                age = int(input("Enter your age : "))
            
            elif age == 20:
                print("You are a" , age, "years old teenager ! \n")
                age = int(input("Enter your age : "))        
                
            elif (age >= 21 and age <= 34):
                print("You are a" , age, "years old young ! \n")
                age = int(input("Enter your age : "))
                
            elif (age >= 35 and age <= 49):
                print("You are a" , age, "years old middle-aged ! \n")
                age = int(input("Enter your age : "))
                
            elif (age >= 50 and age <= 121):
                print("You are a" , age, "years old man or woman ! \n")
    
                age = int(input("Enter your age : "))
                
            else:
                print("Enter the correct age ! \n")
                age = int(input("Enter your age : "))
                
    except ValueError:
            print("Please enter only numbers in the entry ! \n")
    continue
