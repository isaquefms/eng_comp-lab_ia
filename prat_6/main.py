import sys
import math
import random
import matplotlib.pyplot as plt

from typing import List, Tuple


def funcao_objetivo(x: float, y: float) -> float:
    """Função objetivo de análise.

    Args:
        x: Valor x da função.
        y: Valor y da função.

    Returns: A função avaliada em x e y.
    """
    return math.sin(x) * math.exp(math.pow(1 - math.cos(y), 2)) + \
           math.cos(y) * math.exp(math.pow(1 - math.sin(x), 2)) + math.pow(x - y, 2)


def retorno_geracao(populacao: List[List[float]], tam_populacao: int) -> List[float]:
    """Prepara o retorno de uma determinada geração.

    Args:
        populacao: Individuos de uma determinada geração.
        tam_populacao: Tamanho da população.

    Returns: Lista com o resultado do melhor, do pior e a média dos resultados.
    """
    # o melhor é o último indivíduo e o pior o primeiro
    melhor = funcao_objetivo(populacao[-1][0], populacao[-1][1])
    pior = funcao_objetivo(populacao[0][0], populacao[0][1])
    soma_total: float = 0
    for individuo in populacao:
        soma_total += funcao_objetivo(individuo[0], individuo[1])
    return [melhor, pior, soma_total / tam_populacao], populacao[-1]


def cria_populacao(tam_populacao: int) -> List[List[float]]:
    """Cria a população de acordo com o tamanho proposto.

    Args:
        tam_populacao: Tamanho de amostras da população

    Returns: Matriz com os elementos aleatórios criados.
    """
    p = []
    for index in range(tam_populacao):
        x_rand = random.uniform(-10, 10)
        y_rand = random.uniform(-10, 10)
        p.append([x_rand, y_rand])
    return p


def avalia_populacao(populacao: List[List[float]]) -> List[List[float]]:
    """Avalia a população passada como parâmetro utilizando como função fitness o
    próprio valor obtido na função objetivo.

    Args:
        populacao: População que será avaliada.

    Returns: Matriz com os elementos ordenados com o valor na função
    objetivo ordenados do menor para o maior com a adição de uma
    posição em cada indivíduo que representa a sua aptidão ao
    ambiente.
    """

    # Ordena do menor para o maior tomando como base o valor de x e y
    #	de cada indivídio da população.
    populacao_final: List[List[float]] = []
    p_ordenado: List[List[float]] = sorted(populacao,
                                           key=lambda individual: funcao_objetivo(individual[0], individual[1]),
                                           reverse=True)
    sum_index: int = 0
    # verificando a soma total de cada índice de elementos
    for index, individual in enumerate(p_ordenado, start=1):
        sum_index += index
    # adicionando a aptidão a cada indivíduo
    for index, individual in enumerate(p_ordenado, start=1):
        individual.append(int((index / sum_index) * 100))
        populacao_final.append(individual)

    return populacao_final


def seleciona_pai(populacao: List[List[float]]) -> List[float]:
    """Seleciona dentre os elementos um possível pai de acordo com a
    probabilidade.

    Args:
        populacao: População de elementos com a sua aptidão.

    Returns: Elemento sorteado.
    """
    # número sorteado
    num_sorteado = random.randint(1, 100)
    soma_relativa: int = 0
    for indice, individuo in enumerate(populacao):
        # soma relativa é igual ao intervalo da aptidão do indicíduo
        soma_relativa += individuo[2]
        # caso o número sorteado seja menor ou igual a soma relativa
        # podemos retornar o individuo atual
        if num_sorteado <= soma_relativa:
            return individuo
    # caso nenhum número seja retornado anteriormente, retornamos o último,
    # no caso o melhor, isso é um certo elitismo
    return populacao[-1]


def cruzamento(pai_1: List[float], pai_2: List[float], taxa_de_cruzamento: float) -> Tuple[List[float], List[float]]:
    """Realiza o cruzamento entre os pais passados como parâmetro
    levando em conta a taxa de cruzamento.

    Args:
        pai_1: Primeiro indivíduo pai.
        pai_2: Segundo indivíduo pai.
        taxa_de_cruzamento: Valor que informa a taxa de cruzamento.
        Valor entre 0 e 1.

    Returns: Indivíduos filhos gerados pelo cruzamento.
    """
    # definimos um número aleatório para definirmos se iremos ter
    # cruzamento ou não
    num_aleat = random.uniform(0, 1.0)
    filho_1: List[float] = []
    filho_2: List[float] = []
    # há cruzamento
    if num_aleat <= taxa_de_cruzamento:
        # filho 1, x do pai 1 e y do pai 2
        filho_1.append(pai_1[0])
        filho_1.append(pai_2[1])
        # filho 2, x do pai 2 e y do pai 1
        filho_2.append(pai_2[0])
        filho_2.append(pai_1[1])
    # se não houver cruzamento
    else:
        # filho 1 é igual ao pai 1
        filho_1.append(pai_1[0])
        filho_1.append(pai_1[1])
        # filho 2 é igual ao pai 2
        filho_2.append(pai_2[0])
        filho_2.append(pai_2[1])
    return filho_1, filho_2


def mutacao(filho: List[float], taxa_de_mutacao: float) -> List[float]:
    """Realiza a mutação de um filho a partir de uma determinada faixa.

    Args:
        filho: Indivíduo que irá passar pela mutação.
        taxa_de_mutacao: Número de ponto flutuante que informa a taxa
        de indivíduos que serão mutádos.

    Returns: Indivíduo resultante.
    """
    filho_mutado: List[float] = []
    # número aleatório para avaliar se o indivíduo será mutado
    num_aleat = random.uniform(0, 1)
    # fator de mutação
    fator_mutacao = random.uniform(-0.2, 0.2)
    # gene que será mutado
    gene = random.randint(0, 1)
    # se for mutado
    if num_aleat <= taxa_de_mutacao:
        filho[gene] = filho[gene] + fator_mutacao
        filho_mutado.append(filho[0])
        filho_mutado.append(filho[1])
    else:
        filho_mutado.append(filho[0])
        filho_mutado.append(filho[1])
    return filho_mutado


def algoritmo_genetico(tam_populacao: int, taxa_de_cruzamento: float, taxa_de_mutacao: float, limite_geracoes: int) -> \
        List[List[float]]:
    """Execução do algoritmo genético.

    Args:
        tam_populacao: Valor que indica o tamanho da população.
        taxa_de_cruzamento: Valor entre 0 e 1 que representa a probabilidade
        de se ocorrer o cruzamento.
        taxa_de_mutacao: Valor entre 0 e 1 que representa a probabilidade de
        se ocorrer a mutação.
        limite_geracoes: Limite máximo de gerações.

    Returns: Matriz com o melhor e o pior indivíduo da população.
    """
    # primeira população
    p = cria_populacao(tam_populacao)
    g: int = 0  # gerações
    individuos: List[List[float]] = []  # melhor e pior individuo da pop
    # Com o intuito de manter a simplicidade do algoritmo, optamos por manter somente o limite de gerações como condição
    #  de parada. Outra condição seria: a média dos resultados é igual(ou próxima o suficiente) da solução ótima.
    while g < limite_geracoes:
        # avaliação da população
        p_avaliada = avalia_populacao(p)
        # o melhor individuo está na última posição e o pior na primeira
        # retirando a aptidão que é retornada no avalia_populacao
        resultados, melhor_individuo = retorno_geracao(p_avaliada, tam_populacao)
        individuos.append(resultados)
        # nova geração
        q: List[List[float]] = []
        # para cada casal da população
        for _ in range(tam_populacao // 2):
            pai_1 = seleciona_pai(p_avaliada)
            pai_2 = seleciona_pai(p_avaliada)
            filho_1, filho_2 = cruzamento(pai_1, pai_2, taxa_de_cruzamento)
            filho_1 = mutacao(filho_1, taxa_de_mutacao)
            filho_2 = mutacao(filho_2, taxa_de_mutacao)
            # adiciona os filhos
            q.append(filho_1)
            q.append(filho_2)
        # próxima geração
        g += 1
        # nova população é igual a q
        p = q
    return individuos, melhor_individuo


def main(tam_populacao: int = 20, taxa_de_cruzamento: float = 0.7, taxa_de_mutacao: float = 0.1,
         limite_geracoes: int = 20):
    """Executa o algoritmo genético com base nos argumentos passados como parâmetro. Caso nenhum parâmetro seja passado,
        executa com os valores default.
    Args:
        tam_populacao: Tamanho definido para a população de cada geração
        taxa_de_cruzamento: Taxa de cruzamento dos indivíduos
        taxa_de_mutacao: Taxa de mutação dos indivíduos
        limite_geracoes: Número máximo de iterações

    Returns: Plot do gráfico com os resultados obtidos, e print do melhor resultado na linha de comando.
    """
    individuos, melhor_individuo = algoritmo_genetico(int(tam_populacao), float(taxa_de_cruzamento), float(taxa_de_mutacao),
                                    int(limite_geracoes))

    melhores = [individuo[0] for individuo in individuos]
    piores = [individuo[1] for individuo in individuos]
    medias = [individuo[2] for individuo in individuos]
    print(f'O melhor indivíduo foi o ({melhor_individuo[0]}, {melhor_individuo[1]}), obtendo o valor {melhores[-1]}. O gráfico a seguir mostra o desempenho geral do algoritmo.')

    geracoes = range(1, int(limite_geracoes) + 1)
    plt.plot(geracoes, melhores, 'g--', geracoes, medias, 'b--', geracoes, piores, 'r--')
    plt.show()


# Pega os argumentos passados como parâmetro pela linha de comando. O primeiro argumento é o nome do arquivo, entao o
#  ignoramos.
main(*sys.argv[1:])
