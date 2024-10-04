class Animal:
    def __init__(self,info,dormir,passear):
       self.info = info
       self.dormir = dormir
       self.passear = passear
       
    def animal_info (self):
        return self.info
    
    def animal_dormir (self):
        return {self.dormir}
    
    def animal_passear (self):
        return{self.passear}
    
class Gato(Animal):
    def __init__(self,nome,idade,dono, info,dormir,passear):
        self.nome = nome
        self.idade = idade
        self.dono = dono
        
        Animal.__init__(self,info,dormir,passear)
                
    def Gato_nome (self):
        return {self.nome}
    def Gato_idade (self):
        return {self.idade}
    def Gato_dono (self):
        return {self.dono}
    
class Coelho(Animal):
    def __init__(self,nome,idade,sexo,info,dormir,passear):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
        Animal.__init__(self,info,dormir,passear)
   
        
    def Coelho_nome (self):
        return {self.nome}
    def Coelho_idade (self):
        return {self.idade}
    def Coelho_sexo (self):
        return {self.sexo}
    
class Cachorro(Animal):
    def __init__(self,nome,idade,racao,info,dormir,passear):
        self.nome = nome
        self.idade = idade
        self.racao = racao
        
        Animal.__init__(self,info,dormir,passear)
   
        
    def Cachorro_nome (self):
        return {self.nome}
    def Cachorro_idade (self):
        return {self.idade}
    def Cachorro_racao (self):
        return {self.racao}
 
Animal1=Gato("Pantera",8,"André","linda",True,False)

print(Animal1.nome)