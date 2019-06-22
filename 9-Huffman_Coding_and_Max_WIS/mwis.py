def mwis(weights):
    weights = [None] + weights  # Pad with None to ensure indices match with A
    A = [0, weights[1]]

    for i in range(2, len(weights)):
        A.append(max(A[i-1], A[i-2] + weights[i]))

    return A


def reconstruct(A, weights):
    weights = [None] + weights
    S =[]
    i = len(A) - 1
    while i >= 1:
        if A[i-1] >= A[i-2] + weights[i]:
            i = i -1
        else:
            S.append(i)
            i = i - 2
            
    return S


def make_binary_string(S):
    binary_string = ['0'] * 8
    for i, node in enumerate([1, 2, 3, 4, 17, 117, 517, 997]):
        if node in S:
            binary_string[i] = '1'
    binary_string = ''.join(binary_string)

    return binary_string


if __name__ == '__main__':
    weights = [1, 4, 5, 4]

    A = mwis(weights)
    print(A)

    S = reconstruct(A, weights)
    print(S)

