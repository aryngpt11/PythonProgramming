def power_a_b(a,b):
    if b==0:
        return 1
    ans=a*power_a_b(a,b-1)
    return ans
print(power_a_b(2,4))