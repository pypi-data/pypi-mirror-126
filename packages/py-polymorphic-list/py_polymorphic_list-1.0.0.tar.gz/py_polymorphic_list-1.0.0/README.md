# py-polymorphic-list

[![Publish to PyPI](https://github.com/keshprad/py_polymorphic_list/actions/workflows/publish.yml/badge.svg)](https://github.com/keshprad/py-polymorphic-list/actions/workflows/publish.yml) [![Deploy docs to GitHub Pages](https://github.com/keshprad/py_polymorphic_list/actions/workflows/docs.yml/badge.svg)](https://github.com/keshprad/py-polymorphic-list/actions/workflows/docs.yml)

Python implementation of a polymorphic list

[View on PyPI](https://pypi.org/project/py-polymorphic-list/) / [Documentation](https://keshprad.github.io/py-polymorphic-list/) / [GitHub Source Code](https://github.com/keshprad/py-polymorphic-list/)

## What is a Polymorphic List?

A polymorphic list is a data abstraction similar to LinkedLists where objects of two classes, `NonEmptyList`, and `EmptyList`, are employed to cleanly handle edge cases where a LinkedList would be `null`. In a LinkedList, the last node's `next` reference is `null`; however, for a PolymorphicList, the last node's `next` reference is an `EmptyList`, allowing the EmptyList object to override methods defined in a PolymorphicList.

This means that every method is overridden to have a version for a NonEmptyList and for an EmptyList.

## Installation

```bash
pip install py-polymorphic-list
```

Or install with `pip3`, accordingly.

## Documentation

Check out the [documentation](https://keshprad.github.io/py-polymorphic-list/) for full details on usage.
