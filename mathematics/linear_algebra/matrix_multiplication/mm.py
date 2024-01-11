# Last updated: 24-Nov-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to multiply two matrices

# ALL YOU NEED TO DO:
# Call matmul(a, b, c), where
#   where a and b are input matrices
#   of sizes (na1,na2) and (na2,nb2);
#   and c is the output multiplication
#   of matrices, with size (na1,nb2)

# NOTE:
# Matrices can be of any class as long as
#   * multiplies its elements and elements
#   of c can be directly modified
# If matrix A is of size (n1,n2), B is of size (n2,n3),
#   then C is of size (n1,n3)

def matmul(a, b, c):
    na1 = len(a);
    na2 = len(a[0])
    nb2 = len(b[0])
    for i in range(na1):
        for j in range(nb2):
            c[i][j] = 0
            for k in range(na2):
                c[i][j] += a[i][k] * b[k][j]
    return

# Input:
na1 = 3
na2 = 4
nb2 = 5
a = [[i+j for j in range(na2)] for i in range(na1)]
b = [[i-j for j in range(nb2)] for i in range(na2)]
c = [[0 for j in range(nb2)] for i in range(na1)]   # Output Array to store the result

# Calling function:
matmul(a, b, c)

# Printing input and output:
print("Matrix A:")
for t in a:
    print(t)
print()
print("Matrix B:")
for t in b:
    print(t)
print()
print("Matrix C = A * B:")
for t in c:
    print(t)

