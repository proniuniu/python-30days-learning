### write a function to reverse a string

target_str = "Python"
def reverse_string(target_str):
    return target_str[::-1]

print(reverse_string(target_str))
print(target_str[0])
print(target_str[-1])
print(target_str[::2])
print(target_str[::3])
date="2025-01-02"
print(date.split("-"))


### write a function to count vowels
def count_vowels(input_str):
    count = 0
    for char in input_str:
        if char in "aeiouAEIOU":
            count=count+1
    
    return count

print(count_vowels("Hello World"))