# Enclosing, deixei ele por último não por acaso.

# Ja que você aprendeu o comportamento de locals e globals, saiba que o enclosing
# é a mesma coisa, porém relativo, ou seja, a função interna de outra função
# se torna local em relação a ela, veja:
def enclosing_scope_func_global():

    enclosing_scope_var = ''

    def enclosing_scope_func_local():

        enclosing_scope_var += 'Heey'
        return enclosing_scope_var

    return enclosing_scope_func_local()

result = enclosing_scope_func_global()
print(result)


# é isso. tentei resumir da melhor forma o assunto de namespaces e escopos.
# entenda bem esse assunto, e sinta-se confiante com a ferramenta que você esta utilizando.
# um marceneiro não pode ter medo de martelar o proprio dedo.
