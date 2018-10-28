#!/home/yue/github/notes_of_flask/flask_env/bin/python
# -*- coding: utf-8 -*-


# refer to 'https://bitbucket.org/akorn/wheezy.captcha'

import random
import string
import os.path
from io import BytesIO

from PIL import Image

from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype


class Bezier:
    def __init__(self):
        self.tsequence = tuple([t / 20.0 for t in range(21)])
        self.beziers = {}

    def pascal_row(self, n):
        """
        :param n:
        :return: n-th row of pascal's triangle
        """
        result = [1]
        x, numerator = 1, n
        for denominator in range(1, n // 2 + 1):
            x *= numerator
            x /= denominator
            result.append(x)
            numerator -= 1
        if n & 1 == 0:
            result.extend(reversed(result[:-1]))
        else:
            result.extend(reversed(result))
        return result

    def make_bezier(self, n):
        """Bezier curves:
        http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        """
        try:
            return self.beziers[n]
        except KeyError:
            pass
