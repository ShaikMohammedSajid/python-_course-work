
#NAME CREATION
import re
fullname = input("enter your name :")
pattern = r"^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$"# IMP LINE FOR NAME CREATION OF WEBSITE,THERE WE GAVE SPACE SO THAT WE WANT SPACE
res = re.fullmatch(pattern,fullname)
print("valid name" if res else "invalid name")

patttern = r"^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$"
#EMAIL CREATION
import re
email = input("enter your email :")
pattern = r"^[A-Za-z0-9._]+@[A-Za-z0-9._]+\.[A-Za-z]{2,}$" # THIS IS FOR EMAIL CREACTION"\."is for the . we put in email
res = re.fullmatch(pattern,email)
print("valid email" if res else "invalid email")

#PHONE NUMBER CREATION
import re
phone_num = input("enter your phon number :")
pattern = r"^(?:\+91|0)?[6-9]\d{9}$"
res = re.fullmatch(pattern,phone_num)
print("valid number" if res else "invalid number")

#PASSWORD CREATION
import re
password = input("enter your password :")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%8?&]{8,}$"
res = re.fullmatch(pattern,password)
print("valid pasword" if res else "Invalid password")


import re
name = input("enter your username :")
adhar = input("enter your adhar number :")
pan_card = input("enter your pancard number :")
pattern = r"^[A-Za-z0-9._]( [A-Za-z0-9._]){6,}$"
pattern2 = r"^[0-9]{0,12}$"
pattern3 = r"^[A-Za-z0-9]$"
res = re.fullmatch(pattern,name)
res1 = re.fullmatch(pattern2,adhar)
res2 = re.fullmatch(pattern3,pan_card)
print("valid name" if res else "invalid name")
print("valid adhar number" if res1 else "invalid adhar number")
print("valid pan_card" if res2 else "invald pan_card")