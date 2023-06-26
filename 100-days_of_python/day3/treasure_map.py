row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print("{}\n{}\n{}".format(row1, row2, row3))

place = input("Where do you want to put the treasure (column * row) :")
row = (int(place[0])) - 1
column = (int(place[1])) - 1

map[column][row] = "X"

print("{}\n{}\n{}".format(row1, row2, row3))