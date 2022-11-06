import mysql.connector as sql, time as t
import signup, instructor, member, equipment, payment, workout

db = sql.connect(host = "localhost", user = "root", password = "225bench", database = "gym1")
cu = db.cursor()

t.sleep(2)

while True:
    print("1. Sign up")
    print("2. Log in")
    print("3. Exit")
    
    choice = int(input("Enter input: "))
    
    if choice == 1:
        signup.SIGN_UP()
    if choice == 2:
        LOG_USER = input("Enter username: ")
        LOG_PASS = input("Enter password: ")
        cu.execute("SELECT USE_USERNAME FROM USER WHERE USE_USERNAME = '"+LOG_USER+"'")
        LOG_USER1 = cu.fetchone()
        cu.execute("SELECT USE_PASSWORD FROM USER WHERE USE_PASSWORD = '"+LOG_PASS+"'")
        LOG_PASS1 = cu.fetchone()
        if LOG_USER1 != None and LOG_PASS1 != None:
            print()
            print("Sign-in successful")
            print("You will be redirected")
            t.sleep(1)
            print()
            
            while True:
                print()
                print("1. Instructor")
                print("2. Member")
                print("3. Equipment")
                print("4. Payment")
                print("5. Workout")
                print("6. Exit")
                
                choice = int(input("Enter primary input: "))
                print()
                
                if choice == 1:
                    instructor.INSTRUCTOR()
                
                if choice == 2:
                    member.MEMBER()
                
                if choice == 3:
                    equipment.EQUIPMENT()
                
                if choice == 4:
                    payment.PAYMENT()
                
                if choice == 5:
                    workout.WORKOUT()
                
                if choice == 6:
                    break
    if choice == 3:
        break
