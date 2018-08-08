Title: *args and **kwargs
Date: 2017-01-27 03:35 
Modified: 2018-08-08 13:33
Authors: José Aniceto


`*args` and `**kwargs` allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords.

Note that it is not necessary to write `*args` or `**kwargs`. Only the * (aesteric) is necessary. You can also write *var and **vars. Writing `*args` and `**kwargs` is just a convention.


### A normal function: 

```python
def func1(one, two)
  print(one)
  print(two)

func1('arg one', 'arg two')  # Correct
func1('arg one')  # Error
func1('arg one', 'arg two', 'arg three')  # Error
```

### `*args` usage

`*args` is used to send a non-keyworded variable length argument list to the function. Here’s an example:

```python
def func2(*args)
  for stuff in args:
    print(stuff)
    
my_list = ['green', 'yellow', 'blue', 'red']

func2(*my_list)  # Correct
func2('green', 'yellow', 'blue', 'red')  # Correct
```


```python
def func3(one, two, *args)
  print(one)
  print(two)
  for stuff in args:
    print(stuff)
    
my_list = ['green', 'yellow', 'blue', 'red']

func3('required one', 'required two', *my_list)  # Correct
```


### `**kwargs` usage:

`**kwargs` allows you to pass keyworded variable length of arguments to a function. You should use `**kwargs` if you want to handle named arguments in a function. Here is an example:

```python
def func4(**kwargs)
  for key, value in kwargs.items():
    print(key)
    print(value)
    
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

func4(**kwargs)  # Correct
func4(key1 = 'value1', key2 = 'value2', key3 = 'value3')  # Correct
```


### Order of using `*args` `**kwargs` and formal args
If you want to use all three of these in functions then the order is:

```python
some_func(fargs, *args, **kwargs)
```