'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''


class TaskHandler:
    def conect_api(): # 1
        pass

    def create_task(): # 4
        pass

    def update_task(): # 4
        pass

    def remove_task(): # 4
        pass

    def send_notification(): #2
        pass

    def generate_report(): # 3
        pass

    def send_report(): # 3
        pass

