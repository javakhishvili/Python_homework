


# 1.  დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.



# def fibonacci_numbers(n):
#     fib_sequence = []
#     a, b = 0, 1

#     for _ in range(n + 1):
#         fib_sequence.append(a)
#         a, b = b, a + b

#     return fib_sequence

# # Example usage:
# n = 10  # Change this value to get a different number of Fibonacci numbers
# result = fibonacci_numbers(n)
# print(f"The first {n} Fibonacci numbers are: {result}")



# 2.  დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები. 
#     (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

# def are_anagrams(str1, str2):
#     # Remove spaces and convert strings to lowercase for comparison
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if the sorted characters of both strings are equal
#     return sorted(str1) == sorted(str2)

# # Test cases
# string1 = "race"
# string2 = "care"

# result = are_anagrams(string1, string2)
# if result:
#     print(f"{string1} and {string2} are anagrams.")
# else:
#     print(f"{string1} and {string2} are not anagrams.")


# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

# # Example usage:
# number = 5  # Change this value to calculate factorial for a different number
# fact = factorial(number)
# print(f"The factorial of {number} is: {fact}")


# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. 
#    ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.


# def count_char_occurrences(input_string, char):
#     count = 0
#     for c in input_string:
#         if c == char:
#             count += 1
#     return count

# # Example usage:
# string_input = "Hello, how old are you?"
# character_input = 'o'

# result = count_char_occurrences(string_input, character_input)
# print(f"The character '{character_input}' appears {result} times in the string.")






# int_list = [10, 20, 30, 40]


# def add_to_int_list(*numbers):
#     global int_list
#     int_list.extend(numbers)


# add_to_int_list(50, 60, 70)
# print(int_list)  


# ---------------------------------------


# def calculate_sum(numbers):
#     return sum(numbers)

# # Example list
# numbers_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# # Calculate sum of numbers in the list
# result = calculate_sum(numbers_list)
# print("Sum of the numbers:", result)

#------------------------


# gl_str = "Global"

# def create_local_variable():
#     gl_str = "Local"
#     return gl_str

# result = create_local_variable()
# print("Value of local variable:", result) 
# print("Value of global variable:", gl_str) 

# ----------------------


# def sum_of_digits(number):
#     if number < 10:
#         return number
#     else:
#         return number % 10 + sum_of_digits(number // 10)


# num = 12345
# result = sum_of_digits(num)
# print("Sum of digits in", num, "is:", result)


#---------------------------


def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

input_string = "Hello"
result = reverse_string(input_string)
print("Original:", input_string)
print("Reversed:", result)


