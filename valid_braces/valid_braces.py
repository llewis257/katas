def valid_braces(string):
    lis_str = list(string)
    #lis_str_2 = lis_str.copy()
    while lis_str != []:
        if '[' in lis_str:
            print(lis_str.pop(lis_str.index('[')))
            print(lis_str.pop(lis_str.index(']')))
            print(lis_str)
            valid_braces(''.join(lis_str))
        elif '(' in lis_str:
            print(lis_str.pop(lis_str.index('(')))
            print(lis_str.pop(lis_str.index(')')))
            print(lis_str)
            valid_braces(''.join(lis_str))
        elif '{' in lis_str:
            print(lis_str.pop(lis_str.index('{')))
            print(lis_str.pop(lis_str.index('}')))
            print(lis_str)
            valid_braces(''.join(lis_str))
        else:
            return False
        
    return True
        
    

print(valid_braces('}}}}'))