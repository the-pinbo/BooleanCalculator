# Boolean Calculator Engine

> Boolean Algebra Calculator imlemented in python3 using unate recursive paradigm
> `https://github.com/the-pinbo/BooleanCalculator.git`

## PCN File Format

We are using a very simple text file format for this program. Our code will read a Boolean function specified in this format. The file format looks like this:

- The _first line_ of the file is a single positive `int` n: the number of variables. We number the variables starting with index 1, so if number was 3, the variables in your problem are $$X_1, X_2, X_3$$
- The second line of the file is a single positive `int` m: number of cubes in this cube list. If there are 10 cubes in this file, this is a “10”.
- Each of the subsequent m lines of the file describes one cube : you have the same number of lines as the second line of your file. The first number on the line says how many variables are not don't cares in this cube. If this number is, e.g., 5, then the next 5 numbers on the line specify the true or complemented form of each variable in this cube. We use a simple convention: if variable $x_k$ appears in true form, then put integer $“k”$ on the line; if variable $x_k$ appears in complement form $\bar x_k$ then put integer $“-k”$ on the line

_Example :_
Suppose we have a function $F = X_1.X_2 + X_2.X_3 + X_3.X_1$

```
3
3
2 1 2
2 2 3
2 1 3
```

## Boolean Calculator Commands

We are using a very simple text file format for this program. Our code will read a Boolean function specified in this format. The file format looks like this:
_The program will read a cmd file that has commands that tells the calculator to perform various_

- **Command format:** Every line specifies a single operation: an input operation, a Boolean operation, or an output operation. Each line starts with a single ASCII character to specify the operation, and then either one, two, or three integers, to specify what Boolean function to do.
- **Input operation**: a line of
  the form `r n` (n is an integer) tells you to read input file `n.pcn`,
  and store it in your program as Boolean function $F_n$.
- **NOT operation**: a line of the form `! k n` (k,n are integers) tells you to complement the boolean function $F_n$, and store the result $\bar F_n$ into function $F_k$. In other words, this operation does $F_k = \bar F_n$.
- **OR operation**: a line of the form `+ k n m` (k,n,m are integers) tells you to perform this operation: $F_k = F_n + F_m$ (Boolean OR).
- **AND operation**: a line of the form `& k n m` (k,n,m are integers) tells you to perform this operation: $F_k = F_n .F_m$ (Boolean AND).
- **XOR operation**: a line of the form `& k n m` (k,n,m are integers) tells you to perform this operation: $F_k = F_n \oplus F_m$ (Boolean XOR).
- **Boolean difference operation**: a line of the form `dx k n x` (k,n,x are integers) tells you to perform this operation: $F_k =$ $\frac{\partial F_n}{\partial x}$(Boolean difference).
- **Smoothing Function operation**: a line of the form `dx k n x` (k,n,x are integers) tells you to perform this operation: $F_k = S_x(F_k)$(Smoothing Function).
- **Consensus function operation**: a line of the form `dx k n x` (k,n,x are integers) tells you to perform this operation: $F_k = C_x(F_k)$(Consensus function).
- **Output operation**: a line of the form `p n` (n is an integer) tells you to write Boolean function $F_n$ to an output file called `n.pcn`, in our standard ASCII output format.
- **Quit operation**: the line `q` tells you to stop parsing the command file, you are done with processing commands.

_Example 1:_
Suppose we want to calculate the xor of function $F_2$ and $F_3$, and store the result in $F_0 = F_2  \oplus F_3$. Here is the command file. We have added comments for readabilty – but these will **should not** appear in the actual file.

```
r 2 // read in F2
r 3 // read in F3
xor 0 2 3 // F0 = F2 xor F3
p 0 // output F0 = F2 exor F3
q // we are done
```

_Alternative command_

```
r 2 // read in F2
r 3 // read in F3
! 4 2 // F4 = F2’
! 5 3 // F5 = F3’
& 6 2 5 // F6 = F2 . F5, ie, F2 F3’
& 7 3 4 // F7 = F3 . F4, ie, F3 F2’
+ 0 6 7 // F0 = F6 + F7, ie F2 F3’ + F3 F2’
p 0 // output F0 = F2 exor F3
q // we are done
```

_Example 2:_
Suppose we want to calculate the Consensus function of function $F_1$ with respect to variable $X$, and store the result in $F_0 = C_X(F_1)$. Here is the command file.

```
r 1
sx 0 1 1
p 0
q
```

## Output

Suppose we have a function $F_1 = X_1.X_2 + X_2.X_3 + X_3.X_1$

**`1.pcn`**

```
3
3
2 1 2
2 2 3
2 1 3
```

- $F_0 =$ $\frac{\partial F_1}{\partial x}$ $\Rightarrow X_2 \oplus X_3$

<img src="readme_img/dx.png" alt="output screen shot">

- $F_0 = C_X(F_1)$ $\Rightarrow X_2 . X_3$
  
<img src="readme_img/cx.png" alt="output screen shot">

- $F_0 = S_X(F_1)$ $\Rightarrow X_2 + X_3$
  
<img src="readme_img/sx.png" alt="output screen shot">

## Setup

Simply clone this git hub repo and run `main.py ` with the appropriate cmd and pcn files
`https://github.com/the-pinbo/BooleanCalculator.git`

## Contact

Created by [@the-pinbo](https://github.com/the-pinbo) - feel free to contact me!
