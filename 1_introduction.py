# INTRODUÇÃO AO PYTHON NAMESPACES

# name spaces em python são definições de escopo para nomes que por sua vez podem ser qualquer coisa que tenha uma
# alocação na memória pelo python.

# utilize a função locals() e globals() para visualizar o estado do name space local e global
local_namespace = locals()
global_namespace = globals()
print(local_namespace, global_namespace)

# a explicação para a sentença (if __name__ == '__main__': ...) tem como fundamento
# o namespace global, que ao ser inicializado atribui à referência do arquivo executado
# (__name__) o valor __main__ por padrão, sendo possível validar se o arquivo que o código
# se encontra é o arquivo de entrada do sistema/script/app.
if __name__ == '__main__':
    print('Sou o arquivo de entrada do sistema :)')

# se você é um bom programador, necessariamente é curioso. portanto com certeza deve ter
# se perguntado de onde vêm as definições de algumas funções ou palavras, que seja, as quais
# escrevemos no código python sem precisar definir nada ou importar nada. por exemplo a função
# print() que utilizamos no famoso hello world, ou a palavra def que utilizamos para definir 
# uma função. Afinal de onde vem isso tudo?
# Agora que você é capaz, vamos dar uma olhada no nosso name_space globals
print(globals())

#percebeu algo? olhe mais afundo os valores da chave __builtins__.
print(' '*100)
builtins = globals()['__builtins__']
for key, value in builtins.items():
    print(f'{key} ---> {value}')

# viu só que legal?
# nunca deixe nada passar na sua frente sem que você entenda, isso se quiser ser bom naquilo
# caso queira ser um medíocre, tudo bem, o tão definitiva quanto a natureza é a capacidade que
# o tempo tem de separar os bons dos médios.
# seja bom. seja o melhor.
