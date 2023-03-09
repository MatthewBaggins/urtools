# `urtools`

Custom functions and other utilities that I find useful and use across many projects. Not all of them were created by me. Pieces of code borrowed from various people across the internet are annotated with a comment `# source: <URL>`.

## Install

Requires Python >= 3.8

```sh
python -m pip install urtools
```

## Functionalities

If you want to see what these things do in detail, just go to `src/urtools` and read the docstrings. Here, I'll just describe submodules.

- `attr` - getters of attribute names
- `dict` - utilities for working with dictionaries, e.g. indexing one dictionary with multiple keys, deleting many keys from one dictionary, indexing a list of dictionaries with one key, filtering `nan`s from a dictionary, etc.
  - `CallbackDict` is a custom `dict` subclass that deserves some special attention. It allows you to specify exactly how the dictionary is supposed to deal when you ask it a value that it doesn't have.
- `func` - very few functional programming utils
- `json` - loading and saving JSONs with one-liners
- `list` - splitting and pruning lists + checking if it has nulls
- `pandas` - finding duplicate rows in pandas dataframes and converting dataframes to lists with rows as dictionaries (optionally filtering `nan`s)
- `str` - modifying strings, finding all occurences of substring, and partitioning them on substring, with that substring retained in the output
- `type` - mostly typeguards for now, perhaps, there'll be something more in the future
