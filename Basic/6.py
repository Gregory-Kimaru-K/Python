vowels = ['a', 'e', 'i', 'o', 'u']

vowelCount = 0

string = 'Hellodfmioscajjmc9wrikjiqowrekjwgibk'

i = 0
while i < len(string):
    if string[i] in vowels:
        vowelCount += 1
    i += 1

print(vowelCount)