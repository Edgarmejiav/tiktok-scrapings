def read_file_to_list(filename):
    """
    Reads a text file and returns a list of its lines, with newlines and whitespace removed.

    :param filename: Path to the text file to read.
    :return: List of lines from the file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Remove newlines and whitespace
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
# filename = "fanspadredefamilia.txt"
# result = read_file_to_list(filename)
