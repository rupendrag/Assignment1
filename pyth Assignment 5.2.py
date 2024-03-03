# Original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calculate chunk size
chunk_size = len(original_list) // 3

# Slice the list into three equal chunks and reverse each chunk
chunk1 = original_list[:chunk_size][::-1]
chunk2 = original_list[chunk_size:2*chunk_size][::-1]
chunk3 = original_list[2*chunk_size:][::-1]

# Print each chunk separately
print("Chunk 1:", chunk1)
print("Reversed Chunk 1:", chunk1[::-1])
print("Chunk 2:", chunk2)
print("Reversed Chunk 2:", chunk2[::-1])
print("Chunk 3:", chunk3)
print("Reversed Chunk 3:", chunk3[::-1])