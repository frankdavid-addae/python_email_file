fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

fh = open(fileName)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        emails = words[1]
        count += 1
        print(emails)
print("There were", count, "lines in the file with From as the first word")
