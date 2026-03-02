first = 'apple'
second = "banana"

#print them out...
print(f"First: {first}  | Second {second}")

# now switch time
first, second = second, first

print("I've switched things around...")
print(f"First: {first} | Second {second}")