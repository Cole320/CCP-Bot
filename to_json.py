import json

dict1 = {}

with open('bad_words') as wordlist:
    for line in wordlist:
        dict1[line.strip()] = 1

out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()