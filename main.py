from clases.operaciones import Operaciones

def main():
    print("\t------- Bienvenido a la calculadora mágica -------\nIngrese los dos números\n")
    op = Operaciones()
    op.leerNumeros()
    
    print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. División\n5. Residuo\n6. Salir")

    while True:
        o = int(input("\nPor favor, elige una opción: "))
        match o:
            case 1:
                op.sumar()
                break
            case 2:
                op.restar()
                break
            case 3:
                op.multiplicar()
                break
            case 4:
                op.dividir()
                break
            case 5:
                op.residuo()
                break
            case 6:
                print("Saliendo...")
                break
            case _:
                print("El dato no es válido.")    
    op.mostrarResultado()
    print("\nGracias por usar la calculadora mágica")
    
if __name__ == "__main__":
    main()