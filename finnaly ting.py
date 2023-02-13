import os
import random, string
import datetime as dt

intro = f"""

                                                1 SumOfNumbers
                                                2 IsEven
                                                3 EvenOrOddForLoop
                                                4 EvenOrOddWhileLoop
                                                5 Biggest
                                                6 PasswordCrack

"""

def SumOfNumbers(num):
    sum = 0
    i=0
    while i <= num:
         sum = sum + i
         i+=1
    return(sum)

def IsEven(a):
    if a % 2 == 0:
        print(bool(True))
    else:
        print(bool(False))
    return    


def PasswordCrack():
    print('Your password (4 characters)', end=''); num = str(input('  :  '))
    times =0
    print("Cracking password...")
    while True:
        passwordtest = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        if passwordtest == num:
            times+=1
            print(f"cracked password! '{passwordtest}', It took {times} amount of tries")
            break
        else:
            times+=1
            pass      

def EvenOrOddForLoop(num):

    for i in range(num):
        if i % 2 == 0:
            print(f"{i} is an even number.")
        else:
            print(f"{i} is an odd number.")

def Biggest(numbers):
    
    e = 0
    for i in numbers:
        if i > e:
            e = i
    print(f"out of {numbers}, {e} was the biggest")

def EvenOrOddWhileLoop(num):
    x=0
    while x != num:
        x+=1
        if x % 2 == 0:
            print(f"{x} is an even number.")
        else:
            print(f"{x} is an odd number.")
    return

def startmenu():
    print(intro)
    print(f'[>] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       print("SumOfNumbersOutput")
       s = SumOfNumbers(3)
       print(s) # should return 6
       s = SumOfNumbers(9)
       print(s) # should return 45

    elif choice == '2':
        os.system('cls')
        print('Your number (even = true, odd = false)', end=''); a = int(input('  :  ')); IsEven(a)

    elif choice == '3':
        os.system('cls')
        print("")
        print("Even or Odd Output")
        EvenOrOddForLoop(9)
    
    elif choice == '4':
        os.system('cls')
        print("")
        print("Even or Odd Output")
        EvenOrOddWhileLoop(12)

    elif choice == '5':
        os.system('cls')
        print("Biggest Output")
        print(Biggest([3,5,-2,8,1]))
        
    elif choice == '6':
        os.system('cls')
        PasswordCrack()


if __name__ == '__main__':
    startmenu()