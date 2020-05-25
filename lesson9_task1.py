class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.square = width * length
        self.perimeter = (width + length) * 2

    def get_object(self):
        print(f'Ширина прямоугольника: {rectangle.width} \nДлина прямоугольника: {rectangle.length}')

    def get_square(self):
        print(f'Площадь прямоугольника: {self.square}')

    def get_perimeter(self):
        print( f'Периметр прямоугольника: {self.perimeter}')



rectangle = Rectangle (10, 2)
rectangle.get_object()
rectangle.get_square()
rectangle.get_perimeter()


