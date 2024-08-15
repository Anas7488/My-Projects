import phonenumbers
from number import number 


from phonenumbers import geocoder
ch_name = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_name,"en"))

from phonenumbers import carrier
service_name = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_name,"en"))