    
#Importando as bibliotecas
from plyer import notification
from datetime import datetime


#Definindo a função
def alerta(nivel, base, etapa):
    '''
    Cria uma notificação usando o notification
    baseada no nível do alerta, o nome da base
    e etapa providenciadas pelo usuário.
    Adiciona também a data e hora que a notificação
    aconteceu.
    '''
    try:
        #Condicional do alerta
        nome_alerta = ''

        if nivel == 1:
            nome_alerta = "Baixo"
        elif nivel == 2:
            nome_alerta = "Médio"
        else:
            nome_alerta = "Alto"
        
        #Descobrindo a hora e data local
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Criando a notificação
        notification.notify(
            title=f"ATENÇÃO: Alerta {nome_alerta}",
            message=f"Falha no carregamento da base {base} na etapa {etapa}\
            \n{current_date_time}",
            app_name="Python",
            timeout=10
        )
    #Em caso de erro, imprimir uma mensagem de detecção do erro
    except Exception as error:
        print(f"Erro detectado:{error}")

#Usando a função:
alerta(1, "Coder", "Extração")

'''Porque as notificações estão desativadas, coloquei um print no final
para saber se o código funcionou
'''
print("Funcionou")
