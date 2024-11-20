import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from color import Color

def number():
    try:
        print(Color.CYAN + "Enter the mobile number with the country code \ne.g., +129876543210)" + Color.RESET)
        mobileNumber = input(Color.CYAN + "Enter Number: " + Color.RESET)
        
        # Parsing the phone number
        parsed_number = phonenumbers.parse(mobileNumber)

        if not phonenumbers.is_valid_number(parsed_number):
            print(Color.RED + "Invalid phone number." + Color.RESET)
            return
        
        # Displaying timezone information
        timezones = timezone.time_zones_for_number(parsed_number)
        print(Color.GREEN + "Timezones:", ", ".join(timezones), Color.RESET)
        
        # Displaying carrier information
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print(Color.GREEN + "Carrier:", carrier_name, Color.RESET)
        
        # Displaying geolocation information
        location = geocoder.description_for_number(parsed_number, "en")
        print(Color.GREEN + "Location:", location, Color.RESET)
        
        # Checking if the number is possible
        is_possible = phonenumbers.is_possible_number(parsed_number)
        print(Color.GREEN + "Number is possible:", is_possible, Color.RESET)

        # Displaying formatted number
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        print(Color.GREEN + "Formatted Number:", formatted_number, Color.RESET)
        
        # Displaying number type
        number_type = phonenumbers.number_type(parsed_number)
        print(Color.GREEN + "Number Type:", number_type, Color.RESET)
        
    except KeyboardInterrupt:
        print(Color.RED + "Operation interrupted by the user. Exiting Phone Number Verifier..." + Color.RESET)
    

if __name__ == "__main__":
    number()
