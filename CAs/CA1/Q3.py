word = input()

result = ''
best = ''
for item in word:
    if item in result:
        result = result[result.index(item)+1:]
    result = result + item
    if len(result) > len(best):
        best = result


print(len(best))