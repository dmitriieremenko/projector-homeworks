class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        self.name = self.name + other.name
        self.population = self.population + other.population
        return self


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
