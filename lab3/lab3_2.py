# countries = [
#     {"name": "Ukraine", "population": 44.5, "area": 603.5},
#     {"name": "Uganda", "population": 146.7, "area": 17125},
#     {"name": "USA", "population": 331.9, "area": 9834.4},
# ]

countries = []

# Ask the user for the number of countries
N = int(input("Enter the number of countries: "))
while N == 0:
    N = int(input("Enter the number of countries: "))

# Loop to input data for N countries
for _ in range(N):
    name = input("Enter the name of the country: ")
    population = float(input("Enter the population of the country: "))
    area = float(input("Enter the area of the country: "))

    # Create a dictionary for the country and add it to the list
    country = {"name": name, "population": population, "area": area}
    countries.append(country)


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