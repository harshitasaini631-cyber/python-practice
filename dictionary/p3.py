students = {"harshita": 20, "gab": 17, "nec":19}

total = 0

for marks in students.values():
    total =+ marks
average = total // len(students)

print(f"average marks : {average}")