# Matrices Multiplication Script

## How to use it?

It is necessary to enter the two matrices in the format \[\[1,2,3,...\], \[1,2,3,...\],...\]. After you enter the two matrices, it will display the result.

## Limitations and cababilities

This script is not capable of multiplaying single-element matrices due to the way it splits rows and columns. Additionally, the algorithm is implemented using nested for loops, so it is not optimazed for the CPU's SIMD unit for executing the multiplication. However, if you pass the string 'SIMD' as the last parameter to multex, it will be optimized for SIMD execution.