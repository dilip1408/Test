import random
# random.choice returns int and random.choices returns list for whatever the input.
from builtins import enumerate

list1 =[1,2,3,4,5,6,7]
print(type(list1))
r = random.choice(list1)
print(type(r))
print(r)

random.shuffle(list1)
print(list1)
random.shuffle(list1)
print(list1)
random.shuffle(list1)
print(list1)

print(list1)



# print("X is {}".format(x))
# print("Y is {}".format(y))
# print("Z is {}".format(z))

#Split a string
string = "Dil.ip Voruganti"
s = string.split(".")
print(s)

##to get name of caller or obj.
class Test:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Name is {}".format(self.name)

obj = Test('obj')
print(obj)

obj1 = Test('obj1')
print(obj1)
# Tried to get the no. of occurrences in the list for a word
words = ['Dilip','Python','developer','Dilip']
print(type(words))
#[] - is a list comprehension, () - is a generator comprehension. {} - set comprehension, {} - Dict comprehension(same as set comprehension but ":" will be added)
count_of_each_word = {i for i in enumerate(words,start=1)} #Even this is set, duplicate in words will be removed as it adds the start counter and becomes as unique.
print(count_of_each_word)
print(type(count_of_each_word))

# for i in count_of_each_word:
#     print(i)
#     print(type(i))

# words = ['Dilip','Python','developer','Dilip']