def agregarHorizontal(matriz,posicionI,posicionJ,valor):
    contador=0
    if(matriz[posicionI][posicionJ]==0 and matriz[posicionI][posicionJ+1]==0):
        while(contador<2):
            matriz[posicionI][posicionJ]=valor
            posicionJ=posicionJ+1
            contador=contador+1
    elif(matriz[posicionI][posicionJ]==0 and matriz[posicionI][posicionJ-1]==0):
        while(contador<2):
            matriz[posicionI][posicionJ]=valor
            posicionJ=posicionJ-1
            contador=contador+1
    return matriz
def agregarVertical(matriz,posicionI,posicionJ,valor):
    contador=0
    entro=0
    while(contador<2):
        if(matriz[posicionI][posicionJ]==0):
            if(posicionI+1==n):
                if(entro==1):
                    matriz[posicionI][posicionJ]=valor
                return matriz
            else:
                entro=entro+1
                matriz[posicionI][posicionJ]=valor
                contador=contador+1
                posicionI=posicionI+1
                
    return matriz

def recorrerMatriz(matriz,n,m,i=0,j=0,contador=0):    
    if(i<n and j<m):
            contador=contador+1
            if(i%2==0):
                if (contador==0 and matriz[i][j]==0):
                    matriz=agregarHorizontal(matriz,i,j,contador)
                    matriz=recorrerMatriz(matriz,n,m,i,j+2,contador)
                elif (matriz[i][j]==0):
                    if(j==m-2 or j==m-1):
                        matriz=agregarVertical(matriz,i,j,contador)
                        if(j==m-1):
                            if(matriz[i-1][j-1]!=0):
                                matriz=recorrerMatriz(matriz,n,m,i+1,j-2,contador)
                            else:
                                matriz=recorrerMatriz(matriz,n,m,i+1,j-1,contador)
                        else:
                            matriz=recorrerMatriz(matriz,n,m,i,j+1,contador)      
                    else:
                        matriz=agregarHorizontal(matriz,i,j,contador)
                        matriz=recorrerMatriz(matriz,n,m,i,j+2,contador)

            elif(i%2!=0):
                if(j%2==0 and j>1):
                    j=j+1
                    if(j==m-1):
                        j=j-2
                if (matriz[i][j]==0):
                    if((j==0 and i>0) or (j==1 and i>0)):
                        matriz=agregarVertical(matriz,i,j,contador)
                        if(j==0):                            
                            matriz=recorrerMatriz(matriz,n,m,i+1,j+2,contador)
                        else:
                            
                            matriz=recorrerMatriz(matriz,n,m,i,j-1,contador)  
                    else:
                        
                        matriz=agregarHorizontal(matriz,i,j,contador)
                        matriz=recorrerMatriz(matriz,n,m,i,j-2,contador)
    if(j==1 and i==n-1):
        matriz=agregarHorizontal(matriz,i,j,contador)
    return matriz



#principal
n = 7
m = 7
#a = n*m
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(0)

matriz = recorrerMatriz(matriz,n,m)
#print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(matriz[3])
print(matriz[4])
print(matriz[5])
print(matriz[6])