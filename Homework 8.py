


# 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს
#    რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.



# int_list = [10, 20, 30, 40]


# def add_to_int_list(*numbers):
#     global int_list
#     int_list.extend(numbers)


# add_to_int_list(50, 60, 70)
# print(int_list)  



# 2.დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად 
#   უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

# def calculate_sum(numbers):
#     return sum(numbers)

# numbers_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# result = calculate_sum(numbers_list)
# print("Sum of the numbers:", result)




# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე 
#    სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

# gl_str = "Global"

# def create_local_variable():
#     gl_str = "Local"
#     return gl_str

# result = create_local_variable()
# print("Value of local variable:", result) 
# print("Value of global variable:", gl_str) 



# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს
#    (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).


# def sum_of_digits(number):
#     if number < 10:
#         return number
#     else:
#         return number % 10 + sum_of_digits(number // 10)


# num = 12345
# result = sum_of_digits(num)
# print("Sum of digits in", num, "is:", result)




# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს 
#    მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)


# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# input_string = "Hello"
# result = reverse_string(input_string)
# print("Original:", input_string)
# print("Reversed:", result)

# # import requests
#  urt = pip 


import requests
def  get_products():
   api_url = "https://fakestoreapi.com/products"    
   response = requests.get(api_url)

   print(response)
