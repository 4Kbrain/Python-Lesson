from googlesearch import search

#Input Search 
query = "Youtube"
# Output limitation num=10
for url in search(query, num=10):
    print(url)