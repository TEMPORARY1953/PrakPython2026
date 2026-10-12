s = input()
parts = s.split()
surname, name, patronymic, year = parts[:4]
city = " ".join(parts[4:])
print(f"{city}, {name}, {surname}")
