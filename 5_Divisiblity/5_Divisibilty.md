

```python
for value in range(1,1000):
    if value % 3 == 0 or value % 5 == 0:
        print(value)
```

    3
    5
    6
    9
    10
    12
    15
    18
    20
    21
    24
    25
    27
    30
    33
    35
    36
    39
    40
    42
    45
    48
    50
    51
    54
    55
    57
    60
    63
    65
    66
    69
    70
    72
    75
    78
    80
    81
    84
    85
    87
    90
    93
    95
    96
    99
    100
    102
    105
    108
    110
    111
    114
    115
    117
    120
    123
    125
    126
    129
    130
    132
    135
    138
    140
    141
    144
    145
    147
    150
    153
    155
    156
    159
    160
    162
    165
    168
    170
    171
    174
    175
    177
    180
    183
    185
    186
    189
    190
    192
    195
    198
    


```python
def is_divisible_by_3(number):
    if (number % 3) == 0:
        return True
    else :
        return False
    
```


```python
print(is_divisible_by_3(3))
```

    True
    


```python
print(is_divisible_by_3(9))
```

    True
    


```python
print(is_divisible_by_3(19))
```

    False
    


```python
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)
```

    Numbers divisible by 13 are [65, 39, 221]
    


```python

```


```python

```


```python

```
