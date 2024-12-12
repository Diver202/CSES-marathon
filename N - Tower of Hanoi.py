def moveDisk(diskNumber, moves, sourceStack, destinationStack, auxiliaryStack):
    # Base case: If there is only one disk, move it directly from source to destination
    if diskNumber == 1:
        moves.append([sourceStack, destinationStack])
        return

    # Recursive call 1: Move 'n-1' disks from source to auxiliary, swapping roles of destination and auxiliary stacks
    moveDisk(diskNumber - 1, moves, sourceStack, auxiliaryStack, destinationStack)

    # Add the current move to the moves list
    moves.append([sourceStack, destinationStack])

    # Recursive call 2: Move 'n-1' disks from auxiliary to destination, swapping roles of source and auxiliary stacks
    moveDisk(diskNumber - 1, moves, auxiliaryStack, destinationStack, sourceStack)


# Function to solve Tower of Hanoi problem
def towerOfHanoi(numberOfDisks):
    moves = []  # List to store the sequence of moves
    sourceStack, destinationStack, auxiliaryStack = 1, 3, 2  # Initialize stack indices
    moveDisk(numberOfDisks, moves, sourceStack, destinationStack, auxiliaryStack)  # Call the recursive function

    # Output the total number of moves
    print(len(moves))

    # Output the sequence of moves (source stack to destination stack)
    for move in moves:
        print(move[0], move[1])


towerOfHanoi(int(input()))