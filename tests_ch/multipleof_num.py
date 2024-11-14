
def multiple_num(value_upto):

    for num in range(1,value_upto+1):
        if num % 3 == 0 and num % 5 == 0:
            output = "Fizzbuzz"
        elif num % 3 == 0 and num % 5 != 0:
            output = "Fizz"
        elif num % 3 != 0 and num % 5 == 0:
            output = "buzz"
        elif num % 3 != 0 and num % 5 != 0:
            output = num
        print(output)

    return
value_upto = 10
multiple_num(value_upto)
