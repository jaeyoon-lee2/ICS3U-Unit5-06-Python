#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Nov 2019
# This program rounds a number by the user to the digit the user wants


def to_round(decimal, digit):

    decimal[0] = float(decimal[0])
    decimal[0] = decimal[0] * 10**digit
    decimal[0] = decimal[0] + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / 10**digit


def main():
    # this function rounds a number by the user to the digit the user wants

    decimal = []
    # input
    user_decimal = input("Enter a number with decimals: ")
    digit = int(input("Where do you want to round off (integer): "))
    decimal.append(user_decimal)
    to_round(decimal, digit)
    print("The rounded number is {}".format(decimal[0]))


if __name__ == "__main__":
    main()
