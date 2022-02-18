class Matrix:
    def __init__(self, number_1, number_2, number_3, number_4):
        self.number_1 = number_1
        self.number_2 = number_2
        self.number_3 = number_3
        self.number_4 = number_4

    def __str__(self):
        return '{} {}\n{} {}'.format(self.number_1, self.number_2, self.number_3, self.number_4)

    def __add__(self, other):
        return Matrix(self.number_1 + other.number_1, self.number_2 + other.number_2, self.number_3 + other.number_3,
                      self.number_4 + other.number_4)


first_m = Matrix(45, 23, 27, 75)
second_m = Matrix(58, 43, 90, 64)

print(first_m, end='\n\n')

print(second_m, end='\n\n')

print(first_m + second_m)

