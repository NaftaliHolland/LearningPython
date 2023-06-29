#A function that that takes a list of lists of integers and adds up the elements in the nested lists
def nested_sum(t):
    sum_of  = 0
    for i in t:
        sum_of += sum(i)
    return sum_of
        
def main():
    t = [[1, 2], [3], [4, 5, 6]]
    sum = nested_sum(t)
    print(sum)

main()