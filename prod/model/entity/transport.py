class Transport:
    def __init__(self, width, length, number):
        self._width = width
        self._length = length
        self._number = number

    @property
    def square(self):
        return self._width * self._length

    @property
    def width(self):
        return self._width

    @width_setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise Exception()

    @width_deleter
    def width(self):
        del self._width

    @property
    def length(self):
        return self._length

    @length_setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise Exception()

    @length_deleter
    def length(self):
        del self._length

    @property
    def number(self):
        return self._number

    @number_setter
    def number(self, number):
        self._number = number

    @number_deleter
    def number(self):
        del self._number



    def __str__(self):
        return (f"width = {self._width}, " \
               f"length = {self._length}, " \
               f"number = {self._number}")