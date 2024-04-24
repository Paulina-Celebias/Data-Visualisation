import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code

# Wczytani =e danych i umieszczenie ich na liście
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# Utworzenie słownika danych dotyczących populacji
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2000':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            
# Podzielenie państw na trzy grupy wg liczby ludności
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
        
# Wyświetlenie liczby państw w kazdej z tzech grup
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle)
wm = World(style = wm_style) 
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 roku'
wm.add('0 - 10mln', cc_pops_1)
wm.add('10mln - 1mld', cc_pops_2)
wm.add('> 1mld', cc_pops_3)

wm.render_to_file('world_population_light.svg')