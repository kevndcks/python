import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)

from math import pi

print(pi)

from math import pi, sqrt

# import some_module # results in ImportError as module isn't available

from math import sqrt as square_root
print(square_root(100))