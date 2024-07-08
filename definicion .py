class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # Encapsulación del salario como atributo privado

    def calcular_pago(self):
        return self.__salario

    def __str__(self):
        return f"Empleado: {self.nombre}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def calcular_pago(self):  # Polimorfismo: sobrescritura del método calcular_pago
        return (self.
                _Empleado__salario + 1000)  # Aumento de salario para gerentes
    def __str__(self):
        return f"Gerente: {self.nombre}, Departamento: {self.departamento}"

    # Crear instancias de Empleado y Gerente
    empleado1 = Empleado("Juan Pérez", 50000)
    gerente1 = Gerente("María Rodríguez", 70000, "Ventas")

    # Mostrar información de los empleados
    print(empleado1)
    print(f"Salario de {empleado1.nombre}: ${empleado1.calcular_pago()}")

    print()

    print(gerente1)
    print(f"Salario de {gerente1.nombre}: ${gerente1.calcular_pago()}")