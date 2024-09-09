from abc import ABC, abstractmethod

class AprovaExameInterface(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass
    
    @abstractmethod
    def verifica_condicoes_exame(self, exame):
        pass

class AprovaExameSangue(AprovaExameInterface):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")
    
    def verifica_condicoes_exame(self, exame):
        # verifica as condições específicas do exame de Sangue
        mock_result = True
        return mock_result

class AprovaExameRaioX(AprovaExameInterface) :
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Raio-X aprovado!")
    
    def verifica_condicoes_exame(self, exame):
        # verifica as condições específicas do exame de Raio X
        mock_result = True
        return mock_result

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador_sangue = AprovaExameSangue()
aprovador_raio_x = AprovaExameRaioX()

aprovador_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_raio_x.aprovar_solicitacao_exame(exame_raio_x)


