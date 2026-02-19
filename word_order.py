# Enter your code here. Read input from STDIN. Print output to STDOUT

# lines=input("Enter Word Count")
# list=[]

# occurence={}
# for _ in range(lines):
#     list.append=input()
    
# for word in range(list):
#     if word in list:
#         occurence.append={word:}
    

n = int(input().strip())

counts = {}  # word -> occurrences (in insertion order)

for _ in range(n):
    w = input().strip()
    counts[w] = counts.get(w, 0) + 1

print(len(counts))
print(*counts.values())