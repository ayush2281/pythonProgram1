# Python Random randint()Method
# Return a number between 6 adn 9(both included)

import random
print(random.randint(6,9))


# Python Random randrange()Method
#return a number between 3(included) and 11 (not included)

print(random.randrange(3,11))


# Python Random choice()Method
#return a random element from a list:

l = ["apple","orrange", "cherry"]

print(random.choice(l))

       # Random is module and also random is function
#RANDOM(): Return a random float number between 0 and 1
# r = random.random()
print(random.random())

# Shuffle(): takes a sequences and return sequences in random order.

s = [90,80,70,60]
random.shuffle(s)
print(s)


#uniform(): return a random float number between two given parameter
# u = random.uniform(3,9)
print(random.uniform(3,9))

