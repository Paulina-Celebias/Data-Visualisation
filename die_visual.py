import pygal
from die import Die

# Utworzenie kości typu 6D
die = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []

for roll_num in range(1000):
    
    result = die.roll()
    results.append(result)
    
# Analiza wyników
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzucenia pojedynczą kością D6 1000 razy'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
   
print(frequencies)