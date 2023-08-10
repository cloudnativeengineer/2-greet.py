import sys


def normalize_name(name: str) -> str:
    """
    Normalize the provided name if valid.

    Parameters:
        name (str): Name to be normalized.

    Returns:
        str: Normalized name if valid.

    Raises:
        ValueError: If the name contains characters other than letters.
    """
    if name.isalpha():
        return name.lower().capitalize()
    else:
        raise ValueError("Ensure the name contains only letters.")


def greet_user():
    """Greet the user with their provided name or default to 'World'."""
    normalized_name = "World"

    if len(sys.argv) == 2:
        try:
            normalized_name = normalize_name(sys.argv[1])
        except ValueError as error:
            print(error)

    print(f"Hello, {normalized_name}!")


if __name__ == '__main__':
    greet_user()

