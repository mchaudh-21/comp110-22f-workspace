'''some tender, loving functions'''

def love(subject:str)-> str:
    """Given subject as a paramter, returns a loving sting"""
    return f"i love you {subject}!"


'''generates a str repeating a loving message n times'''
def spread_love(to:str, n:int) -> str:
    love_note = ''
    counter = 0
    while counter < n:
        love_note += f"{love(to)} \n"
        counter += 1
    
    return love_note


# main
print(spread_love('divya 1.0',7))