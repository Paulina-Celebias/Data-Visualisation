from random import choice

class RandomWalk():
    '''Klasa przeznaczona do wygenerowania bładzenia losowego'''
    
    def __init__(self, num_points = 5000):
        '''Inicjalizacja atrybutów bładzenia'''
        self.num_points = num_points
        
        # Punkt początkowy ma współrzędne (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        '''Wygenerowanie wszytskich punktów dla bładzenia losowego'''
        
        # Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów
        while len(self.x_values) < self.num_points:
            # Ustalenie kierunku oraz odległości do pokonania nw tym kierunku
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Odrzucenie ruchów, które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue
            
            # Ustalenie następnych wartości x i y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)