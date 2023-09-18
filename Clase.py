class Persona:
    #Atributos
    id=0
    nombre=""
    edad=0

    #Funciones Obligatorias
    #Constructor sin parametros
    """""
    def __init__(self):
        pass
    """""
     #Constructor con parametros y construtor por defaul


    def __init__(self,pId,pNombre,pEdad):
        self.id= pId
        self.nombre=pNombre
        self.edad=pEdad
#Getter
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
#setter
    def setId (Self,pId):
        Self.id=pId
    

    def setNombre(Self,pNombre):
        Self.nombre=pNombre

    def setEdad (Self,pEdad):
        Self.edad=pEdad

    #Funciones No obligatorias
    def __str__(self):#tostring
        return "La persona {} con nombre {}, tiene una edad de {}".format(self.id,self.nombre,self.edad)

    def calculoEdad(self):
        if(self.edad>18):
            print("La persona tiene {} entonces es mayor de edad".format(self.edad))
        
        else:
            ("La persona tiene {} entonces es menor de edad".format(self.edad))


    #Destructor
    def _del_(self):
        print ("El objeto va ser destruido")
    



personita=(1,"JOB",18)
print(personita.__str__())







