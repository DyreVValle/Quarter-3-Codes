import numpy as np

#arrays for stacking

days = np.array(['Name','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
tokyo_temp = np.array(['Tokyo',22, 21, 23, 24, 26, 25, 27])
kyoto_temp = np.array(['Kyoto',20, 19, 21, 22, 23, 24, 22])

#final two-dimensional array

city_temps = np.array([days, tokyo_temp, kyoto_temp])

# 1. ACCESS a specific value
print(f"Tokyo's temperature on Wednesday: {tokyo_temp[3]}°C")
print(f"Kyoto's temperature on Friday: {kyoto_temp[5]}°C")

# 2. UPDATE a specific value
tokyo_temp[2] = 20  # Change Tuesday temperature from 21 to 20
print(f"\nUpdated Tokyo Tuesday temp: {tokyo_temp[2]}°C")

# 3. SUMMARIZE the dataset
tokyo_temps_numeric = tokyo_temp[1:].astype(float)
kyoto_temps_numeric = kyoto_temp[1:].astype(float)
print(f"\nTokyo - Avg: {np.mean(tokyo_temps_numeric):.1f}°C, Max: {np.max(tokyo_temps_numeric):.0f}°C, Min: {np.min(tokyo_temps_numeric):.0f}°C")
print(f"Kyoto - Avg: {np.mean(kyoto_temps_numeric):.1f}°C, Max: {np.max(kyoto_temps_numeric):.0f}°C, Min: {np.min(kyoto_temps_numeric):.0f}°C")

