# <u>Data structure & Algorithm Analysis.</u>

*
    * <b>Data structure</b> is a systematic way of organizing and accessing data.
    * <b>Algorithm</b> is a step-by-step procedure for performing some task in a finite amount of time.

___

## <u>Experimental Studies.</u>

___

*
    * Using clock function to measure time might not be consistent if repeating the identical
      algorithm on the identical input, and its granularity will depend upon the computer
      system
    * Python includes a more advanced module, named timeit, to help automate
      such evaluations with repetition to account for such variance among trials.
    * We can then visualize the results by plotting the performance of each run of the algorithm
      as a point with `x-coordinate` equal to the input size, `n`, and `y-coordinate` equal to the
      running time, `t`.
    * This visualization may provide intuition regarding the relationship between problem size and
      execution time for the algorithm.
    * This may lead to a statistical analysis that seeks to fit the best function of the input size
      to the experimental data.

### Challenges of Experimental Analysis

* Limitations of using experimental analysis to their use for algorithm analysis.
*
    * Experimental `running times of two algorithms are difficult to directly compare` unless the
      experiments are performed in the same hardware and software environments.
    * Experiments `can be done only on a limited set of test inputs`; hence, they
      leave out the running times of inputs not included in the experiment (and
      these inputs may be important).
    * An `algorithm must be fully implemented in order to execute it to study` its
      running time experimentally

### Measuring Operations as a Function of Input Size

*
    * Associate an algorithm with a function with input size n: `f( n )`
    * <p id="functions">There are seven `functions`</p>
    *
        1. The Constant Function
        2. The Logarithm Function
        3. The Linear Function
        4. The `N-Log-N` Function
        5. The Quadratic Function
        6. The Cubic Function and Other Polynomials
        7. The Exponential Function
    * Also, there are mathematical <ins>frameworks/notation</ins>  to compare functions. They are known
      as asymptotic Analysis.
    *
        * The Big-Oh Notation
        * The Big-Omega Notation
        * The Big-Theta Notation

#### 1. The Constant Function `f ( n ) = c`.

___

*
    * It does not matter what the value of `n` is `f ( n )` will always be equal to the constant value `c`
    * The interest is in `integer functions`, the most fundamental constant function is `g( n ) = 1`
    * `1` is a constant value i.e `c`, hence in `f ( n ) = c`.
    *
        * `f ( n ) = c`
        * and `g( n ) = 1` where `1` is constant `c`
        * hence, `f ( n ) = c` is same as `f ( n ) = cg( n )`

#### 2. The Logarithm Function f (n) = log<sub>b</sub> n.

___

*
    * f (n) = log<sub>b</sub> n, for some constant b > 1
    * This function is defined as follows: `x = log`<sub>`b`</sub> `n` if and only if `b`<sup>`x`</sup>` = n`.
    * This case we are dealing with base 2 where we can write `log n` is same as `log`<sub>`2`</sub>`n`.

##### Proposition (Logarithm Rules) `f (n) = log`<sub>`b`</sub>`n`.

* Given real numbers a > 0 , b > 1 , c > 0 and d > 1 , we have:

| #   | Preposition(Logarithm Rules)             |     |                                                 | 
|-----|------------------------------------------|:---:|-------------------------------------------------|
| 1.  | `log`<sub>`b`</sub>`(ac)`                |  =  | `log`<sub>`b`</sub>`a` `+ log`<sub>`b`</sub>`c` |
| 2.  | `log`<sub>`b`</sub>`(a/c)`               |  =  | `log`<sub>`b`</sub>`a`` − log`<sub>`b`</sub>`c` |
| 3.  | `log`<sub>`2`</sub>`(a`<sup>`c`</sup>`)` |  =  | `c log`<sub>`2`</sub>`a`                        |
| 4.  | `log`<sub>`b`</sub> `a`                  |  =  | `log`<sub>`d`</sub>`a` / `log`<sub>`d`</sub>`b` |
| 5.  | `b`<sup>`log`<sub>`d`</sub>`a`</sup>     |  =  | `a`<sup>`log`<sub>`d`</sub>`b`</sup>            |

#### 3. The Linear Function `f ( n ) = n`.

___

*
    * That is, given an input `value n`, the linear `function f` assigns the `value n` itself.
      This function arises in algorithm analysis any time we have to do a single basic
      operation for each of `n elements`.
    * For example, comparing a `number x` to each element of a sequence of `size n` will require `n comparisons`.

#### 4. The N-Log-N Function `f ( n ) = n log n`.

___

*
    * That is, the function that assigns to an `input n` the value of n times the `logarithm
      base-two of n`.
    * This function grows a little more rapidly than the linear function and
      a lot less rapidly than the quadratic function.
    * Preferably, use an algorithm with a running time that is proportional to `n log n`,
      than one with `quadratic` running time.

#### 5. The Quadratic Function `f (n) = n`<sup>`2`</sup> .

___

*
    * That is, given an input value n, the function f assigns the product of n with itself
      (in other words, “n squared”).
    * Quadratic function appears in the analysis of algorithms is that there are many algorithms that have nested loops, where the inner
      loop performs a linear number of operations and the outer loop is performed a linear number of times.
    * Quadratic function can also arise in the context of nested loops where the first
      iteration of a loop uses one operation, the second uses two operations, the third uses
      three operations, and so on i.e `1 + 2 + 3 + · · · + (n − 2) + (n − 1) + n`.

#### 6. The Cubic Function and Other Polynomials `f (n) = n`<sup>`3`</sup> .

___

* It assigns to an input value n the product of n with itself three times.

##### Polynomials

*
    * Polynomial function has the form, `f (n) = a`<sub>`0`</sub> `+ a`<sub>`1`</sub>`n + a`<sub>`2`</sub>`n`<sup>`2`</sup> + `a`<sub>`3`</sub>n<sup>`3`</sup> `+ · · · +
      a`<sub>`d`</sub>`n`<sup>`d`</sup> ,
    * Where `a`<sub>`0`</sub>, `a`<sub>`1`</sub>, `a`<sub>`d`</sub> are constants known as coefficients of polynomial which is not equal to zero.
    * Integer `d` indicates the highest power of the polynomial known as degree of polynomial.

#### 7. The Exponential Function `f (n) = b`<sup>`n`</sup> .

___

*
    * Where `b` is a positive constant, called the `base`, and the argument `n` is the `exponent`.

| #   | Proposition (Exponent Rules)         |     |                       | 
|-----|--------------------------------------|:---:|-----------------------|
| 1.  | `(b`<sup>`a`</sup>`)`<sup>`b`</sup>  |  =  | `b`<sup>`ac`</sup>    |
| 2.  | `b`<sup>`a`</sup>`b`<sup>`c`</sup>   |  =  | `b`<sup>`a + c`</sup> |
| 3.  | `b`<sup>`a`</sup> /`b`<sup>`c`</sup> |  =  | `b`<sup>`a - c`</sup> |

## <u> Asymptotic Analysis. </u>

___

*
    * Asymptotic analysis refers to computing the running time of any operation using a mathematical function.
    * In algorithm analysis the growth rate of the running time of a function depends on the input size n.
    * Running time of an algorithm grows proportionally to input size n.
    * Example;

```python
def find_max(data):
    """Return the maximum element from a nonempty Python lis"""
    biggest = data[0]       # The initial value to beat
    for val in data:        # For each value:
        if val > biggest:   # if it is greater than the best so far,
            biggest = val   # we have found a new best (so far)
    return biggest 
```
#### 1. The Big-Oh Notation.
* * We say that `f (n)` is `O(g(n))` if there is a real constant `c > 0` and an integer 
constant `n`<sub>`0`</sub>`≥ 1` such that `f (n) ≤ cg(n)`, for `n ≥ n`<sub>`0`</sub>.
  * Pronounced as f (n) is big-Oh of g(n) i.e `f (n) is O(g(n))`.
  * The big-Oh notation allows us to say that a function f (n) is “less than or equal
to” another function g(n) up to a constant factor i.e `f (n) ≤ g(n)`.
  > NOTE: The difference.
  > > `f (n) is O(g(n))` is not the same as `f (n) ≤ g(n)`
* * We can also say “ `f (n)` is order of `g(n)`”, that is mathematically saying `f (n) ∈ O(g(n))`

#### 2. The Big-Omega Notation.
* * We say that `f (n)` is `Ω(g(n))`  if `g(n) is O( f (n))` and there is a real constant `c > 0` and an integer 
constant `n`<sub>`0`</sub>`≥ 1` such that `f (n) ≥ cg(n)`, for `n ≥ n`<sub>`0`</sub>.
  * Pronounced as  f (n) is big-Omega of g(n).

#### 3. The Big-Theta Notation.
* * . We say that f (n) is Θ(g(n)), pronounced “ f (n)
is big-Theta of g(n),” if f (n) is O(g(n)) and f (n) is Ω(g(n)) , that is, there are real
constants c′ > 0 and c′′ > 0, and an integer constant n0 ≥ 1 such that
c′g(n) ≤ f (n) ≤ c′′g(n), for n ≥ n0.

### <u> Comparative Analysis </u>
* * Our [seven functions](#functions) are ordered by increasing growth rate in the following sequence, that is, if a function f (n) precedes a function g(n) in the sequence,
then f (n) is O(g(n)):

| 1   | log n | n   | n log n | n<sup>2</sup> | n<sup>3</sup> | 2<sup>n</sup> |
|-----|-------|-----|---------|---------------|---------------|---------------|




















