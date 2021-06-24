"""What are lambda functions in Python?
In Python, an anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions."""

double = lambda x:x * 2

print(double(5))

"""Use of Lambda Function in python
We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function 
that takes in other functions as arguments). 

Lambda functions are used along with built-in functions like filter(), map() etc."""

#FILTER()
"""Example use with filter()
The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains 
items for which the function evaluates to True.

Here is an example use of filter() function to filter out only even numbers from a list."""

#Program to filter out only

my_list = [1,2,5,8,5,34,5,22,90]

new_list = list(filter(lambda x:( x % 2 == 0), my_list))
print("Original",my_list)
print("Filter(Even Numbers)",new_list)

#MAP()
"""Example use with map()
The map() function in Python takes in a function and a list.

The function is called with all the items in the list and a new list is returned 
which contains items returned by that function for each item.

Here is an example use of map() function to double all the items in a list."""

my_list = [1,2,5,8,5,34,5,22,90]

new_list = list(map((lambda x: x*2),my_list))
print("Original",my_list)
print("Doubled by map()",new_list)
