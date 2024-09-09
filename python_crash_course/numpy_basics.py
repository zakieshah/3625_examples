import python_crash_course.numpy_basics as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
arr += 1
print(arr)

arr = arr.dot(arr)
print(arr)

mat = np.array([[1, 2], [2, 3]])
print(mat, type(mat))