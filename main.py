# This is a sample Python script.

import sys
import time
import random
from functools import reduce
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pip._vendor.distlib.compat import raw_input


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Joshua')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# display print with timer, type writer style
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c != "\n":
            time.sleep(0.01)
        else:
            time.sleep(0.01)


def action0():
    print_menu()


def action1():
    kilo = float(raw_input('enter number of kilometer to convert into miles: '))

    kilo_to_mile(kilo)


def kilo_to_mile(input_kilo):
    # conversion ratios kilo to miles
    conv_fac = 0.621371

    # converts kilo to miles
    miles = input_kilo * conv_fac

    return print('%0.2f Kilometers is equal to %0.2f Miles' % (input_kilo, miles))


def action2():
    year = int(raw_input('Python Program to Check Leap Year: '))
    check_leap(year)


def check_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return print("{0} is a leap year\n".format(year))
            else:
                return print("{0} is not a leap year\n".format(year))
        else:
            return print("{0} is a leap year\n".format(year))
    else:
        return print("{0} is not a leap year\n".format(year))


def action3():
    number = int(raw_input('Python Program to a Decimal number into Bin, Oct and Hex: '))
    dec_conv(number)


def dec_conv(dec):
    print("The decimal value of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.\n")


def action4():
    num = int(raw_input('enter a positive number: '))

    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))


# Factorial of a number using recursion

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


def action5():
    while True:
        # asking for user to enter two prime numbers, p q
        p = int(raw_input('Enter the 1st large prime number: '))
        q = int(raw_input('Enter the 2nd large prime number: '))
        # check if they are prime numbers, multiply them together to get, n
        if is_prime(p) == 1 | is_prime(q) == 1:
            break
        else:
            print('sorry one of your numbers is not a prime number')
    n = p * q  # used in key (n,e)

    r = (p - 1) * (q - 1)  # 1 mod r
    # calc two factors of r, check if not a prime
    i = 1
    while True:
        t = r * i
        if is_prime(t + 1) == 1:  # if true cycle again because it is a prime
            i += 1

        else:  # save doubled value of r into temp check to make sure then save r as temp
            is_prime(t + 1)
            e, d = factors(t + 1)

            if e == d:
                i += 1
            else:
                break

    # public key (n,e) public key is, e, n is p*q
    # private key computed through, p q and e
    # using ed = 1 mod (p-1)(q-1)
    print('Your public key is: ', n, e)
    print('your private key is: ', n, d)

    # msg = int(raw_input('enter your number message here: '))
    # enmsg = encrypt(msg, e, n)
    # print('Your cipher number is: ', enmsg)

    # encmsg = int(raw_input('Enter you encrypted number here: '))
    # demsg = decrypt(encmsg, d, n)
    # print('Your decrypted number is: ', demsg)

    s = raw_input('enter your message here: ')
    action6(s, e, d, n)


def encrypt(msg, e, n):
    return pow(msg, e, n)


def decrypt(msg, d, n):
    return pow(msg, d, n)


# old algorithm to find factors too slow for large numbers
def print_factors(x):
    print("The factors of", x, "are:")
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:  # check if it's a factor
            if (i != x) & (i != 1):  # filter out 1 and x factor.
                factors.append(i)

    e = factors[0]
    d = factors[-1]
    return e, d


# new algorithm to find factors can go up to 16-bit numbers after it is too slow
def factors(n):
    # filter out 1 and n factor
    fac = list(
        reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if (n % i == 0) & (i != n) & (i != 1))))
    e = fac[0]
    d = fac[1]
    return e, d


def check_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                return False
        else:
            print(num, "is a prime number")
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")
        return False


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def action6(s, e, d, n):
    # s = raw_input('enter your message here: ')
    stn = string_to_utf8(s)
    print('\nthis is your message in utf8: \n', stn, '\n')  # change to num

    print('this is your message encrypted: ')  # encrypt
    b = []
    for i in stn:
        b.append(encrypt(i, e, n))
    print(b, '\n')

    print('this is your message decrypted: ')  # decrypt
    g = []
    for i in b:
        g.append(decrypt(i, d, n))
    print(g, '\n')

    nts = utf8_to_string(g)  # change to char
    print('this is your message in ASCII: ', ''.join(nts))


def string_to_utf8(s):
    word = split(s)
    numb = []
    for i in range(0, len(word)):
        msg = ord(word[i])
        # print('utf8 code: ', msg, ' and letter ', word[i])
        numb.append(msg)
    return numb


def utf8_to_string(s):
    number = s  # list(map(int, s.split(' ')))
    string = []
    for i in range(0, len(s)):
        msg = chr(number[i])
        # print('letter : ', msg, ' and utf8 code ', number[i])
        string.append(msg)
    return string


def split(word):
    return list(word)


def no_such_action():
    print('Invalid choice\n')


def print_menu():
    print(
        'Main Menu\n'
        '0: Show menu again\n'
        '1: Python Program to Convert Kilometers to Miles\n'
        '2: Python Program to Check Leap Year\n'
        '3: Python Program to a Decimal number into Bin, Oct and Hex\n'
        '4: Python Program to Find Factorial of Number Using Recursion\n'
        '5: Python Program to hash encrypt a file\n'
        '6: Python Program to convert string to utf8\n'
    )


def test():
    print(factors(16667202255280345128))


def main():
    actions = {
        '0': action0,
        '1': action1,
        '2': action2,
        '3': action3,
        '4': action4,
        '5': action5,
        '6': action6,
        '7': test,
    }
    print_menu()
    while True:
        selection = raw_input("Your Selection: ")
        if "quit" == selection:
            return
        toDo = actions.get(selection, no_such_action)
        toDo()


if __name__ == "__main__":
    main()
