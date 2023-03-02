
from Car import Car
from CarInventory import CarInventory
from CarInventoryNode import CarInventoryNode

bst = CarInventory()

car1 = Car("Nissan", "New", 1999, 21000)
car2 = Car("Tesla", "Model3", 2008, 68000)
car3 = Car("Nissan", "New", 2030, 5000)
car4 = Car("Honda", "Civic", 2011, 2000)
car5 = Car("Nissan", "Altima", 2019, 25000)
car6 = Car("Nissan", "Altima", 2019, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)

def test__lab08():
    assert bst.getBestCar("Nissan", "New") == car3
    assert bst.getBestCar("Tesla", "Model3") == car2
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "New") == car1
    assert bst.getWorstCar("Nissan", "Altima") == car5
    assert bst.getBestCar("Mercedes", "Benz") == None
    assert bst.getTotalInventoryPrice() == 121000

    assert car4 < car2
    assert car5 == car6
    assert car1 > car4

    assert str(car1) == 'Make: NISSAN, Model: NEW, Year: 1999, Price: $21000'

    assert bst.doesCarExist(car2) == True

    
def test__lab08a():   
    assert bst.preOrder() == 'Make: NISSAN, Model: NEW, Year: 1999, Price: $21000\nMake: NISSAN, Model: NEW, Year: 2030, Price: $5000\nMake: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\n'

    assert bst.inOrder() == 'Make: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: NISSAN, Model: NEW, Year: 1999, Price: $21000\nMake: NISSAN, Model: NEW, Year: 2030, Price: $5000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\n'

    assert bst.postOrder() == 'Make: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\nMake: NISSAN, Model: NEW, Year: 1999, Price: $21000\nMake: NISSAN, Model: NEW, Year: 2030, Price: $5000\n'

def test__lab09():
    
    assert bst.getSuccessor('Tesla', 'Model3') == None

def test__lab09a():  
    bst.removeCar("Nissan", "New", 1999, 21000)
    assert bst.preOrder() == 'Make: NISSAN, Model: NEW, Year: 2030, Price: $5000\nMake: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\n'
    assert bst.inOrder() == 'Make: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: NISSAN, Model: NEW, Year: 2030, Price: $5000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\n'
    assert bst.postOrder() == 'Make: NISSAN, Model: ALTIMA, Year: 2019, Price: $25000\nMake: HONDA, Model: CIVIC, Year: 2011, Price: $2000\nMake: TESLA, Model: MODEL3, Year: 2008, Price: $68000\nMake: NISSAN, Model: NEW, Year: 2030, Price: $5000\n'

def test__lab09b():
    assert bst.removeCar("Nissan", "Altima", 2019, 25000) == True

def test__lab09c():
    assert bst.removeCar("Honda", "Civic", 2011, 2000) == True

def test__lab09d():
    assert bst.removeCar("Mercedes", "Benz", 2001, 20300) == False

    








    










