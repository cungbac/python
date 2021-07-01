# BASIS OF A VECTOR SPACE

## 1. Definition
S = {$e_1$, $e_2$, ..., $e_n$} is a basis of vector space V if:

* S is linear dependence and
* Every element (x) of V may be written in a unique way as finite linear combination of elements of S

## *x = $\lambda_1e_1$ + $\lambda_2e_2$ + ... + $\lambda_ne_n$*

* Dimension of V (dim V) = n = number of elements of S

<u>*Note:*</u>
* V may have many different basis
* If V = {$\varnothing$} $\Rightarrow$ V has no basis and dim V = 0

## 2. Canonical basis (standard basis)
### a.  $R^3$ = {(a,b,c)} 
$\Rightarrow$ (a,b,c) = a(1,0,0) + b(0,1,0) + c(0,0,1) <br>
$\Rightarrow \forall$ vectors of $R^3$ are able to written as linear combination of elements of: <br>
 S = {(1,0,0),(0,1,0),(0,0,1)} <br>

  det $\begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{vmatrix}$ = 1 $\ne$ 0 <br> 

$\Rightarrow$ S is the canonical basis of $R^3$, dim $R^3$ = 3 <br>
$\Rightarrow$ dim $R^n$ = n <br> <br>

### b. $M_{2x2}$ = $\begin{Bmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \end{Bmatrix}$

$\Rightarrow$ 
$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ = 
    a$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ + 
    b$\begin{pmatrix}0 & 1 \\ 0 & 0 \end{pmatrix}$ + 
    c$\begin{pmatrix}0 & 0 \\ 1 & 0 \end{pmatrix}$ + 
    d$\begin{pmatrix}0 & 0 \\ 0 & 1 \end{pmatrix}$ <br>

$\Rightarrow$ $\forall$ matrix $\in M_{2x2}$ are able to written as linear combination of elements of: <br>

S = 
$\begin{Bmatrix} 
    \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix},
    \begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix},
    \begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix},
    \begin{pmatrix}0 & 0 \\ 0 & 1\end{pmatrix}
\end{Bmatrix}$ <br>

$\Rightarrow$ S is the canonical basis of $M_{2x2}$ , dim $M_{2x2}$ = 4 <br>
$\Rightarrow$ dim $M_{mxn}$ = m x n <br> <br>

### c. $P_2$ = {$a + bx + c$}
$\Rightarrow$ $a + bx + c$ = $a.1 + b.x + c.x^2$ <br>
$\Rightarrow$ $\forall$ polynomials in $P_2$ are able to written as linear combination of elements of: <br>

S = {$1,x,x^2$} and <br>

det
    $\begin{vmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{vmatrix}$ = 1 <br>

$\Rightarrow$ S is the canonical basis of $P_2$, dim $P_2$ = 3 <br>
$\Rightarrow$ dim $P_n$ = $n + 1$


