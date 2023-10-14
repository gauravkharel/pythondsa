# def Loga(): # Linear solution
#     arr = [1, 3, 13, 23, 34, 43, 54]
#     for x in arr: # T.C O(n)
#         if x == 13:
#             print("Found 13 at index")
# Loga()


def newLoga():
    arr = [1, 2, 12, 32, 43, 56, 65, 72]
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (start + end) / 2 
        if(arr[mid] == 43):
            print("found whatever it was: " + mid)
            break
        elif(arr[mid] < 43):
            start = mid + 1   
            print("hello")
        else:
            end = mid - 1
            print("wow")

newLoga()