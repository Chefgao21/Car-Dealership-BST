from Car import Car

class CarInventoryNode():

    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = []
        self.parent = None
        self.left = None
        self.right = None
        self.cars.append(car)

    def isLeaf(self):
        return not (self.right or self.left)
        
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model

    def hasBothChildren(self):
        return self.right and self.left
    
    def getParent(self):
        if self.parent != None:
            return self.parent
        else:
            return None
        
    def setParent(self, parent):
        self.parent = parent
    
    def getLeft(self):
        if self.left != None:
            return self.left
        else:
            return None
    
    def setLeft(self, left):
        self.left = left
        
    def getRight(self):
        if self.right != None:
            return self.right
        else:
            return None
        
    def setRight(self, right):
        self.right = right
        
    def __str__(self):
        string = ''
        for car in self.cars:
            string += (str(car))
            string += ('\n')
        return string

    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current


    def findMax(self):
        current = self
        while current.right:
            current = current.right
        return current




            
        
