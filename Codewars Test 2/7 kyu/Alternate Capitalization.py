def capitalize(s):
    even_index = ''
    odd_index = ''
    for i, char in enumerate(s):
        if i % 2 == 0:
            even_index += char.upper()
            odd_index += char
        else:
            even_index += char
            odd_index += char.upper()
    return [even_index, odd_index]