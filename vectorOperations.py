'''
Program Description: 
Adds, subtracts and multiplies vectors with vectors or scalar values.
Follows rules of vector multiplication and addition/subtraction.
It will correctly catch errors, displaying them to the user.
'''


class Vector:

    def __init__(self, vector_list):
        self.vector = vector_list

    '''This method along with the __repr__ method will display to the user a more legible 
    output in the format Vector([])'''
    def __str__(self):
        return "Vector({})".format(self.vector)

    __repr__ = __str__

    '''This adding method will check first that only vectors are being adding, then it will
    proceed to check whether both vectors are the same length, if it passes all those tests
    it will add each component of the vectors and return a new vector as a response'''
    def __add__(self, other):
        addList = []
        if type(other) == int:
            return 'Error - Invalid operation'
        elif len(self.vector) != len(other.vector):
            return 'Error - Invalid dimensions'
        for i in range(len(self.vector)):
            x = self.vector[i] + other.vector[i]
            addList.append(x)
        return Vector(addList)
    '''This __radd__  will make sure that the vectors are added in the same way even if the 
    vectors are switched positions'''
    __radd__ = __add__

    '''This method will check make sure that what's being subtracted are two vectors using the 
    same tests as the __add__ method and will subtract each component of the vectors and return 
    a new vector to the user'''
    def __sub__(self, other):
        subList = []
        if type(other) == int:
            return 'Error - Invalid operation'
        elif len(self.vector) != len(other.vector):
            return 'Error - Invalid dimensions'
        for i in range(len(self.vector)):
            x = self.vector[i] - other.vector[i]
            subList.append(x)
        return Vector(subList)

    '''This method check if there are two vectors being multiplied which will return a scalar 
    response instead of a vector, otherwise it will check if a vector is being multiplied by scalar 
    which will return a Vector'''
    def __mul__(self, other):
        finalNum = 0
        if type(other) == int:
            mulList = []
            for i in range(len(self.vector)):
                x = other*self.vector[i]
                mulList.append(x)
            return Vector(mulList)
        for i in range(len(self.vector)):
            x = self.vector[i]*other.vector[i]
            finalNum += x
        return finalNum

    '''This method will make sure that the vectors will be multiplied the same way even if the position 
    of the two values are switched'''
    __rmul__ = __mul__

    '''This method will check if the vectors given are equal to each other by checking each of their values 
    to the corresponding vector. If they are all equal it will return True, otherwise it will return False.'''
    def __eq__(self, other):
        try:
            for i in range(len(self.vector)):
                self.vector[i] = other.vector[i]
                continue
        except:
            return False
        return True








    