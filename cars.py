class Car:
	def __init__(self, dailyFee, currentStatus, makeAndModel, registration):
		self.__dailyFee = dailyFee
		self.__currentStatus = currentStatus
		self.__makeAndModel = makeAndModel
		self.__registration = registration

	def setDailyFee(self, dailyFee):
		if(dailyFee > 0):
			self.__dailyFee = dailyFee
		else:
			raise Exception('A daily fee can not be negative.')

	def getDailyFee(self):
		return self.__dailyFee

	def setCurrentStatus(self, currentStatus):
		if currentStatus in ['available', 'booked', 'in repair']:
			self.__currentStatus = currentStatus
		else:
			raise Exception('A car\'s status can only be available, booked, or in repair')

	def getCurrentStatus(self):
		return self.__currentStatus

	def setMakeAndModel(self, makeAndModel):
		self.__makeAndModel = makeAndModel

	def getMakeAndModel(self):
		return self.__makeAndModel

	def getRegistration(self):
		return self.__registration

class SmallCar(Car):
	def __init__(self, dailyFee, currentStatus, makeAndModel, registrationDetails):
		super().__init__(dailyFee, currentStatus, makeAndModel, registrationDetails)
class MediumCar(Car):
	def __init__(self, dailyFee, currentStatus, makeAndModel, registrationDetails):
		super().__init__(dailyFee, currentStatus, makeAndModel, registrationDetails)
class LargeCar(Car):
	def __init__(self, dailyFee, currentStatus, makeAndModel, registrationDetails):
		super().__init__(dailyFee, currentStatus, makeAndModel, registrationDetails)
class PremiumCar(Car):
	def __init__(self, dailyFee, currentStatus, makeAndModel, registrationDetails):
		super().__init__(dailyFee, currentStatus, makeAndModel, registrationDetails)
