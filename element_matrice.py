# Dimensions de la matrice
row = int(input("Entrer le nombre de ligne"))
col= int(input("Entrer le nombre de colonne"))
A = []
for i in range(row):
	A.append([0]*col)
	for j in range(col):
		A[i][j] = int(input("Entrer les elements de la matrice"))
print(A)