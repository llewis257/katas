'''You were given a string of integer temperature values. 
Create a function close_to_zero(t) and return the closest value to 0 or 0 if the string is empty. 
If two numbers are equally close to zero, return the positive integer.'''
def close_to_zero(t):
    min = 100000000 # insert a large number
    t_list = t.split()
    if t != '': # checking for empty strings
        print(t)
        for l in t_list:
            if abs(int(l)) < abs(min) :
                min = int(l)
            elif abs(int(l)) == abs(min):
                if int(l) != min:
                    min = abs(int(l))
                else:
                    min = int(l)
            elif int(l) == min:
                min = int(l)
    else:
        min = 0
    return min
    ## shortest solution
    #return min(map(int, t.split()), key=lambda t: (abs(t), -t), default=0)
if __name__ == "__main__":
    print(close_to_zero(''))
    print(close_to_zero('-1 50 -4 20 22 -7 0 10 -8'))
    print(close_to_zero('28 35 -21 17 38 -17'))
    print(close_to_zero('28 35 -21 38 -17'))