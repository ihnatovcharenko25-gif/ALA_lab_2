import numpy as np

#A = np.array([[2, 1], [1, 3]], dtype=float)

#A = np.array([[4, 1, 2, 0], [1, 3, 0, 1], [2, 0, 5, 2], [0, 1, 2, 6]], dtype=float)


rng = np.random.default_rng(0)
M = rng.integers(-5, 6, (10, 10)).astype(float)
A = (M + M.T) / 2
''''''

n = A.shape[0]

eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvalues = eigenvalues.real
eigenvectors = eigenvectors.real
'''eigenvectors_adjusted = eigenvectors
for i in range (0, n):
    for j in range (0, n):
        eigenvectors_adjusted[i][j] *= eigenvalues[j]'''

print("Matrix A: \n", A.round(4), "")
print("Eigenvalues: ", eigenvalues.round(4))
print("Eigenvectors (columns): \n", eigenvectors.round(4))
#print("Eigenvectors adjusted by eigenvalues (columns): \n", eigenvectors_adjusted)

for i in range(n):
    print(f"\nEigenvalue {i+1}: {eigenvalues[i].round(4)}")
    print(f"Eigenvector {i+1}: {eigenvectors[:, i].round(4)}")

    left_side = np.dot(A, eigenvectors[:, i])
    right_side = eigenvalues[i] * eigenvectors[:, i]
    print("A * v: ", left_side.round(4))
    print("λ * v: ", right_side.round(4))
    print("Verification (A * v - λ * v): ", (left_side - right_side).round(4))