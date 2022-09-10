# password will be demanded untill you give a correct password
import getpass
database = {"virat.kumar.jha": "123456", "vishal.kumar.jha": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")

