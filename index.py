import numpy as np
# Code is not working properly, there is something wrong with the mutex function.

# Check to see wether each line in the matrix has the same length:
def checkLen(composedList):
    firstCase = len(composedList[0])
    for list in composedList:
        if len(list) != firstCase: raise ValueError("Not equal length through out the matrix.")
    
    return False        

# Getting inputs:
def takeInput():
    while True:
        composedList = []
        try:
            strTempList = input("Enter the elements as [[1,2,3,4,],...]: ")
            strTempList = strTempList.strip()
            strTempList = strTempList.replace(" ", "")
            
            tempList = strTempList.split("],")

            for element in tempList:
                element = element.replace("[", "")
                element = element.replace("]", "")
                element = element.split(',')
                composedList.append(element)

            for outCounter in range(0, len(composedList)):
                for innerCounter in range(0, len(composedList[outCounter])):
                    composedList[outCounter][innerCounter] = int(composedList[outCounter][innerCounter])

            checkLen(composedList)

        except Exception as error:
            print(f'exception: {error.args} has occurred.')
            print("You must have entered an invalid type, try again please.")
            
        else:
            return composedList

# Here we caculate the result of the mutiplication:    
def multex(matrixOne, matrixTwo, mode = ''):
    # Checking if multiplication is possible, if not raise an exception:
    if len(matrixOne[0]) != len(matrixTwo): 
        raise ValueError("Number of columns from one different from number of rows from two.")

    resultMatrix = []

    # Using the SIMD processor's unit:
    if mode == 'SIMD':
        print('from simd...')
        resultMatrix = np.array(matrixOne) @ np.array(matrixTwo)
        return resultMatrix

    for i in range(0, len(matrixOne[0])):
        partialLine = []
        for j in range(0, len(matrixTwo)):
            sum = 0
            for k in range(0, len(matrixTwo)):
                sum += matrixOne[i][k] * matrixTwo[k][j]
            partialLine.append(sum)
        resultMatrix.append(partialLine)

    return resultMatrix
            


        
def main():
    print("Enter the first matrix: ")
    matrixOne = takeInput()
    print("Enter the second matrix: ")
    matrixTwo = takeInput()

    # call the funtion to mutiply the two matrixes:
    result = 0
    try:
        result = multex(matrixOne, matrixTwo)
    except Exception as error:
        print(f'Exception: {error.args} has occurred.')
    else:
        for item in result:
            print(f'{item}')


if __name__ == "__main__": main()