# bounce.py
#
# Exercise 1.5

drop_height = 100
heights_after_bounce = []
for i in range(10):
    drop_height *= 0.6
    heights_after_bounce.append(round(drop_height, ndigits = 2))

for i, height in enumerate(heights_after_bounce):
    print(i, height)
