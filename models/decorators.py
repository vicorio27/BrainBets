def decorador(f):
    def funcion_nueva():
        print("Funcionalidad extra")
        f()

    return funcion_nueva


@decorador
def funcion_inicial():
    print("Funcionalidad inicial")


funcion_inicial()

# OUTPUT
# Funcionalidad extra
# Funcionalidad inicial
