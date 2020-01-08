##
# Hi, I am Sofya, I am a CS student. This program  uses classes to store, search, sort, remove and filter country data.
#
class Country :
    def __init__(self, name, pop, area, continent) :
        self._name = name  # name: The name of the country (string)
        self._pop = pop  # population: The population in the country (integer)
        self._area = area  # area: The area of the country (float)
        self._continent = continent  # continent: The name of the continent to which the country belongs (string)
        self._popDensity = 0

    def getName(self) :
        return str(self._name)
    def getPopulation(self) :
        return int(self._pop)
    def getArea(self) :
        return float(self._area)
    def getContinent(self) :
        return str(self._continent)
    def setPopulation(self, newPop) :
        self._pop = newPop
    def setArea(self, newArea) :
        self._area = newArea
    def setContinent(self, newContinent) :
        self._continent = newContinent
    # getPopDensity: This calculates and returns the population density for the country.
    def getPopDensity(self) :
        self._popDensity = round(self._pop/self._area, 2)
        return self._popDensity
    # def __repr__(self): generates a string representation for class objects.
    def __repr__(self) :
        return self._name + " (pop: "+ str(self._pop) + ", size: "+ str(self._area) + ") in "+ self._continent

