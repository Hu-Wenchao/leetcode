"""
You are playing the following Bulls and Cows game with 
your friend: You write down a number and ask your friend 
to guess what the number is. Each time your friend makes 
a guess, you provide a hint that indicates how many digits 
in said guess match your secret number exactly in both 
digit and position (called "bulls") and how many digits 
match the secret number but locate in the wrong position 
(called "cows"). Your friend will use successive guesses 
and hints to eventually derive the secret number.
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                A += 1
                secret = secret[:i] + secret[i+1:]
                guess = guess[:i] + guess[i+1:]
            else:
                i += 1
        for digit in secret:
            if digit in guess:
                B += 1
                guess = guess.replace(digit, '', 1)
        return str(A) + 'A' + str(B) + 'B'

    def getHint2(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = collections.Counter(secret), collections.Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)
