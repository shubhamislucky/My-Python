# Let's write a code on list comprehensions

"""
    You are given three integers X,Y,Z representing the dimensions of a cuboid
    along with an integer N. You have to print a list of all possible
    coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not
    equal to N.
"""

x = int(input("Enter the coordinate i : "))
y = int(input("Enter the coordinate j : "))
z = int(input("Enter the coordinate k : "))
n = int(input("Enter the number n : "))

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) != n)])
