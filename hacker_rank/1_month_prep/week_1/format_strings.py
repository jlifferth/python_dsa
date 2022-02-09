strings1 = []
with open('strings.txt') as strings_in:
    for line in strings_in:
        line = line.strip()
        strings1.append(line)

queries1 = []
with open('queries.txt') as strings_in:
    for line in strings_in:
        line = line.strip()
        queries1.append(line)

print(queries1)