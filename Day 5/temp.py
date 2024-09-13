def celsius_to_fahrenheit(temp_c):
    temp_f =  (temp_c*9/5)+32
    return  temp_f

def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f-32)*5/9
    return temp_c

def celcius_to_kelvin(temp_c):
    temp_k = temp_c + 273.15


try:
    temp = float(input("enter temperature : "))
    unit = input("Enter unit : ")
    unit_to_convert = input("enter unit to convert : ")


except ValueError:
    print("Not a numeric value !")

else:
    if unit == "fahrenheit":
        print(celsius_to_fahrenheit(temp))

    if unit == "kelvin":
        print(celcius_to_kelvin(temp))

finally:
    print("Conversion completed !")



