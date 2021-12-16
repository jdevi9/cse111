import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
def surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
def storage_efficiency(volume, surface_area):
    return volume / surface_area
def cost_efficiency(volume, cost):
    return volume / cost
def main():    
    with open('canSizes.csv') as can_size_file:
        next(can_size_file)
        for line in can_size_file:
            info = line.split(',')
            name = info[0]
            radius = float(info[1])
            height = float(info[2])
            cost = float(info[3])
            volume = cylinder_volume(radius, height)
            surf_area = surface_area(radius, height)
            storage_eff = round(storage_efficiency(volume, surf_area),2)
            cost_eff = round(cost_efficiency(volume, cost))
            print(f'{name} SE: {storage_eff} CE: {cost_eff}')
#starts execution
main()