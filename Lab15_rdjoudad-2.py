"""
Visualizing Data 
Ryma Djoudad
Make a graph representing a math formula using matplotlib
No starter code (Inspired by textbook)
4/29/2026
"""

import matplotlib.pyplot as plt 

# Part 1: First 5 Cubes

input = [1, 2, 3, 4, 5]
output = [1, 8, 27, 64, 125]

my_fig, my_plot = plt.subplots()

my_plot.plot(input, output, linewidth=2, color='red')
my_plot.set_title("First 5 Cubes", fontsize=30)
my_plot.set_xlabel("Value", fontsize=20)
my_plot.set_ylabel("Cube of Value", fontsize=20)

my_fig.savefig('cubes_5.png')
plt.show()

# Part 2: First 5000 Cubes

input = range(1, 5001)
output = [x**3 for x in input]

second_fig, second_plot = plt.subplots()

second_plot.plot(input, output, linewidth=2, color='green')
second_plot.set_title("First 5000 Cubes", fontsize=20)
second_plot.set_xlabel("Value", fontsize=20)
second_plot.set_ylabel("Cube of Value", fontsize=20)

second_fig.savefig('first_5000_cubes.png')
plt.show()

