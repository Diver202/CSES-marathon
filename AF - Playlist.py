def longest_unique_sequence(n, songs):
    song_set = set()  # To track unique songs in the current window
    start = 0
    max_length = 0

    for end in range(n):
        while songs[end] in song_set:
            song_set.remove(songs[start])
            start += 1
        song_set.add(songs[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Input handling
n = int(input())
songs = list(map(int, input().split()))
print(longest_unique_sequence(n, songs))

