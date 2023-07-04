import string
import random

characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()")


# print(characters)

# generated_password_list = []

def password_generator():
    password_length = int(input("Enter the password length: "))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print(password)

    password = "".join(password)
    print(password)
    # generated_password_list.append(password)


option = input("If you want to generator password (Yes / No) : ")
if option == "Yes":
    password_generator()
    print(generated_password_list)
elif option == "No":
    print('Program Ended...')
    quit()
else:
    print('Invalid Input. Enter Yes or No next time if you want to generate password.')
    quit()
