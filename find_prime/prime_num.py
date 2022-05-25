# Define a function that takes one integer argument and returns logical 
# value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater 
# than 1 that has no positive divisors other 
# than 1 and itself.
# Requirements

#     You can assume you will be given an integer input.
#     You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
#     NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.

# Example

# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
def is_prime(num):
  lis_range = []
  i = 0
  while(i < abs(num)):
    i += 1
    lis_range.append(i)
  recursive_pop(2,1, num, lis_range)


def recursive_pop(j,k, num, lis_range):
  if len(lis_range) > 2:
    prod = j*k
    while (prod <= abs(num) and len(lis_range)>2):
      if prod in lis_range:
        lis_range.pop(prod) 
        print(f'deleted {prod} multiple of {j}')
        k +=1
        prod = j*k
      else:
        pass
     

    else:
      if len(lis_range) == 1:
        return False
      elif len(lis_range) == 2:
        return True
      else:
        j +=1
        k = 1
      recursive_pop(j,k, num, lis_range)
  elif len(lis_range) == 1:
    return False
  elif len(lis_range) == 2:
    return True
  else:
    print(lis_range)


  



if __name__ == "__main__":
  print(is_prime(-1))
  print(is_prime(2))
  print(is_prime(19))
  print(is_prime(-31))
  print(is_prime(19863))
