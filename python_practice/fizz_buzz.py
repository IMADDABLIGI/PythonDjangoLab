def fizz_buzz(num: int) -> None:
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz_Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    num += 1
