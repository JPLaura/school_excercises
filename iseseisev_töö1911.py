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

x = cars.get("car1", {}).get("brand")
print(x)