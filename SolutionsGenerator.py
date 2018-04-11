class SolutionsGenerator:
    ''' SolutionsGenerator helps you generate the common error and solutions file '''

    file_name = ""
    all_errors = {}
    not_solved_errors = []
    last_id = 0


    def __init__(self, file_name):
        self.file_name = file_name
        file = open(file_name, "r");
        for line in file:
            id, error, tda, solution = line.split('-')
            self.all_errors[int(id)] = [error,tda,solution]
            if(solution == '\n'): self.not_solved_errors.append(int(id))
            if(self.last_id < int(id)): self.last_id = int(id)
        file.close()

    def add_error_without_solution(self, error, tda):
        self.all_errors[self.last_id+1] = [error, tda, '\n']
        self.not_solved_errors.append(self.last_id+1)
        self.last_id += 1

    def add_error_with_solution(self, error, tda, solution):
        self.all_errors[self.last_id+1] = [error, tda, solution]
        self.last_id += 1

    def solve_error(self, error_id, solution):
        self.all_errors[error_id][2] = solution
        self.not_solved_errors.remove(error_id)

    def error_not_resolved(self, error_id):
        return (error_id in self.not_solved_errors)

    def get_all_unsolved_errors(self):
        ''' Returns a list of all unsolved errores in the form
            (error_id, error, tda) '''
        all_unsolved_errors = []
        for error_id in self.not_solved_errors:
            ''' solution has to be "" '''
            error, tda, solution = self.all_errors[error_id]
            all_unsolved_errors.append((error_id, error, tda))
        return all_unsolved_errors

    def get_unsolved_errors_from_tda(self, tda_recieved):
        ''' Returns a list of all unsolved errores from the tda recieved
            in the form (error_id, error, tda) '''
        unsolved_errors_from_tda = []
        for error_id in self.not_solved_errors:
            ''' solution has to be "" '''
            error, tda, solution = self.all_errors[error_id]
            if(tda_recieved == tda):
                unsolved_errors_from_tda.append((error_id, error, tda))
        return unsolved_errors_from_tda

    def write_file(self):
        file = open(self.file_name, "w")
        for error_id in self.all_errors:
            error, tda, solution = self.all_errors[error_id]
            file.write(str(error_id) + "-" + str(error) + "-" + str(tda) + "-" + str(solution))
        file.close()
