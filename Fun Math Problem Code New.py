"This is only for polynomials. I can't figure out how to make python input other complex equations without writing separate code for each family of functions. "
"You would have a scrolling thing on the side in GUI"



print("Indicate function type: 1. Polynomial, 2. Exponential")
function_type = int(input("INPUT FUNCTION TYPE: "))
if function_type == 1:
    function_type = "polynomial"
elif function_type == 2:
    function_type = "exponential"

#print(function_type)

# Function types: code specific to different types of functions; function value generator and and function string displayer
# Note: for functions that are a sum of the basic functions below, function value can be found by adding the function value of each basic function separately

# POLYNOMIAL FUNCTION:

# Inputs:
if function_type == "polynomial":
    print("Polynomials of the form (a0)x^n + (a1)x^n-1 + (a2)x^n-2 + (a3)x^n-3")
    degree = int(input("INPUT DEGREE OF POLYNOMIAL: "))
    coefficient_list = []
    for k in range(degree+1):
        kth_coefficient = input("INPUT COEFFICIENT %s : "%(k))
        coefficient_list.append(kth_coefficient)

# Python functions evaluating function value and displayer string:
    def function_polynomial_value(x):
        polynomial_value = 0
        term_value = 0
        for k in range(degree+1):
            term_value = int((coefficient_list[k]))*(x**(degree-k))
            polynomial_value += term_value
            #function_value += int((coefficient_list[k]))*(x**(degree-k))
        return polynomial_value

        
    def function_polynomial_string_displayer():
        polynomial_string = ""
        for k in range(degree+1):
            term_string = ("(%s)x^%s + "%(coefficient_list[k], (degree-k)))
            polynomial_string += term_string
        return polynomial_string


# EXPONENTIAL FUNCTION:

# Input: 
elif function_type == "exponential":
    print("Exponential of the form a^(kx)")
    base = int(input("INPUT BASE: "))
    k = int(input("INPUT EXPONENT COEFFICIENT: "))

# Python functions evaluating function value and displayer string:
    def function_exponential_value(x):
        y = float((k*x))
        number = float(base**y)
        return(number)
    def function_exponential_string_displayer():
        return("Given Equation: %s^(%sx)"%(base,k))

# Assigning these specific function values and displayer strings to general common variables to be used in subsequent root approximations
# (Because only the function value and string displayer are specific to the function. The subsequent algorithms for root evaluations only care about 
# function values).

if function_type == "polynomial":
    function_value = function_polynomial_value
    function_string = function_polynomial_string_displayer
elif function_type == "exponential":
    function_value = function_exponential_value
    function_string = function_exponential_string_displayer
print(function_value)

print("Function inputed: %s"%(function_string()))

function_value_needed = int(input("INPUT VALUE OF f(c): "))

def modified_function_value(x):  #The algorithm will try to find zeroes of this function and hence the root returned will be the argument of function_value_needed
    return (function_value(x) - function_value_needed)

print("Max error in c is max deviation from the true value")
max_error = float(input("INPUT MAX ERROR TOLERATED: "))

print("Make an educated guess of where the you may find your a0 and b0, where (f(a0))(f(bo))<0")
guessed_random_interval_lower_bound = int(input("INPUT GUESSED INTERVAL LOWER BOUND: "))
guessed_random_interval_upper_bound = int(input("INPUT GUESSED INTERVAL UPPER BOUND: "))

a = "not a number"
b = "not a number"
num_iterations_random_ab = 0
import random
while True:
    num_iterations_random_ab += 1
    random_x = int(random.randint(guessed_random_interval_lower_bound,guessed_random_interval_upper_bound))
    print(random_x)
    if a != "not a number" and b != "not a number":
            break
    else:    
        if modified_function_value(random_x) == 0:
                    print("Yay!! You found the root = %s"%(random_x))
                    break
        elif modified_function_value(random_x) < 0:
            a = int(random_x)
            while True:
                    random_x = int(random.randint(guessed_random_interval_lower_bound,guessed_random_interval_upper_bound))
                    if modified_function_value(random_x) > 0:
                        b = int(random_x)
                        break
        elif modified_function_value(random_x) > 0:
            b = int(random_x)
            while True:
                    random_x = int(random.randint(guessed_random_interval_lower_bound,guessed_random_interval_upper_bound))
                    if modified_function_value(random_x) < 0:
                        a = int(random_x)
                        break
        break


print ("a0 = %s and b0 = %s"%(a,b))    
print (("Number of iterations to get ao and bo = %s")%(num_iterations_random_ab))


c = float((a+b)/2) #First midpoint

#The midpoint of the ever shrinking intervals can be also be thought of as the approximate value of the root
first_root_approximation = c
error = abs(a-c) #It could very well have been abs(b-c) since c is equidistant from both a and b

print("First root/c approximation is %s within a maximum error of %s"%(first_root_approximation, error))
#print("First error: %s"%(error))


# Next, f(x) is evaluated at the changing c's.

print("")

iterations = 0
while error > max_error:
    if function_value(c) == 0:
        print("Yay!! You found the root = %s"%(c))
        break
    elif modified_function_value(c) > 0 and modified_function_value(c) < modified_function_value(b):
        b = c
        error = float(abs(c - a))
        c = (a + b)/2

    elif modified_function_value(c) < 0 and modified_function_value(c) > modified_function_value(a):
        a = c
        error = float(abs(c - b))
        c = float((a + b)/2)
    iterations += 1
    print("Iteration %s, a = %s, b = %s, maximum error = %s"%(iterations, a, b, error))

root_approximation = c
error = error
print("")
print("The root/c approximation is %s within a maximum error of %s"%(c, error))
print("Number of iterations to get to the root approximation: %s"%(iterations))

print("\nHit enter any key to exit program")
end_statement = input("")
        

