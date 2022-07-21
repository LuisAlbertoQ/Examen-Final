class Usuario:
    
    def __init__(self, dni, nombres_apellidos, direccion, telefono, email):
        self.dni = dni
        self.nombres_apellidos = nombres_apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return "{}; {}; {}; {}; {}\n".format(
            self.dni, self.nombres_apellidos, self.direccion, self.telefono, self.email
        )