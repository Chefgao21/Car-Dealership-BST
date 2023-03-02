from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory():
    
    def __init__(self):
        self.size = 0
        self.root = None
        
    def findNode(self, car):
        return self.findNode1(car, self.root)

    def findNode1(self, car, currentnode):
        if currentnode == None:
            return None
        elif (car.model == currentnode.model) and (car.make == currentnode.make):
            return currentnode
        elif (car.model < currentnode.model and car.make == currentnode.make) or car.make < currentnode.make:
            return self.findNode1(car, currentnode.left)
        elif (car.model > currentnode.model and car.make == currentnode.make) or car.make > currentnode.make:
            return self.findNode1(car, currentnode.right) 

    def doesCarExist(self, car):
        node = self.findNode(car)
        if node == None:
            return False
        for i in node.cars:
            if i == car:
                return True
        return False
        
    def addCar(self, car):
        self.root = self.addCar1(self.root, car)
        self.size += car.price

    def addCar1(self, node, car):
        if node == None:
            return CarInventoryNode(car)
        else:
            if node.make < car.make:
                node.right = self.addCar1(node.right, car)
                node.right.parent = node
            elif node.make == car.make:
                if node.model < car.model:
                    node.right = self.addCar1(node.right, car)
                    node.right.parent = node
                elif node.model > car.model:
                    node.left = self.addCar1(node.left, car)
                    node.left.parent = node
                else:
                    node.cars.append(car)
            else:
                node.left = self.addCar1(node.left, car)
                node.left.parent = node
            return node

    def getTotalInventoryPrice(self):
        return self.size

    def preOrder(self):
        return self.preOrder1(self.root)

    def preOrder1(self, node):
        string = ''
        if node != None:
            for i in node.cars:
                string += str(i) + '\n'
            string += self.preOrder1(node.left)
            string += self.preOrder1(node.right)
        return string

    def inOrder(self):
        return self.inOrder1(self.root)

    def inOrder1(self, node):
        string = ''
        if node != None:
            string += self.inOrder1(node.left)
            for i in node.cars:
                string += str(i) + '\n'
            string += self.inOrder1(node.right)
        return string

    def inOrder2(self, node):
        lis = []
        if node != None:
            lis = self.inOrder2(node.left)
            lis.append(node)
            lis = lis + self.inOrder2(node.right)
        return lis


    def postOrder(self):
        return self.postOrder1(self.root)

    def postOrder1(self, node):
        string = ''
        if node != None:
            string += self.postOrder1(node.left)
            string += self.postOrder1(node.right)
            for i in node.cars:
                string += str(i) + '\n'
        return string

    def getWorstCar(self, make, model):
        car = Car(make, model, 0, 0)
        new = self.findNode(car)
        if new == None:
            return None
        return min(new.cars)

    def getBestCar(self, make, model):
        car = Car(make, model, 0, 0)
        new = self.findNode(car)
        if new == None:
            return None
        return max(new.cars)

    def getSuccessor(self, make, model):
        car = Car(make, model, 0, 0)
        new = self.findNode(car)
        if new == None:
            return None
        succ = None

        lis = self.inOrder2(self.root)
        for i in range(len(lis) - 1):
            if(lis[i].make.upper() == make.upper() and lis[i].model.upper() == model.upper()):
                succ = lis[i + 1]
        return succ


    def spliceOut(self, node):
        if node == None:
            return
	# Case 1:
	# If node to be removed is a leaf, set parent's left or right
	# child references to None
        if (node.right == None) and (node.right == None):
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

	# Case 2:
	# Not a leaf node. Should only have a right child for BST
	# removal
        elif (node.left != None) or (node.right != None):
            if node.right != None:
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent


    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        new = self.findNode(car)
        if new == None:
            return False
        for i in range(len(new.cars)):
            if new.cars[i].make == car.make and new.cars[i].model == car.model and new.cars[i].year == car.year and new.cars[i].price == car.price :
                new.cars.remove(new.cars[i])
                break
            if i == len(new.cars) - 1:
                return False
        if new.cars == []:
            self.remove(new)
        return True

        

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.findNode1(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # remove modifies the tree
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

# Used to remove the node and account for BST deletion cases
    def remove(self, node):

        if node.left == None and node.right == None:
            if(node.parent == None):
                self.root = None
            else:
                if(node.parent.left == node):
                    node.parent.left = None
                else:
                    node.parent.right = None
        
        elif  node.left == None :
            if(node.parent != None):
                if(node.parent.left == node):
                    node.parent.left = node.right
                    node.right.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
            else:
                node.right.parent = None
                self.root = node.right

 
        elif  node.right == None :
            if(node.parent != None):
                if(node.parent.left == node):
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.left
                    node.left.parent = node.parent
            else:
                node.left.parent = None
                self.root = node.left
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        else:
            succ = self.getSuccessor(node.make, node.model)
             
            # Copy the inorder successor's
            # content to this node
            if succ != None:
                tempMake = succ.make
                tempModel = succ.model
                tempCars = succ.cars
                if succ.left == None and succ.right == None:
                    if succ.parent == None:
                        self.root = None
                    else:
                        if succ.parent.left == succ:
                            succ.parent.left = None
                        else:
                            succ.parent.right = None
                
                elif  succ.left == None :
                    if succ.parent != None:
                        if succ.parent.left == succ:
                            succ.parent.left = succ.right
                            succ.right.parent = succ.parent
                        else:
                            succ.parent.right = succ.right
                            succ.right.parent = succ.parent
                    else:
                        succ.right.parent = None
                        self.root = succ.right

         
                elif  succ.right == None :
                    if succ.parent != None:
                        if succ.parent.left == succ:
                            succ.parent.left = succ.left
                            succ.left.parent = succ.parent
                        else:
                            succ.parent.right = succ.left
                            succ.left.parent = succ.parent
                    else:
                        succ.left.parent = None
                        self.root = succ.left
     

                node.make = tempMake
                node.model = tempModel
                node.cars = tempCars







