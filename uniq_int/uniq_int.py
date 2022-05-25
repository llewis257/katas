# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

tests = [[0, 1, 1, 1, 1, 1, 1, 1], [8, 8, 8, 8, 8, 8, 8, 7], [5, 5, 5, 5, 4, 5, 5, 5], [3, 10, 3, 3, 3]]
def find_uniq(arr):
    # your code here
    n = None # unique integer
    temp= None
    count = 0
    for i in range(len(arr)):
        if count < 2:
            if arr[i] != n:
                count +=1
                n = arr[i]
        else:
            return n
                
    return n

for j in tests:
    print(find_uniq(j))