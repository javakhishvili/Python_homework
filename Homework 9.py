# 1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

#       params: [1, 2, 3, 4, 5, 6, 7]
#       outputs: [1, 3, 5, 7]






# def group_with_zip(lst1, lst2):
#     return [f"({x}, '{y}')" for x, y in zip(lst1, lst2)]


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# result = group_with_zip(list1, list2)
# print(result)


# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions),
#    თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError). ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
#     params: [1, 2, 3, 4, 5, 6, 7]
#     outputs: [1, 3, 5, 7]



# from functools import reduce
# def product_of_elements(lst):
#     try:
#         product = reduce(lambda x, y: x * y, lst)
#         return product
#     except TypeError:
#         return "Invalid input type. Please provide a list of numbers."
# input_list = [1, 2, 3, 4, 5]
# result = product_of_elements(input_list)
# print(result)

# 3.  დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
#      params: [1, 2, 3, 4, 5, 6, 7]
#      outputs: [1, 3, 5, 7]



# get_odd_elements = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
# input_list = [1, 2, 3, 4, 5, 6, 7]
# result = get_odd_elements(input_list)
# print(result)



# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, 
#    მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა 
#    ისიც გაითვალისწინეთ. მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

#     params: ['hello', 'world', 'coding', 'nod'], 'ing'  
#     outputs: ['coding'] 





def filter_by_ending(lst, ending):
    try:
        filtered_list = list(filter(lambda x: x.endswith(ending), lst))
        return filtered_list
    except TypeError as e:
        return f"Error: {e}"

# Example usage:
input_list = ['hello', 'world', 'coding', 'nod']
ending_string = 'ing'
result = filter_by_ending(input_list, ending_string)
print(result)