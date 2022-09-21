class Queen:
    def __init__(self, row, column):
        self.row = self.handle_errors(row, 'row')
        self.column = self.handle_errors(column, 'column')

    def handle_errors(self, cordinate, row_or_column):

        if cordinate < 0:
            raise ValueError("{} not positive".format(row_or_column))
        if cordinate >= 8:
            raise ValueError("{} not on board".format(row_or_column))

        return cordinate


    def can_attack(self, another_queen):

        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        sum_this_queen = self.row + self.column
        sub_this_queen = self.row - self.column

        sum_other_queen = another_queen.row + another_queen.column
        sub_other_queen = another_queen.row - another_queen.column
        
        if self.row == another_queen.row:
            return True
        elif self.column == another_queen.column:
            return True
        elif sum_this_queen == sum_other_queen:
            return True 
        elif sub_this_queen == sub_other_queen:
            return True
        else: 
            return False
