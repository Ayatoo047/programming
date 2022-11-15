from random import randint

# binary converter
def binaryconverter():
    binarylist = [randint(0,1) for number in range(4)]
    binarynumber = "".join([str(i) for i in binarylist])
    print(f'The binary number is {binarynumber}')
    base10 = int(binarynumber, 2)
    return (f'The binary number in base ten is {base10}')


# print(binaryconverter())


#----------------------------------------------------------------------------

## fibonacci

def fibonacci(n):
    a = 0
    b = 1
    flist = []

    if n < 0:
        print("invalid input")

    elif n == 0:
        return 0

    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c

            flist.append(c)
        return flist

# print(sum(fibonacci(50))) 

#----------------------------------------------------------------------------

## SHIRT COLOUR
monday = 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'
tuesday = 'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLUE, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE'
wednessday = 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE'
thursday = 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'
friday = 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'

mondaylist = monday.split(', ')
tuesdaylist = tuesday.split(', ')
wednessdaylist = wednessday.split(', ')
thursdaylist = thursday.split(', ')
fridaylist = friday.split(', ')

total_day = mondaylist + tuesdaylist + wednessdaylist + thursdaylist + fridaylist

#----------------------------------------------------------------------------

# getting the median colour
def getMedian(days):
    return (f'The Median colour is {days[round(len(days)/2)]}')
# print(getMedian(total_day))

#----------------------------------------------------------------------------

# get the most worn

def getMostWorn(days):
    return (f'The Most worn colour is {(max(days,key=days.count))}')

# print(getMostWorn(total_day))

#----------------------------------------------------------------------------

def getMean(days):
    b = {}
    for item in days:
        b[item] = b.get(item, 0) + 1

    mean = len(days) / len(b)
    return (f'The Mean colour is {days[round(mean)]}')
# print(getMean(total_day))