# def duplicates(s,seen=None):
#     if seen is None:
#         seen=set()
#     if not s:
#         return ''
#     currchar=s[0]
#     if currchar in seen:
#         return duplicates(s[1:],seen)
#     else:
#         seen.add(currchar)
#         return currchar+duplicates(s[1:],seen)

# s='axbxccdxxb'
# print(duplicates(s))  
# 
# 
# 
# #second method  
def remove_duplicates(s, index=0, result=""):
    # Base case: if we've processed all characters
    if index == len(s):
        return result

    currchar = s[index]

    # Check if the current character is already in the result
    if currchar not in result:
        result += currchar  # Add current character to result if not already present

    # Recursive call with the next character
    return remove_duplicates(s, index + 1, result)

# Test the function
s = 'axbxccdxxb'
print(remove_duplicates(s))
