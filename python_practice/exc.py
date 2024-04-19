from fizz_buzz import fizz_buzz


#--------------Open-File--------------
#--------------Write-Append--------------
    
# with open("text1.txt", "w") as file:
#     file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# with open("text1.txt", "a") as file:
#     file.write("\n Birds flyins high.")

#--------------Try-Except-Block--------------
#--------------Read-Only--------------

# try:
#     with open("text1.txt") as file: #by using {with}block it makes sure that the file is safely oppened and safely closed
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

# def printing(**user):
#     print(user["name"])
#     print(user["city"])

# printing(name="IMAD", age=23, school=1337, city="CASABLANCA")

#---------------Fizz-Buzz--------------

fizz_buzz(97)