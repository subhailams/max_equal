def update_max_equal_frequency(signalOne, signalTwo):
    max_equal_frequency = 0
    count = 0
    for i in range(len(signalOne)):
        if signalOne[i] == signalTwo[i]:
            if signalOne[i] > max_equal_frequency:
                max_equal_frequency = signalOne[i]
                count += 1
    return count

signalOne = [1,2,3,3,3,5,4]
signalTwo = [1,2,3,4,3,5,4]
print(update_max_equal_frequency(signalOne, signalTwo))
