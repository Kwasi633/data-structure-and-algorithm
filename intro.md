**ALGORITHM**
Algorithm is a set of well-defined instructions to solve a particular problem.

*Everday Life Example*

Ingredients -> Recipe -> Tasty dish

*Algorithm to add two numbers*

**Inputs** `Two numbers(a and b)` -> **Algorithm** `(i) Add numbers using (ii)Return the value` -> **Output** `Sum of a and b`.

**CHARACTERISTICS OF AN ALGORITHM**
- Well defined inputs and outputs.
- Each step should be clear and unambiguous.
- Language independent.

**ADVANTAGES OF ALGORITHMS**
-It helps to solve dufferent types of problems.
- It translates to learning different techniques to efficiently solve those problems.
- One problem can be solved in many ways using different algorithms.
- It helps to know the most efficient algorithm.

**ALGORITHM ANALYSIS**
Factors used to analze an algorithm:
- Programming language used to implement the algorithm.
- The computer the program runs on.
- Other programs running at the same time.
- Quality of the operating system.

Performance of an algorithm is eveluated `in terms of its input size`.

`Time Complexity` - Amount of time taken by an algorithm to run as a function of input size.
`Sapce Complexity` - Amount of memory taken by an algorithm to run as a function of input size.

**ASYMPTOTIC NOTATIONS**
They arfe mathematical tools used to represent time and space complexity.
1. Big-0 Notation - Worst case complexity. ✔️
2. Omega Notation - Best case complexity.
3. Theta Notation - Average case complexity.

**BIG-O NOTATION**
It describes the complexity of an algorithm using algebraic terms.

**CHARACTERISTICS**
- It is expressed in terms of input.

```javascript
const summation(n) = {
    let sum = 0 //runtime 1
    for (let i = 0; i <= n; i++){
        sum += i; //runtime 4
    }
    return sum; //runtime 1
}
summation(4)
```
Here the time complexity is dependent on the input size so here we get `n + 2`. If `summation(10)` then time complexity becomes `10 + 2`

- It focuses on the bigger picture.

Time complexity of this algorithm is `0(n) - Linear` 
```javascript
const summation(n) = {
    let sum = 0 //runtime 1
    for (let i = 0; i <= n; i++){
        sum += i; //runtime 4
    }
    return sum; //runtime 1
}
summation(4)
```

**SPACE COMPLEXITY**
0(1) - Constant: When the algorithm doesnt need extra memory.
0(n) - Linear: Where the extra space needed grows as the input size grows.
0(log n) - Logarithmic: Where the extra space needed grows but not as the same as the input size.

- Multiple algorithms exist for the same problem and there is no one right solution. Different alg work well under different constraints.
- The same algorithm with the same programming language can be implemented in deifferent ways.
- Write code that is simple to read and maintain.