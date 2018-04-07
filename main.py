from cars import SmallCar, MediumCar, LargeCar, PremiumCar
from Booking import booking

cars = []

cars.append(SmallCar(50, 'Available', 'Toyota Prius', 'TP4-428','Small'))
cars.append(MediumCar(60, 'Available', 'Mazda 3', 'M32-498','Medium'))
cars.append(LargeCar(100, 'Booked', 'Range Rover', 'RR2-450','Large'))
cars.append(PremiumCar(200, 'Available', 'Mercedes Benz', 'MB4-433','Premium'))
cars.append(SmallCar(50, 'Available', 'Smart Car', 'SC4-395','Small'))
cars.append(MediumCar(60, 'In repair', 'Ford Focus', 'FF4-498','Medium'))
cars.append(LargeCar(100, 'Available', 'Semi Trailer', 'ST4-594','Large'))
cars.append(PremiumCar(200, 'Available', 'Veyron', 'V49-348','Premium'))
print('We have the following cars available:')
for car in cars:
	print(cars.index(car), end=': ')
	print('A {} for ${} with registration number {}'.format(car.getMakeAndModel(), car.getDailyFee(), car.getRegistration()))
for car in cars:
	book = booking(period=3,pickUp='UNSW',dropOff='Central station',insurance='Yes',name='Andrew',licenceNum='123456',age=18,email='AndrewZhang@outlook.com',booked_car=car)

	print(book)
