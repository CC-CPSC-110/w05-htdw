"""Tests for Ball"""
from cs110 import expect, summarize
from ball import Ball

# Setup
b = Ball(100, 100)

# Tests
expect(b.move(1, 1), Ball(101, 101))

# Summarize
summarize()