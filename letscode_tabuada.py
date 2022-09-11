
i = -1

while i != 0 :
    print("Para sair do sistema digite 0")
    i =float(input("digite um numero inteiro para lhe mostrar sua tabuada:"))
    if i != 0:
            for t in range(11):
                m = float(t * i)
                print(f" tabuada {t} X {i} = {m}")
    else:
        break
        