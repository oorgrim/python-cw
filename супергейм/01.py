class Kettle:
    material = 'steel'
    color = 'red'
    volume = 2.4
    water = 0

    def fill(self, liters):
        self.water += liters

my_kettle = Kettle()
print(my_kettle.water)
my_kettle.fill(2)
print(my_kettle.water)
# print(my_kettle)