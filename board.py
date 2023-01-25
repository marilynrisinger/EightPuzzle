#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# Marilyn Risinger


GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    
    
    
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)
       
        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
       
        rest = []
        for i in range(3):
            for l in range(3):
                self.tiles[i][l]=digitstr[3*i+l]
                if self.tiles[i][l]=='0':
                    self.blank_r=i
                    self.blank_c=l

    
    
   
    
    def __repr__(self):
        """ returns a string representation of a Board object"""
        rest = ""
        for i in range(3):
            for l in range(3):
                if self.tiles[i][l]!='0':
                    rest+=self.tiles[i][l] + " "
                else:
                    rest+= "_" + " "
            rest+="\n"
        return rest
    
    
    
    def move_blank(self, direction):
        """akes as input a string direction that specifies the direction in w
        hich the blank should move, and that attempts to modify the contents 
        of the called Board object accordingly"""
        if direction == 'up' and self.tiles[1][0] == '0':
            self.tiles[1][0]=self.tiles[0][0]
            self.tiles[0][0]='0'
            self.blank_r=0
            return True
        elif self.tiles[1][1]=='0' and direction == 'up':
            self.tiles[1][1]=self.tiles[0][1]
            self.tiles[0][1]='0'
            self.blank_r=0
            return True
        elif self.tiles[1][2]=='0' and direction == 'up':
            self.tiles[1][2]=self.tiles[0][2]
            self.tiles[0][2]='0'
            self.blank_r=0
            return True
        elif self.tiles[2][0]=='0' and  direction == 'up':
            self.tiles[2][0]=self.tiles[1][0]
            self.tiles[1][0]='0'
            self.blank_r=1
            return True
        elif self.tiles[2][1]=='0' and  direction == 'up':
            self.tiles[2][1]=self.tiles[1][1]
            self.tiles[1][1]='0'
            self.blank_r=1
            return True
        elif self.tiles[2][2]=='0' and  direction == 'up':
            self.tiles[2][2]=self.tiles[1][2]
            self.tiles[1][2]='0'
            self.blank_r=1
            return True
        elif self.tiles[0][0]=='0' and direction == 'down':
            self.tiles[0][0]=self.tiles[1][0]
            self.tiles[1][0]='0'
            self.blank_r=1
            return True
        elif self.tiles[0][1]=='0' and direction == 'down':
            self.tiles[0][1]=self.tiles[1][1]
            self.tiles[1][1]='0'
            self.blank_r=1
            return True
        elif self.tiles[0][2]=='0' and direction == 'down':
            self.tiles[0][2]=self.tiles[1][2]
            self.tiles[1][2]='0'
            self.blank_r=1
            return True
        elif self.tiles[1][0]=='0' and direction == 'down':
            self.tiles[1][0]=self.tiles[2][0]
            self.tiles[2][0]='0'
            self.blank_r=2
            return True
        elif self.tiles[1][1]=='0' and direction == 'down':
            self.tiles[1][1]=self.tiles[2][1]
            self.tiles[2][1]='0'
            self.blank_r=2
            return True
        elif self.tiles[1][2]=='0' and direction == 'down':
            self.tiles[1][2]=self.tiles[2][2]
            self.tiles[2][2]='0'
            self.blank_r=2
            return True
        elif self.tiles[0][0]=='0' and direction == 'right':
            self.tiles[0][0]=self.tiles[0][1]
            self.tiles[0][1]='0'
            self.blank_c=1
            return True
        elif self.tiles[0][1]=='0' and direction == 'right':
            self.tiles[0][1]=self.tiles[0][2]
            self.tiles[0][2]='0'
            self.blank_c=2
            return True
        elif self.tiles[1][0]=='0' and direction == 'right':
            self.tiles[1][0]=self.tiles[1][1]
            self.tiles[1][1]='0'
            self.blank_c=1
            return True
        elif self.tiles[1][1]=='0' and direction == 'right':
            self.tiles[1][1]=self.tiles[1][2]
            self.tiles[1][2]='0'
            self.blank_c=2
            return True
        elif self.tiles[2][0]=='0' and direction == 'right':
            self.tiles[2][0]=self.tiles[2][1]
            self.tiles[2][1]='0'
            self.blank_c=1
            return True
        elif self.tiles[2][1]=='0' and direction == 'right':
            self.tiles[2][1]=self.tiles[2][2]
            self.tiles[2][2]='0'
            self.blank_c=2
            return True
        elif self.tiles[0][1]=='0' and direction == 'left':
            self.tiles[0][1]=self.tiles[0][0]
            self.tiles[0][0]='0'
            self.blank_c=0
            return True
        elif self.tiles[0][2]=='0' and direction == 'left':
            self.tiles[0][2]=self.tiles[0][1]
            self.tiles[0][1]='0'
            self.blank_c=1
            return True
        elif self.tiles[1][1]=='0' and direction == 'left':
            self.tiles[1][1]=self.tiles[1][0]
            self.tiles[1][0]='0'
            self.blank_c=0
            return True
        elif self.tiles[1][2]=='0' and direction == 'left':
            self.tiles[1][2]=self.tiles[1][1]
            self.tiles[1][1]='0'
            self.blank_c=1
            return True
        elif self.tiles[2][1]=='0' and direction == 'left':
            self.tiles[2][1]=self.tiles[2][0]
            self.tiles[2][0]='0'
            self.blank_c=0
            return True
        elif self.tiles[2][2]=='0' and direction == 'left':
            self.tiles[2][2]=self.tiles[2][1]
            self.tiles[2][1]='0'
            self.blank_c=1
            return True
        else:
            return False
                
        
        
    
        
    def digit_string(self):
        """creates and returns a string of digits that corresponds to the current 
        contents of the called Board object’s tiles attribute"""
        final = self.tiles[0][0] + self.tiles[0][1] + self.tiles[0][2] + self.tiles[1][0] + self.tiles[1][1] + self.tiles[1][2] + self.tiles[2][0] + self.tiles[2][1] + self.tiles[2][2]
        return final
             
    
    
    
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of 
        the called object (i.e., of the object represented by self)"""
        new=''
        for r in range(3):
            for c in range(3):
             new+=str(self.tiles[r][c])
        new_ = Board(new)
        return new_
               
    
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state. You should not 
        include the blank cell in this count, even if it’s not where it should 
        be in the goal state"""
        count = 0 
        for i in range(3):
            for r in range(3):
                if self.tiles[i][r]==self.tiles[0][1] and self.tiles[0][1]!='1':
                    count+=1
                elif self.tiles[i][r]==self.tiles[0][2] and self.tiles[0][2]!='2':
                    count+=1
                elif self.tiles[i][r]==self.tiles[1][0] and self.tiles[1][0]!='3':
                    count+=1
                elif self.tiles[i][r]==self.tiles[1][1] and self.tiles[1][1]!='4':
                    count+=1
                elif self.tiles[i][r]==self.tiles[1][2] and self.tiles[1][2]!='5':
                    count+=1
                elif self.tiles[i][r]==self.tiles[2][0] and self.tiles[2][0]!='6':
                    count+=1
                elif self.tiles[i][r]==self.tiles[2][1] and self.tiles[2][1]!='7':
                    count+=1
                elif self.tiles[i][r]==self.tiles[2][2] and self.tiles[2][2]!='8':
                    count+=1
                else:
                    count = count
                
        return count
                
    
    
    def __eq__(self, other):
        """that can be called when the == operator is used to compare two 
        Board objects. The method should return True if the called object 
        (self) and the argument (other) have the same values for the tiles 
        attribute, and False otherwise"""
        if self.tiles==other.tiles:
            return True
        else:
            return False
        
        
                
    def col_row_misplaced(self):
        """added method for h2 heuristic state that determines the
        roe and column misplaced. if a number is in the wrong row it 
        adds a 1 and if it is in the wrong column it adds a one and returns
        the final value of all of the numbers misplaced by rows and columns"""
        rest=0
        for r in range(3):
            for c in range(3):
                if r==0 and c==1:
                    if self.tiles[1][c]=='1':
                        rest+=1
                    elif self.tiles[2][c]=='1':
                        rest+=1
                    elif self.tiles[r][2]=='1':
                        rest+=1
                    elif self.tiles[r][0]=='1':
                        rest+=1
                    elif self.tiles[1][0]=='1':
                        rest+=2
                    elif self.tiles[1][2]=='1':
                        rest+=2
                    elif self.tiles[2][0]=='1':
                        rest+=2
                    elif self.tiles[2][2]=='1':
                        rest+=2
                if r==0 and c==2:
                    if self.tiles[1][c]=='2':
                        rest+=1
                    elif self.tiles[2][c]=='2':
                        rest+=1
                    elif self.tiles[r][1]=='2':
                        rest+=1
                    elif self.tiles[r][0]=='2':
                        rest+=1
                    elif self.tiles[2][0]=='2':
                        rest+=2
                    elif self.tiles[2][1]=='2':
                        rest+=2
                    elif self.tiles[0][0]=='2':
                        rest+=2
                    elif self.tiles[0][1]=='2':
                        rest+=2
                elif r==1 and c==0:
                   if self.tiles[0][c]=='3':
                       rest+=1
                   elif self.tiles[2][c]=='3':
                       rest+=1
                   elif self.tiles[r][1]=='3':
                       rest+=1
                   elif self.tiles[r][2]=='3':
                       rest+=1
                   elif self.tiles[0][1]=='3':
                       rest+=2
                   elif self.tiles[0][2]=='3':
                       rest+=2
                   elif self.tiles[2][1]=='3':
                       rest+=2
                   elif self.tiles[2][2]=='3':
                       rest+=2
                elif r==1 and c==1:
                    if self.tiles[2][c]=='4':
                        rest+=1
                    elif self.tiles[0][c]=='4':
                        rest+=1
                    elif self.tiles[r][2]=='4':
                        rest+=1
                    elif self.tiles[r][0]=='4':
                        rest+=1
                    elif self.tiles[0][0]=='4':
                        rest+=2
                    elif self.tiles[0][2]=='4':
                        rest+=2
                    elif self.tiles[2][0]=='4':
                        rest+=2
                    elif self.tiles[2][2]=='4':
                        rest+=2
                elif r==1 and c==2:
                    if self.tiles[0][c]=='5':
                        rest+=1
                    elif self.tiles[2][c]=='5':
                        rest+=1
                    elif self.tiles[r][1]=='5':
                        rest+=1
                    elif self.tiles[r][0]=='5':
                        rest+=1
                    elif self.tiles[0][0]=='5':
                        rest+=2
                    elif self.tiles[2][1]=='5':
                        rest+=2
                    elif self.tiles[2][0]=='5':
                        rest+=2
                    elif self.tiles[0][1]=='5':
                        rest+=2
                elif r==2 and c==0:
                    if self.tiles[1][c]=='6':
                        rest+=1
                    elif self.tiles[0][c]=='6':
                        rest+=1
                    elif self.tiles[r][2]=='6':
                        rest+=1
                    elif self.tiles[r][1]=='6':
                        rest+=1
                    elif self.tiles[1][1]=='6':
                        rest+=2
                    elif self.tiles[1][2]=='6':
                        rest+=2
                    elif self.tiles[0][1]=='6':
                        rest+=2
                    elif self.tiles[0][2]=='6':
                        rest+=2
                elif r==2 and c==1:
                    if self.tiles[1][c]=='7':
                        rest+=1
                    elif self.tiles[0][c]=='7':
                        rest+=1
                    elif self.tiles[r][2]=='7':
                        rest+=1
                    elif self.tiles[r][0]=='7':
                        rest+=1
                    elif self.tiles[1][0]=='7':
                        rest+=2
                    elif self.tiles[1][2]=='7':
                        rest+=2
                    elif self.tiles[0][0]=='7':
                        rest+=2
                    elif self.tiles[0][2]=='7':
                        rest+=2
                elif r==2 and c==2:
                    if self.tiles[1][c]=='8':
                        rest+=1
                    elif self.tiles[0][c]=='8':
                        rest+=1
                    elif self.tiles[r][1]=='8':
                        rest+=1
                    elif self.tiles[r][0]=='8':
                        rest+=1
                    elif self.tiles[1][0]=='8':
                        rest+=2
                    elif self.tiles[1][1]=='8':
                        rest+=2
                    elif self.tiles[2][0]=='8':
                        rest+=2
                    elif self.tiles[2][1]=='8':
                        rest+=2
        return rest
                        
                    
                       
                       
            
                
                    
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    