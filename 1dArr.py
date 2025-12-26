import numpy as np
# Create a 1D array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# Display the array
print("Original array:", arr)

# Indexing
print("\nIndexing:")
print("First element (index 0):", arr[0])
print("Last element (index -1):", arr[-1])
print("Third element (index 2):", arr[2])
arr[2] = 35
print("Modified array:", arr)


# Slicing
print("\nSlicing:")
print("Elements from index 2 to 5:", arr[2:6])  # Upper bound is exclusive
print("Elements from start to index 3:", arr[:4])
print("Elements from index 3 to end:", arr[3:])
print("Every other element:", arr[::2])
print("Reverse the array:", arr[::-1])

# Additional NumPy operations
print("\nAdditional Operations:")
print("maximum element in the array : ",np.max(arr))
print("minimum element in the array : ",np.min(arr))
print("Sum of elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))
print("Standard deviation of elements:", np.std(arr))
print("after multiplying with 2 with the array elements : ",arr*2)