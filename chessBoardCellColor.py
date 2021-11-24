#chessBoardCellColor
#CodeSignal task 29 
#Given two cells on the standard chess board, determine whether they have the same color or not.

def solution(cell1, cell2):
    if get_color(cell1) == get_color(cell2):
        return True
    return False
    
def get_color(cell):
    #split coordinates
    letter = cell[0]
    num = cell[1]
    
    # convert letter to it's numeric type
    letter = ord(letter)
    
    #fail safe conversion to integer
    letter = int(letter)
    num = int(num)
    
    #if cell is even:odd or odd:even it is black, else it is white 
    if letter % 2 == 0 and num % 2 !=0:
        return 'Black'
    elif letter % 2 != 0 and num % 2 ==0: 
        return 'Black'
        
    else:
        return 'White'
