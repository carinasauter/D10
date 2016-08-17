#!/usr/bin/env python3

# Write a program that given a text file will create a new text file in
# which all the lines from the original file are numbered from 1 to n (where n is
# the number of lines in the file). [use small.txt]


def numbered_lines():
    with open("small.txt", "r") as doc:
        text = doc.readlines()
        file = open("new_small.txt", "w")
        number = 1
        for line in text:
            if len(line) > 0:
                file.write(str(number) + " " + line)
                number += 1
    return None


def main():
    numbered_lines()

if __name__ == "__main__":
    main()
