"""
Write e method to extend the size of big intiger if one is added to it.
"""


class BigIntiger(object):

    def __init__(self):
        self.big_num = [4, 5, 6]

    def add(self, num):
        """-Each digit is a node
           -Head of ll is last digit
           -Iterate over keeping overflow
           -If reach end of ll and overlow is not 0, add one more node, assign overflow to that node
           -*Make over-flow node the new head

           internal_num = 234 [0 ,1, 2] [-3, -2, -1]
           1 [0] index [-1]
        """
        overflow = None
        # Created empty list of 0's with the same length of big_num, otherwise would get index out of range
        # error in the for-loop below

        new_num = [0]*len(self.big_num)

        for n in xrange(-1, -len(self.big_num)-1, -1):  # This iterates in order -1, -2, -3, -4 ...
            # Used try/except to handle index errors for len(num) < len(self.big_num)
            try:
                if overflow is None:
                    overflow, nn = divmod(self.big_num[n] + num[n], 10)
                    new_num[n] = nn
                else:
                    overflow, new_num[n] = divmod(self.big_num[n] + num[n] + overflow, 10)
            except:
                overflow, new_num[n] = divmod(self.big_num[n] + overflow, 10)

        if overflow > 0:
            """Add new node"""
            new_num = [overflow] + new_num
        return new_num

    def printout(self, num):
        print self.add(num)

my_big_int = BigIntiger()
my_big_int.printout([4, 4, 4])
