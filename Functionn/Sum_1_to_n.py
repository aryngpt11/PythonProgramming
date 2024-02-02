def sum_1_to_n(n):
    if n==1:
        return 1
    ans=n+sum_1_to_n(n-1)
    return ans
print(sum_1_to_n(6))