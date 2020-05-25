class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.square = width * length
        self.perimeter = (width + length) * 2

    def get_square(self):
        print('\nПлощадь прямоугольника: ',  self.square)

    def get_perimeter(self):
        print( '\nПериметр прямоугольника: ', self.perimeter)



rectangle = Rectangle (10, 2)
rectangle.get_square()
rectangle.get_perimeter()

print('Ширина прямоугольника: ',rectangle.width,
      '\nДлина прямоугольника: ',rectangle.length)