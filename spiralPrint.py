import re
from urllib.request import urlopen
import validators

def spiralPrint(url):
    if not(validators.url(url)):
        raise ValueError('invalid url!')
    html = urlopen(url).read()
    data = bytes.decode(html, encoding='utf-8')

    if(all(x == data[0] for x in data)):
        return data
    if(len(data) % 2 != 0):
        raise ValueError('this is not a square matrix!')
    dataList = re.findall(r'\d+', data)
    try:
        dataListint = [int(i) for i in dataList]
        for i in dataListint:
            if(i < 0):
                raise ValueError('all elements of the matrix must be positive!')
    except ValueError:
        raise ValueError('the matrix contains non-integers!')
    size = int(len(dataListint) ** (1 / 2)) #matrix size
    matrix = [dataListint[i:i + size] for i in range(0, len(dataListint), size)]


    n = size
    m = size
    k = 0
    l = 0
    res = []
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            res.append(matrix[i][k])
            # print(matrix[i][k], end=" ")

        k += 1
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            res.append(matrix[n - 1][i])
            # print(matrix[n - 1][i], end=" ")

        n -= 1




        # Print the first column from
        # the remaining columns
        if (k < m):
            for i in range(n - 1, l - 1, -1):
                res.append(matrix[i][m - 1])
                # print(matrix[i][m - 1], end=" ")

            m -= 1


        # Print the last row from
        # the remaining rows
        if (l < n):
            for i in range(m - 1, (k - 1), -1):
                res.append(matrix[l][i])
                # print(matrix[l][i], end=" ")

            l += 1

    return res