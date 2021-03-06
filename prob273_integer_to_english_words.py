"""
Convert a non-negative integer to its english words 
representation. Given input is guaranteed to be less 
than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four 
Thousand Five Hundred Sixty Seven"
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        billion = 10**9
        million = 10**6
        thousand = 10**3
        if num == 0:
            res = 'Zero'
        if num >= billion:
            res += self.helper(num / billion) + 'Billion '
            num %= billion
        if num >= million:
            res += self.helper(num / million) + 'Million '
            num %= million
        if num >= thousand:
            res += self.helper(num / thousand) + 'Thousand '
            num %= thousand
        if num > 0:
            res += self.helper(num)
        return res.rstrip(' ')
        
    def helper(self, num):
        dic = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
               6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
               11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
               15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen',
               18 : 'Eighteen', 19 : 'Nineteen', 20 : 'Twenty',
               30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
               70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety'}
        res = ''
        if num >= 100:
            res += dic[num / 100] + ' Hundred '
            num %= 100
        if num > 20:
            res += dic[num / 10 * 10] + ' '
            num %= 10
        if num >0:
            res += dic[num] + ' '
        return res
