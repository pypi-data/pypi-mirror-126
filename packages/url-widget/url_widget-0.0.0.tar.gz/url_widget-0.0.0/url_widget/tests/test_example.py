#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alex Lewandowski.
# Distributed under the terms of the Modified BSD License.

import pytest

from ..url import ExampleWidget


def test_example_creation_blank():
    w = ExampleWidget()
    assert w.value == 'Hello World'
