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
        ret = []
        line, n = [], 0
        for w in words:
            if n + len(w) + len(line) > maxWidth:
                if len(line) == 1:
                    ret.append(line[0] + ' ' * (maxWidth - n))
                else:
                    num_spaces = maxWidth - n - len(line) + 1
                    space, extra_space = divmod(num_spaces, len(line)-1)
                    for i in xrange(extra_space):
                        line[i] += ' '
                    ret.append((' ' * (1+space)).join(line))
                line, n = [], 0
            line += [w]
            n += len(w)
        ret.append(' '.join(line) + ' ' * (maxWidth - n - len(line) + 1))
        return ret
