class Vehicle:
    # the constructer
    def __init__(self,name, Model, year):
        self.name = name
        self.Model = Model
        self.year = year

     # every methode in the Class should have a self as first Param
    def infos(self):
        print(f"The vehicle: [{self.name}] its Model [{self.Model}], made in [{self.year}]")


V1 = Vehicle('BMW','0040','2009')
print(V1.year)
V1.infos()

