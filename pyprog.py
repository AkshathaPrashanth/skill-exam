
def set_min(A):
    mini = float('inf')  
    for num in A:
        if num < mini:
            mini = num
    return mini

def set_max(A):
    maxi = float('-inf')  
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

# Driver code
if __name__ == "__main__":
    A = [4, 9, 6, 5, 2, 3]
    N = len(A)
    print("Minimum element is:", set_min(A))
    print("Maximum element is:", set_max(A))
