# Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique = set()

for dictionary in sample:
    for value in dictionary.values():
        unique.add(value)
print("Unique Values:", unique)