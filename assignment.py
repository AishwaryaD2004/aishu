# fruits = {'grapes','orange'}
# new_fruits = fruits.copy()
# new_fruits.add('blueberry')
# print(fruits)
# print(new_fruits)

# new_fruits.discard("grapes")
# print(new_fruits)

# set1 = {1,2,3,4,5,6}
# set2 = {1,2,3,8,9,4}
# print(set1.isdisjoint(set2))

# print(set1.symmetric_difference(set2))

# set1.update(set2)
# print(set1)

# dict = {'name':'aishu','age':'21','city':'mysore'}
# dict.copy()
# print("copy:",dict)
# print("pop:",dict.pop('name'))
# print("keys:",dict.keys())
# print("values:",dict.values())

# color = input("enter the color of the traffic light(red,yellow,green):").lower()
# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("wait")
# elif color == "green":
#     print("go")
# else:
#     print("invalid color!")

# secret_number = 6
# guess = int(input("guess the number(between 1 and 10):"))
# if guess == secret_number:
#     print("correct! you win!")
# elif guess < secret_number:                               
#     print("too low!")
# else:
#     print("too high!")

# marks = int(input("enter your marks(0-100):"))
# if marks >=90:
    # print("grade A")
# elif marks >=75:
#     print("grade B")
# elif marks >=50:
#     print("grade C")
# else:
#     print("fail")

# day_number = int(input("enter a number(1-7):"))
# if day_number == 1:
#     print("monday")
# elif day_number == 2:
#     print("tuesday")
# elif day_number == 3:
#     print("wednesday")
# elif day_number == 4:
#     print("thursday")
# elif day_number == 5:
#     print("friday")
# elif day_number == 6:
#     print("saturday")
# elif day_number == 7:
#     print("sunday")
# else:
#     print("invalid day number")

# temp = float(input("enter the temperature in celsius:"))
# if temp >= 35:
#     print("it's too hot!")
# elif temp >= 20:
#     print("the weather is pleasant,")
# elif temp >= 10:
#     print("it's a bit cold,")
# else:
#     print("it's freezing!")

# name = input("enter your name:")
# age = input("enter your age:")
# print("type of name:",type(name))
# print("type of age:",type(age))

# num = input("enter a number:")
# if "." in num:
#     print("it's a float.")
# else:
#     print("it's an integer.")

# val1 = eval(input("enter first value:"))
# val2 = eval(input("enter second value:"))
# if type(val1) == type(val2):
#     print("both are of the same type:", type(val1))
# else:
#     print("different types:",type(val1),"and",type(val2))

# text = input("enter a string:")
# print("first character:",text[0])
# print("last character:",text[-1])
# print("reversed string:",text[::-1])
# print("first 3 characters:",text[:3])

# str1 = input("enter first string:")
# str2 = input("enter second string:")
# result = str1 + " " + str2
# print("concatenated string:",result)

# text = input("enter a string:")
# print("uppercase:", text.upper())
# print("lowercase:", text.lower())
# print("title case:", text.title())
# print("capitalized:", text.capitalize())

# sentence = input("enter a sentence:")
# count = sentence.lower().count("the")
# print("the word 'the' appears",count,"times.")

# text = input("enter a string:")
# if text.isalpha():
#     print("the string contains only alphabets.")
# else:
#     print("the string contains other cahracters too.")

# text = input("enter a string:")
# result = text.replace(" ","-")
# print("string with hyphens:",result)

# test = input("enter a string:")
# vowels = 0
# consonants = 0
# for char in text.lower():
#     if char.isalpha():
        # if char in "aeiou":
        #     vowels += 1
        # else:
        #     consonants += 1
        # print("vowels:", vowels)
        # print("consonants:",consonants)

# marks = int(input("enter your marks:"))
# if marks >= 35:
#     print("you passed the exam!")
# else:
#     print("you failed the exam!")

# length = float(input("enter length of rectangle:"))
# breadth = float(input("enter breadth of rectangle:"))
# area = length * breadth 
# perimeter = 2 *(length + breadth)
# print("area:",area)
# print("perimeter:",perimeter)

# mark1 = float(input("enter marks of subject 1:"))
# mark2 = float(input("enter marks of subject 2:"))
# mark3 = float(input("enter marks of subject 3:"))
# average = (mark1 + mark2 + mark3)/3
# print("average marks:",average)

# P = float(input("enter principal amount:"))
# R = float(input("enter rate of interest:"))
# T = float(input("enter time in years:"))
# SI = (P*R*T)/100
# print("simple interest:",SI)

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# print(a, ">",b,":", a > b)
# print(a, "<",b, ":", a < b)
# print(a, "==",b,":", a == b)
# print(a, "!=",b, ":", a != b)
# print(a, ">=",b, ":", a >= b)
# print(a, "<=",b, ":", a <= b)

# num = float(input("enter a number:"))
# if num == 100:
#     print("the number is equal to 100.")
# elif num > 100:
#     print("the number is greater than 100.")
# else:
#     print("the number is less than 100.")

# str1 = input("enter first string:")
# str2 = input("enter second string:")
# if len(str1) == len(str2):
#     print("both strings have equal length.")
# else:
#     print("strings do not have equal length.")

# x = 10
# x += 5
# x *= 2
# x -= 3
# print("final value of x:",x)

# num = float(input("enter a number:"))
# num /= 2
# print("after /= 2:", num)
# num //=2
# print("after //= 2:",num)
# num **= 2
# print("after **= 2:",num)

# fruits = ["apple","banana","orange","grape"]
# print("is 'apple' in fruits?","apple" in fruits)
# print("is 'orange' in fruits?", "mango" in fruits)

# text = input("enter a string:")
# char = input("enter a character to check:")
# if char in text:
#     print(f"'{char}' is present in the string.")
# # else:
#     print(f"'{char}' is not present in the string.")

# numbers = [1,2,3,4,5]
# print("is 3 in list?", 3 in numbers)
# print("is 7 not in list?", 7 not in numbers)

# sentence = input("enetr a sentence:")
# if "python" in sentence:
#     print("the word 'python' is  present.")
# else:
#     print("the word 'python' is not present.")

# list1 = [1,2,3]
# list2 = [1,2,3]
# print("list1 == list2:", list1 == list2)
# print("list1 is list2:",list1 is list2)

# listA = [10,20,30]
# listB = listA
# print("listA is listB:", listA is listB)
# print("listA is not listB:",listA is not listB)

#  topping = input("choose a pizza topping(cheese,pepperoni,mushroom):").lower()
#  if topping == "cheese":
#     print("cheesy choice!")
# elif topping == "pepperoni":
#     print("spicy and nice!")
# elif topping == "mushroom":
#     print("good healthy!")
# else:
#     print("that's a unique  topping!")

# height = int(input("enter your height in cm:"))
# if height >= 140:
#     print("you can ride all the roller coasters!")
# elif height >= 120:
#     print("you can ride kids' rides only.")
# else:
#     print("you are too small for the rides.")

# score = int(input("enter your game score (0-100):"))
# if score >= 90:
#     print("champion!")
# elif score >= 70:
#     print("good player!")
# # elif score >= 50:
#     print("not bad!")
# else:
#     print("try again!")

# weather = input("enter the weather(sunny,rainy,cold):").lower()
# if weather == "sunny":
#     print("wear sunglasses!")
# elif weather == "rainy":
#     print("take an umbrella!")
# elif weather == "cold":
#     print("wear a jacket!")
# else:
#     print("check the weather again!")

# month = int(input("enter your birth month(1-12):"))
# if month in [1,2,3]:
#     print("you were born in early year!")
# elif month in [4,5,6]:
#     print("you were born in summer!")
# elif month in [7,8,9]:
#     print("you were born in mid-year!")
# elif month in [10,11,12]:
#     print("you were born at year end!")
# else:
#     print("invalid month!")

# import random 
# secrete_number =random.randint(1,20)
# attempt=10
# print("WELCOME TO THE GUESS NUMBER")
# while True:
#     guess_number =int(input("enter the guess  number:"))
#     attempt=attempt-1
#     if guess_number<secrete_number:
#         print(f"(guess_number): is too low")
#     elif guess_number==secrete_number:
#         print(f"CONGRATS YOU GUESS THE NUMBER IN (attempt)is ATTEMPT ")
#     else:
#         print(f"(guess_number): is too high")

# import random 
# print("welcome to rock☁,paper📄,scissors✂")
# print("rules: rock beats scissors,scissors beats paper,paper beats rock.")
# user_input = input("choose rock,paper,or scissors:").lower()
# computer_choice=random.choices (('rock','paper','scissors'))
# print('your choice=',user_input)
# print('computer_choice=',computer_choice)
# if user_input == computer_choice:
#     print("it's a tie!😑")
# elif user_input == 'rock' and computer_choice == 'scissors':
#     print('you win!😍')
# elif user_input == 'scissors' and computer_choice == 'paper':
#      print('you win!😍')
# elif user_input == 'paper' and computer_choice =='rock':
#      print('you win!😍')
# else:
#     print('you loose!😌')
# print('THANK YOU FOR PLAYING😊')
            
# import random
# words = ["apple", "grape", "light", "stone", "crane"]
# secret = random.choice(words)

# print("🎉 Welcome to Wordle!")
# print("Guess the 5-letter word. You have 6 tries.")
# print("✅ = Correct spot, 🔁 = Wrong spot, ❌ = Not in word")

# for turn in range(6):
#     guess = input(f"\nGuess {turn + 1}: ").lower()

#     if len(guess) != 5:
#         print("Please enter a 5-letter word.")
#         continue

#     result = ""
#     for i in range(5):
#         if guess[i] == secret[i]:
#             result += "✅"
#         elif guess[i] in secret:
#             result += "🔁"
#         else:
#             result += "❌"
#     print("Result:", result)

#     if guess == secret:
#         print("🎉 You guessed it!")
#         break
# else:
#     print("😢 You ran out of tries. The word was:", secret)

# import random

# words = ["apple", "grape", "light", "stone", "crane"]
# secret = random.choice(words)
# print("Secret word is:", secret)

# import random
# words = ["apple", "grape", "stone", "crane", "light"]
# secret = random.choice(words)

# print("🎉 Welcome to Wordle!")
# print("Guess the 5-letter word. You have 6 tries.")
# print("✅ = Correct spot, 🔁 = Wrong spot, ❌ = Not in word")
# for attempt in range(6):
#     guess = input(f"\nAttempt {attempt + 1}/6: ").lower()
#     if len(guess) != 5:
#         print("❗ Please enter a 5-letter word.")
#         continue
#     if guess not in words:
#         print("❗ Not a valid word.")
#         continue
#     result = ""
#     for i in range(5):
#         if guess[i] == secret[i]:
#             result += "✅"
#         elif guess[i] in secret:
#             result += "🔁"
#         else:
#             result += "❌"
#     print("Feedback:", result)

#     if guess == secret:
#         print("🎉 Correct! You guessed the word!")
#         break
# else:
#     print("😢 You're out of tries. The word was:", secret)

# import random
# words = ["apple", "grape", "share", "crane", "light"]
# secret = random.choice(words)

# print("🎉 Welcome to Wordle!")
# print("Guess the 5-letter word. You have 6 tries.")
# print("✅ = Correct spot, 🔁 = Wrong spot, ❌ = Not in word")
# for attempt in range(6):
#     guess = input(f"\nAttempt {attempt + 1}/6: ").lower()

#     if len(guess) != 5:
#         print("❗ Enter a 5-letter word.")
#         continue
#     if guess not in words:
#         print("❗ Not a valid word.")
#         continue

#     feedback = ""
#     for i in range(5):
#         if guess[i] == secret[i]:
#             feedback += guess[i].upper() + "✅ "
#         elif guess[i] in secret:
#             feedback += guess[i].upper() + "🔁 "
#         else:
#             feedback += guess[i].upper() + "❌ "

#     print("Guess: ", guess.upper())
#     print("Result:", feedback.strip())

#     if guess == secret:
#         print("🎉 You guessed it!")
#         break
# else:
#     print("😢 Out of tries! The word was:", secret.upper())

# import random
# words = ["apple", "grape", "light", "share", "crane"]
# secret = random.choice(words)

# print("🎉 Welcome to Wordle!")
# print("Guess the 5-letter word. You have 6 tries.")
# print("✅ = Right place, 🔁 = Wrong place, ❌ = Not in word")

# for i in range(6):
#     guess = input(f"\nAttempt {i+1}/6: ").lower()

#     if len(guess) != 5:
#         print("❗ Enter exactly 5 letters.")
#         continue
#     if guess not in words:
#         print("❗ Not a valid word.")
#         continue

#     result = ""
#     for j in range(5):
#         if guess[j] == secret[j]:
#             result += guess[j].upper() + "✅ "
#         elif guess[j] in secret:
#             result += guess[j].upper() + "🔁 "
#         else:
#             result += guess[j].upper() + "❌ "
#     print("Result:", result.strip())

#     if guess == secret:
#         print("🎉 You guessed the word!")
#         break
# else:
#     print("😢 Out of tries. The word was:", secret.upper())

# import random
# words = ["apple", "grape", "light", "share", "crane"]
# print("🎉 Welcome to Wordle!")
# while True:
#     secret = random.choice(words)
#     print("\nGuess the 5-letter word. You have 6 tries.")
#     print("✅ = Right place, 🔁 = Wrong place, ❌ = Not in word")

#     for i in range(6):
#         guess = input(f"\nAttempt {i+1}/6: ").lower()

#         if len(guess) != 5:
#             print("❗ Enter exactly 5 letters.")
#             continue
#         if guess not in words:
#             print("❗ Not a valid word.")
#             continue

    #     result = ""
    #     for j in range(5):
    #         if guess[j] == secret[j]:
    #             result += guess[j].upper() + "✅ "
    #         elif guess[j] in secret:
    #             result += guess[j].upper() + "🔁 "
    #         else:
    #             result += guess[j].upper() + "❌ "
    #     print("Result:", result.strip())

    #     if guess == secret:
    #         print("🎉 You guessed it!")
    #         break
    # else:
    #     print("😢 Out of tries. The word was:", secret.upper())
    # again = input("\nPlay again? (yes/no): ").lower()
    # if again != "yes":
    #     print("👋 Thanks for playing!")
    #     break

# import random
# import time
# words = ["apple", "grape", "light", "share", "crane"]
# GREEN = "\033[92m"   
# YELLOW = "\033[93m"
# GREY = "\033[90m" 
# RESET = "\033[0m"

# wins = 0
# losses = 0

# print("🎉 Welcome to Wordle!")

# while True:
#     secret = random.choice(words)
#     guesses = []
#     start = time.time()
#     print("\nGuess the 5-letter word. You have 6 tries.")

#     for attempt in range(6):
#         guess = input(f"\nAttempt {attempt+1}/6: ").lower()
#         if len(guess) != 5:
#             print("❗ Enter exactly 5 letters.")
#             continue
#         if guess not in words:
#             print("❗ Word not in list.")
#             continue

#         guesses.append(guess)
#         feedback = ""
#         for i in range(5):
#             if guess[i] == secret[i]:
#                 feedback += GREEN + guess[i].upper() + "✅ " + RESET
#             elif guess[i] in secret:
#                 feedback += YELLOW + guess[i].upper() + "🔁 " + RESET
#             else:
#                 feedback += GREY + guess[i].upper() + "❌ " + RESET
#         print("Feedback:", feedback.strip())

#         if guess == secret:
#             end = time.time()
#             print(f"🎉 You guessed it in {attempt+1} tries and {int(end - start)} seconds!")
#             wins += 1
#             break
#     else:
#         losses += 1
#         print(f"😢 Out of tries! The word was: {secret.upper()}")
#     print("\nYour guesses:")
#     for g in guesses:
#         print("-", g.upper())


#     print(f"\nScore: Wins = {wins}, Losses = {losses}")

#     again = input("\nPlay again? (yes/no): ").lower()
#     if again != "yes":
#         print("👋 Thanks for playing!")
#         break

# def great_user(name,greeting = "hello"):
#     print(f"{greeting}, {name}!")

# great_user("aishu")

# def power(base,exponent=2):
#     return base ** exponent
# print(power(6))

# def student_info(name,age,grade):
#     print(f"name: {name},age: {age},grade: {grade}")
# student_info(name="aishu",age=22,grade="A")

# def book_info(title, author,price):
#     print(f"title: {title},author:{author},price:${price}")
# book_info("python 101",author="john doe",price=499)

# def sum_all(*numbers):
#     return sum(numbers)
# print(sum_all(1,2,3,4,5))
# print(sum_all(10,20))

# def display_names(*names):
#     for name in names:
#         print(name)
# display_names("aishu","chethu","abhi","nidhi","bhumi")

# def print_student_data(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# print_student_data(name="aishu",age=22,grade="A",city="mysore")

# def calculate_bill(**items):
#     total = sum(items.values())
#     return total
# print(calculate_bill(apple=50,banana=30,milk=60))

# def profile(name, *hobbies,**details):
#     print(f"name: {name}")
#     print("*hobbies:",','.join(hobbies))
#     for key, value in details.items():
#         print(f"{key}:{value}")
# profile("aishu","reading","coding",age=22,city="mysore",profession="student")

# def order_summary(customer,items=None,*extras,**order_details):
#     print(f"customer:{customer}")
#     print(f"items:{items}")
#     print(f"extras:",extras)
#     for key,value in order_details.items():
#         print(f"{key}:{value}")
# order_summary(
#     "aishu",
#     ["pizza","burger"],
#     "extra cheese","cold drink",
#     address="mysore",payment="online",
#     delivery_time="40 mins"
# )

# class Place:
#     def __init__(self, state, district, specialization):
#         self.state = state
#         self.district = district
#         self.specialization = specialization

#     def display_info(self):
#         print("State:", self.state)
#         print("District:", self.district)
#         print("Specialization:", self.specialization)

# p1 = Place("Karnataka", "Udupi", "Famous for Krishna Temple and Beaches")
# p1.display_info()

# class Animal:
#     def __init__(self, name, species, habitat, diet, special_feature):
#         self.name = name
#         self.species = species
#         self.habitat = habitat
#         self.diet = diet
#         self.special_feature = special_feature

#     def display_info(self):
#         print("Animal Bio ")
#         print("Name:", self.name)
#         print("Species:", self.species)
#         print("Habitat:", self.habitat)
#         print("Diet:", self.diet)
#         print("Special Feature:", self.special_feature)
#         print("-" * 30)

# animal1 = Animal("Elephant", "Elephas maximus", "Grasslands", "Herbivore", "Largest land animal")
# animal1.display_info()

# class Tree:
#     def __init__(self, tree_name, fruit_name, fruit_color):
#         self.tree_name = tree_name
#         self.fruit_name = fruit_name
#         self.fruit_color = fruit_color

#     def display_info(self):
#         print("🌳 Tree Information 🌳")
#         print("Tree Name:", self.tree_name)
#         print("Fruit Name:", self.fruit_name)
#         print("Fruit Color:", self.fruit_color)
#         print("-" * 30)


# class Plant:
#     def __init__(self, plant_name, fruit_name, fruit_color):
    #     self.plant_name = plant_name
    #     self.fruit_name = fruit_name
    #     self.fruit_color = fruit_color

    # def display_info(self):
    #     print("🌱 Plant Information 🌱")
    #     print("Plant Name:", self.plant_name)
    #     print("Fruit Name:", self.fruit_name)
    #     print("Fruit Color:", self.fruit_color)
    #     print("-" * 30)

# tree1 = Tree("Mango Tree", "Mango", "Yellow")
# plant1 = Plant("Tomato Plant", "Tomato", "Red")

# tree1.display_info()
# plant1.display_info()

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks

#     def display_info(self):
#         print("🎓 Student Details 🎓")
#         print("Name:", self.__name)
#         print("Roll No:", self.__roll_no)
#         print("Marks:", self.__marks)

# s1 = Student("Aishu Shetty", 101, 95)
# s1.display_info()

            
