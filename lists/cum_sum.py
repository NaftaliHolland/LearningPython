#A function that takes a list of numbers and returns the cummulative sum as a new list where the ith element is the sum of the first i + 1 elements from the original list

def cum_sum(t):
    new_t = []
    
    for em, i in enumerate(t, start = 1):
        new_t.append(sum(t[:em]))
    return new_t
def main():
    t = [1, 2, 3]
    print(cum_sum(t))
    print(t)

main()