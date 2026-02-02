
def rem(text):
    val = ["<", ">", "/"]
    for char in val:
        text = text.replace(char, "")
    return text
def remo(text,Val ):
    return text.replace(Val, "")
def doc_help():
    """
    This provides help.
    This has 3 module .
    for removing one desired char 
    for removing <,>,/
    and a doc function
    """
    print(__doc__)


