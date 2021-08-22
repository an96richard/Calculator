#Richard An
#Calculator in Python
#=======================
#GOALS
#1. Create a program that can perform basic arithmetic DONE
#2. Create Functional GUI for users
#3. Build Functions to tackle complex expressions e.g parenthesis, PEMDAS, etc.
#
#======================
from decimal import Decimal
numberArr1 = []
numberArr2 = []
symbolArr = []
def add_function(x,y):
    return x + y

def sub_function(x,y):
    return x-y

def multi_function(x,y):
    return x*y

def divide_function(x,y):
    if(y == 0):
        return "ERROR"
    else:
        return x/y


#Function to evaluate an expression, where arr1 and arr2 are arrays that contain the numbers in the expression.
#Using Recursion we can evaluate each expression appropriately.
#CURRENTLY DOES LEFT TO RIGHT ARITHMETIC
def expresssionEval(arr1,arr2):
    i = len(arr1)
    j = len(symbolArr)
    sum = arr2[i-1];
    while True:
        if(i == 1):
            if symbolArr[j-1] == "+":
                return Decimal(arr1[0]) + Decimal(arr2[0])
            elif symbolArr[j-1] == "-":
                return Decimal(arr1[0]) - Decimal(arr2[0])
            elif symbolArr[j-1] == "*":
                return Decimal(arr1[0]) * Decimal(arr2[0])
            elif symbolArr[j-1] == "/":
                return Decimal(arr1[0]) / Decimal(arr2[0])
        else:
            arr1.pop(i-1)
            arr2.pop(i-1)

            if symbolArr[j-1] == "+":
                symbolArr.pop(j-1)
                return Decimal(sum) + Decimal(expresssionEval(arr1, arr2))
            elif symbolArr[j-1] == "-":
                symbolArr.pop(j-1)
                return Decimal(expresssionEval(arr1, arr2)) - Decimal(sum)
            elif symbolArr[j-1] == "*":
                symbolArr.pop(j-1)
                return Decimal(sum) * Decimal(expresssionEval(arr1, arr2))
            elif symbolArr[j-1] == "/":
                symbolArr.pop(j-1)
                if(sum == "0"):
                    return print("Sorry You Cannot Divide by 0")
                return Decimal(expresssionEval(arr1, arr2)) / Decimal(sum)


#Main Method will first parse the string and separate each number and operator into separate arrays. This will allow for simple manipulation of the expression and help do order of operations later.
# Then it will call the expressionEval function to evaluate the expression.
def main():
    input_expression = input("Enter Your Expression: ")
    i = 0
    isSameNumber = True
    alreadyFoundSymbol = False
    newString = ""
    while i <= len(input_expression):
        if(i == len(input_expression)):
            numberArr1.append(newString)
            numberArr2.append(newString)
            symbolArr.append("+")
            numberArr2.append("0")
            i+=1
        elif(input_expression[i] == '+' or input_expression[i] == '-' or input_expression[i] == '*' or input_expression[i] == '/' ):
            if(alreadyFoundSymbol == False):
                if(not numberArr1):
                    numberArr1.append(newString)
                    newString = ""
                else:
                    numberArr1.append(newString)
                    numberArr2.append(newString)
                    newString = ""
                symbolArr.append(input_expression[i])
                isSameNumber = False
                alreadyFoundSymbol = True
                i+= 1
            else:
                return print("Sorry This Is Not A Valid Expression (Too Many Operations Next To Each Other!)")
        else:
            if(input_expression[i].isdigit() and isSameNumber == True):
                newString = newString + input_expression[i]
                i+=1
            elif input_expression[i].isdigit() and isSameNumber == False:
                newString = newString + input_expression[i]
                isSameNumber = True
                alreadyFoundSymbol = False
                i+=1
            else:
                return print("Sorry That Is Not A Valid Expression (A Value In Your Expression Is Not A Digit nor an Operator)")
    print(numberArr1)
    print(symbolArr)
    print(numberArr2)
    print(expresssionEval(numberArr1, numberArr2))



main()
