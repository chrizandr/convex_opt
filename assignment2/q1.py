from cvxpy import *
import numpy as np
# Initialising random seed
np.random.seed(1)
# Size of matrix
n = 10
# Constant parameters
gamma1 = 3
gamma2 = 2
gamma3 = 1
# Randomly generated vectors x1, x2 and x3
x1 = np.random.randn(n, 1)
x2 = np.random.randn(n, 1)
x3 = np.random.randn(n, 1)

# Define a variable semidefinite matrix of size n X n
X = Semidef(n)
# Define the objective function
obj = Minimize(trace(X))
# Constraints for the problem
constr1 = (X == X.T)    # Symmetric
constr2 = (X >> 0)      # Positive semidefinite
constr3 = ((x1.T * X) * x1 >= gamma1)       # Problem constraint 1
constr4 = ((x2.T * X) * x2 >= gamma2)       # Problem constraint 2
constr5 = ((x3.T * X) * x3 >= gamma3)       # Problem constraint 3

# Combining problem with constraints
prob = Problem(obj , [constr1, constr2, constr3, constr4, constr5])
# Solving
print("Optimal value is", prob.solve())
print("The matrix is:")
# X* or optimal point
print(X.value)

# Checking if all eigen values are positive
X_num = np.array(X.value , dtype=np.float)
print("Eigen values are:")
print(np.linalg.eigvalsh(X_num))

# NOTE: Negative values are extremely small and can be regarded to be zeros
