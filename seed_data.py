from Trabajo.models import familiar

familiar( nombre="Ezequiel", parentesco="Hermano", ocupacion= 'Arquitecto', DNI=12312400, edad=26).save()
familiar( nombre="Viviana", parentesco="Madre", ocupacion='Profesora', DNI=12312900, edad=56).save()
familiar( nombre="Luis", parentesco="Padre", ocupacion='Contador', DNI=12312300, edad=60).save()
familiar( nombre="Damian", parentesco="Tio", ocupacion='Abogado', DNI=12312399, edad=50).save()
familiar( nombre="Carolina", parentesco="Prima", ocupacion='Medica', DNI=12312355, edad=30).save()

print("Se cargo correctamente")