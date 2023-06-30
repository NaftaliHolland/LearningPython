def plus_line(columns):
    print("+", end = "")
    for i in range(columns):
        for i in range(4):
            print(" - ", end = "")
        print("+", end = "")
    print("")

def draw_columns(columns):
    for i in range(4):
        print("|", end = "")
        for i in range(columns):
            for i in range(4):
                print("   ", end = "")
            print("|", end = "")
        print("")

def draw_grid(rows, columns):
    for i in range(rows):
        plus_line(columns)
        draw_columns(columns)
    plus_line(columns)


def main():
    draw_grid(3, 10)
    
main()