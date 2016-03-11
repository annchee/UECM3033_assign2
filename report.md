UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** Ng Ann Chee**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/annchee/UECM3033_assign1]

Explain your selection criteria here.
Check matrix A is strictly diagonally dominant Matrix. If the result is true, then solve by LU. 
If the result is false, then check whether matrix A is positive definite element. If the result is true, then solve by SOR.

Explain how you implement your `task1.py` here.
The matrix A is strictly diagonally dominant matrix, when the diagonal element is greater than sum of row. If Matrix A is strictly diagonally matrix, 
then solve it by LU. If Not, then check for positive definite element. If the all the elements is positive definite, then solve it by SOR.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (tohoshinki.jpg)

![tohoshinki.jpg](tohoshinki.jpg)

How many non zero element in $\Sigma$?
For image size $M\times N$,$(N\times M-N)$ is the number of zeros in $\Sigma$.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.
The image with the lower resolution
![Tohoshinki_lower.jpg](Tohoshinki_lower.jpg)
The image with the better resolution
![Tohoshinki_better.jpg](Tohoshinki_better.jpg)
Calculate new $\Sigma_i$ with $i$ number of eigenvector, 30 and 200 for lower and better resolution respectively. These two images obtain by using U$\Sigma_i$
V for each of the color layer. Thus, combine together and become an image in RGB format.
What is a sparse matrix?
The sparse matrix is a matrix in which most of the elements are zero.$\Sigma_i$ is the example 
of sparse matrix which contain only $n$ non-zero element out of $M\timeN$ element.
-----------------------------------

<sup>last modified: 11/3/16</sup>
