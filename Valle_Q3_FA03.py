import numpy as np

#arrays for stacking

days = np.array(['Name','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
tokyo_temp = np.array(['Tokyo','22°C', '21°C', '23°C', '24°C', '26°C', '25°C', '27°C'])
kyoto_temp = np.array(['Kyoto','20°C', '19°C', '21°C', '22°C', '23°C', '24°C', '22°C'])

#final two-dimensional array

city_temps = np.array([days, tokyo_temp, kyoto_temp])

#sum

print(f"Tokyo's total temperature: {np.sum(tokyo_temp)}")
print(f"Kyoto's total temperature: {np.sum(kyoto_temp)}")

#average
print(f"Tokyo's average temperature: {np.mean(tokyo_temp)}")
print(f"Kyoto's average temperature: {np.mean(kyoto_temp)}")
