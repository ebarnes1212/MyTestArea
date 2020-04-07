import converters as c

s1 = c.ScaleConverter('inches', 'mm', 25)
print(s1.description())

print('converting 2 inches')
print(str(s1.convert(2)) + s1.units_to)