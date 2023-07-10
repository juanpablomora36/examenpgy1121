from os import system
system("cls")
#SECCION DE LISTAS Y GUARDADOS
cant_entr=0
tot_tot=0
tot_pla=0
tot_gol=0
tot_silv=0
cant_pla=0
cant_gold=0
cant_silv=0
platinum=["1", "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9", "10"]
gold=["21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]
silver=["51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
"71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
"81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
"91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
asis=[]
ent_tot=[[platinum], [gold], [silver]]

#SECCION DE COMANDO PRINCIPAL
while True:
    op=input("""
Bienvenido a Creativos.cl
 1. Comprar entradas
 2.Mostrar ubicaciones disponbles
 3.ver listado de asistencia
 4.Mostrar ganancias totales
 5.Salir
    """)
    match op:
        case "1":
            while True:
                ru=int(input("Antes de continuar ingrese run sin punto ni codigo verificador: "))
                if ru<=50000000 and ru>=9999999:
                     print("run guardado con exito.")
                     asis.append(ru)
                     break
                     
                else:
                   print("Ingrese run valido.")
                   

            while True:
                cant=int(input("""Ingrese cantidad de entradas; recuerde que solo se pueden 1, 2 o 3: 
                    """))
                    
                if cant<=3:
                    break
                else:
                   print("Ingrese numero de entradas validas.")
            for i in range (cant):
                print(f"Seleccione ubicación persona {i+1} ")
                print(ent_tot)
                ub=int(input(""))
             #UBICACION PLATINUM
                if ub<=20:
                    tot_pla=cant*120000
                    for ub in platinum:
                        platinum[ub]="x"

            #UBICACION GOLD
                elif ub<=50:
                    tot_gol=cant*80000
                    for ub in gold:
                        gold.remove(ub)
            #UBICACION SILVER
                elif ub<=100:
                    tot_silv=cant*50000
                    for ub in silver:
                        silver.insert(ub, "x")


    #CASO 2
        case "2":
            print(*platinum)
            print(*gold)
            print(*silver)
        case "3":
            asis.sort
            print(asis)
        case "4":
            print(f"""
TIPO DE ENTRADA         CANTIDAD            TOTAL
PLATINUM 120000        {cant_pla}          {tot_pla}
GOLD     80000         {cant_gold}         {tot_gol}
SILVER   50000         {cant_silv}         {tot_silv}
TOTAL                  {cant_entr}         {tot_tot} """)

        case "5":
            print("Gracias por elegir Creativos.cl Hasta la proxima ")
            break
        case other:
            print("Ingrese valor valido.")
















