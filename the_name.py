#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import collections

lists = glob.glob("*.txt")
names = []
for name_list in lists:
    with open(name_list,'r') as _list:
        names += [name.strip() for name in _list.readlines()]

counter=collections.Counter(names)
names_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
winner = names_counter[0][0]
clasifications = "\n".join([str(j) + " -> " + str(i) for i,j in names_counter])
print("And the winner is: " + winner + " ehhhhhhhhh!!!!!")
print(clasifications)

