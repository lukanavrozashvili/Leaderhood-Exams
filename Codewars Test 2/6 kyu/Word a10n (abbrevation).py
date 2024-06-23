def abbreviate(s):
    def abbreviate_word(word):
        if len(word) >= 4:
            return f"{word[0]}{len(word) - 2}{word[-1]}"
        else:
            return word
    
    result = []
    current_word = []
    
    for char in s:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                result.append(abbreviate_word(''.join(current_word)))
                current_word = []
            result.append(char)
    
    if current_word:
        result.append(abbreviate_word(''.join(current_word)))
    
    return ''.join(result)