import matplotlib.pyplot as plt
import random as rd
'''generate random numbers and represent it
'''

squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_squares = rd.choices(squares, k = 9)
plt.plot(random_squares, linewidth=3)

plt.title('Random  Squares Numbers')
plt.show()
