import hashlib

flg = "irisFLG{bRut3F0rC3d}"
flg1 = "bRut3F0rCed"

f = open("hash.txt",'r')
res = f.readline()

print(res == hashlib.sha256(flg.encode()).hexdigest())
print(len(flg1))