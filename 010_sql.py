import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("""SELECT population.city, population.population, 
        regions.region FROM population, regions
        WHERE population.city = regions.city;""")

    rows = c.fetchall()

    for r in rows:
        print(f"City: {r[0]}")
        print(f"Population: {r[1]}")
        print(f"Regions: {r[2]}\n")








