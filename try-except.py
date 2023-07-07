# prompt for input and turn fahrenheit into celsius 

inp = input('Please enter Fahrenheit Temp:')
try:
    fahr = float(inp)
    cel= (fahr -32.0)* 5/9
    print ('That would be', cel,'Celsius')
except:
    print ('Opps that\'s not a number, please try again.')
print (5/9)