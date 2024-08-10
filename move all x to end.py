def move_x_to_end(s):
    if not s:
        return ""

    if s[0]=='x':
        return move_x_to_end(s[1:])+'x'
    else:
        return s[0]+move_x_to_end(s[1:])


s='axbxccdxxb'
print(move_x_to_end(s))
    