# greeting = "hello"
# #print(greeting)

# greeting = 10
# #print(greeting)
# a = "apple"
# a_b = "pie"
# print(a + " " + a_b)

#name = input("what is your name?")
#print(name + "hello ")

# greeting = "Hello! so nice to see you,%s! "
# result = greeting%name
# print(result)


#.format()
# greeting2 = "Hello! So so great that {} is here"

# formattedString = "Big big person is: {}".format(name)

# print(formattedString)

# greeting3 = f"Hellooooo {name}"
# print(greeting3)
import random
import time

while True:   
    list = ["wonderful","plesant","smart","handsome","skilled"]
    randomitem = random.choice(list)

    name = input("What is your name?")

    complement  = f"{name}, you are so {randomitem}"
    print(complement)
    time.sleep(1)
