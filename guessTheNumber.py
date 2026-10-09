'''
Computer to generate a number between 1-5
you have to ask the user to guess the computer number 

if the user guessed 
if correctly then print "you win, congrate!"

if the use gess ti wrong 
you print "wrong guess, attempt again"

user will input again 
like this they contineu

they will have a total of 3 attempts
 if they reahch 3 attempt then pring "attempt over , good luck next time"!
# '''
i = 0
while i < 3:
    import random 
    computer_number = random.randint(1,5)

    random_number = int(input("Enter your number : "))
    if computer_number == random_number:
        print("You win, Congras!")
        i+=1
    else:
        print("Wrong gess, Attempt again!")
        i+=1
print("3 Attempt over , Go look for the next time") 

# +++++++++ some only the valid marks +++++++++++++++++
marks = [2,3,4,-7,6,7,-9,7,-3]
toalstudent = 0
count = 0
for mark in marks:
    if mark < 0:
        toalstudent += 1
        continue
    toalstudent += 1
    count+=1
print("Pass student", count)
print("total student", toalstudent)

# +++++++++++++ looking for the friend's name with break +++++++++++
names = ["shraddha", "supriya", "satya", "avantika", "mohan"]
for name in names:
    if name == "satya":
        print("found the satya")
        break
    print(name)
