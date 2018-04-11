from SolutionsGenerator import *

class SolutionsGeneratorInterface:
    ''' Abstraction of the class SolutionsGenerator '''
    sg = 0
    def __init__(self, file_name):
        self.sg = SolutionsGenerator(file_name)

    def print_all_unsolved_errors(self):
        all_errors = self.sg.get_all_unsolved_errors()
        if(len(all_errors) == 0):
            print("No hay errores sin resolver!")
            return
        print("Todos los errores sin resolver:\n")
        for error in all_errors:
            print("ID: " + str(error[0]) + " - Error: '" + str(error[1]) + "' - TDA: " + str(error[2]))

    def print_all_unsolved_errors_from_tda(self):
        posibles_tdas = ["General", "TP0", "VD", "Pila", "Cola", "Lista", "Hash", "Heap", "ABB"]
        tda = ""
        while(tda not in posibles_tdas):
            tda = input("Ingrese el TDA elegido (opciones: "+ str(posibles_tdas) +"): ")
        all_errors = self.sg.get_unsolved_errors_from_tda(tda)
        if(len(all_errors) == 0):
            print("No hay errores sin resolver de ese TDA!")
            return
        print("Todos los errores sin resolver del tda "+ tda +":\n")
        for error in all_errors:
            print("ID: " + str(error[0]) + " - Error: '" + str(error[1]) + "' - TDA: " + str(error[2]))


    def add_solution_to_error(self):
        self.print_all_unsolved_errors()
        try:
            error_id = int(input("Ingrese el id del error a resolver: "))
        except:
            print("Id inválido. No es un valor decimal.")
            return
        if(not self.sg.error_not_resolved(error_id)):
            print("Id inválido. No hay un error sin resolver con ese id.")
            return
        solution = input("Ingrese la solución al error seleccionado: ")
        self.sg.solve_error(error_id, solution+'\n')
        print("Solución agregada!")

    def add_error_without_solution(self):
        error = input("Ingrese el error: ")
        posibles_tdas = ["General", "TP0", "VD", "Pila", "Cola", "Lista", "Hash", "Heap", "ABB"]
        tda = ""
        while(tda not in posibles_tdas):
            tda = input("Ingrese el TDA al que pertenece ese error (opciones: "+ str(posibles_tdas) +"): ")
        self.sg.add_error_without_solution(error, tda)
        print("Error sin solución agregado!")

    def add_error_with_solution(self):
        error = input("Ingrese el error: ")
        posibles_tdas = ["General", "TP0", "VD", "Pila", "Cola", "Lista", "Hash", "Heap", "ABB"]
        tda = ""
        while(tda not in posibles_tdas):
            tda = input("Ingrese el TDA al que pertenece ese error (opciones: "+ str(posibles_tdas) +"): ")
        solution = input("Ingrese la solución: ")
        self.sg.add_error_with_solution(error, tda, solution+'\n')
        print("Error y solución agregados!")



    def finish(self):
        self.sg.write_file()
