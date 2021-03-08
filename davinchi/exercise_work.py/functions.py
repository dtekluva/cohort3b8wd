data = []
take_in = input("Enter a hyphen separated sequence of words:\n ")
store = take_in.split('-')
print(store)
store.sort()
print(store)
print('-'.join(store))



