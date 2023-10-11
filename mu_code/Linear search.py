# Write your code here :-)
import multiprocessing
import Pool

def linearSearchParallel(lst, item, numProcesses):
    pool = multiprocessing.Pool(numProcesses)
    chunkSize = len(lst) // numProcesses
    chunks =   [lst[i:i+chunkSize] for i in range( 0, len(lst), chunkSize)]
    results = pool.starmap(linearSearchChunk, [(chunk, item) for chunk in chunks])
    pool.close()
    pool.join()
    return any(results)


l = list(range(10000000))
print(linearSearchParallel(l, 1, 2))
print(linearSearchParallel(l, 20, 2))
print(linearSearchParallel(l, 500, 2))
print(linearSearchParallel(l, 1000, 2))
print(linearSearchParallel(l, 50000, 2))
print(linearSearchParallel(l, 100000, 2))
print(linearSearchParallel(l, 2000000, 2))

