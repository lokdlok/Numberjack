
class XCSPOut():
    # Map variable idents to xcsp variable name
    variables = {}
    domains = {}

    def __init__(self, model):
        self.model = model
        self.model.close()
    
    def output(self, filename):
        self.readModel()

    def readModel(self):
        for variable in self.model.variables:
            self.variables[variable.ident] = 'V'+str(len(self.variables))
            domain = variable.get_domain_tuple()
            if domain[2] == None:
                domain_string = "%d..%d" % (domain[0], domain[1])
            else:
                domain_string = " ".join(domain[2])

            if domain_string in self.domains:
                self.domains[domain_string].add(variable.ident)
            else:
                self.domains[domain_string] = {variable.ident}






