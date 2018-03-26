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
        if self.__car.getCurrentStatus() is 'available':
            self.__price = (self.__car.getDailyFee())*self.__period
            if self.__car.getSize is 'large':
                self.__price = self.__price * 1.05
                
            if self.__car.getType is 'premium':
                self.__price = self.__price * 1.2 
        else:
            return 'Unavaliable car'
            
            
    def __str__(self):
        return "Costumer name:%s\nPick up location:%s\nDrop off location:%s\nCar type:%s\nPeriod:%s\nPrice:%f\n"%(self.__name)(self.__pickUpLocation)(self.__dropOffLocation)(self.__car.getType())(self.__period)(self.__price)
        