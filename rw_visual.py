import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Tworzenie nowego bładzenia losowego, dopóki program pozostaje aktywny
while True:

    # Przygotowanie danych bładzenia losoego i wyświetlanie punktów
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Określenie wielkości okna wykresu
    plt.figure(dpi = 128, figsize = (10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)
    
    # Podkreślenie pierwszego i ostatniego punktu bładzenia losowego
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
    
    # Ukrycie osi
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input('Czy utworzyć kolejne bładzenie losowe? (t/n): ')
    if keep_running == 'n':
        break