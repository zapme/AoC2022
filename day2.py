#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Advent of code 2022 Day 2
# Rock paper scissors

# Problem 1
# Only 9 possible outcomes, only need to lookup value based on line read and sum
possible_scores = {
  'A X': 1+3, 'A Y': 2+6, 'A Z': 3+0,
  'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
  'C X': 1+6, 'C Y': 2+0, 'C Z': 3+3,
}

with open('day2-input.txt') as fp:
  lines = fp.readlines()

  total_score = 0
  for line in lines:
    total_score += possible_scores[line.strip()]

print (total_score)

# Problem 2
# Same 9 outcomes, but different scoring
possible_scores = {
  'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6,
  'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
  'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6,
}

with open('day2-input.txt') as fp:
  lines = fp.readlines()

  total_score = 0
  for line in lines:
    total_score += possible_scores[line.strip()]  

  print(total_score)