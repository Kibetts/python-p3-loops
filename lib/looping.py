#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0):
        if i == 1:
            print("Happy New Year!")
    print(i)
   
happy_new_year()

def square_integers(int_list):
    for item  in int_list:
        return item * item

    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
