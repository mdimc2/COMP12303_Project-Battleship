

# Board Initialisation
boardP1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

boardP2 = boardP1

# Dictionary Definitions
lengthDict = {'R':5, 'B':4, 'C':3, 'S':3, 'D':2}

sClassDict = {'R':'Carrier',
              'B':'Battleship',
              'C':'Cruiser',
              'S':'Submarine',
              'D':'Destroyer'}

# Function Definitions

#   Phase 1: Placing ships onto board.

def placeShip(boardP0,x0,y0,dir,ID):
    if dir == "V":
        for i1 in range(int(lengthDict[ID])):
            boardP0[int(x0)+int(i1)-1][int(y0)-1] = lengthDict[ID]
    if dir == "H":
        for i2 in range(int(lengthDict[ID])):
            boardP0[int(x0)-1][int(y0)+int(i2)-1] = lengthDict[ID]


def placeShipSequence(boardP0):
    for st in ['R','B','C','S','D']:
        placeShip(boardP0,
                  input('Input top leftmost vertical coordinate of your '+sClassDict[st]+': '),
                  input('Input top leftmost horizontal coordinate of your '+sClassDict[st]+': '),
                  input('Input direction of ship, "V" for vertical, "H" for Horizontal: '),
                  st)

#   Phase 2: Hit events.

def hitEvent(boardP0,x0,y0):
    cell = boardP0[x0][y0]
    if cell==9:
        hitStatus = 2
    if cell==2:
        print("Good hit on enemy Destroyer.")
        hitStatus = 1
    if cell==3:
        print("Good hit on enemy Cruiser or Destroyer.")
        hitStatus = 1
    if cell==4:
        print("Good hit on enemy Battleship.")
        hitStatus = 1
    if cell==5:
        print("Good hit on enemy Carrier.")
        hitStatus = 1
    else:
        print("Miss.")
        hitStatus = 0
    cell = 9
    return hitStatus


def hitPrompt():
    x = input('Insert firing X coordinates: ')
    y = input('Insert firing Y coordinates: ')
    return x,y


def hitSequence(BoardP0):
    (x,y)=hitPrompt()
    hitStatus = hitEvent(BoardP0,x,y)
    while hitStatus == 2:
        print("You have already hit this cell.")
        (x, y) = hitPrompt()
        hitStatus = hitEvent(BoardP0, x, y)
    while hitStatus == 1:
        (x, y) = hitPrompt()
        hitStatus = hitEvent(BoardP0, x, y)
    if hitStatus == 0:
        print("We have lost our tactical turn. Brace for enemy fire!")


def checkBoard(boardP0):
    if boardP0.count(2,3,4,5) == 0:
        boardStatus = "LL"
    else:
        boardStatus = 'OK'
    return boardStatus


def turnSequence(boardP0):
    print("Our turn has begun. Take aim.")
    hitSequence(boardP0)
    boardStatus = checkBoard(boardP0)
    return boardStatus


# Script Elements

placeShipSequence(boardP1)

if __name__ == '__main__':
    for element in boardP1:
        print(element)
