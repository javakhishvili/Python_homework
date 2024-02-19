

# chess_players = [
#   {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
#   {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
#   {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
#   {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
#   {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
#   {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
#   {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
#   {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
#   {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
# ]


# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს

# 3. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს


# 4. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს

# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია


import json

def convert_to_json(file_address, data):
    with open(file_address, 'w') as file:
        json.dump(data, file)

def read_file_content(file_address):
    with open(file_address, 'r') as file:
        content = file.read()
    return content

def update_file_content(file_address, new_content):
    with open(file_address, 'w') as file:
        file.write(new_content)

def add_players_to_file(file_address, new_players):
    with open(file_address, 'r+') as file:
        data = json.load(file)
        data.extend(new_players)
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()


file_address = "chess_players.json"


convert_to_json(file_address, chess_players)


content = read_file_content(file_address)
print("File content:")
print(content)


new_content = content.upper()  
update_file_content(file_address, new_content)


new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59}
]
add_players_to_file(file_address, new_players)


content_after_addition = read_file_content(file_address)
print("\nFile content after adding new players:")
print(content_after_addition)
