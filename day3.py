#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Advent of code 2022 Day 3
# Rucksack reorganization

# Start string with a throwaway character so lowercase a is index 1
item_priorities = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

sum_priorities = 0
sum_group_priorities = 0
group_line_counter = 0

with open('day3-input.txt') as fp:
  lines = fp.readlines()

  group_sack = [0,1,2]
  for line in lines:
    # Problem 1
    # Find item in both rucksack compartments
    first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:].strip()
    first_compartment = set(first_compartment)
    second_compartment = set(second_compartment)
    for item in first_compartment:
      if item in second_compartment:
        sum_priorities += item_priorities.index(item)

    # Problem 2
    # find group symbol, in 3 lines, and sum priorities
    group_sack[group_line_counter] = set(line.strip())
    group_line_counter += 1
    if group_line_counter % 3 == 0:
      group_line_counter = 0
      for item in group_sack[0]:
        if item in group_sack[1] and item in group_sack[2]:
          sum_group_priorities += item_priorities.index(item)
    

print(sum_priorities)
print(sum_group_priorities)