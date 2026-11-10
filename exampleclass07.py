class Student:
    def __init__(self, firstname, lastname, weight):
        print('  constructor')
        self.firstname=firstname
        self.lastname=lastname
        self.weight=weight

    @property
    def name(self):
        print('  name getter')
        return self.firstname+' '+self.lastname

    @name.setter
    def name(self, fullname):
        print('  name setter')
        firstname, lastname=fullname.split()
        self.firstname=firstname
        self.lastname=lastname

    @property
    def weight(self):
        print('  weight getter')
        #Use protected variable _weight to store weight
        return self._weight

    @weight.setter
    def weight(self, weight):
        print('  weight setter')
        if weight<0 or weight>500:
            raise ValueError
        self._weight=weight

if __name__=='__main__':
    matti=Student('Matti', 'Mainio', 85.5)
    jussi=Student('Jussi', 'Juonio', 78.8)

    print(matti.name)
    print(jussi.name)

    matti.name='Matt Superb'
    print(matti.name)

    try:
        matti.weight=-10.2
    except:
        print('Got an exception!')

    matti.weight=87.7
    print('Matt\'s weight is',matti.weight)
