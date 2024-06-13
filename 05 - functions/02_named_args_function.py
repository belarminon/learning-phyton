def add(mark, model, year, plate):
    print(f"The car {mark}/{model}/{year}/{plate} was added successful")

add("Chebrolet","Tracker",2024,"ABC1D234")
add(mark="Chebrolet",model="Tracker",year=2024,plate="ABC1D234")
add(**{"mark":"Chebrolet","model":"Tracker","year":2024,"plate":"ABC1D234"})