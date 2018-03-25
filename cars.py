from ABC import ABC, abstractfunction

class Car:
	def __init__(self, dailyFee currentStatus, type, makeAndModel, registrationDetails):
		self.__dailyFee = dailyFee
		self.__currentStatus = currentStatus
		self.__type = type
		self.__makeAndModel = makeAndModel
		self.__registrationDetails = registrationDetails

	def setDailyFee(self, dailyFee):
		if(dailyFee > 0):
			self.__dailyFee = dailyFee
		else:
			raise Exception('A daily fee can not be negative.')

	def getDailyFee(self):
		return self__dailyFee

	def setCurrentStatus(self, currentStatus):
		if currentStatus in ['available', 'booked', 'in repair']:
			self.__currentStatus = currentStatus
		else:
			raise Exception('A car\'s status can only be available, booked, or in repair')

	def getCurrentStatus(self):
		return self.__currentStatus

	def setType(self, type):
		if type in ['small', 'medium', 'large', 'premium']:
			self.__type = type
		else:
			raise Exception('A car\'s type can only be small, medium, large, or premium')

	def getType(self):
		return self.__type

	def setMakeAndModel(self, makeAndModel):
		self.__makeAndModel = makeAndModel

	def getMakeAndModel(self):
		return self.__makeAndModel

