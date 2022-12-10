#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Advent of code 2022 Day 4
# Camp Cleanup

# Problem 1
# Number of complete subsets
subset_counter = 0
with open('day4-input.txt') as fp:
  lines = fp.readlines()

  for line in lines:
    elf_0, elf_1 = line.strip().split(',')
    elf_0 = [ int(x) for x in elf_0.split('-')]
    elf_1 = [ int(x) for x in elf_1.split('-')]
    if (elf_0[0] <= elf_1[0]) and (elf_0[1] >= elf_1[1]):
      subset_counter += 1
    elif (elf_1[0] <= elf_0[0]) and (elf_1[1] >= elf_0[1]):
      subset_counter += 1

print(subset_counter)

# Problem 2
# number of partial overlap (# intersecting elements > 0)

partial_overlaps = 0
with open('day4-input.txt') as fp:
  lines = fp.readlines()
  
  for line in lines:
    elf_0, elf_1 = line.strip().split(',')
    elf_0 = [ int(x) for x in elf_0.split('-')]
    elf_0 = set(range(elf_0[0], elf_0[1]+1))
    elf_1 = [ int(x) for x in elf_1.split('-')]
    elf_1 = set(range(elf_1[0], elf_1[1]+1))
    if len(elf_0.intersection(elf_1)) > 0:
      partial_overlaps += 1

print(partial_overlaps)