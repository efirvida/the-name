#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from collections import defaultdict
from os import path
from typing import Tuple, Dict, List


def the_name() -> Tuple[str, str]:
    names = defaultdict(int)  # type: Dict[str, int]
    name_owners = defaultdict(list)  # type: Dict[str, List[str]]
    results = {}
    for fname in glob.glob("files/*.txt"):
        with open(fname, 'r') as f:
            owner = path.splitext(path.basename(fname))[0].capitalize()

            for name in set([name.strip() for name in f.readlines()]):
                names[name] = names[name] + 1
                name_owners[name].append(owner)
                results[name] = [names[name], name_owners[name]]

    ordered_names = sorted(results.items(), key=lambda item: item[1][0], reverse=True)

    winner = ordered_names[0][0]
    return winner, ordered_names


if __name__ == '__main__':
    winner, owners = the_name()
    print(f"And the winner is: {winner} ehhhhhhhhh!!!!!")
    for owner in owners:
        print(f"{owner[1][0]} -> {owner[0]} from \"{', '.join(owner[1][1])}\"")
