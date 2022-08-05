import random
import os
import time

os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import numpy as np

def matmul(A, B, C):
  for i in range(N):
    for j in range(N):
      for k in range(N):
        mul = A[i][k] * B[k][j]
        C[i][j] = mul

def mprint(m):
  for row in m:
    print(row)

N = 256
#N = 2048
#N = 4096

A = np.random.randn(N, N).astype(np.float32)
B = np.random.randn(N, N).astype(np.float32)
C = np.zeros((N, N)).astype(np.float32)

start = time.monotonic()

# numpy method
C = A @ B

# my method
#matmul(A, B, C)

end = time.monotonic()

print(C)

print("time elapsed: ", end-start)
