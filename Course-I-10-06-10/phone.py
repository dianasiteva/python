import phonenumbers
from phonenumbers import geocoder, carrier

phone_number_str = '+359888222888'

phone_number = phonenumbers.parse(phone_number_str)

if phonenumbers.is_valid_number(phone_number):
    print('Valid phone number!')

    location = geocoder.description_for_number(phone_number, lang='en')
    print(f'Location: {location}')

    service_provider = carrier.name_for_number(phone_number, lang='en')
    print(f'Carrier: {service_provider}')

else:
    print('Invalid phone number!')
