from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Zwraca stosowany przez pygal dwuznakowy kod państwa'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Jeżeli panstwo nie zostało znalezione, wartością zwrotną będzie None
    return None

print(get_country_code('Andorra'))