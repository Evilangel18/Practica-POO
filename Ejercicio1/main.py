from Email import Email
from menu import Menu
import sys
def test():
    return

cuenta= Email()
xmenu = Menu()
x = False
while x == False:
 op= int(input('Ingrese la operacion que desea realizar:\n|1|Registrar nueva cuenta.\n|2|Cambiar la contraseña de la cuenta creada anteriormente\n|3|Cargar correos desde un archivo csv.\n|4|Salir\n'))
 if op == 1 or 2 or 3:
     xmenu.manejoMenu(op,cuenta)
 elif op == 3:
     xmenu.manejoMenu(op)
 else:
     sys.exit()