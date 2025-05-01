from datetime import datetime

def days_between_dates(date_str1: str, date_str2: str) -> int:
    """
    Calculate the number of days between two dates given in 'YYYY-MM-DD' format.

    Parameters:
        date_str1 (str): The first date as a string.
        date_str2 (str): The second date as a string.

    Returns:
        int: The number of days between the two dates.

    Raises:
        ValueError: If either date string is not in the correct format.

    Examples:
        >>> days_between_dates("2023-05-20", "2025-06-20")
        762

        >>> days_between_dates("2024-01-01", "2024-01-31")
        30
    """
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    return abs((date2 - date1).days)


# Example usage:
if __name__ == "__main__":
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        result = days_between_dates(d1, d2)
        print(f"Number of days between {d1} and {d2} is {result} days.")
    except ValueError as ve:
        print(f"Error: {ve}")
