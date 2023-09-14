# asgmt-1-programming-and-data-analysis-2023

> Assignment 1: Programming and Data Analysis 2023.

Define functions in `asgmt-one.py` with given names and templates then run `test-runner.py`.

## 01. Define a funct ion `use_abs_function()` which uses the built-in `abs()` function to return the absolute value of a given integer.

```python
def use_abs_function(x: int) -> int:
    """
    >>> use_abs_function(-2)
    2
    >>> use_abs_function(-3)
    3
    >>> use_abs_function(0)
    0
    >>> use_abs_function(2)
    2
    >>> use_abs_function(3)
    3
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `use_pow_function()` which uses the built-in `pow()` function to return a given integer `x` to the power `y`.

```python
def use_pow_function(x: int, y: int) -> int:
    """
    >>> use_pow_function(-2, 3)
    -8
    >>> use_pow_function(-3, 2)
    9
    >>> use_pow_function(0, 2)
    0
    >>> use_pow_function(2, 3)
    8
    >>> use_pow_function(3, 2)
    9
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `use_round_function()` which uses the built-in `round()` function to return the number rounded to ndigits precision after the decimal point.

```python
def use_round_function(x: float, ndigits: int) -> float:
    """
    >>> use_round_function(2.71828, 3)
    2.718
    >>> use_round_function(2.71828, 4)
    2.7183
    >>> use_round_function(3.141592, 2)
    3.14
    >>> use_round_function(3.141592, 5)
    3.14159
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `use_bin_function()` which uses the built-in `bin()` function to convert an integer number to a binary string prefixed with "0b".

```python
def use_bin_function(x: int) -> str:
    """
    >>> use_bin_function(0)
    '0b0'
    >>> use_bin_function(1)
    '0b1'
    >>> use_bin_function(2)
    '0b10'
    >>> use_bin_function(3)
    '0b11'
    >>> use_bin_function(4)
    '0b100'
    >>> use_bin_function(5)
    '0b101'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `use_bool_function()` which uses the built-in `bool()` function to convert an integer number to a boolean value.

```python
def use_bool_function(x: int) -> bool:
    """
    >>> use_bool_function(0)
    False
    >>> use_bool_function(1)
    True
    >>> use_bool_function(2)
    True
    >>> use_bool_function(3)
    True
    >>> use_bool_function(4)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function named `calculate_bmi()` which calculates BMI given heights in centimeters and weights in kilograms.

Source: <https://en.wikipedia.org/wiki/Body_mass_index>

```python
def calculate_bmi(height: int, weight: int) -> float:
    """
    >>> calculate_bmi(216, 147)
    31.507201646090532
    >>> calculate_bmi(206, 113)
    26.628334433028563
    >>> calculate_bmi(211, 110)
    24.70744143213315
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `format_integer_with_dollar_sign_and_commas()` which returns a comma format with dollar sign given an integer.

```python
def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    """
    >>> format_integer_with_dollar_sign_and_commas(1000)
    '$1,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000)
    '$1,000,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000000)
    '$1,000,000,000'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `is_positive()` which returns whether input is a positive integer or not.

```python
def is_positive(x: int) -> bool:
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `is_even()` which returns whether input is an even number or not.

```python
def is_even(x: int) -> bool:
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `are_vowels_contained()` which returns whether input text contains one of the vowels: a, e, i, o, u.

```python
def are_vowels_contained(x: str) -> bool:
    """
    >>> are_vowels_contained('pythn')
    False
    >>> are_vowels_contained('ncnd')
    False
    >>> are_vowels_contained('rtclt')
    False
    >>> are_vowels_contained('python')
    True
    >>> are_vowels_contained('anaconda')
    True
    >>> are_vowels_contained('reticulate')
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```