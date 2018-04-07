class booking():
    def __init__(self,period,pickUp,dropOff,insurance,name,licenceNum,age,email,booked_car):
        self.__period = period
        self.__costumerName = name
        self.__costumerLicence = licenceNum
        self.__costumerAge = age
        self.__costumerEmail = email
        self.__pickUpLocation = pickUp
        self.__dropOffLocation = dropOff
        self.__insurance = insurance
        self.__car = booked_car
        
        self.__price = (self.__car.getDailyFee())*self.__period
        if self.__car.getSize is 'Large':
            self.__price = self.__price * 1.05
            
        if self.__car.getSize is 'Premium':
            self.__price = self.__price * 1.2 
            
            
    def __str__(self):
        if self.__car.getCurrentStatus() != "Available":
            return "%s, not avaliable\n"%(self.__car.getCurrentStatus())
        else:
            return "Costumer name:%s\nPick up location:%s\nDrop off location:%s\nCar type:%s\nPeriod:%s days\nPrice:$%d\n"%(self.__costumerName,self.__pickUpLocation,self.__dropOffLocation,self.__car.getMakeAndModel(),self.__period,self.__price)

        
