#!/usr/bin/env python
# coding: utf-8

# In[2]:


mtab=("\t\t\t\t\t\t")
mtab1=("\t\t")
mtab3=("\t\t\t\t\t\t\t\t\t\t\t")
mtab0=("\t")
mtab5=("\t\t\t")
mtab6=("\t\t\t\t\t\t\t\t")
mtab7=("\t\t\t\t\t\t\t")
a=input("enter your starting point:-")
b=input("enter your end point:-")
c=input("enter travels agency name:-")
d=input("enter name of passenger:-")
x=input("enter age of passenger:-")
y=input("enter gender of passenger:-")
e=input("enter type of bus seat type(sleeper,ac,general,superdelux ac bus):-")
f=input("enter traveling date :-")
g=input("enter reorting time:-")
h=input("enter departure time:-")
k=int(input("enter travelling distance:-"))
print("************************************************************************************************************************\n")
print(mtab,"PYTHON BUS")
print("-------------------------------------------------------------------------------------------------------------------------")
print(mtab,"m.PythonBus.in")
print("--------------------------------------------------------------------------------------------------------------------------")
print("=",mtab,"BOOK BUS TICKET ONLINE",mtab1,"PythonBus*=--")
print(mtab3,"PythonBus Helpline:")
print(mtab3,"8619005685")
print("***************************************************************************************************************************")
print(a," to ",b,mtab1,f,mtab5,c)
print("***************************************************************************************************************************\n")
print("Passanger NAME:",mtab0,"PythonBus ticket#",mtab0,"Seat Numbers(s)",mtab0,"PNR#",mtab1,"Trip#")
print("MR./MRS.",d,mtab1,"TF6Z98757372",mtab1,"SU4",mtab5,"JBR19054",mtab0,"24241791")
print("---------------------------------------------------------------------------------------------------------------------------\n")
print("BUS TYPE",mtab0,"REPORTING TIME")
print(e,mtab0,g,"\n\n")
print("Boarding Point Address:",mtab0,"DEPARTURE TIME")
print("Sholinganallur",mtab5,h)
print("---------------------------------------------------------------------------------------------------------------------------\n")
print("Payment Detail")
print("Insurance Fee: ",mtab,"4.00 Rupees")
print("Convenience Fee:",mtab,"11.80 Rupees")
if e=="GENERAL":
    fare=k*0.94
    totalamount=11.80+4.00+fare
    print("FARE:",mtab6,fare,"Rupees")
    print("TotalAmount:",mtab7,totalamount,"Rupees")
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("The Total Price displayed on the ticket includes all applicable goverement taxes.")
    print("There will be no refund for any condition")
    print("Seats are subject to availability")
elif e=="SLEEPER":
    fare=k*1.25
    totalamount=11.80+4.00+fare
    print("FARE:",mtab6,fare,"Rupees")
    print("TotalAmount:",mtab7,totalamount,"Rupees")
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("The Total Price displayed on the ticket includes all applicable goverement taxes.")
    print("There will be no refund for any condition")
    print("Seats are subject to availability")
elif e=="AC":
    fare=k*1.59
    gst=(fare-(fare*0.05))
    totalamount=11.80+4.00+gst
    print("FARE:",mtab6,fare,"Rupees")
    print("GST5%:",mtab6,gst,"Rupees")
    print("TotalAmount:",mtab7,totalamount,"Rupees")
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("The Total Price displayed on the ticket includes all applicable goverement taxes.")
    print("There will be no refund for any condition")
    print("Seats are subject to availability")
elif e=="SUPERDELUX AC":
    fare=k*2.47
    gst=(fare-(fare*0.05))
    totalamount=11.80+4.00+gst
    print("FARE:",mtab6,fare,"Rupees")
    print("GST5%:",mtab6,gst,"Rupees")
    print("TotalAmount:",mtab7,totalamount,"Rupees")
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("The Total Price displayed on the ticket includes all applicable goverement taxes.")
    print("There will be no refund for any condition")
    print("Seats are subject to availability")
else:
    print("Please check the availability of seat nd bustype")
    print("-------------------------------------------------------------------------------------------------------------------------\n")
    print("The Total Price displayed on the ticket includes all applicable goverement taxes.")
    print("There will be no refund for any condition")
    print("Seats are subject to availability")
    


# In[ ]:




