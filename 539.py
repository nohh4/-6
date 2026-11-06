first = {"x": 1, "y": 2, "z": 3}
second = {"w": 10, "x": 11, "y": 2}

common_keys = first.keys() & second.keys()
print(*common_keys)