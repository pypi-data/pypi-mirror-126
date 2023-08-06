# Coxeter 3: Sage

This package provides a wrapper for [Coxeter 3](http://math.univ-lyon1.fr/~ducloux/coxeter/coxeter3/english/coxeter3_e.html), written by Fokko Ducloux, which supports arbitrary coxeter groups.
In particular, this package allows the user to generate intervals in Bruhat order and Kazhdan-Lusztig polynomials using [coxeter](http://math.univ-lyon1.fr/~ducloux/coxeter/coxeter3/english/coxeter3_e.html).

This is a package that is intended for use with [SageMath](https://www.sagemath.org/) on top of Python 3.

## Why this package

Although [SageMath](https://www.sagemath.org/) supports coxeter 3, this feature only seems to be available for the finite and affine irreducible Coxeter groups.

This package offers a small wrapper around Coxeter, in fact, this it only provides one small class with 3 methods.

## How to Install

Requirements:
* this package requires SageMath to be installed with Python 3; and
* a compiled (not necesarily installed) copy of [Coxeter 3](http://math.univ-lyon1.fr/~ducloux/coxeter/coxeter3/english/coxeter3_e.html).

To install this simply run
```bash
pip3 install coxeter3-sage
```

## Documentation

### Creating an instance

Creating an instance of `Coxeter3` has the following signature.
```sage
Coxeter3(W, q, command, timeout)
```
where
* `W` is a coxeter group *(required)*;
* `q` is the indeterminent of the Kazhdan–Lusztig polynomials *(required)*;
* `command` is the path to the executable for coxeter 3 *(optional; defaults to 'coxeter')*; and
* `timeout` is a timeout, in seconds, to wait for responces from coxeter 3, `None` if no timeout *(optional; defaults to `None`)*.

The returned object with handle an instance of coxeter using [pexpect](https://github.com/pexpect/pexpect/).

Notice here that `command` can be the path to a file, for example `"./coxeter3/bin/coxeter"`.

### Methods

For the documentation of the methods, please see the examples below.

## Example Usage

We now give some basic usage examples as follows.

### Starting an instance

We can create an instance of `Coxeter3` as follows.

```sage
# create an aribtrary Coxeter group `W`
M = CoxeterMatrix([
    [1, 4, 4],
    [4, 1, 4],
    [4, 4, 1]])
W = CoxeterGroup(M)
s1,s2,s3 = W.gens()

# import the `Coxeter3` class
from coxeter3_sage import Coxeter3

# create an instance of `Coxeter3`
R.<q> =  LaurentPolynomialRing(ZZ)
cox = Coxeter3(W, q)

# the object `cox` is now managing a connection with an instance of `coxeter`
```

### Bruhat intervals

We can use this instance of `Coxeter3` to produce bruhat intervals as follows.

```sage
# compute and returns the closed interval `[s1*s2, s1*s3*s2*s1*s3]` as a list
interval1 = cox.bruhat_interval(s1*s2, s1*s3*s2*s1*s3)

# alternatively, you can input these as a list of integers as in `Coxeter3`
interval2 = cox.bruhat_interval([1,2], [1,3,2,1,3])

# we can compute the compute the interval `[1, s1*s3*s2*s1*s3]` as follows
interval3 = cox.bruhat_interval([1,3,2,1,3])
```

### Kazhdan–Lusztig polynomials

Further, we can use `cox` to to compute Kazhdan–Lusztig polynomials as follows.

```sage
# these are some elements which we will use in this example
x, y = (s1*s2, s1*s3*s2*s1*s3)

# compute all of the Kazhdan–Lusztig polynomials `P_{z,y}`
#  where `z \leq x` in Bruhat order
kl_polynomials = cox.klbasis(y)

# the variable `kl_polynomials` is a map
# for example, the following retrieves the `P_{x,y}`
poly = kl_polynomials[x]

# we can iterate through it as follows
for z, P in kl_polynomials.items():
    print("P_{"+str(z.reduced_word())+",y} =", str(P))

# Alternatively we can retrieve an individual polynomial as follows
poly = cox.P(x,y)
```
