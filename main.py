from sympy import symbols, diff, parse_expr, solveset, S, Interval, oo, lambdify
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations


def calcular_domínio(funcao, variaveis):
    dominio = S.Reals  
    
    restricoes = []

    
    denominadores = funcao.as_numer_denom()[1]
    if denominadores != 1:
        restricoes.append(denominadores != 0)

    
    for subfunc in funcao.atoms():
        if subfunc.func == symbols('log').func and subfunc.args:
            restricoes.append(subfunc.args[0] > 0)

    
    for subfunc in funcao.atoms():
        if subfunc.func == symbols('sqrt').func and subfunc.args:
            restricoes.append(subfunc.args[0] >= 0)

    
    for restricao in restricoes:
        dominio &= solveset(restricao, variaveis, domain=S.Reals)

    return dominio


def calcular_imagem(funcao, variaveis):

    if len(variaveis) == 1:  
            var = variaveis[0]
            derivada = diff(funcao, var)
            criticos = solveset(derivada, var, domain=S.Reals) 
            extremos = [funcao.subs(var, ponto) for ponto in criticos]
            extremos.extend([funcao.subs(var, limite) for limite in [-oo, oo]])
            return Interval(min(extremos), max(extremos))

    funcao_lambda = lambdify(variaveis, funcao, modules="numpy")
    grid = np.linspace(-10, 10, 100)
    pontos = np.meshgrid(*[grid for _ in variaveis])
    valores = funcao_lambda(*pontos)
    imagem_min = np.min(valores)
    imagem_max = np.max(valores)
    return Interval(imagem_min, imagem_max)

def calcular_derivadas_todas_ordens(funcao, ordem_maxima):
    """
    Calcula todas as derivadas possíveis até a ordem especificada, incluindo permutações.

    :param funcao: Função simbólica a ser derivada
    :param ordem_maxima: Ordem máxima das derivadas
    :return: Lista de derivadas com as combinações e seus resultados
    """
    x, y = symbols('x y')
    derivadas = []

    for ordem in range(1, ordem_maxima + 1):  
        indices = ['x'] * ordem + ['y'] * ordem
        permutacoes = set(permutations(indices, ordem)) 
        for permutacao in permutacoes:
            derivada_str = ''.join(permutacao)
            derivada = funcao
            for var in permutacao:
                derivada = diff(derivada, symbols(var))
            derivadas.append((derivada_str, derivada))

    return derivadas


def plotar_grafico(funcao, titulo):
    """
    Plota gráficos 3D de uma função simbólica.
    """
    x, y = symbols('x y')
    funcao_lambda = lambdify((x, y), funcao, modules='numpy')
    X = np.linspace(-10, 10, 400)
    Y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(X, Y)

    try:
        Z = funcao_lambda(X, Y)
        if np.isscalar(Z):
            Z = np.full_like(X, Z)
    except TypeError:
        Z = np.full_like(X, funcao_lambda(0, 0))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(titulo)
    plt.show()

escolhaContinuar = 's'
while escolhaContinuar == 's':
    print(40 * '-')
    print('   CALCULADORA DE CÁLCULO DIFERENCIAL')
    print(40 * '-')
    print('''MENU:
    [1] - DERIVAR FUNÇÕES
    [2] - MOSTRAR GRÁFICOS/IMAGEM/DOMINIO
    [3] - MOSTRAR AMBOS
    ''')

    escolhaMenu = str(input('Digite: '))
    while not escolhaMenu.isnumeric() or not (1 <= int(escolhaMenu) <= 3):
        print('Valor inválido!')
        print('''MENU:
            [1] - DERIVAR FUNÇÕES
            [2] - MOSTRAR GRÁFICOS/IMAGEM/DOMINIO
            [3] - MOSTRAR AMBOS
            ''')
        escolhaMenu = input('Digite: ')
    escolhaMenu = int(escolhaMenu)


    x, y = symbols('x y')
    funcao_input = input('Digite uma função (em termos de x e y): ')
    while not funcao_input.strip():
        print('Função inválida')
        funcao_input = input('Digite uma função (em termos de x e y): ')

    funcao_simb = parse_expr(funcao_input, transformations="all", evaluate=False)

    if escolhaMenu in [1, 3]:
        ordem = int(input('Até qual ordem você quer calcular as derivadas? '))
        while ordem < 1:
            print('Valor inválido')
            ordem = int(input('Até qual ordem você quer calcular as derivadas? '))

        derivadas = calcular_derivadas_todas_ordens(funcao_simb, ordem)

        print("\nDerivadas calculadas:")
        for derivada_str, derivada in derivadas:
            print(f"f(x,y) derivada ({derivada_str}): {derivada}")

    if escolhaMenu in [2, 3]:
        print("\nDomínio e imagem da função:")
        dominio = calcular_domínio(funcao_simb, [x, y])
        imagem = calcular_imagem(funcao_simb, [x, y])
        print(f"Domínio: {dominio}")
        print(f"Imagem: {imagem}")

        print("\nPlotando gráficos...")
        plotar_grafico(funcao_simb, "Função Original")

        if escolhaMenu == 3:
            print("\nPlotando gráficos das derivadas...")
            for derivada_str, derivada in derivadas:
                plotar_grafico(derivada, f"Derivada: {derivada_str}")
    escolhaContinuar = input('Deseja continuar? (S/N)').lower()
    if len(escolhaContinuar) > 0:
        escolhaContinuar = escolhaContinuar[0]
    while escolhaContinuar != 's' and escolhaContinuar != 'n' or escolhaContinuar == '':
        print(escolhaContinuar)
        print('Valor Inválido')
        escolhaContinuar = input('Deseja continuar? (S/N)').lower()
        if len(escolhaContinuar) > 0:
            escolhaContinuar = escolhaContinuar[0]
print('Parando Sistema .... ')