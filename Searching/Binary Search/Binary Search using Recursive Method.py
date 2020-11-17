# Python Program for Binary Search using Recursive Method
# By Prashant Agheda - https://github.com/prashant-agheda

def binarySearch(myarray, low, high, element):

    # Checking the Base Case
    if high >= low:
        mid = (high + low) // 2

        # If the Element is present at middle position
        if myarray[mid] == element:
            return mid

        # If (Element < mid) then it can only be present at LEFT side of Array
        elif myarray[mid] > element:
            return binarySearch(myarray, low, mid - 1, element)

        # Else the Element can obviously be present at RIGHT side of Array
        else:
            return binarySearch(myarray, mid + 1, high, element)

    # If Element is NOT present in Array
    else:
        return -1


# Array Declaration
myarray = [ 10, 20, -90, 200, 100, -76 ]
element = 100

# Function Call
highLength = len(myarray) - 1
answer = binarySearch(myarray, 0, highLength, element)

# Checking the Conditions
print("\nGiven Array = ", str(myarray))
print("\nElement to Search for = ", str(element))

if answer != -1:
    print("\n\tThe Element is present in Array at index", str(answer))
else:
    print("\n\tThe Element is NOT present in Array")
