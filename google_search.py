from googlesearch import search


query = input("what do you want to search: ")
for result in search(query, start=0, pause=2):
    print(result)
