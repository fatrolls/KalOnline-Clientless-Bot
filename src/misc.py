import random
import string

def GetValueFromKey(lines, key):
    for line in lines:
        pos = line.find("=")
        if line[0:pos] == key:
            return line[pos+1:]


class Rectangle():
    def __init__(self, x, y, width, height):   
        if width >= 0:
            self.width = width
            self.x = x
        else:
            self.width = abs(width)
            self.x = x + width  # width negative this shifts x to smaller value
        if height >= 0:
            self.height = height
            self.y = y
        else:
            self.height = abs(height)
            self.y = y + height  # height negative this shifts y to smaller value

    def IsCoordinateInside(self, x, y):
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            return True
        return False


def RandomString(type, length):
    res = ""
    sigma_hexdigits = list(string.hexdigits[0:10]) + list(string.hexdigits[16:22])
    sigma_letter_digits = list(string.ascii_letters) + list(string.digits)
    sigma_digits = list(string.digits)
    for _ in range(length):
        if type == 0:  # hexdigits
            res += sigma_hexdigits[random.randint(0, len(sigma_hexdigits) - 1)]
        elif type == 1:
            res += sigma_letter_digits[random.randint(0, len(sigma_letter_digits) - 1)]
        elif type == 2:
            res += sigma_digits[random.randint(0, len(sigma_digits) - 1)]
    return res


