CAN1=0
CAN2=0
CAN3=0
CAN4=0
VOTO=int(input("Ingrese para quién es el voto (Candidato 1-4): "))
while (VOTO!=0):
    if VOTO==1:
        CAN1+=1
    elif VOTO==2:
        CAN2+=1
    elif VOTO==3:
        CAN3+=1
    elif VOTO==4:
        CAN4+=1
    VOTO=int(input("Ingrese para quién es el voto (Candidato 1-4): "))
SUMV=CAN1+CAN2+CAN3+CAN4
POR1=(CAN1/SUMV)*100
POR2=(CAN2/SUMV)*100
POR3=(CAN3/SUMV)*100
POR4=(CAN4/SUMV)*100
print("El total de los votos del candidato 1 es de: ",CAN1)
print("El porcentaje de los votos del candidato 1 es de: ",POR1)
print("El total de los votos del candidato 2 es de: ",CAN2)
print("El porcentaje de los votos del candidato 2 es de: ",POR2)
print("El total de los votos del candidato 3 es de: ",CAN3)
print("El porcentaje de los votos del candidato 3 es de: ",POR3)
print("El total de los votos del candidato 4 es de: ",CAN4)
print("El porcentaje de los votos del candidato 4 es de: ",POR4)
print("El total de los votos es de: ",SUMV)

