LL = [1, [2, [3, [4, None]]]]
ptr = LL

# Traverse the linked list to find the value 2
while ptr != None:
    if ptr[0] == 2:
        # Ask the user for the new value to insert
        new_value = int(input("Enter a value to insert after 2: "))

        # Create a new node with the new value
        new_node = [new_value, ptr[1]]

        # Update the current node to point to the new node
        ptr[1] = new_node

        break  # Exit the loop after adding the new value

    ptr = ptr[1]

# Print the updated linked list
ptr = LL
while ptr is not None:
    print(ptr[0])
    ptr = ptr[1]
