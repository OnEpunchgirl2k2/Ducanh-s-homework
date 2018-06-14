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
    for box in boxes:
        if box not in destination:
            return False
        else:
            return True


def gameRule():
    while True:     
        createBox()  
        if isWin():
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

        if 0 <= player['x'] + dx <map["size_x"] \
            and 0 <= player['y'] + dy < map["size_y"]:
           
            new_positionX_player = player["x"] + dx
            new_positionY_player = player["y"] + dy
            lengthBoxes = len(boxes)
            for i in range(lengthBoxes):
                if boxes[i]["x"] == new_positionX_player\
                    and boxes[i]["y"] == new_positionY_player:
                        new_boxes = boxes[:]
                        if boxes[i]["x"] + dx < map["size_x"] \
                            and boxes[i]["y"] + dy < map["size_y"]:
                            new_boxes.remove(boxes[i])
                            for j in range(len(new_boxes)):
                                if new_boxes[j]["x"] != boxes[i]["x"] + dx \
                                    or new_boxes[j]["y"] != boxes[i]["y"] + dy \
                                    and j == (len(new_boxes) - 1):
                                    boxes[i]["x"] += dx
                                    boxes[i]["y"] += dy
                                    player['x'] += dx
                                    player['y'] += dy
                                   
                                    break  
                else:
                    # player don't match position box
                    if i == (lengthBoxes - 1):
                        player["x"] += dx
                        player["y"] += dy  
        if isWin() :
            print("GG")
            break

gameRule()
