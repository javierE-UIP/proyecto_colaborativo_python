import matematicas
import cuento
import utilidades

def main():
    utilidades.bienvenida("Equipo")

    print("Suma:", matematicas.suma(10, 5))
    print("Resta:", matematicas.resta(10, 5))
    print("Multiplicación:", matematicas.multiplicacion(10, 5))
    print("División:", matematicas.division(10, 5))

    cuento.imprimir_cuento()
    utilidades.despedida()

if __name__ == "__main__":
    main()