class Calculattor:
    def add(self, a: int, b: int, c:int=10) -> int:
        return a + b + c
    
calc = Calculattor()
print(calc.add(1, 2))  # Output: 13
print(calc.add(1, 2, 3))  # Output: 6
print(calc.add(1, 2, 8))  # Output:
    
