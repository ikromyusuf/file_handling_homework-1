def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = data.split("\n")
    l = []
    for i in data:
        l.append(len(i))
    return l
data = open("txt_file/data06.txt").read()
print(main(data))
# Read data from file
