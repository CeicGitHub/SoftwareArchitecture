class Singleton:
    # Atributo de clase donde guardaremos la ÚNICA instancia creada
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        __new__ se ejecuta ANTES que __init__ y es quien realmente crea el objeto.
        Si ya hay una instancia guardada en _instance, la reutiliza.
        Si no, crea una nueva y la guarda.
        """
        if cls._instance is None:                  # ¿Ya existe?
            print("Creando nueva instancia...")    # Solo verás esto una vez
            cls._instance = super().__new__(cls)   # Crea la instancia real
        return cls._instance                       # Devuelve SIEMPRE la misma

    def __init__(self, valor):
        """
        __init__ se ejecuta cada vez que llamas a Singleton(...),
        aunque la instancia sea la misma.
        Aquí solo asignamos un atributo para que veas el efecto.
        """
        self.valor = valor


# --- Uso / demo ---
s1 = Singleton("A")   # Primera vez: se crea la instancia y luego se inicializa con "A"
s2 = Singleton("B")   # Segunda vez: NO se crea, pero sí se vuelve a llamar __init__ con "B"

print(s1.valor)       # Imprime "B" (porque s1 y s2 son el MISMO objeto)
print(s2.valor)       # Imprime "B"

# Comprobación de identidad (misma dirección en memoria)
print(id(s1), id(s2))
if id(s1) == id(s2):
    print("Singleton funciona: ambas variables tienen la misma instancia")
