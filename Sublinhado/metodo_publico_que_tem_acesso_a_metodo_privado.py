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

    def altera_salario(self):
        self.salary1 = self.salary1 + 1

        return self.salary1

class employee_protected:
    def __init__(self, name2, sal2):
        self._name2 = name2  # protected attribute 
        self._salary2 = sal2 # protected attribute
    def altera_salario(self):
        self._salary2 = self._salary2 + 2

        return self._salary2

class employee_private:
    def __init__(self, name3, sal3):
        self.__name3 = name3  # private attribute 
        self.__salary3 = sal3 # private attribute
    def altera_salario(self):
        self.__salary3 = self.__salary3 + 3

        return self.__salary3

class employee_private2:
    def __init__(self, name3, sal3):
        self.__name3 = name3  # private attribute 
        self.__salary3 = sal3 # private attribute
    
    def __altera_salario(self):
        self.__salary3 = self.__salary3 + 4
        return self.__salary3
    
    def roda_altera_salario(self):
        return self.__altera_salario()

print('PUBLIC')
e1 = employee_public("Wesley", 1000)
print(e1.name1)
novo_salary1 = e1.altera_salario()
print(novo_salary1)

print('PROTEGIDO')
e2 = employee_protected("Wesley", 1000)
print(e2._name2)
novo_salary2 = e2.altera_salario()
print(novo_salary2)

print('PRIVADO')
e3 = employee_private("Wesley", 1000)
#print(e3.__name3)  --> Nao tenho permissao para acessar de fora
novo_salary3 = e3.altera_salario() # Mas o metodo é publico e posso usar
print(novo_salary3)

print('PRIVADO')
e4 = employee_private2("Wesley", 1000)
#print(e4.__name3)  --> Nao tenho permissao para acessar de fora
#novo_salary4 = e3.__altera_salario() # Não tenho permissao para acessar esse método
novo_salary4 = e4.roda_altera_salario() # Mas posso rodar um metodo que tem acesso a o metodo privado
print(novo_salary4)