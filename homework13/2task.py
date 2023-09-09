class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def __add__(self, other):
        name_add = self.name + other.name
        population_add = self.population + other.population
        return Country(name_add, population_add)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
