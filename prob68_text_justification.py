"""
Given an array of words and a length L, format the text 
such that each line has exactly L characters and is fully 
(left and right) justified.

You should pack your words in a greedy approach; that is, 
pack as many words as you can in each line. Pad extra 
spaces ' ' when necessary so that each line has exactly 
L characters.

Extra spaces between words should be distributed 
as evenly as possible. If the number of spaces on a 
line do not divide evenly between words, the empty 
slots on the left will be assigned more spaces than 
the slots on the right.

For the last line of text, it should be left justified 
and no extra space is inserted between words.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
                else:
                    num_spaces = maxWidth - num_of_letters - len(cur) + 1
                    space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1)
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append( (' '*(1+space_between_words)).join(cur) )
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        res.append( ' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1) )
        return res
