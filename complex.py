class Complex_no:
    from typing import Literal
    
    def __init__(self, real_part: int, imaginary_part: int = 0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
    
    @property
    def number(self):
        if self.real_part == 0:
            if self.imaginary_part > 0:
                return f"i{self.imaginary_part}"
            elif self.imaginary_part < 0:
                return f"-i{-self.imaginary_part}"
        elif self.imaginary_part > 0:
            return f"{self.real_part} + i{self.imaginary_part}"
        elif self.imaginary_part < 0:
            return f"{self.real_part} + (-i{-self.imaginary_part})"
        else:
            return f"{self.real_part} + i{self.imaginary_part}"
            
    def __add__(self, complex2):
        new_real = self.real_part + complex2.real_part
        new_image = self.imaginary_part + complex2.imaginary_part
        return Complex_no(new_real, new_image)
    
    def __sub__(self, complex2):
        new_real = self.real_part - complex2.real_part
        new_image = self.imaginary_part - complex2.imaginary_part
        return Complex_no(new_real, new_image)
    
    def __mul__(self, complex2):
        new_real = self.real_part*complex2.real_part - self.imaginary_part*complex2.imaginary_part
        new_image = self.real_part*complex2.imaginary_part + self.imaginary_part*complex2.real_part
        return Complex_no(new_real, new_image)
    
    def __truediv__(self, complex2):
        denom = complex2.real_part**2 + complex2.imaginary_part**2
        new_real = (self.real_part * complex2.real_part + self.imaginary_part * complex2.imaginary_part) / denom
        new_image = (self.imaginary_part * complex2.real_part - self.real_part * complex2.imaginary_part) / denom
        
        return Complex_no(new_real, new_image)

    def __neg__(self):
        new_real = -self.real_part
        new_image = -self.imaginary_part
        return Complex_no(new_real, new_image)
    
    def __pos__(self):
        return Complex_no(self.real_part, self.imaginary_part)
    
    def __invert__(self):
        a, b = self.real_part, self.imaginary_part
        new_real = a/(a**2 + b**2)
        new_image = -b/(a**2 + b**2)
        return Complex_no(new_real, new_image)
    
    def __format__(self, format_spec: str) -> str:
        return self.number
    
    def __str__(self) -> str:
        return self.number
    
    def __repr__(self) -> str:
        return self.number
    
    def __getitem__(self, key: Literal['r', 'i', 1, 2]):
        if key == "r" or key == 1:
            return self.real_part
        return self.imaginary_part
    
    def __setitem__(self, index: Literal['r', 'i', 1, 2], value):
        if  index == "r" or index == 1:
            self.real_part = value
        elif index == "i" or index == 2:
            self.imaginary_part = value
            
    def __iter__(self):
        return iter([self.real_part, self.imaginary_part])

    def __eq__(self, other: complex):
        return (self.real_part, self.imaginary_part) == (other.real_part, other.imaginary_part)
        
    def __iadd__(self, other):
        self.real_part  += other.real_part
        self.imaginary_part  += other.imaginary_part
        return self

    def __isub__(self, other):
        self.real_part  -= other.real_part
        self.imaginary_part  -= other.imaginary_part
        return self
    
    def modulus(self) ->  float:
        return (self.real_part**2 + self.imaginary_part**2)**0.5
        
    def  conjugate(self) -> complex:
        return Complex_no(self.real_part, -self.imaginary_part)

    def polar_form(self) ->  str:
        pass
