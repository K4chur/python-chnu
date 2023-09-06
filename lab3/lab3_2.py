countries = [
    {"name": "Ukraine", "population": 44.5, "area": 603.5},
    {"name": "Uganda", "population": 146.7, "area": 17125},
    {"name": "USA", "population": 331.9, "area": 9834.4},
]

def calculate_density(country):
    population = country["population"]
    area = country["area"]
    density = population / area
    return density

min_density = float('inf')
country_name = ""

for country in countries:
    density = calculate_density(country)
    if density < min_density:
        min_density = density
        country_name = country["name"]

print(f"The country with the minimum population density is: {country_name}")