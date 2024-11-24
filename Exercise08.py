names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_term = input("Enter the name you want to search for: ").strip()

if search_term in names:
    print(f"{search_term} is in the list!")
else:
    print(f"{search_term} is not in the list.")