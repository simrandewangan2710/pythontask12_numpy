
import numpy as np

print("=== NumPy Attributes Examples ===\n")

# 1. ndim: Returns the number of dimensions
print("1. ndim (Number of dimensions):")
arr1 = np.array([1, 2, 3])  # 1D
print(f"   1D array: {arr1.ndim}")  # Output: 1
arr2 = np.array([[1, 2], [3, 4]])  # 2D
print(f"   2D array: {arr2.ndim}")  # Output: 2
arr3 = np.array([[[1, 2]], [[3, 4]]])  # 3D
print(f"   3D array: {arr3.ndim}")  # Output: 3
arr4 = np.array([[[[1]]]])  # 4D
print(f"   4D array: {arr4.ndim}")  # Output: 4
arr5 = np.array(5)  # 0D
print(f"   0D array: {arr5.ndim}")  # Output: 0

# 2. shape: Returns a tuple of array dimensions
print("\n2. shape (Tuple of array dimensions):")
arr1 = np.array([1, 2, 3, 4, 5])
print(f"   1D array: {arr1.shape}")  # Output: (5,)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"   2D array: {arr2.shape}")  # Output: (2, 3)
arr3 = np.array([[[1, 2]], [[3, 4]], [[5, 6]]])
print(f"   3D array: {arr3.shape}")  # Output: (3, 1, 2)
arr4 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(f"   Reshaped 2x3: {arr4.shape}")  # Output: (2, 3)
arr5 = np.array(42)
print(f"   Scalar: {arr5.shape}")  # Output: ()

# 3. size: Total number of elements
print("\n3. size (Total number of elements):")
arr1 = np.array([1, 2, 3])
print(f"   1D array: {arr1.size}")  # Output: 3
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(f"   2D array: {arr2.size}")  # Output: 6
arr3 = np.array([[[1, 2, 3]], [[4, 5, 6]]])
print(f"   3D array: {arr3.size}")  # Output: 6
arr4 = np.array([1, 2, 3, 4]).reshape(2, 2)
print(f"   2x2 array: {arr4.size}")  # Output: 4
arr5 = np.array([])
print(f"   Empty array: {arr5.size}")  # Output: 0

# 4. dtype: The type of data in the array
print("\n4. dtype (Data type of array elements):")
arr1 = np.array([1, 2, 3])
print(f"   Default int: {arr1.dtype}")  # Output: int32 or int64
arr2 = np.array([1.0, 2.0, 3.0])
print(f"   Float: {arr2.dtype}")  # Output: float64
arr3 = np.array([1, 2, 3], dtype=np.int16)
print(f"   Specified int16: {arr3.dtype}")  # Output: int16
arr4 = np.array(['a', 'b', 'c'])
print(f"   String: {arr4.dtype}")  # Output: <U1
arr5 = np.array([True, False, True])
print(f"   Boolean: {arr5.dtype}")  # Output: bool

# 5. itemsize: Length of one array element in bytes
print("\n5. itemsize (Size of one element in bytes):")
arr1 = np.array([1, 2, 3])
print(f"   int32: {arr1.itemsize}")  # Output: 4
arr2 = np.array([1.0, 2.0, 3.0])
print(f"   float64: {arr2.itemsize}")  # Output: 8
arr3 = np.array([1, 2, 3], dtype=np.int8)
print(f"   int8: {arr3.itemsize}")  # Output: 1
arr4 = np.array([True, False])
print(f"   bool: {arr4.itemsize}")  # Output: 1
arr5 = np.array(['hello', 'world'])
print(f"   string: {arr5.itemsize}")  # Output: 10 (for <U5)

print("\n=== NumPy Methods Examples ===\n")

# 6. sum: Sum of array elements
print("6. sum (Sum of array elements):")
arr1 = np.array([1, 2, 3, 4])
print(f"   1D array: {arr1.sum()}")  # Output: 10
arr2 = np.array([[1, 2], [3, 4]])
print(f"   2D array total: {arr2.sum()}")  # Output: 10
print(f"   2D array axis=0: {arr2.sum(axis=0)}")  # Output: [4 6]
print(f"   2D array axis=1: {arr2.sum(axis=1)}")  # Output: [3 7]
arr3 = np.array([1.5, 2.5, 3.5])
print(f"   Float array: {arr3.sum()}")  # Output: 7.5
arr4 = np.array([])
print(f"   Empty array: {arr4.sum()}")  # Output: 0.0

# 7. mean: Mean of array elements
print("\n7. mean (Mean of array elements):")
arr1 = np.array([1, 2, 3, 4, 5])
print(f"   1D array: {arr1.mean()}")  # Output: 3.0
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"   2D array total: {arr2.mean()}")  # Output: 3.5
print(f"   2D array axis=0: {arr2.mean(axis=0)}")  # Output: [2.5 3.5 4.5]
arr3 = np.array([1.0, 2.0, 3.0, 4.0])
print(f"   Float array: {arr3.mean()}")  # Output: 2.5
arr4 = np.array([10])
print(f"   Single element: {arr4.mean()}")  # Output: 10.0
arr5 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(f"   2x3 array: {arr5.mean()}")  # Output: 3.5

# 8. std: Standard deviation of array elements
print("\n8. std (Standard deviation):")
arr1 = np.array([1, 2, 3, 4])
print(f"   1D array: {arr1.std():.2f}")  # Output: 1.12
arr2 = np.array([[1, 2], [3, 4]])
print(f"   2D array: {arr2.std():.2f}")  # Output: 1.12
print(f"   2D array axis=0: {arr2.std(axis=0)}")  # Output: [1. 1.]
arr3 = np.array([10, 10, 10])
print(f"   Constant array: {arr3.std()}")  # Output: 0.0
arr4 = np.array([1, 3, 5, 7, 9])
print(f"   Odd numbers: {arr4.std():.2f}")  # Output: 2.83
arr5 = np.array([0, 1])
print(f"   Binary: {arr5.std():.2f}")  # Output: 0.50

# 9. min: Minimum value in array
print("\n9. min (Minimum value):")
arr1 = np.array([5, 2, 8, 1])
print(f"   1D array: {arr1.min()}")  # Output: 1
arr2 = np.array([[3, 7], [1, 9]])
print(f"   2D array: {arr2.min()}")  # Output: 1
print(f"   2D array axis=1: {arr2.min(axis=1)}")  # Output: [3 1]
arr3 = np.array([10.5, 20.3, 5.1])
print(f"   Float array: {arr3.min()}")  # Output: 5.1
arr4 = np.array([-5, -2, -8])
print(f"   Negative: {arr4.min()}")  # Output: -8
arr5 = np.array([42])
print(f"   Single: {arr5.min()}")  # Output: 42

# 10. max: Maximum value in array
print("\n10. max (Maximum value):")
arr1 = np.array([1, 5, 3, 9])
print(f"    1D array: {arr1.max()}")  # Output: 9
arr2 = np.array([[2, 8], [4, 6]])
print(f"    2D array: {arr2.max()}")  # Output: 8
print(f"    2D array axis=0: {arr2.max(axis=0)}")  # Output: [4 8]
arr3 = np.array([1.1, 2.2, 3.3])
print(f"    Float array: {arr3.max()}")  # Output: 3.3
arr4 = np.array([-1, -5, -3])
print(f"    Negative: {arr4.max()}")  # Output: -1
arr5 = np.array([100, 200, 50])
print(f"    Larger numbers: {arr5.max()}")  # Output: 200