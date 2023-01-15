import sys
import re
from functools import reduce

#load data
data = []
file = open("input.txt")
for row in file:
    data.append(row.strip())

def part(RoundNumber, Divider):
        #parsing
        Items = []
        DivideTest = []
        TrueOutcome = []
        FalseOutcome = []
        Operations = []

        for row in data:
            if "Monkey" in row:
                continue

            elif "Starting" in row:
                Items.append(re.findall('\d+', row))

            elif "Operation" in row:
                temp = row.split()
                Operations.append([temp[-2], temp[-1]])

            elif "Test" in row:
                num = re.findall('\d+', row)
                for number in num:
                    DivideTest.append(int(number))

            elif "true" in row:
                num = re.findall('\d+', row)
                for number in num:
                    TrueOutcome.append(int(number))

            elif "false" in row:
                num = re.findall('\d+', row)
                for number in num:
                    FalseOutcome.append(int(number))
            
            elif row == '':
                pass
            
            else:
                print(row, 'error')
                break
        
        Inspections = [0] * len(Items)
        #round
        for _ in range(RoundNumber): #number of rounds
            count = 0
            result = bool
            for item in Items: #for each item
                for _ in range(len(item)):
                    CurrentItem = int(item[0]) #copy the value
                    Condition = reduce(lambda x, y: x * y, DivideTest)
                    if CurrentItem > Condition: #if its bigger then all the dividents u need to reduce it to its core numbers
                        CurrentItem = CurrentItem % Condition
                    Inspections[count] += 1
                    CurrentItem = (int(operation(CurrentItem, Operations[count]) / Divider)) #result of operation is divided by 3 and made a whole num
                    result = divisible(CurrentItem, DivideTest[count])
                    if result == True:
                        DesiredItemList = TrueOutcome[count]
                        Items[DesiredItemList].append(CurrentItem)
                    else:
                        DesiredItemList = FalseOutcome[count]
                        Items[DesiredItemList].append(CurrentItem)
                    del item[0]
                count += 1
        SortedInspections = sorted(Inspections, reverse= True)
        PartResult = SortedInspections[1] * SortedInspections[0]      
        return PartResult #, Inspections

def operation(arg, op): #returns new = old(op[0], op[1])
    symbol = op[0]
    num = op[1]

    if num == 'old':
        if symbol == '+':
            return arg + arg
        elif symbol == '-':
            return arg - arg
        elif symbol == '*':
            return arg * arg
        elif symbol == '/':
            return arg / arg
        else:
            print(op, "error")
            sys.exit()

    elif num.isdigit():
        num = int(num)
        if symbol == '+':
            return arg + num
        elif symbol == '-':
            return arg - num
        elif symbol == '*':
            return arg * num
        elif symbol == '/':
            return arg / num
        else:
            print(op, "error")
            sys.exit()
    else: 
        print(op, 'error')
        sys.exit()

def divisible(arg, num):
    if arg % num == 0:
        return True
    else: return False

def main():  
    print('Part1: ', part(20, 3))
    print('Part2: ', part(10000, 1))

if __name__ == '__main__':
    main()