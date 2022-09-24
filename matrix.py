import numpy as np
mat1 = np.array(list())
mat2 = np.array(list())
res = np.array(list())
m1 = list()
m2 = list()
rows = int(input("Enter the no of Rows [matrix A]: "))
cols = int(input("Enter the no of cols [matrix A]: "))
for i in range(0, rows):
    sub_lst = list()
    for x in range(0,cols):
        val = float(input("Enter row {}, col {}: ".format(i+1,x+1)))
        sub_lst.append(val)
    m1.append(sub_lst)
   
rows = int(input("Enter the no of Rows [matrix B]: "))
cols = int(input("Enter the no of cols [matrix B]: "))
for i in range(0, rows):
    sub_lst = list()
    for x in range(0,cols):
        val = float(input("Enter row {}, col {}: ".format(i+1,x+1)))
        sub_lst.append(val)
    m2.append(sub_lst)
mat1 = np.array(m1)
mat2 = np.array(m2)
    
    
def displayOptions():
    print("\nchoose '1' for Matrix Addn")
    print("choose '2' for Matrix Subn")
    print("choose '3' for  Scalar Matrix Muln")
    print("choose '4' for  Element Matrix Muln")
    print("choose '5' for  Matrix Muln")
    print("choose '6' for  Matrix Transpose")
    print("choose '7' for  Trace of Matrix")
    print("choose '8' for  Solve system of linear Eqns")
    print("choose '9' for  Determinant")
    print("choose '10' for  Inverse")
    print("choose '11' for  Singular Value Decomposition")
    print("choose '12' for  Eigen Value")
    print("choose '13' for  Search an Element")
    print("choose '14' for  Sum of Diff of U-Triangle and L-Triangle Matrix")
    print("choose '15' for  Exit the Program")
  
def matrixAddn():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    if numRows1 == numRows2 and numCols1 == numCols2:
        res = mat1+mat2
        print("Matrix Addition: ")
        print(res)
    else:
        print("Matrix Addition is not possible..")
    
def matrixSubn():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    if numRows1 == numRows2 and numCols1 == numCols2:
        res = mat1-mat2
        print("Matrix Subtraction: ")
        print(res)
    else:
        print("Matrix Subtraction is not possible..")
    
def scalar_matrixMul():
    sc = float(input("Enter a scalar: "))
    res = sc*mat1
    print("Scalar mul [Matrix A]: ")
    print(res)
    res = sc*mat2
    print("Scalar mul [Matrix B]: ")
    print(res)
    
def elemWise_matrixMul():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    if numRows1 == numRows2 and numCols1 == numCols2:
        res = mat1*mat2
        print("Element wise multiplication: ")
        print(res)
    else:
        print("Element wise matrix multiplication is not possible..")
    
def matrixMuln():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    # AXB BxC
    if numCols1 == numRows2:
        res = np.matmul(mat1, mat2)
        print("Matrix Multiplication: ")
        print(res)
    else:
        print("Matrix Multiplication is not possible..")

def matrixTranspose():
    print("Transpose [Matrix A]: ")
    print(mat1.transpose())
    print("Transpose [Matrix B]: ")
    print(mat2.transpose())
    
def traceMatrix():
    numRows1, numCols1 = mat1.shape
    numRows2, numCols2 = mat2.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    if numRows1 == numCols1:
        print("Trace [Matrix A]: {}".format(mat1.trace()))
    else:
        print("[Matrix A]: is not a square matrix")
        
    if numRows2 == numCols2:
        print("Trace [Matrix B]: {}".format(mat2.trace()))
    else:
        print("[Matrix B]: is not a square matrix")
    
def solveSystemEqns():
    print("Assume quations in standard form (a1x1+a2x2+a3x3+...aNxN = b1)")
    m = list()
    k = list()
    rows = int(input("Enter the no of equations to be solved: "))
    for i in range(0, rows):
        sub = list()
        for x in range(0,rows):
            val = float(input("Enter coeff {} in [equation {}]: ".format(x+1, i+1)))
            sub.append(val)
        cns = float(input("Enter the constant in [equation {}]: ".format(i+1)))
        k.append(cns)
        m.append(sub)
    coeff_Matrix = np.array(m)
    cnst_mat = np.array(k)
    
    # checking for singularity in matrix (in this case no solution exists)
    if(np.linalg.det(coeff_Matrix)==0):
        print("No solution exists. Because coeff matrix is singular..")
    else:
        print("The solutions for the set of provided equations is: ")
        print(np.linalg.solve(coeff_Matrix, cnst_mat))
    
def determinant_Matrix():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    
    if numRows1 == numCols1:
        print("Determinant [Matrix A]: {}".format(np.linalg.det(mat1)))
    else:
        print("Matrix A is not a square matrix [determinant DNE]")
    if numRows2 == numCols2:
        print("Determinant [Matrix B]: {}".format(np.linalg.det(mat2)))
    else:
        print("Matrix B is not a square matrix [determinant DNE]")
        
def inverse_matrix():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    
    if(numRows1 == numCols1):
        # if det(matrix) is 0, inverse doesnt exists
        if(np.linalg.det(mat1)==0):
            print("Inverse doesnt exists for [Matrix A]: Singular Matrix")
        else:
            print("Inverse [Matrix A]: ")
            print(np.linalg.inv(mat1))
    else:
        print("[Matrix A] is not a square matrix")
    
    if(numRows2 == numCols2):
        if(np.linalg.det(mat2)==0):
            print("Inverse doesnt exists for [Matrix B]: Singular Matrix")
        else:
            print("Inverse [Matrix B]: ")
            print(np.linalg.inv(mat2))
    else:
        print("[Matrix B] is not a square matrix")

def singularValue_decomposition():
    U, s, VT = np.linalg.svd(mat1)
    print("Singular value decomposition of matrix A: ")
    print("> ",U)
    print("> ",s)
    print("> ",VT)
    
    U, s, VT = np.linalg.svd(mat2)
    print("\nSingular value decomposition of matrix B: ")
    print("> ", U)
    print("> ",s)
    print("> ",VT)
    
def eigenValue():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    
    if numRows1 == numCols1:
        eigValues, eigVect = np.linalg.eig(mat1)
        print("Eigen values of [Matrix A]: {}".format(eigValues))
    else:
        print("[Matrix A] is not a square Matrix")
    
    if numRows2 == numCols2:
        eigValues, eigVect = np.linalg.eig(mat2)
        print("Eigen values of [Matrix B]: {}".format(eigValues))
    else:
        print("[Matrix B] is not a square Matrix")
    
def searchElem():
    elem = float(input("Enter a element to be searched [from Matrix A]: "))
    pos = np.where(mat1 == elem)
    print(pos)
    
    elem = float(input("Enter a element to be searched [from Matrix B]: "))
    pos = np.where(mat2 == elem)
    print(pos)
    
def diff_sum_Ut_Lt():
    numRows1, numCols1 = mat1.shape
    print("[Matrix A]: rows- {}, cols- {}".format(numRows1, numCols1))
    numRows2, numCols2 = mat2.shape
    print("[Matrix B]: rows- {}, cols- {}".format(numRows2, numCols2))
    
    if numRows1 == numCols1:
        sum_low=0
         # lower triangular matrix
        for i in range(0, numRows1):
            for j in range(0, i+1):
                sum_low+=mat1[i][j]
                
        sum_up=0
         # upper triangular matrix
        for i in range(0, numRows1):
            for j in range(i, numRows1):
                sum_up+=mat1[i][j]
        print("DIfference of sum of UT Matrix and LT Matrix in [Matrix A]: {}".format(sum_up-sum_low))
    else:
        print("[Matrix A] is not a square Matrix")
    
    if numRows2 == numCols2:
        sum_low=0
         # lower triangular matrix
        for i in range(0, numRows2):
            for j in range(0, i+1):
                sum_low+=mat2[i][j]
                
        sum_up=0
         # upper triangular matrix
        for i in range(0, numRows2):
            for j in range(i, numRows2):
                sum_up+=mat2[i][j]
        print("DIfference of sum of UT Matrix and LT Matrix in [Matrix B]: {}".format(sum_up-sum_low))
    else:
        print("[Matrix B] is not a square Matrix")

b = True
while b:
    displayOptions()
    ch = int(input("Enter your choice: "))
    if ch == 1:
        matrixAddn()
    elif ch == 2:
        matrixSubn()
    elif ch == 3:
        scalar_matrixMul()
    elif ch == 4:
        elemWise_matrixMul()
    elif ch == 5:
        matrixMuln()
    elif ch == 6:
        matrixTranspose()
    elif ch == 7:
        traceMatrix()
    elif ch == 8:
        solveSystemEqns()
    elif ch == 9:
        determinant_Matrix()
    elif ch == 10:
        inverse_matrix()
    elif ch == 11:
        singularValue_decomposition()
    elif ch == 12:
        eigenValue()
    elif ch == 13:
        searchElem()
    elif ch == 14:
        diff_sum_Ut_Lt()
    elif ch == 15:
        b = False
    else:
        print("[CHOICE_ERROR]: incorrect choice.. Try Again..")