def compound_interest(principal, rate, time):
    """
    Calculates compound interest.

    Args:
        principal (float): Principal amount.
        rate (float): Annual interest rate (in percentage).
        time (float): Time in years.

    Returns:
        float: Compound interest.
    """
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci


def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))

    compound_interest_value = compound_interest(principal, rate, time)
    print(f"Compound interest is {compound_interest_value:.2f}")


if __name__ == "__main__":
    main()
