def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char != " ":  
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


text = "data structures and algorithms"
frequencies = count_char_frequencies(text)
print(frequencies)
