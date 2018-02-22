import numpy as np
import sys
import time

SIZE = 100000

print("### Size comparison of list and numpy array")
list_a = range(SIZE)
list_size = (sys.getsizeof(5)*len(list_a))
print("Size of list: ", list_size)

np_array = np.arange(SIZE)
np_array_size = (np_array.size * np_array.itemsize)
print("Size of np array: ", np_array_size)

print("### Computation comparison of list and numpy array")

list1 = range(SIZE)
list2 = range(SIZE)
start_time = time.time()
result = [(x,y) for x,y in zip(list1,list2)]
print("List: Time Diff: ",(time.time() - start_time)*1000)

st_time = time.time()
np1 = np.arange(SIZE)
np2 = np.arange(SIZE)
result = np1+np2
print("NP Array: Time Diff: ",(time.time()-st_time)*1000)