def sorter():
    """
    The sorter function takes user input and sorts the numbers in ascending order.
    :return: The sorted list
    """
    NumList = []

    Number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element : " % i))
        NumList.append(value)

    for i in range(Number):
        for j in range(i + 1, Number):
            if NumList[i] > NumList[j]:  # 10>5
                temp = NumList[i]  # temp = 10
                NumList[i] = NumList[j]  # 10 = 5
                NumList[j] = temp  # 5 = temp

    print("Element After Sorting List in Ascending Order is : ", NumList)


def is_even(k):
    return True if k[-1] == 0 or 2 or 4 or 6 or 8 else False


if __name__ == "__main__":
    k = input("Please enter k: ")
    result = is_even(list(k))
    print("true!") if result is True else print("false!")
