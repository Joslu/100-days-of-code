my_dict = {"root": 18, "blue": [75, "R", 2], 21: "Venus", -14: None}


# Iterate over a dictionary
for key, value in my_dict.items():
    print(f"{key}, {value}")

# Another way to do it
for key in my_dict:
    print(f"{key}, {my_dict[key]}")
