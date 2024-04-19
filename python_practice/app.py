print('Hello world')

# name = input("Enter your name : ")
# birth_year= input("Enter your year of birth : ")
# print(name)
# print(2024 - int(birth_year))


#--------------Conditions-------------- 
# tempature = int(input("Enter today's tempature : "))
# if (tempature > 30):
#     print("It's a hot day")
# elif (tempature < 15):
#     print("It's a cold day")
# else:
#     print("It's a good day")
# print("Drink water")


#--------------While_Loops--------------

# i = 1
# while i <= 1_0:
#     print(i * '+')
#     i+=1

#--------------Lists--------------

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, -1)
# numbers.append(6)
# print(5 in numbers)
# print(numbers) 
# print("lenght of list is : " + str(len(numbers)))
# print(10 in numbers)

#--------------For_Loops--------------

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

#--------------Func-range()--------------

# numbers = range(5, 10, 2)

# for num in numbers:
#     print(num)

#--------------Practicing-function--------------
    
# def welcome(name, age):
#     print(f"Welcome in 1337 {name} {age}") #the function that has not a return value always returns none
 
# welcome("IMAD", 20)
# print(round(1.6))


#--------------Open-File--------------
#--------------Write-Append--------------
    
# with open("text1.txt", "w") as file:
#     file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# with open("text1.txt", "a") as file:
#     file.write("\n Birds flyins high.")

#--------------Try-Except-Block--------------
#--------------Read-Only--------------

# try:
#     with open("text1.txt") as file: #by using with block it makes sure that the file is safely oppened and safely closed
#         print("||---" , file.read() + "---||")
# except FileNotFoundError:
#     print("File not exsited !")

# try:
#     print(file.closed) #Checking if file got closed
# except Exception as e:
#     print(e)

#--------------Function-Optional-Argument--------------
    
# def increment(num, by=1): #The optional argument always comes after the required argument not before !
#     return num + by

# print(increment(2 + 5))

#--------------Tuples-*arg------------- #You can't append a new value to the tuples
#--------------Methodes1
# def multiplication(*numbers):
#     i = 0
#     count = 1
#     max = len(numbers)
    
#     while i < max:
#         count *= numbers[i]
#         i += 1
#     return count

#--------------Methodes2
# def multiplication(*numbers):
#     count = 1
    
#     for number in numbers:
#         count *= number
#     return count

# print(multiplication(4, 5, 10))

#--------------Dictinories-**arg--------------

def printing(**user):
    print(user["name"])
    print(user["city"])

printing(name="IMAD", age=23, school=1337, city="CASABLANCA")