import random 
class Robo:
    nivel_critico = 0.50
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = random.uniform(0,1)

    def __repr__(self):
       return f"Robo = nome: {self.nome} | vida: {self.vida:.2f}"
    
    def __add__(self, novoRobo):
        nomePart1 = self.nome.split("-")[0]
        nomePart2 = novoRobo.nome.split("-")[0]
        nomeBebe = f"${nomePart1} - ${nomePart2}"
        return nomeBebe

    def precisa_de_medico(self):
        if(self.vida < Robo.nivel_critico):
            return True
        else:
            return False
#Criar robo
r1 = Robo("Capitao-america")
r2 = Robo("Sol-Scarlat")
print(r1)
print(r2)
#Testando precisa de medico
print(r1.precisa_de_medico())  
print(r2.precisa_de_medico()) 

# Reprodução de robôs
robo_bebe =r1 + r2
print(robo_bebe)  # Exemplo de Robo(nome=Robo1-Robo2, vida=0.53)