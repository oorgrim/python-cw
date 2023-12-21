
import math
def get_volume(height, diameter):
    volume_formula = (math.pi * height * diameter**2) / 4
    return volume_formula
result = get_volume(17, 7)
print(result)