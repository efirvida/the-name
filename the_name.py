#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
from collections import defaultdict
from os import path
from typing import Tuple, Dict, List


def the_name() -> Tuple[str, str]:
    names = defaultdict(int)  # type: Dict[str, int]
    name_owners = defaultdict(list)  # type: Dict[str, List[str]]

    for fname in glob.glob("files/*.txt"):
        with open(fname, 'r') as f:
            owner = path.splitext(path.basename(fname))[0]

            for name in set([name.strip() for name in f.readlines()]):
                names[name] = names[name] + 1
                name_owners[name].append(owner)

    ordered_names = sorted(names.items(), key=lambda item: item[1], reverse=True)

    name = ordered_names[0][0]
    return name, name_owners[name]


if __name__ == '__main__':
    winner, owners = the_name()
    print(f"And the winner is: {winner} from {', '.join(owners)} ehhhhhhhhh!!!!!")
