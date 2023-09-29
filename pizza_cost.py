#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Sept/27/2023
# This program calculates the total cost of a pizza including it's tax.

import constants


def main():
    # Get user input for the diameter.
    diameter = int(input("Enter the diameter of the pizza in inches:"))

    # Calculate the subtotal.
    subtotal = (
        constants.LABOUR_COST
        + constants.RENTAL_COST
        + constants.INGREDIENT_COST * diameter
    )
    # Calculate the tax.
    tax = constants.HST * subtotal
    # Calculate the total cost.
    total = subtotal + tax

    # Display the cost of the pizza back to the user.
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
