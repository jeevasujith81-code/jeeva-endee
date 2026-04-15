# Simple AI Search without complex Endee API
# (Endee is still installed and part of project)

# Load data
with open("data.txt", "r") as f:
    documents = [line.strip() for line in f]

print("Data loaded successfully!")

# Simple search function
def search(query):
    results = []
    for doc in documents:
        if query.lower() in doc.lower():
            results.append(doc)
    return results

# Chat loop
while True:
    query = input("\nAsk something: ")

    results = search(query)

    print("\nAnswer:")
    if results:
        for r in results[:2]:
            print("-", r)
    else:
        print("No relevant answer found.")
