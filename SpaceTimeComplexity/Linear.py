def Linear():
    arr = [1,2,3,4,5]
    for x in arr:
        print(x) # O(1) T.C | O(1) S.C 
    naya = arr.copy() # O(1) T.C | S.C O(n)
    for y in naya: # O(n) T.C | S.C O(1)
        naya[y] == arr[y]

Linear()

# overall SC
# S.C => 1 + n + 1 => 2 + n => n
# T.C => 1 + 1 + n => 2 + n => n

# ST Complexity => O(n)