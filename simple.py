"""

Toyexampleof small step semantics from understanding computation
"""

class  Number(object):

    def __init__(self, value):

        self.value =value
        self.reducible = False

    def __repr__(self):

        return '«' +str(self.value) +'»'

class Add(object):

    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.reducible = True

    def reduce(self):

        if self.left.reducible:
            return Add(self.left.reduce(), self.right)
        elif self.right.reducible:
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value + self.right.value)

    def __repr__(self):

        return '«' + str(self.left) + ' * ' + str(self.right) + '»'

class Multiply(object):

    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.reducible = True

    def reduce(self):

        if self.left.reducible:
            return Add(self.left.reduce(), self.right)
        elif self.right.reducible:
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value * self.right.value)


    def __repr__(self):

        return '«' + str(self.left) + ' * ' + str(self.right) + '»'


