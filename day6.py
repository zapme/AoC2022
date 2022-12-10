#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Advent of code 2022 Day 6
# Tuning Trouble

# Problem 1
examples = [
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

with open('day6-input.txt') as fp:
  lines = fp.readlines()

  for line in lines:
      chars = list(line)
      begin_char = 0
      end_char = 4
      for i in range(end_char, len(chars)):
          for j in range(begin_char, end_char):
              if (
                  (chars[begin_char] not in chars[begin_char + 1 : end_char])
                  and (chars[begin_char + 1] not in chars[begin_char + 2 : end_char])
                  and (chars[begin_char + 2] not in chars[begin_char + 3 : end_char])
              ):
                  print(chars[begin_char : end_char], end_char)
                  break
          else:
            begin_char += 1
            end_char += 1
            continue
          break

# Problem 2

examples = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]

with open('day6-input.txt') as fp:
  lines = fp.readlines()
  for line in lines:
        chars = list(line)
        begin_char = 0
        end_char = 14
        for i in range(end_char, len(chars)):
            for j in range(begin_char, end_char):
                if (
                    (chars[begin_char] not in chars[begin_char + 1 : end_char])
                    and (chars[begin_char + 1] not in chars[begin_char + 2 : end_char])
                    and (chars[begin_char + 2] not in chars[begin_char + 3 : end_char])
                    and (chars[begin_char + 3] not in chars[begin_char + 4 : end_char])
                    and (chars[begin_char + 4] not in chars[begin_char + 5 : end_char])
                    and (chars[begin_char + 5] not in chars[begin_char + 6 : end_char])
                    and (chars[begin_char + 6] not in chars[begin_char + 7 : end_char])
                    and (chars[begin_char + 7] not in chars[begin_char + 8 : end_char])
                    and (chars[begin_char + 8] not in chars[begin_char + 9 : end_char])
                    and (chars[begin_char + 9] not in chars[begin_char + 10 : end_char])
                    and (chars[begin_char + 10] not in chars[begin_char + 11 : end_char])
                    and (chars[begin_char + 11] not in chars[begin_char + 12 : end_char])
                    and (chars[begin_char + 12] not in chars[begin_char + 13 : end_char])
                ):
                    print(chars[begin_char : end_char], end_char)
                    break
            else:
              begin_char += 1
              end_char += 1
              continue
            break