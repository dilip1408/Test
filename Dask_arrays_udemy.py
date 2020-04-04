# import os
# os.environ["PATH"] += os.pathsep + 'C:/Users/dvoruga/Downloads/graphviz-2.38/release/bin'
#
# import numpy as np
# import dask
# import dask.array as da
#
# np_arr = np.random.randint(20,size=10)
# print(np_arr)
# print(type(np_arr))
# #
# dask_arr = da.random.randint(20,size=22,chunks=5)
# print(dask_arr)
# print(dask_arr.compute())
#
# print(dask_arr.chunks)
#
# dask_arr_np_array = da.from_array(np_arr,chunks=5)
# print(dask_arr_np_array)
#
# dask_arr_np_array.sum().visualize(filename='C:/Users/dvoruga/Documents/Python_scripts/dask_graph_sample.jpeg')


#
# print(dask_arr_np_array.sum().compute()) #This changes bcoz original array s developed using random numbers.
#
# da_size = da.random.randint(10, size=(5,10)) #In size parameter, first element is no. of arrays and second element is no. of elements in an array.
# print(da_size.compute())
# import time
# t1 = time.process_time()
# da_large_arr = da.random.randint(1000,size=(5000,5000),chunks=(500,100)) # we can see the size of the array with the 'nbytes' and we can notice that the array size is greater than the RAM memory but it can be computed without any issue. By default dask arrays can be computed in parallel. But when we try printing the array directly then it will hang the system bcoz for computation the array sizes can be more than RAM but for printing all of the memory is utilized- It should be bcoz after computation result should be less than of RAM. If the o/p after the computation is more than RAM then do not compute and use the array directly into another computation. This is kind of generator concept - Lazy evaluation.
# print(da_large_arr.nbytes)
# print("In GB---",da_large_arr.nbytes/1e+9)
# da_large_arr_sum = da_large_arr.sum()
#
# print(da_large_arr_sum.compute())
# print(time.process_time()-t1)
#
# #more exercises by dask.array
# #scalar operations
# my_arr = da.random.randint(10,size=20,chunks=3)
# print(my_arr.compute())
# my_hundred_array = my_arr + 100 #This is a scalar operation - Adding 100 to each element of an array, even numpy supports this scalar operations.
# print(my_hundred_array.compute())
#
# print((my_arr*(-1)).compute()) #sone more scalar operation similar to numpy
#
# dask_sum= my_arr.sum()
# print(dask_sum)
# print(dask_sum.compute())
#
# my_ones_arr = da.ones((10,10),chunks=2, dtype=int)
# print(my_ones_arr.compute())
#
# my_custom_array = da.random.randint(10, size=(4,4),chunks=(1,4),dtype=int)
# print(my_custom_array.compute())
# print(my_custom_array.mean(axis=0).compute())
# print(my_custom_array.mean(axis=1).compute())
#
# #slicing
# print(my_custom_array[1:3,2:4].compute())
#
# #Dask arrays also support broadcasting- search for broadcasting in numpy. it s simple .
# print("This is my_custom_array",my_custom_array.compute())
#
# my_small_arr = da.ones(4,chunks=2)
# brd_example1 = da.add(my_custom_array,my_small_arr) # adding each element of both the axis. check after execution
# print("Broadcast example 1 by adding my_small_arr",brd_example1.compute())
# ten_arr = da.full_like(my_small_arr,10)#Similar to numpy.full_like. Takes original array and replaces with each element in the array with the element which we specify. in this case, it is 10.
# print("Ten_array",ten_arr.compute())
#
# brd_example2= da.add(my_custom_array,ten_arr)
# print("Broadcast example 2 array with my_custom_array and ten_arr \n",brd_example2.compute())
#
# #Dask also supports reshaping.
# custom_arr_id = my_custom_array.reshape(16)
# print(custom_arr_id)
# print(custom_arr_id.compute())
#
# #Dask supports stacking
# stacked_arr =da.stack([brd_example1,brd_example2])
# print("Stacked array with brd_example1,brd_example2\n",stacked_arr.compute())
#
# another_stacked = da.stack([brd_example1,brd_example2],axis=1)
# print("Stacked array with brd_example1,brd_example2\n",another_stacked)
#
# #Concatenate
# concate_arr = da.concatenate([brd_example1,brd_example2])
# print(concate_arr.compute())
#
# another_concate_arr = da.concatenate([brd_example1,brd_example2], axis=1)
# print(another_concate_arr.compute())
#


#Performance comparision with NumPy Arrays

# import numpy as np
# import dask.array as da
# import timeit as time
#
# size_tuple = (1800,1800)
# np_arr = np.random.randint(10, size=size_tuple)
# np_arr2 = np.random.randint(10, size=size_tuple)
#
# #Lets perform a complex random operation over these arrays
# # print(%time(((np_arr*2).T)*2+np_arr2+100).sum(axis=1).mean()) #%time is not working so not worked on performance things much.

# Creating universal NumPy functions with Dask. #This inlcudes more complex codes includes scipy.. So skipped it.

import numpy as np
import dask.array as da

# size_tuple =(500,500)
# chunks_tuple = (10,500)
# da_arr = da.random.randint(10,size=size_tuple,chunks=chunks_tuple)
# da_arr2 = da.random.randint(10,size=size_tuple,chunks=chunks_tuple)
# def random_func(x):
#     return np.mean((((x *2 ).T)**2),axis=0)
#
#
