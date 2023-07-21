import math

# 1. Function definitions

# define a function called rectangle_area with one required parameter (width) and 
# one optional parameter (height). This function should compute and return the area
# of a rectangle with the given width and height. If height is not provided, the 
# function should assume that both width and height are equal and compute the area
# accordingly. Make sure to include a docstring describing this function in your
# definition below.

def rectangle_area(width, height=None):
    """Compute and return the area of a rectangle with the given height and width"""

    if height == None:
        height = width
        
    return height * width

# 2. lambda definitions

# Alter the statement below to assign a function value to circle_area using a 
# lambda expression. The function you create should have one parameter (the
# radius of a circle) and should compute and return the circle's area. Your
# function must be correct to 5 decimal places to pass the tests. 

circle_area = lambda radius: math.pi * math.pow(radius, 2) # TODO: replace None with your lambda


# 3. Collections / Comprehensions
# part 1: use a comprehension to create a list of the first 10 perfect squares 
# (starting with 1). Then convert this list to a tuple and assign it to 
# the variable perfect_squares below. 

perfect_squares = tuple([x*x for x in range(1,11)]) # TODO: replace None with your tuple

# part 2: Now convert the tuple in to a set. Use set operations to exclude
# any numbers that fall within the set 'exclusions' below and assign the 
# resulting set to the variable squares_set below. 

exclusions = set(range(5,50))
#squares_set = set(perfect_squares) - exclusions # TODO: replace None with your set
squares_set = set(perfect_squares) & exclusions # TODO: replace None with your set

# 4. generators
# Write a generator function called 'gen_squares' that generates perfect squares.
# Rather than starting with the first perfect square, generate the i-th perfect 
# square, one at a time, where start <= i < stop. 
def gen_squares(start, stop):
    """Generator that returns perfect squares from start to stop"""
    for i in range(start, stop):
        yield i*i  # TODO: replace with function body for generator 
        

def main():
    print(f'Area of rectangle with sides 3 and 4: {rectangle_area(3,4)}')
    print(f'Area of rectangle with sides 3 and 3: {rectangle_area(3)}')
    print(f'Area of circle with radius 3: {circle_area(3)}')
    print(f'10 perfect squares: {perfect_squares}')
    print(f'10 perfect squares with exclusions: {perfect_squares}')
    print(f'Perfect squares in range 50 - 100: {[x for x in gen_squares(50,100)]}')

if __name__ == "__main__":
    main()