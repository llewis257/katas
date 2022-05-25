# import math
# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     return -1 if (math.modf(math.sqrt(sq))[0] != 0) else (math.sqrt(sq) + 1)**2

    ## best solution
def find_next_square(sq):
    return -1 if (sq**0.5)%1 else ((sq**0.5)+1)**2

print(find_next_square(145))


