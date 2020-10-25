# Write a list comprehension which, from a list, generates a lowercased version of each string
# that has length greater than five

strings = ['Some string', 'Art', 'Music', 'Artifical Intelligence']
for x in strings:
    if len(x) > 5:
        print(x.lower())