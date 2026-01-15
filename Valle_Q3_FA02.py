import numpy as np

#arrays for stacking

days = np.array(['Name','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
tokyo_temp = np.array(['Tokyo',22, 21, 23, 24, 26, 25, 27])
kyoto_temp = np.array(['Kyoto',20, 19, 21, 22, 23, 24, 22])

#final two-dimensional array

city_temps = np.array([days, tokyo_temp, kyoto_temp])

#access
print(f"Tokyo's temperature on Wednesday: {tokyo_temp[3]}°C")
print(f"Kyoto's temperature on Friday: {kyoto_temp[5]}°C")
