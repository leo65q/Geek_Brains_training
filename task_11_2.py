class DivisionByNull:
    def __init__(self, x, y):
        self.divider = x
        self.denominator = y

    @staticmethod
    def divide_by_null(x, y):
        try:
            return x / y
        except:
            return f"Деление на ноль запрещено!"


div = DivisionByNull(10, 100)
print(div.divide_by_null(156, 0))
print(div.divide_by_null(545, 54))
print(div.divide_by_null(55, 0))
print(div.divide_by_null(354, 4))
print(div.divide_by_null(33, 0))
print(div.divide_by_null(66, 2))
