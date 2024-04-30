tile_width_metre = 0
tile_length_metre = 0
per_tile_cost = 0

floor_area_metresq = 0

# while loop is repeated 4 times so that user does not need to go all the way back to the top in the event of mistype

# floor area
while True:
    try:
        floor_area_metresq = int(input("Please enter your floor area (in square metres): "))
    except ValueError:
        print("Please only enter digits.")
    else:
        break

# tile length
while True:
    try:
        tile_length_metre = int(input("Please enter your tile's length (in cm): "))/100
    except ValueError:
        print("Please only enter digits.")
    else:
        break

# tile width
while True:
    try:
        tile_width_metre = int(input("Please enter your tile's width (in cm): "))/100
    except ValueError:
        print("Please only enter digits.")
    else:
        break

# tile cost
while True:
    try:
        per_tile_cost = int(input("How much do your tiles cost per tile?: "))
    except ValueError:
        print("Please only enter digits.")
    else:
        break

# get tile area
tile_area = tile_length_metre * tile_width_metre

# calculate tiles needed
tiles_needed = floor_area_metresq/tile_area

# get tile cost
final_cost = tiles_needed * per_tile_cost


print(f"For your floor area of {floor_area_metresq} sqaure metres, you will need roughly {round(tiles_needed)} of {tile_width_metre * 100}cm X {tile_length_metre * 100}cm tiles for a total estimated cost of ${round(final_cost, 2)} at ${per_tile_cost} per tile.")


        

