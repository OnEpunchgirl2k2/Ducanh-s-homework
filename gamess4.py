map = {
    "size_x": 5,
    "size_y": 5
}

player ={
    "x": 3,
    "y": 4
}

boxes = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},
]

destination = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3},
]

while True:
    for y in range(map['size_y']):
        for x in range (map["size_x"]):
            player_is_here = False
            box_is_here = False
            dest_is_here = False
            for box in boxes:
                if box["x"] == x and box['y'] == y:
                    box_is_here = True
                if player['x'] == x and player['y'] == y:
                    player_is_here = True
                    break

            for dest in destination:
                if dest['x'] == x and dest['y'] == y:
                    dest_is_here = True
                    break

            if player_is_here is True:
                print("P ", end="")
            elif box_is_here is True:
                print("B ", end="")
            elif dest_is_here is True:
                print("D ", end="")
            else:
                print("- ", end="")
        print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False


    if win:
        print("GG")
        break


    move = input("your move: ").upper()

    dx = 0
    dy = 0


    if move == "W":
        dy =  -1
    elif move == "S":
        dy =  +1
    elif move == "A":
        dx =  -1
    elif move == "D":
        dx =  +1
    else:
        print("ezzzzz")
        break

    if 0 <= player['x'] + dx <map["size_x"] \
       and 0 <= player['y'] + dy < map["size_y"]:
       player['x'] += dx
       player['y'] += dy

    for box in boxes:
        if box["x"] == player["x"] \
            and box['y'] == player['y']:
            box["x"] += dx
            box['y'] += dy
            break

    win = True
    for box in boxes:
        if box not in destination:
            win = False
