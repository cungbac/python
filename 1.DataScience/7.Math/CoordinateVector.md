# COORDINATE VECTORS

## 1. Definition
S = {$e_1,e_2,...,e_n$} is a basis of V <br>
$\Rightarrow$ vector x $\in$ V is written as linear combination of elements of S will be: <br>
### x = $\lambda_1e_1 + \lambda_2e_2 + \dots \lambda_ne_n \space(*)$ <br>
$\Rightarrow$ coordinate of x: <br>

$$
    \begin{bmatrix} x \end{bmatrix}_S = 
        \begin{pmatrix} 
            \lambda_1 \\
            \lambda_2 \\
            ... \\
            \lambda_n
        \end{pmatrix}
$$

<u>*Note*</u>
$\space (*) \Leftrightarrow 
    \begin{pmatrix}e_1 & e_2  & \dots & e_n \end{pmatrix}
    \begin{pmatrix}
        \lambda_1 \\
        \lambda_2 \\
        ... \\
        \lambda_n 
    \end{pmatrix}$ = x <br>

$\begin{pmatrix}e_1 & e_2 & \dots & e_n\end{pmatrix}$ is the coordinate matrix of S <br>
$\Rightarrow$ the augmented matrix:
$\left[
    \begin{matrix}
    S
    \end{matrix}
    \left|
        \,
    \begin{matrix}
    x
    \end{matrix}
    \right.
\right]$

<u>Exp 1:</u> <br>
a. Find coordinate of vector: <br>
$x = 3 + x^2$ relative to S = $\begin{Bmatrix} 1 + x + x^2, 1 + x, 1 - 2x \end{Bmatrix}$ <br>
we have:
$$[x]_S \Leftrightarrow 
\left(
    \begin{matrix}
    1 & 1 & 1 \\
    1 & 1 & -2 \\
    1 & 0 & 0
    \end{matrix}
    \left |
    \,
    \,
    \begin{matrix}
    3 \\
    0 \\
    1
    \end{matrix}
    \right.
    \right)$$ 

<!-- $\left( \left |\right. \right)$ -->

$$ \Leftrightarrow
\begin{cases} 
    \lambda_1 = 1 \\ 
    \lambda_2 = 1 \\
    \lambda_3 = 1
\end{cases}
\,
\,
\Rightarrow [x]_S = \begin{pmatrix}1 \\ 1 \\1 \end{pmatrix}$$ 

b. Find the coordinate of matrix: $M = \begin{pmatrix}2 & 4 \\ 0 & 3 \end{pmatrix}$ 
relative to:
$S = 
\begin{Bmatrix}
    \begin{pmatrix}
        1 & 1\\
        1 & 1
    \end{pmatrix}
    \,
    ,
    \,
    \begin{pmatrix}
        0 & 1 \\
        -1 & 1
    \end{pmatrix}
    \,
    ,
    \,
    \begin{pmatrix}
        1 & 1 \\
        0 & 0
    \end{pmatrix}
    \,
    ,
    \,
    \begin{pmatrix}
        0 & 1 \\
        0 & 1
    \end{pmatrix}
\end{Bmatrix}
$

We have:
$$[M]_S \Leftrightarrow 
\left(
    \begin{matrix}
    1 & 0 & 1 & 0 \\
    1 & 1 & 1 & 1 \\
    1 & -1 & 0 & 0 \\
    1 & 1 & 0 & 1
    \end{matrix}
\left |
\,
\,
    \begin{matrix}
        2 \\
        4 \\
        0 \\
        3
    \end{matrix}
\right.
\right)
\Leftrightarrow
\left(
    \begin{matrix}
        1 & 0 & 1 & 0 \\
        0 & 1 & 0 & 1 \\
        0 & -1 & -1 & 0 \\
        0 & 1 & -1 & 1
    \end{matrix}
\left |
\,
\,
    \begin{matrix}
        2 \\
        2 \\
        -2 \\
        1
    \end{matrix}
\right.
\right)
\Leftrightarrow
\left(
    \begin{matrix}
        1 & 0 & 1 & 0 \\
        0 & 1 & 0 & 1 \\
        0 & 0 & -1 & 1 \\
        0 & 0 & -1 & 0
    \end{matrix}
\left |
\,
\,
    \begin{matrix}
        2 \\
        2 \\
        0 \\
        -1
    \end{matrix}
\right.
\right)
\Leftrightarrow
\left(
    \begin{matrix}
        1 & 0 & 1 & 0 \\
        0 & 1 & 0 & 1 \\
        0 & 0 & -1 & 1 \\
        0 & 0 & 0 & -1
    \end{matrix}
\left |
\,
\,
    \begin{matrix}
        2 \\
        2 \\
        0 \\
        -1
    \end{matrix}
\right.
\right)
$$
$\Rightarrow 
    \begin{cases}
        \lambda_1 = 1 \\
        \lambda_2 = 1 \\
        \lambda_3 = 1 \\
        \lambda_4 = 1
    \end{cases}
\Rightarrow [M]_S = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}$