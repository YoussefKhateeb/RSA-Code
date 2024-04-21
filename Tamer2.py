import math
def calculate_phi_n(p, q):
    return (p - 1) * (q - 1)
def brute_force_private_exponent(N, e, phi_n):
    for d in range(1, phi_n + 1):
        if (d * e) % phi_n == 1:
            return d
    return None  

N = 143 
e = 7 
p = 11  
q = 13   


phi_n = calculate_phi_n(p, q)


d = brute_force_private_exponent(N, e, phi_n)

if d is not None:
    print("Private exponent (d):", d)
else:
    print("Private exponent not found within phi_n limit")
message=20
print(message)
cipher = pow(message, e, N)
print(cipher)
decipher = pow(cipher,d,N)
print(decipher)