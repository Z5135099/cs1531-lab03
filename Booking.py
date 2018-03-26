class booking():
    def __init__(self,period,pickUp,dropOff,insurance,name,licenceNum,age,email,car):
        self.__period = period
        self.__costumerName = name
        self.__costumerLicence = licenceNum
        self.__costumerAge = age
        self.__costumerEmail = email
        self.__pickUpLocation = pickUp
        self.__dropOffLocation = dropOff
        self.__insurance = insurance
        self.__car = car
        
    def calculation(self):
        
        self.__price = (self.__car.getDailyFee())*self.__period
        if car.type == 'large':
            self.__price = self.__price * 1.05
            
        if car.type == 'premium':
            self.__price = self.__price * 1.2
        return self.__price    
            
    def __str__(self):
        return "Costumer name:%s\nPick up location:%s\nDrop off location:%s\n
        Car type:%s\nPeriod:%s\nPrice:%f\n%(self.__name)(self.__pickUpLocation)
        (self.__dropOffLocation)(self.__car.getType())(self.__period)
        (self.__price)"
        
