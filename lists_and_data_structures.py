# ==============================================================================
# Lists and Data Structures in Python
# ==============================================================================
# This program demonstrates Python's most versatile built-in sequence: Lists.
# It covers:
# - Creating lists and accessing items (indexing/slicing)
# - Modifying lists (append, remove, pop)
# - List sorting and ordering
# - Iterating through lists and list comprehensions
# ==============================================================================

def main():
    print("--- 1. Creating Lists and Basic Indexing ---")
    # Lists can store items of different data types, but are usually homogeneous
    ai_tech_stack = ["Python", "TensorFlow", "PyTorch", "Keras", "Scikit-Learn"]
    print(f"Original list: {ai_tech_stack}")
    print(f"Number of items: {len(ai_tech_stack)}")
    
    # Positive Indexing (starts at 0)
    print(f"First item (index 0): {ai_tech_stack[0]}")
    print(f"Third item (index 2): {ai_tech_stack[2]}")
    
    # Negative Indexing (starts at -1 from the end)
    print(f"Last item (index -1): {ai_tech_stack[-1]}")
    print(f"Second to last item (index -2): {ai_tech_stack[-2]}")
    print()

    print("--- 2. List Slicing ---")
    # Syntax: list[start:end:step] - end is exclusive
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Numbers: {numbers}")
    print(f"Slice [2:6]: {numbers[2:6]}")       # elements from index 2 to 5
    print(f"Slice [:4]: {numbers[:4]}")         # elements from start to index 3
    print(f"Slice [6:]: {numbers[6:]}")         # elements from index 6 to end
    print(f"Slice [::2]: {numbers[::2]}")       # every second element (even numbers)
    print(f"Slice [::-1]: {numbers[::-1]}")     # reverse the list
    print()

    print("--- 3. Modifying Lists (Methods) ---")
    # Append: Add to end
    ai_tech_stack.append("JAX")
    print(f"After append('JAX'): {ai_tech_stack}")
    
    # Insert: Add at specific position
    ai_tech_stack.insert(1, "Pandas")
    print(f"After insert(1, 'Pandas'): {ai_tech_stack}")
    
    # Remove: Delete item by value
    ai_tech_stack.remove("Keras")
    print(f"After remove('Keras'): {ai_tech_stack}")
    
    # Pop: Delete and return item by index (defaults to last item)
    popped_item = ai_tech_stack.pop(2) # removes TensorFlow (index 2)
    print(f"Popped item at index 2: {popped_item}")
    print(f"Current list: {ai_tech_stack}")
    print()

    print("--- 4. List Sorting ---")
    fruits = ["banana", "apple", "cherry", "date"]
    print(f"Unsorted fruits: {fruits}")
    
    # sorted() returns a new sorted list (original unchanged)
    sorted_fruits = sorted(fruits)
    print(f"Sorted (new list): {sorted_fruits}")
    print(f"Original fruits: {fruits}")
    
    # sort() sorts the list in-place
    fruits.sort()
    print(f"Sorted in-place: {fruits}")
    
    # Sort in reverse order
    fruits.sort(reverse=True)
    print(f"Sorted reverse in-place: {fruits}")
    print()

    print("--- 5. Iterating and List Comprehensions ---")
    # Iterating through a list with a for loop
    print("AI Frameworks in uppercase:")
    for framework in ai_tech_stack:
        print(f" - {framework.upper()}")
        
    # List Comprehension: Concise way to create new lists from existing ones
    # Example: square each number in a list if it's odd
    source_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    squared_odds = [x**2 for x in source_nums if x % 2 != 0]
    print(f"Source numbers: {source_nums}")
    print(f"Squared odd numbers (via List Comprehension): {squared_odds}")

if __name__ == "__main__":
    main()
