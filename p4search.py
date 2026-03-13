search_data={
 "python":500,
 "python list":150,
 "java error":300,
 "javascript":400
}

prefix_map={}

for word,freq in search_data.items():
    for i in range(1,len(word)+1):
        prefix=word[:i]
        prefix_map.setdefault(prefix,[]).append((word,freq))

for p in prefix_map:
    prefix_map[p].sort(key=lambda x:x[1],reverse=True)

def suggest(prefix):
    return [w for w,f in prefix_map.get(prefix,[])[:5]]

print(suggest("python"))