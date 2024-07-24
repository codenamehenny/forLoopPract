# Classroom Seat Assignment: Use for loops with the range function to assign seats in a classroom setting.

# list of students and position in row, and list of columns.
columns = 6
rows = 6
seats_assigned =[]

for row in range(1,  rows + 1):
    for column in range(1, columns + 1):
        seat_assigning =(f"Row {row}, Column {column}")
        seats_assigned.append(seat_assigning)

for column in seats_assigned:
    print(column)