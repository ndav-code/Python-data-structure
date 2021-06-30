def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    
    diagnal1=[]
    diagnal2=[]

    for i in range(0, len(matrix)):
        diagnal1.append(matrix[i][i])
        diagnal2.append(matrix[i][len(matrix)-1-i])  

    return sum(diagnal1) + sum(diagnal2)