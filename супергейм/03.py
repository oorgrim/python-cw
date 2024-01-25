class Kettle:
    material = 'steel'
    color = 'red'
    volume = 2.4
    water = 0

    def fill(self, liters):
        self.water += liters

my_kettle1 = Kettle()
my_kettle2 = Kettle()
print(my_kettle1.water, my_kettle2.water)
my_kettle1.fill(2)
print(my_kettle1.water)
# print(my_kettle)