#NO-6------------------------------
"""var="Kishore"
print("Hello",var)"""

#NO-7------------------------------

'''fname="Kishore"
lname="c"
fullname=fname+lname
print(fullname)
print(len(fullname))'''

#NO-8------------------------------

'''no=56
item_cost=509.56
description=""
print(type(no))
print(type(item_cost))
print(type(description))'''

#NO-9------------------------------

'''os="Windows"
if ("W" in os):
    print("Yes,W is in windows")
else:
    print("W is not in windows")'''

#NO-10-----------------------------

"""name=str(input("Enter student name:"))
Maths=int(input("Enter Maths mark:"))
Science=int(input("Enter Science mark:"))
Social=int(input("Enter Social mark:"))
total=Maths+Science+Social
print()
average=total/3
print("Name:",name,"\nMaths:",Maths,"\nScience:",Science,"\nSocial:",Social,"\nTotal marks is:",total,"\nAverage of three subject is:",average)
"""

#NO-11-----------------------------

'''print("Enter Business enquiry number from 500 to 600")
number=int(input("Business enquiry number:"))

if number>500 and number<600:
    print("Enter quotation number from 550 to 650")
    quo_number=int(input("Enter the quotation number:"))

    if quo_number>550 and quo_number<650:
        print("Customer names ibm,orcle,hp,klabs")
        cust_name=str(input("Enter customer name:"))
   
        
        if cust_name==('ibm' or 'orcle' or 'hp' or 'klabs'):
            print("Enter PO number from 500 to 1000")
            po_number=int(input("Enter PO number:"))
       
            if po_number>500 and po_number<1000:
                print("Business enquiry number is:",number,"\nQuotation number is:",quo_number,"\nCustomer name is:",cust_name,"\nPO is:",po_number)
            else:
                print("PO number is not within range")
        else:
            print("Customer name is not matched")
    else:
        print("Quotation number is not within range")
else:
    print("Business enquiry number is not matched")'''


#NO-12-------------------------------

'''s='1A2B3C45d6e7'
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
        
print('total number of digit is:',sum)'''
    

#NO-13-------------------------------

'''s='welcome'
x=0
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        print("vowels present in s=",i)
        
        x+=1
print("total number of vowels is:",x)'''
        
        
        
#NO-15-------------------------------

"""s1="bin:usr:daemon:/bin/bash:x:/usr/bin/tcsh:false"
x=0
for i in s1:
    if i==":":
        x=x+1
print("number of ':' present in s1 is:",x)


s2="This is sample test line\n"
s2.strip()
print(s2)"""














