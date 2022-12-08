class MySolution:
    def plusOne(self, digits):
        one = 1
        i = len(digits) - 1
        while one:
            if i > 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                if digits[0] == 9:
                    digits[0] = 1
                    digits.append(0)
                else:
                    digits[0] += 1
                one = 0
            i -= 1
        return digits




