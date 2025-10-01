def letter_frequency(input_string):
    freq_dict = {}
    for char in input_string:
        if char.isalpha(): 
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict

input_str = input("Enter string: ")

frequency = letter_frequency(input_str)

for char, count in frequency.items():
    print(f"{char}={count}", end=", ")
