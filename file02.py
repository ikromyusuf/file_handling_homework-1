def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)
f = open("text_file/data01.txt")
print(main(f.read()))
# Read data from file