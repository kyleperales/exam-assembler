#<- start with this for comments

#variables
#greet = "Hello"
#print(greet)

#computation
#print (10 * 10)
#print(1 + 1)

#inputs
#print("Please provide a name")
#name = input()
#print("Please provide your age")
#age = int(input())
#print("Welcome {0}, aged {1}".format(name, age))


# for loops
#for i in range(0, 20):
#    print("i is now {0}".format(i))

#arrays
#arr = [1,2,3,4,5,6]
#print(arr[-1])

#arr = [1, "hello", 2]
#print(arr[1])


#if conditions
import random

number = random.randint(1,10)
tries = 1

print("I'm thinking of a number between 1 and 10")
guess = int(input("Have a guess: "))
if guess > number:
    print("Guess lower...")
if guess < number:
    print("Guess higher...")
