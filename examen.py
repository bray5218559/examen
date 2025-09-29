from abc import ABC, abstractmethod

# Excepción personalizada
class SalarioInvalidoExceptionB16(Exception):
    pass

# Clase abstracta
class EmpleadoB16(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self.rfc = rfc
        self.apellidos = apellidos
        self.nombres = nombres

    def mostrar(self):
        return f"RFC: {self.rfc}, Nombre: {self.nombres} {self.apellidos}"

    @abstractmethod
    def ingresos(self):
        pass

    @abstractmethod
    def descuentos(self):
        pass

    @abstractmethod
    def sueldo_neto(self):
        pass


# Clase hija: Vendedor
class EmpleadoVendedorB16(EmpleadoB16):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
        if self.ingresos() < 150:
            raise SalarioInvalidoExceptionB16("El ingreso de vendedor es menor al mínimo (150).")

    def ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def bonificacion(self):
        ing = self.ingresos()
        if ing < 1000:
            return 0
        elif ing <= 5000:
            return ing * 0.05
        else:
            return ing * 0.10

    def descuentos(self):
        ing = self.ingresos()
        if ing < 1000:
            return ing * 0.11
        else:
            return ing * 0.15

    def sueldo_neto(self):
        return self.ingresos() + self.bonificacion() - self.descuentos()

    def __str__(self):
        return f"{self.mostrar()} | Vendedor -> Neto: {self.sueldo_neto():.2f}"


# Clase hija: Permanente
class EmpleadoPermanenteB16(EmpleadoB16):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, nss):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.nss = nss
        if self.sueldo_base < 150:
            raise SalarioInvalidoExceptionB16("El sueldo base es menor al mínimo (150).")

    def ingresos(self):
        return self.sueldo_base

    def descuentos(self):
        return self.sueldo_base * 0.11

    def sueldo_neto(self):
        return self.ingresos() - self.descuentos()

    def __str__(self):
        return f"{self.mostrar()} | Permanente -> Neto: {self.sueldo_neto():.2f}"


# --- MAIN PARA PROBAR ---
if __name__ == "__main__":
    empleados = [
        EmpleadoVendedorB16("RFCB16A", "Lopez", "Luis", 6000, 0.12),
        EmpleadoPermanenteB16("RFCB16B", "Perez", "Lucia", 3500, "NSS001")
    ]

    total = 0
    for e in empleados:
        print(e)
        total += e.sueldo_neto()
    print(f"Total nómina B16: {total:.2f}")

