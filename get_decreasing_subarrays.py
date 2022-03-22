# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def myFunc(s: [int]):
    count = 0
    groups = 0

    for i in range(len(s)-1):
        if s[i] > s[i + 1]:
            groups += i-count+1
        else:
            count = i
            groups += 1

    return groups


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = myFunc(s=[9, 8, 7, 6, 5, 4])
    print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
