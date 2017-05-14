class Perceptron:
    def __init__(self, entradas, salidas):
        self.entradas = entradas  # xi
        self.salidas = salidas  # ti
        self.pesos = [0, 0, 0]  # wi
        self.conta= 0

    def recalcularPesos(self, pesoj, ti, xi):
        return (pesoj + 0.5 * ti * xi)

    def pesosAleatorios(self):
        import random
        # Otener pesos aleatorios
        for j in range(len(self.pesos)):
            self.pesos[j] = random.random()  # pesos aleatorios
            print("Peso", j, "=", self.pesos[j])

    # Funcion para que aprenda
    def Aprendizaje(self):
        yi = 0  # salida calculada
        i = 0  # control del proceso
        while(i < len(self.entradas)):
            yi = self.pesos[0] * self.entradas[i][0] + self.pesos[1] * self.entradas[i][1] + self.pesos[2] * self.entradas[i][2]
            if yi >= 0:
                yi = 1
            else:
                yi = -1

            if yi == self.salidas[i]:
                print("Correcto", self.salidas[i], "y=", yi)
            else:
                print("Entrada = Salida")
                print("Incorrecto", self.salidas[i], "y=", yi)
                print("Correcion de pesos:")
                for n in range(len(self.pesos)):
                    self.pesos[n] = self.recalcularPesos(
                        self.pesos[n], self.salidas[i], self.entradas[i][n])
                    print("Peso", n, ":",self.pesos[n])
                print("--------------Recalcular---------")
                i = -1  # para recalcular
            i = i+1
            self.conta= self.conta+1
            input()
        print("Iteraciones:",self.conta)

# Iniciar
#Con los 0's se cicla
#salidas = [0, 1, 1, 1]  # Compuerta OR [0,1,1,1] Compuertan AND [0,0,0,1]
#entradas = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
salidas = [-1, 1, 1, 1]  # Compuerta OR [0,1,1,1] Compuertan AND [0,0,0,1]
entradas = [[-1, -1, -1], [-1, 1, -1], [1, -1, -1], [1, 1, -1]]
perceptron = Perceptron(entradas, salidas)
perceptron.pesosAleatorios()
perceptron.Aprendizaje()
