# Locate Card - Binary Search Algorithm

This Python program searches for a specific card's position in a **decreasingly sorted list** using **Binary Search**, making it more efficient than a linear search.

## 🚀 Features
- Uses **Binary Search** for fast lookup (O(log n) complexity).
- Works with a **strictly decreasing list**.
- Prints the position of the card if found, otherwise displays **"Card not found"**.

## 🛠 How It Works
1. The function `locate_card(query)` takes an integer `query` as input.
2. It searches for the `query` in the **sorted** list `[13, 12, 11, 7, 4, 3, 1, 0]`.
3. If found, it prints the index; otherwise, it prints `"Card not found"`.
4. The algorithm uses **binary search** for efficient searching.

## 📜 Code
```python
def locate_card(query):
    # Alice's cards in strictly decreasing order
    all_cards = [13, 12, 11, 7, 4, 3, 1, 0]
    
    # Binary search implementation
    left, right = 0, len(all_cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if all_cards[mid] == query:
            print(f"Card found at position {mid}")
            return
        elif all_cards[mid] < query:
            right = mid - 1  # Move left (since the list is in decreasing order)
        else:
            left = mid + 1   # Move right

    print("Card not found")

# Test the function
locate_card(7)


## Example Output: Card found at position 3
