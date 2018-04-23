from functools import reduce

"""
manual_exponent(2, 3) => 8
manual_exponent(10, 2) => 100
"""

"""
# Iterative approach
def manual_exponent(num, exp):
  counter = exp - 1
  total = num

  while counter > 0:
    total *= num
    counter -= 1

  return total
"""


print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

# Functional approach
def manual_exponent(num, exp):
  computed_list = [num] * exp 

  return(reduce(lambda total, element: total * element, computed_list))