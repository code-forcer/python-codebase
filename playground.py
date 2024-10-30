#Wrtiting a script to slice user email on input

#Take user email:

email_value = str(input("Enter your email here: "))

print("Hello your email is:",email_value)

if '@' in email_value:
    print('Your input value is correct')
    print("starting  the mail spliting logic")
    email_split = email_value.split('@')
    print("Your mail split value is :",email_split)
else:
    print('Invalid input')


#Start slicing logic:
