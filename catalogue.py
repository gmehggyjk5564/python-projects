from country import Country

class CountryCatalogue :
    def __init__(self, firstFile, secondFile) :
        self._cDictionary = {}
        continentFile = open(firstFile, "r")
        for line in continentFile :
            line = line.strip("\n")
            continentList = line.split(",")
            aKeywordName = continentList[0]
            aValueContinent = continentList[1]
            self._cDictionary[aKeywordName] = aValueContinent
        self._cDictionary.pop("Country")

        self._countryCat = {}
        self._nameList = []
        self._populationList = []
        self._areaList = []
        dataFile = open(secondFile, "r")
        for line in dataFile :
            line = line.strip("\n")
            line = line.replace(",", "")
            line = line.split("|")
            self._nameList.append(line[0])
            self._populationList.append(line[1])
            self._areaList.append(line[2])
        self._nameList.pop(0)
        self._populationList.pop(0)
        self._areaList.pop(0)

        for name in self._nameList : # creating a dict with country names and country objects.
            countryObject = Country(name, self._populationList[self._nameList.index(name)], self._areaList[self._nameList.index(name)],self._cDictionary[name])
            self._countryCat[name] = countryObject

    def findCountry(self, name) :
        if name in self._countryCat :
            return self._countryCat[name]
        else :
            return "None"
    def setPopulationOfCountry(self, name, newPop) :
        if name in self._countryCat :
            self._countryCat[name].setPopulation(newPop)
            return True
        else :
            return False
    def setAreaOfCountry(self, name, newArea) :
        if name in self._countryCat :
            self._countryCat[name].setArea(newArea)
            return True
        else :
            return False
    def addCountry(self, name, pop, area, continent) :
        if name not in self._countryCat :
            self._countryCat[name] = (Country(name, pop, area, continent))
            self._cDictionary[name] = continent
            return True
        else:
            return False
    def deleteCountry(self, name) :
        if name in self._countryCat :
            self._cDictionary.pop(name)
            self._countryCat.pop(name)
    def printCountryCatalogue(self) :
        str(self._countryCat)
        print(self._countryCat)
    def getCountriesByContinent(self, continent) :
        continentList = []
        for i in self._cDictionary:
            if continent == self._cDictionary[i] :
                continentList.append(i)
                return continentList
    def getCountriesByPopulation(self, continent) :
        countryListbyPop = []
        if continent != "" :
            for i in self._cDictionary :
                if continent == self._cDictionary[i] :
                    countryListbyPop.append((i, float(self._countryCat[i].getPopulation())))
            return sorted(countryListbyPop, key=lambda countryListbyPop : countryListbyPop[1], reverse = True)
        elif continent == "" :
            for i in self._cDictionary :
                countryListbyPop.append((i, float(self._countryCat[i].getPopulation())))
            return sorted(countryListbyPop, key=lambda x : x[1], reverse = True)
        else :
            return countryListbyPop
    def getCountriesByArea(self, continent) :
        countryListbyArea = []
        if continent != "" :
            for i in self._cDictionary :
                if continent == self._cDictionary[i] :
                    countryListbyArea.append((i, float(self._countryCat[i].getArea())))
            return sorted(countryListbyArea, key=lambda countryListbyArea : countryListbyArea[1], reverse=True)
        elif continent == "" :
            for i in self._cDictionary:
                countryListbyArea.append((i, float(self._countryCat[i].getArea())))
            return sorted(countryListbyArea,key=lambda x : x[1], reverse = True)
        else:
            return countryListbyArea
    def findMostPopulousContinent(self) :
        continentWithMostPop = {}
        for i in self._cDictionary :
            continentWithMostPop[self._cDictionary[i]] = [float(self._countryCat[i].getPopulation())]
        return (list(continentWithMostPop.keys())[list(continentWithMostPop.values()).index(max(continentWithMostPop.values()))],max(continentWithMostPop.values()))
    def filterCountriesByPopDensity(self, lowerBound, upperBound) :
       countryListbyPopDensity = []
       for i in self._countryCat:
            if lowerBound <= self._countryCat[i].getPopulationDensity() <= upperBound :
                countryListbyPopDensity.append((i, round(self._countryCat[i].getPopulationDensity(), 2)))
       return sorted(countryListbyPopDensity, key=lambda x : x[1], reverse = True)
    def saveCountryCatalogue(self, file) :
       catFile = open(file, "w") # writing, creating a new Catalogue file
       listFile = []
       for i in self._cDictionary:
            strRepr = str(self._countryCat[i].getName())+"|"+str(self._countryCat[i].getContinent())+"|"+str(self._countryCat[i].getPopulation())+"|"+str(self._countryCat[i].getArea())+"|"+str(self._countryCat[i].getPopulationDensity())+"\n"
            listFile.append(strRepr)
       listFile = sorted(listFile)
       for i in listFile :
           catFile.write(i)
       catFile.close()
       tryFile = open(file)
       tryList = []
       for i in tryFile:
        tryList.append(i)
       if len(tryList) > 0 :
        return len(tryList)
       else:
        return -1
       tryFile.close()




