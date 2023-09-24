# def echanger(arr,i,j):
#     arr[i],arr[j] = arr[j],arr[i]
    


# def selection_sort(arr):
#     size = len(arr)
#     type_sort = int(input('''Would you sort your array : 
#                       ASC ===> ENTER 1 
#                       DESC ===> ENTER 2 
#                       '''))
#     if type_sort == 1:
#         for i in range(size):
#             min_idx = i

#             for j in range(i+1, size):
#                 if arr[min_idx] > arr[j]:
#                     min_idx = j
#             # arr[i],arr[min_idx] = arr[min_idx],arr[i]
#             echanger(arr,i,min_idx)

#     elif type_sort == 2:
#         for i in range(size):
#             min_idx = i

#             for j in range(i+1, size):
#                 if arr[min_idx] < arr[j]:
#                     min_idx = j
#             echanger(arr,i,min_idx)
#     else:
#         return None
#     return arr


# # EXAMPLE
# a = [65,33,7,3,19]
# print('Sorted array is : {arr}'.format(arr=selection_sort(a)))




# #=====================================================
# #======================================================


# # Bubble sort 
# def buble_sort(arr):
#     size = len(arr)

#     for i in range(size):
#         swap = False
      
#         for j in range(0, size-i-1):
#             if arr[j] > arr[j+1]:
#                 echanger(arr,j,j+1)
#                 swap = True

#         if swap == False:
#             break

#     return arr

# print(buble_sort(a))



# #=============================================
# #=============================================
# ''' insertion sort '''
# def insertion_sort(arr):
#     size = len(arr)

#     for i in range(1,size):
#         key = arr[i]
#         j = i-1
#         while  j>=0 and key < arr[j] :
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# print(insertion_sort(a))
def echanger(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

# algorithms of sort 
def bubble_sort(L):
    size = len(L)
    for i in range(size):

        for j in range(i+1,size):
            if L[i] > L[j]:
                echanger(L,i,j)

def selection(L):
    size = len(L)
    for i in range(size):
        min_ = i 
        for j in range(i+1, size):
            if L[min_] > L[j]:
                min_ = j

        L[i],L[min_] = L[min_],L[i]

def insertionSort(array):
    size = len(array)
    for step in range(1, size):
        key = array[step]
        j = step - 1  # 0
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

  
       
arr = [16,2,8,0,7]
# bubble_sort(arr)
selection(arr)
print(arr)





