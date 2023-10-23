def freq_dict(data):
    freq = {}
    for c in data:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1


    return freq


str1 = "hello, how are you?"

print(freq_dict(str1))