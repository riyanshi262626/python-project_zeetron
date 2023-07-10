#!/usr/bin/env python
# coding: utf-8

# # ELECTRICITY BILL

# In[1]:


billmonth=input("ENter bill month:")
cn=input("enter consumers name:")
ca=input("Enter consumer's address")
crd=input("Enter current reading date:")
prd=input("Enter past reaing date:")
cr=eval(input("Enter the current reading:"))
pr=eval(input("Enter the past reading"))
tc=cr-pr
FS=69.12
UC=43.35
print("\n\n")
print("\t\t\t\t\t\tJODHPUR VIDYUT NIGAM LTD>")
print("\t\t\t\t\t\tCIN no. U4G8GB98HF84HG88949 *BILLOF SUPPLY*")
print("\n\n")
print("Bill month date     : ",billmonth)
print("Subdivision name    : Mahaveer Nagar")
print("Account number      : 838473948")
print("Consumer name       : ",cn)
print("Consumer address    : ",ca)
print("Bill no.            : 439483")
print("Current reading date: ",crd)
print("past reading date   : ",prd)
print("Current reading     : ",cr)
print("past reading        : ",pr)
print("Total consumption   : ",tc)
print("\n\n")
if tc>=0 and tc<=50:
    total=((tc*4.75)+FS+UC)
    print("Total amount till date:",total)
elif tc>50 and tc<=150:
    total=(237.5((tc-50)*6.50)+FS+UC)
    print("total amount till date:",total)
else:
    print("Wrong values entered.")


# In[ ]:




