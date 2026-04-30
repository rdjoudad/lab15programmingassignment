"""
Visualizing Data 
Ryma Djoudad
Make a graph representing a math formula using matplotlib
No starter code
4/29/2026
"""

import matplotlib.pyplot as plt 

input = [1, 2, 3, 4, 5]
output = [1, 8, 27, 64, 125]

my_fig, my_plot = plt.subplots()

my_plot.plot(input, output, linewidth=2)
my_plot.set_title("First 5 Cubes", fontsize=30)
my_plot.set_xlabel("Value", fontsize=20)
my_plot.set_ylabel("Cube of Value", fontsize=20)

plt.show()



