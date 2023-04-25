# example;
# surreal python
# 1 s, 1 u, 2 r, 1 e, 1 a, 1 l, 1 p, 1 y, 1 t, 1 h, 1 o, 1 n
# 112111111111
# add the ends of each side into a new number
# 223222
# 445
# 94
# give as percentage

def calc():  
    nameFirst = input("Enter first name: ")
    nameSecond = input("Enter second name: ")
    nameSum = nameFirst + nameSecond #returns 'nameFirstnameSecond' String
    val1 = []
    char_count = {}
    
    for i in nameSum:
        char_count[i] = nameSum.count(i) #assigns all char to an empty dict
    
    val = list(char_count.values()) #assigns the dict to a list

    for i in val:
        val1.append(val[0] + val[-1])
        val.pop(0)
        val.pop() #removes first and last values
    val2 = val1 + val
    val3 = []
    for i in val2:
        val3.append(val2[0] + val2[-1])
        val2.pop(0)
        val2.pop() #removes first and last values

    a = val3[0]
    b = val3[-1]
    print(F"Your love is {a}{b}%")
calc()

