"""

Toyexampleof small step semantics from understanding computation
"""

class  Number(object):

    def __init__(self, value):

        self.value =value
        self.reducible = False

    def __repr__(self):

        return '«' +str(self.value) +'»'


class Boolean(object):

    def __init__(self, value):

        self.value = value
        self.reducible = False

    def __repr__(self):

        return '«' +str(self.value) +'»'


class Variable(object):

    def __init__(self, name):

        self.name = name
        self.reducible =True



    def reduce(self, environment):

        return environment[self.name]

    def __repr__(self):

        return '«' +str(self.name) +'»'




class Add(object):

    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.reducible = True

    def reduce(self, environment):

        if self.left.reducible:
            return Add(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return Add(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.value + self.right.value)

    def __repr__(self):

        return '«' + str(self.left) + ' * ' + str(self.right) + '»'

class Multiply(object):

    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.reducible = True

    def reduce(self, environment):

        if self.left.reducible:
            return Multiply(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return Multiply(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.value * self.right.value)


    def __repr__(self):

        return '«' + str(self.left) + ' * ' + str(self.right) + '»'


class LessThan(object):

    def __init__(self, left, right):

        self.left = left
        self.right = right
        self.reducible =True


    def reduce(self, environment):

        if self.left.reducible:
            return LessThan(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return LessThan(self.left, self.right.reduce(environment))
        else:
            return Boolean(self.left.value < self.right.value)

    def __repr__(self):

        return '«' + str(self.left) + ' < ' + str(self.right) + '»'



class Machine(object):

    def __init__(self, expression, environment):

        self.expression = expression
        self.environment = environment

    def step(self):

        self.expression = self.expression.reduce(self.environment)

        return

    def run(self):

        while self.expression.reducible:

            print(self.expression)
            self.step()

        print(self.expression)

        return


if __name__=="__main__":

    expression3 = Add(Variable('x'), Variable('y'))
    environ2 ={'x':Number(2),'y':Number(4)}
    Machine(expression3, environ2).run()








