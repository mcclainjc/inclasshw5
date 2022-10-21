#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list):
    less = []
    equal = []
    greater = []

    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list

    pivot = numbers_in_a_list[0]
    for number in numbers_in_a_list:
        if number < pivot:
            less.append(number)
        elif number > pivot:
            greater.append(number)
        else:
            equal.append(number)

    less = quicksort(less)
    greater = quicksort(greater)
    return less + equal + greater


def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE
    data = open("numbers.txt").read()
    data = data[1:-1] # Exclue the '[' ']'
    values = [int(n.strip()) for n in data.split(',')]
    sorted = quicksort(values)
    output = open("sorted.txt", "w")
    output.write(str(sorted))

    return 0


if __name__ == "__main__":
    main()
