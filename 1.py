def count_characters(input_string):
    """Counts vowels, consonants, spaces, and other characters in a string."""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    other_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():  
            consonant_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Spaces:", space_count)
    print("Other characters:", other_count)

input_string = input("Enter a string: ")
count_characters(input_string)
