'''
Existem 3 tipo de recursos: Public, private and protected

Membros privados de uma classe tem acesso negado de fora da classe,
podendo ser manipuladores somento de dentro da classe.

Membros publico são acessiveis de fora da classe. É necessario um 
objeto da classe para invocar um método público.

Os membros protegidos de uma classe são acessíveis de dentro da classe
e também estão disponíveis para suas subclasses. Nenhum outro ambiente
tem acesso permitido.

'''

#  ----- Atributo publico -----

class employee_public:
    def __init__(self, name1, sal1):
        self.name1 = name1
        self.salary1 = sal1

#  ----- Atributo protegido -----
''' Pode ser acessado apenas na classe e nas subclasses (Na teoria)
Na verdade o '_' indica para os programadores que essas variáveis
devem ser ateradas apenas dentro da classe e subclasses
'''
class employee_protected:
    def __init__(self, name2, sal2):
        self._name2 = name2  # protected attribute 
        self._salary2 = sal2 # protected attribute

#  ----- Atributo privado -----
''' Da um forte sugestão para não tocar de fora da classe
'''
class employee_private:
    def __init__(self, name3, sal3):
        self.__name3 = name3  # private attribute 
        self.__salary3 = sal3 # private attribute


# ---------------------------------------------------- Public
employee_wesley1 = employee_public("Wesley", 10000)
print(employee_wesley1.salary1) # Consigo acessar a variavel de fora da classe

# ---------------------------------------------------- Protected
employee_wesley2 = employee_protected("Wesley", 11000)
print(employee_wesley2._salary2)
# ---------------------------------------------------- Private
employee_wesley3 = employee_private("Wesley", 12000)
print(employee_wesley3.__salary3)