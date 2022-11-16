def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l = []
    for i in data.split(","):
        l.append(int(i))
    return l
f = open("txt_file/data01.txt")
print(main(f.read()))
# Read data from file