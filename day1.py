#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Advent of code 2022 Day 1
# Calorie Counting - Reindeer food

# Problem 2, forgot to save problem 1, but mostly similar
max = 0
with open('day1-input.txt') as fp:
  lines = fp.readlines()

  total = 0
  line_count = 0
  blank_count = 0
  sums = []

  for line in lines:
    try:
      total += int(line)
      line_count += 1
    except ValueError:
      sums.append(total)
      blank_count += 1
      if total > max:
        max = total
      total = 0

print(f'Line count is {line_count}')
print(f'Blank count is {blank_count}')
print(sum(sorted(sums)[-3:]))
print(max)