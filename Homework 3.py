



# # 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც 
#  შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

# arr = [44, 23, 11, 8, 20, 56, 33, 55]
# num = int(input("Enter a number: "))

# if num is arr[5]:
#   print("The number in list")
# else:
#   print("The number not in list")


#-----------------------------------------


  
# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი 
# ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

# Enter an integer: 25
# The number is odd
# #===========================
# Enter an integer: 36
# The number is even


# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

#-------------------------------------------------------

# 3.შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ 
# ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"


# st1 = [12, 23, 6, 3, 55]
# st2 = [6, 2, 23, 44, 55]

# print("Same object : " + str(st1))
# print("Different object : " + str(st2))

# if st1 is st2:
# 	print("Same object")
# else:
# 	print("Different object ")



#-------------------------------------------------------

# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
# თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
# თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.




num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num = int(input("Enter a number: "))

if num == num_list[6]:
      print("Equal ")
elif num >= num_list[3] and num <= num_list[7]:
    print("More than list elements")

else:
    print("None of the conditions were met")

   

