#FUNCTION ReverseList(LIST A OF LENGTH n)
#    SET left = 0
#    SET right = n - 1
#    WHILE left < right DO
#        SWAP A[left] WITH A[right]
#        INCREMENT left by 1
#        DECREMENT right by 1
#    END WHILE
#    RETURN A
#END FUNCTION

def ReverseList(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left  += 1
        right -= 1
    return array

array = list(range(9))
print(array)
print(ReverseList(array))