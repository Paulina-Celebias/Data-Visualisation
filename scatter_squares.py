import matplotlib.pyplot as plt

# plt.scatter(2, 4, s = 200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

# Kolor z gradientem
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 20)

# Kolor zwykły
# plt.scatter(x_values, y_values, c = 'red', edgecolor = 'none', s = 20)

# Zdefiniowanie tytułu wykresu i etykiet osi
plt.title('Square values', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Squares', fontsize = 14)

# Zdefiniowanie wielkości etykiet
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.axis([0, 1100, 0, 1100000])

plt.show()

# Zapis wykresu i usunięcie białych znaków wokół niego 
plt.savefig('Squares_plot.png', bbox_inches = 'tight')