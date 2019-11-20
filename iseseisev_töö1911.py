cars = {
    "car1" : {
     "brand": "Ford",
      "color": "red",
      "year": "2009"
    },
    "car3" : {
      "brand": "Audi",
      "color": "pink",
      "year": "1973"
    },
    "car2" : {
      "brand": "BMW",
      "color": "black",
      "year": "1964"
    }
}

for tag, g in cars.items():
    if g["year"] == "2009":
        print(g["name"])
