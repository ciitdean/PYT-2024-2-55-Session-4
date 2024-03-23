# Base class
class Shape:
    def draw(self):
        raise NotImplementedError("Draw method not implemented")

# Trying to use the Shape class directly
shape = Shape()

try:
    shape.draw()
except NotImplementedError as e:
    print(f"Error: {e}")
