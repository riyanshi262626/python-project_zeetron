#!/usr/bin/env python
# coding: utf-8

# In[49]:


class ClothingStore:
    def __init__(self):
        print("\t\t\t\t\tABC clothing store")
        print("\t\t\t\t\tBy Masaba")
        print("Items")
        x=["male","female","other"]
        for k in x:
            print("\n\n\n",k)
    def male(self):
        q=["Bottomwear","Topwear","Accessories"]
        for k in q:
            print("\n\n",k)
    def female(self):
        w=["Bottomwear","Topwear","Accessories"]
        for k in w:
            print("\n\n",k)
    def bottom(Self):
        e=["jeans","pants","shorts","pyjamas"]
        r=[700,433,434,222]
        bottom1={"Bottomwear types":e,"Price":r}
        import pandas as pd
        df=pd.DataFrame(bottom1)
        print("\nBottom Wear\n")
        print(df)
        d=[]
        while e:
            e=True
            b=int(input("Enter the value position : "))
            c=int(input("Enter the Quantity:"))
            z=bottom1["Price"][b]
            y=z*c
            d.append(y)
            e=input("you want to reorder(yes/no):")
            if(e=="no"):
                print('Thank you')
                break
        t=sum(d)
        m=(sum(d)*0.12)
        k=t+m
        print("Service tax = 12%")
        print("Total amount:",t,"rupees")
        print("Total Amount Including Service Tax:",k,"Rupees")        
    def top(Self):
            e=["Shirt","T-shirt","vests","Tops"]
            r=[700,433,434,222]
            top1={"Topwear types":e,"Price":r}
            import pandas as pd
            df=pd.DataFrame(top1)
            print("\nTop Wear\n")
            print(df)
            d=[]
            while e:
                e=True
                b=int(input("Enter the value position : "))
                c=int(input("Enter the Quantity:"))
                z=top1["Price"][b]
                y=z*c
                d.append(y)
                e=input("you want to reorder(yes/no):")
                if(e=="no"):
                    print('Thank you')
                    break
            t=sum(d)
            m=(sum(d)*0.12)
            k=t+m
            print("Service tax = 12%")
            print("Total amount:",t,"rupees")
            print("Total Amount Including Service Tax:",k,"Rupees")
    def accessories(Self):
            e=["watches","bags","sunglasses","skincare"]
            r=[700,433,434,222]
            accessories1={"accessories types":e,"Price":r}
            import pandas as pd
            df=pd.DataFrame(accessories1)
            print("\naccessories\n")
            print(df)
            d=[]
            while e:
                e=True
                b=int(input("Enter the value position : "))
                c=int(input("Enter the Quantity:"))
                z=accessories1["Price"][b]
                y=z*c
                d.append(y)
                e=input("you want to reorder(yes/no):")
                if(e=="no"):
                    print('Thank you')
                    break
            t=sum(d)
            m=(sum(d)*0.12)
            k=t+m
            print("Service tax = 12%")
            print("Total amount:",t,"rupees")
            print("Total Amount Including Service Tax:",k,"Rupees")


# In[50]:


obj=ClothingStore()



# In[51]:


x=input("Select your gender:")
if x=="male":
    print(obj.male())
elif x=="female":
    print(obj.female())
else:
    print("Wrong option")


# In[52]:


x=input("Select what you want to buy")
if x=="bottomwear":
    print(obj.bottom())
elif x=="Topwear":
    print(obj.top())
elif x=="accessories":
    print(obj.accessories())


# In[ ]:




