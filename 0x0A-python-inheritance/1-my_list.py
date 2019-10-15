#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
