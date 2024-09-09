# Avançando um pouco no assunto dos namespaces

# vamos dar uma olhada mais afundo no escopo locals
# o escopo locals é todo escopo criado no momento em que o 
# interpretador python entra numa função/metodo

# variavel no escopo global
some_memory_ref_container = ''

def my_great_function_that_does_almost_everything_in_my_code():
    my_awesome_variable = '' 

    # aqui printamos nossa variavel de escopo global
    print(some_memory_ref_container)
    # aqui printamos nossa variavel de escopo local
    print(my_awesome_variable)

    # se chegou até aqui, ja deve ser capaz de executar o codigo
    # e procurar nos escopos locals() e globals() onde se encontram
    # as variaveis do nosso exemplo.

    # como percebeu, nos temos acesso às variaveis globais, mesmo no nosso
    # escopo local. TEMOS ACESSO, apenas acesso, quer ver? Tire o comentario
    # do codigo abaixo e tente executar, perceba o erro que enfrentaremos:

    #some_memory_ref_container = 'changing global scope value'

    #EERO -> local variable 'some_memory_ref_container' referenced before assignment
    #por que sera que esse erro ocorre?
    #entenda que por padrão, não podemos alterar valores do escopo globals
    #se estivermos dentro do escopo locals. Aliás, esse não é o único caso que não podemos alterar
    #valores. Porém veremos isso em breve.

    #por enquanto eu quero que perceba algo no que eu disse: POR PADRÃO não podemos alterar valores
    #do escopo globals, porém isso não é regra.

    #Entenda agora a utilidade do name global.
    #Vamos tentar executar o mesmo código, porém agora adicionando a palava global antes da variavel:
    global some_memory_ref_container
    some_memory_ref_container = 'Hello'


    #o código acima não vai rodar se voce não comentar a linha 16 hahaha.
    #o erro acontece pois quando declaramos referenciamos a variavel global com a keyword global
    #ele irá buscar pela variavel no estado que se encontra global, e então não podemos usa-la
    #até que declaremos dentro do nosso escopo locals.

my_great_function_that_does_almost_everything_in_my_code()


# LEGB rule
# A regra LEGB nos ajuda a decorar quais são os escopos do python
# L = Locals; E = Enclosing; G = Globals; B = Builtins
# Calma, tem um que você não viu ainda e deve estar se perguntando, correto? Pois deveria...
# O próximo arquivo vai te explicar sobre o Enclosing.