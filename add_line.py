import os

files = os.listdir()

inputs = [file for file in files if file.endswith(".in")]

inputs.sort()


for file in inputs:
    with open(file, "w") as f:
        result = input(f"file {file} expected is: ")

        if result == "t":
            result = "True"
        elif result == "f":
            result = "False"
        else:
            result = "ValueError"

        f.write(f"\nexpected output: {result}")