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
