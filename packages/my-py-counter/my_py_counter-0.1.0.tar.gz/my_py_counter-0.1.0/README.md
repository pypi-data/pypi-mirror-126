# my_py_counter

A python package to count number of words in a file

## Installation

```bash
$ pip install my_py_counter
```

## Usage

`my_py_counter` can be used to count words in a text file and plot the results as follows:

```python
from my_py_counter.my_py_counter import count_words
from my_py_counter.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt" # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`my_py_counter` was created by Kazeem Omoloja. It is licensed under the terms of the MIT license.

## Credits

`my_py_counter` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
