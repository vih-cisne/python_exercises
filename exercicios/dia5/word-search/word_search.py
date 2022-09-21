


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        #other is a tuple?
        if other != None:
            return self.x == other[0].x and self.y == other[0].y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        line_left_to_right = self.search_line_left_to_right(word)
        line_right_to_left = self.search_line_right_to_left(word)

        vert_top_to_bottom = self.search_top_to_bottom(word)
        vert_bottom_to_top = self.search_bottom_to_top(word)

        diag_top_left_to_bottom_right = self.search_top_left_to_bottom_right(word)
        diag_top_right_to_bottom_left = self.search_top_right_to_bottom_left(word)

        diag_bottom_left_to_top_right = self.search_bottom_left_to_top_right(word)
        diag_bottom_right_to_top_left = self.search_bottom_right_to_top_left(word)


        if line_left_to_right  != None:
            return line_left_to_right
        
        if line_right_to_left != None:
            return line_right_to_left

        if vert_top_to_bottom != None:
            return vert_top_to_bottom
        
        if vert_bottom_to_top != None:
            return vert_bottom_to_top

        if diag_top_left_to_bottom_right != None:
            return diag_top_left_to_bottom_right
        
        if diag_top_right_to_bottom_left != None:
            return diag_top_right_to_bottom_left

        if diag_bottom_left_to_top_right != None:
            return diag_bottom_left_to_top_right
        
        if diag_bottom_right_to_top_left != None:
            return diag_bottom_right_to_top_left


    
    def search_line_left_to_right(self, word):

        for y, line in enumerate(self.puzzle):
            x = line.find(word) 
            if x != -1:
                return Point(x,y)

    def search_line_right_to_left(self, word):

        word_reverse = list(word)
        word_reverse.reverse()
        word_reverse = ''.join(word_reverse)

        for y, line in enumerate(self.puzzle):
            x = line.find(word_reverse) 
            if x != -1:
                return Point(x+len(word_reverse)-1,y)

    def search_top_to_bottom(self, word):

        finded = 0
        x = None
        y = 0

        for index, line in enumerate(self.puzzle):
            position = -1
            for i,char in enumerate(line):
                if char == word[finded] and (i == x or x == None): 
                    position = i 
            
            if position == -1:
                x = None
                finded = 0
            else:
                if x == None and finded == 0:
                    finded += 1
                    y = index
                    x = position
                elif x == position:
                    finded += 1

            if finded == len(word):
                return Point(x,y)

    def search_top_left_to_bottom_right(self, word):

        finded = 0
        x = None
        y = 0

        for index, line in enumerate(self.puzzle):
            position = -1
            for i,char in enumerate(line):
                if char == word[finded] and (x == None or i == x+1): 
                    position = i
            
            if position == -1:
                x = None
                finded = 0
            else:
                if x == None and finded == 0:
                    finded += 1
                    y = index
                    x = position
                elif x + 1 == position :
                    finded += 1
                    x = position 
            if finded == len(word):
                return Point(x-len(word)+1,y)

    def search_top_right_to_bottom_left(self, word):

        finded = 0
        x = None
        y = 0


        for index, line in enumerate(self.puzzle):
            position = -1
            
            for i,char in enumerate(line):
                if char == word[finded] and (x == None or i == x-1): 
                    position = i 
            
            if position == -1:
                x = None
                finded = 0
                for i,char in enumerate(line):
                    if char == word[finded] and (x == None or i == x-1): 
                        position = i
            if x == None and finded == 0 and position != -1:
                finded += 1
                y = index
                x = position
            elif x == position + 1:
                finded += 1
                x = position

            if finded == len(word):
                return Point(x+len(word)-1,y)

    def search_bottom_right_to_top_left(self, word):
        word_reverse = list(word)
        word_reverse.reverse()
        word_reverse = ''.join(word_reverse)

        finded = 0
        x = None

        for index, line in enumerate(self.puzzle):
            position = -1
            for i,char in enumerate(line):
                if char == word_reverse[finded] and (x == None or i == x+1): 
                    position = i
            
            if position == -1:
                x = None
                finded = 0
            else:
                if x == None and finded == 0:
                    finded += 1
                    x = position
                elif x + 1 == position:
                    finded += 1
                    x = position

            if finded == len(word_reverse):
                return Point(x,index)

    def search_bottom_left_to_top_right(self, word):
        word_reverse = list(word)
        word_reverse.reverse()
        word_reverse = ''.join(word_reverse)

        finded = 0
        x = None

        for index, line in enumerate(self.puzzle):
            position = -1
            for i,char in enumerate(line):
                if char == word_reverse[finded] and (x == None or i == x-1 ): 
                    position = i
            
            if position == -1:
                x = None
                finded = 0
            else:
                if x == None and finded == 0:
                    finded += 1
                    x = position
                elif x - 1 == position:
                    finded += 1
                    x = position

            if finded == len(word_reverse):
                return Point(x,index)


    def search_bottom_to_top(self, word):
        word_reverse = list(word)
        word_reverse.reverse()
        word_reverse = ''.join(word_reverse)

        finded = 0
        x = None

        for index, line in enumerate(self.puzzle):
            position = -1
            for i,char in enumerate(line):
                if char == word_reverse[finded] and (i == x or x == None): 
                    position = i
            
            if position == -1:
                x = None
                finded = 0
                for i,char in enumerate(line):
                    if char == word_reverse[finded] and (i == x or x == None): 
                        position = i
            if x == None and finded == 0 and position != -1:
                finded += 1
                x = position
            elif x == position:
                finded += 1

            if finded == len(word_reverse):
                return Point(x,index)








        

