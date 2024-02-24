Sintaxis basica

class Example:
    pass

Example.variable = "something"
Example.data = "other-value"

print(Example.variable)
print(Example.data)
#---#
class Example:

    def __init__(self, variable, data)
    self.variable = variable
    self.data = data

p = Example("something", "other-value")
print(p.variable)
print(p.data)
