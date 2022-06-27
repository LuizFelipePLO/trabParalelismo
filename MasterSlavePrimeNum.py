from mpi4py import MPI 
import numpy 
import math
import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()
def master():
    for i in range(1,size):
    start_time = time.perf_counter_ns()
        number = numpy.random.randint(10000)
        comm.send(obj=number,dest=i)
    for i in range(1,size):
        result = comm.recv(source = MPI.ANY_SOURCE)
        print(result)
    end_time = time.perf_counter_ns()
    print("Process time: ", end_time - start_time, "nanoseconds")
def slave():
    for i in range(1,size):
        number = comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
        isPrime = ""    
        if(number<=1):    
            isPrime = str(number) +  "nao e primo"
        for i in range(2,(int(math.sqrt(number))+1)):
            if(number%i==0):
                isPrime = str(number) +  " nao e primo" 
                break;
                isPrime = str(number) +  " e primo"  
            else:

        comm.send(obj=isPrime,dest=0)    
if rank==0:
    master()

else:
    slave()






    


