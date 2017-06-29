"""Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 
A player gets +1 point for each occurrence of the substring in the string .

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.
"""


def minion_game(s):
    """This method creates all subsets and then counts"""

    vowels = set(['A', 'E', 'I', 'O', 'U'])
    if len(set(string)) == 1:
        sub = [string[0]]
    else:
        #This finds all subsets of words in subsequent order
        sub = []
        for i in range(len(s)):
            sub.append(s[i])
            for j in range(i+1, len(s)):
                sub.append(s[i:j+1])

    kevin_sum = 0
    stuart_sum = 0    

    for item in sub:
        if item[0] in vowels:
            kevin_sum +=1
        else:
            stuart_sum += 1
            
    if stuart_sum > kevin_sum:
        print "Stuart %s" % stuart_sum
    elif stuart_sum < kevin_sum:
        print "Kevin %s" % kevin_sum
    else:
        print "Draw"


def minion_game_better_runtime(s):
    """This is O(n) runtime solution"""

    vowels = set(['A', 'E', 'I', 'O', 'U'])

    kevsc = 0
    stusc = 0
    for i in xrange(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"

minion_game_better_runtime('banana')


