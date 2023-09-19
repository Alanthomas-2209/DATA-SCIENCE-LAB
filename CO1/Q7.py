class complex:
    realpart = 0
    complexPart = 0

    def __init__(self,realPart, complexPart) -> None:
        self.realpart = realPart
        self.complexPart = complexPart
    def __add__(self,obj):
        return