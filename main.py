from SolutionsGeneratorInterface import *

def main():
    sg = SolutionsGeneratorInterface("solutions.txt")
    opciones = "A continuación las opciones: \n\
    1-Agregar un error con solución\n\
    2-Agregar un error sin solución\n\
    3-Ver todos los errores sin resolver\n\
    4-Ver todos los errores sin resolver de un determinado TDA\n\
    5-Resolver un error existente\n\
    6-Salir"
    input_usuario = 0
    while(input_usuario != 6):
        print("\n\nBienvenido")
        print(opciones)
        try:
            input_usuario = int(input("Ingrese el código de la opción elegida: "))
        except:
            print("Opción no válida. No es decimal.")
            continue
        if(input_usuario == 1):
            sg.add_error_with_solution()
            sg.finish()
        elif(input_usuario == 2):
            sg.add_error_without_solution()
            sg.finish()
        elif(input_usuario == 3): sg.print_all_unsolved_errors()
        elif(input_usuario == 4): sg.print_all_unsolved_errors_from_tda()
        elif(input_usuario == 5):
            sg.add_solution_to_error()
            sg.finish()
        elif(input_usuario == 6): break
        else: print("Opción no válida. No es una de las opciones posibles.")
main()
