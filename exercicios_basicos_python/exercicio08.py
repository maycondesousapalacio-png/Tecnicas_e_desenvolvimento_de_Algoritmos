# Peça ao usuário um número e exiba a soma de seus dígitos.
num=input("Informe um número de 5 dígitos: ")
dig1=dig2=dig3=dig4=dig5=0

dig1+=int(num[0])
dig2+=int(num[1])
dig3+=int(num[2])
dig4+=int(num[3])
dig5+=int(num[4])
soma=dig1+dig2+dig3+dig4+dig5
print(soma)
