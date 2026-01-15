import numpy as np

#arrays for stacking

days = np.array(['Name','Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
me_steps = np.array(['Me', 4500, 5200, 4800, 5000, 5300])
lia_steps = np.array(['Lia', 4000, 4100, 3900, 4200, 4600])
jake_steps = np.array(['Jake', 6000, 5800, 5900, 6100, 6200])

#final two-dimensional array

friend_steps = np.array([days, me_steps, lia_steps, jake_steps])

#sum

print(f"My total steps: {np.sum(me_steps)}")
print(f"Lia's total steps: {np.sum(lia_steps)}")
print(f"Jake's total steps: {np.sum(jake_steps)}")

#person with highest total steps
total_me_steps = np.sum(me_steps)
total_lia_steps = np.sum(lia_steps)
total_jake_steps = np.sum(jake_steps)
lowest_steps = min(total_me_steps, total_lia_steps, total_jake_steps)
highest_steps = max(total_me_steps, total_lia_steps, total_jake_steps)
if highest_steps == total_me_steps:
    print("I have the highest total steps.")

elif highest_steps == total_lia_steps:
    print("Lia has the highest total steps.")

elif highest_steps == total_jake_steps:
    print("Jake has the highest total steps.")

#difference between highest and lowest steps
difference = highest_steps - lowest_steps
print(f"The difference between the highest and lowest total steps is: {difference}")
