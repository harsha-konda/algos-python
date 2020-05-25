class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        bigger = 'Billion Million Thousand'.split()

        if num == 0:
            return "Zero"

        def words(n):
            if n==0:
                return []

            if n<20:
                return [to19[n-1]]

            if n<100:
                return [tens[n//10-2]] + words(n%10)

            if n<1000:
                return words(n//100) + ["Hundred"] + words(n%100)

            value = 10**9
            for i,name in enumerate(bigger):
                times = n//value
                if (times) > 0 :
                    return words(times) + [name] + words(n%value)
                value //=10**3

        return ' '.join(words(num))
        