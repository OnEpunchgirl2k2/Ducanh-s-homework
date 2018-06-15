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

wall = [
    {"x": 5, "y": 1},
]


def createBox():
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

def isWin():
    win = True
    for box in boxes:
        if box not in destination:
            win = False
    return win

def resolvePlayerMove(dx, dy):
    if 0 <= player['x'] + dx <map["size_x"] \
        and 0 <= player['y'] + dy < map["size_y"]:
        
        new_positionX_player = player["x"] + dx
        new_positionY_player = player["y"] + dy
        lengthBoxes = len(boxes)
        i = 0
        for box in boxes:
            i += 1
            vitural_boxes = boxes[:]
            if box["x"] == new_positionX_player \
                and box["y"] == new_positionY_player:
                new_positionX_box = box["x"] + dx
                new_positionY_box = box["y"] + dy
                if 0 <= new_positionX_box < map["size_x"] \
                    and 0 <= new_positionY_box < map["size_y"]:
                    vitural_boxes.remove(box)
                    lengthVituralBoxes = len(vitural_boxes)
                    j = 0
                    for vitural_box in vitural_boxes:
                        j += 1
                        if vitural_box["x"] == new_positionX_box \
                            and vitural_box['y'] == new_positionY_box:
                            print("duplicate position box")
                        else:
                            # box can move, player can move
                            if j == lengthVituralBoxes:
                                print("box can move, player can move")
                                box["x"] += dx
                                box["y"] += dy
                                player["x"] = new_positionX_player
                                player["y"] = new_positionY_player
                                
                else:
                    # player can't push box outside the wall
                    break
            else:
                # player don't match any position box
                if i == (lengthBoxes):
                    print("player don't match any position box")
                    player["x"] = new_positionX_player
                    player["y"] = new_positionY_player
                


def gameRule():
    while True:     
        createBox()  
        win = isWin()
        if win:
            print("GG")
            break
        move = input("your move: ").upper()
        playerCanMove = True
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

        resolvePlayerMove(dx, dy)
          
        win = isWin()
        if win:
            print("GG")
            break

gameRule()
