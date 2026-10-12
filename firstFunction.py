# def mysum():
#     a = 10
#     b = 20
#     sum = a+b
#     print(sum)
# mysum()

# def mysum(a,b):
#     print("inside mysun() function")
#     sum = a+b
#     print(sum)

# a = int(input("enter a value : "))
# b = int(input("enter b valuse : "))

# mysum(a,b)
# print("after mysum() function ")
# mysum(a)


# def mysum(a,b=1000):
#     print("inside mysun() function")
#     sum = a+b
#     print(sum)

# a = int(input("enter a value : "))
# b = int(input("enter b valuse : "))

# mysum(a,b)
# print("after mysum() function ")
# mysum(a)

# def mysum(a,c,b=1000,):
#     print("inside mysun() function")
#     sum = a+b+c
#     print("the sum is " , sum)

# def foo():
#     print("foo")

# a = int(input("enter a value : "))
# b = int(input("enter b valuse : "))

# print("after mysum() function ")
# # mysum(a)
# foo()
# mysum(a,b)
# c = 10
# mysum(a,b,c)


# def calculate_total(price , quantity):
#     print("Item price", price)
#     print("Item quantity", quantity)
# calculate_total(150, 2)




# def mysum(a,b=1000,):
#     sum = a+b               //this variable is available for only this function outside it will not work 
#     # return sum
#     print("the sum is", sum)

# a = int(input("enter a value : "))
# b = int(input("enter b valuse : "))
# returnedsum = mysum(a,b)
# print(returnedsum)
# print("the sum is", sum)    // sum can not acces because of sum variable is available only inside of the function 


# +++++++++++++= local global variable ++++++++++++++++++
'''
global variabel that is defined is global scope , that is not  withina particlar function 
are available access the file

Local variable that is defined in local scope, within that function only 
it cannot be acessed outside on the function
'''


def book_policy_update():
    days = int(input("Enter the days how many days read books : "))
    book_name = input("Enter the your book name that you read : ")
    premium_member = input("Do you have premium membership? (yes/no): ").lower()

    if days >5 and book_name == "standard"and premium_member == "no":
        total = ((days-5)*10) + (5*5)
        return total 
    elif days >0 and book_name == "refrence" and premium_member == "no":
        return days*20
    elif days >5 and book_name == "standard" and premium_member == "yes":
        total = ((days-5)*10) + (5*5) 
        return total - (20 / 100 * total)
    elif days >0 and book_name == "refrence" and premium_member == "yes":
        return (days * 20) - (20 / 100 * (days*20))
    elif days <= 5 and book_name == "standard" and premium_member == "no":
        return days *5 
    elif days <= 5 and book_name == "standard" and premium_member == "yes":
        return (days*5)-((20/100)*(days*5))

print(book_policy_update())
    
