n = int(input("Enter No. of E-mails : "))
print("Enter Valid Emails: ")
email = tuple([input("> ") for _ in range(n)])
print(email)
username = tuple([i.split('@')[0] for i in email])
domain = tuple([i.split('@')[1] for i in email])
print(username)
print(domain)    
