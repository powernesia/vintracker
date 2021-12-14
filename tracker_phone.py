import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number=input("Masukin No Nya Dengan +62___ : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone, "in")
reg=geocoder.description_for_number(phone, "in")
print(phone)
print(time)
print(car)
print(reg)