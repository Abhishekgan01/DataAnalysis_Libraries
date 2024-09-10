from scipy import constants

print(dir(constants))
print("kilo ",constants.kilo)
print("speed of sound ",constants.speed_of_sound)
print("speed of light ",constants.speed_of_light)

#metrics
print(constants.kilo)     #1000.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)

#binary
print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)

#temperature
print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556

#horsepower
print(constants.hp) 	    #745.6998715822701
print(constants.horsepower) #745.6998715822701