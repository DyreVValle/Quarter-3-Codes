import numpy as np

tokyo_kyoto_temperature = np.array([
    ['Name','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    ['Tokyo',22, 21, 23, 24, 26, 25, 27],
    ['Kyoto',20, 19, 21, 22, 23, 24, 22]
    ])

data = tokyo_kyoto_temperature[1:, 1:].astype(float)
averages = data.mean(axis=1)

print("Tokyo and Kyoto Temperatures:")
for name, avg in zip(tokyo_kyoto_temperature[1:, 0], averages):
    print(f"  {name} average = {avg:.2f}°C")