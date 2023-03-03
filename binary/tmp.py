flag = "irisFLG{IaMsUrEyOuDiDnOtBrUtEfOrCeMe}"
x=""
for i in range(len(flag)):
    x = x+"if(flg.charAt("+str(i)+") != '"+flag[i]+"'){\n\tSystem.out.println(\"Incorrect flag\");\n\treturn;\n}\n"
print(x)
print(len(flag))
print(len("IaMsUrEyOuDiDnOtBrUtEfOrCeMe"))