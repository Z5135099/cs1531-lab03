from cars import SmallCar, MediumCar, LargeCar, PremiumCar
from Booking import booking

cars = []

cars.append(SmallCar('50', 'available', 'Toyota Prius', 'TP4-428'))
cars.append(MediumCar('60', 'available', 'Mazda 3', 'M32-498'))
cars.append(LargeCar('100', 'booked', 'Range Rover', 'RR2-450'))
cars.append(PremiumCar('200', 'available', 'Mercedes Benz', 'MB4-433'))
cars.append(SmallCar('50', 'available', 'Smart Car', 'SC4-395'))
cars.append(MediumCar('60', 'in repair', 'Ford Focus', 'FF4-498'))
cars.append(LargeCar('100', 'available', 'Semi Trailer', 'ST4-594'))
cars.append(PremiumCar('200', 'available', 'Veyron', 'V49-348'))
print('We have the following cars available:')
for car in cars:
	print(cars.index(car), end=': ')
	print('A {} for ${} with registration number {}'.format(car.getMakeAndModel(), car.getDailyFee(), car.getRegistration()))








