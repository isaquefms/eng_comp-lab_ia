# Arquivo para criação do algoritmo de Redes Neurais
import pandas as pd
import numpy as np


def activation_function(entry: np.array, function_type: int = 0) -> np.array:
	"""Função de ativação de uma determinada entrada.

	Args:
		entry: Array de entrada.
		function_type: Tipo da função de ativação.

	Returns: Array com o resultado de acordo com a avaliação.
	"""
	# array de retorno
	return_array = np.array([0, 0, 0])
	return_array = return_array.reshape((3, 1))
	# fazer a análise de acordo com cada entrada
	for index, line in enumerate(entry):
		if function_type == 0:
			# caso o valor contido na coluna da linha seja maior ou igual a 0
			return_array[index][0] = 1 if line[0] >= 0 else 0
	return return_array


def sum(entry: np.array) -> float:
	"""Método para cálculo do erro quadrático.

	Args:
		entry: Matriz de entrada.

	Returns: Somatório dos valores da Matriz ao quadrado.
	"""
	sum: float = 0
	for index, line in enumerate(entry):
		sum += line[0] ** 2
	return sum



def prepare_d(X: pd.DataFrame) -> np.array:
	"""Prepara o vertor de respostas dado o dataset de entrada.

	Args:
		X: Dados lidos do arquivo CSV.

	Returns: Matriz com a representação das classes.
	"""
	D: list[np.array] = []	
	for _, element in enumerate(X):
		if element == 'Iris-setosa':
			D.append(np.array([0, 0, 1]).reshape((3, 1)))
		elif element == 'Iris-versicolor':
			D.append(np.array([0, 1, 0]).reshape((3, 1)))
		elif element == 'Iris-virginica':
			D.append(np.array([1, 0, 0]).reshape((3, 1)))
	return D



def perceptron(max_it: int, alpha: float, X: np.array, D: np.array) -> np.array:
	"""Método para execução do algoritmo de redes neurais.

	Args:
		max_it: Total de épocas.
		alpha: Taxa de aprendizagem.
		X: Matriz contendo as informações lidas dos arquivos.
		D: Matriz com os valores da classe de cada instância de X.

	Returns: Matriz W com os valores de treino.
	"""
	# inicializando as matrizes de peso e bias
	W: np.array = np.array([0.1, 0.2, 0.2, 0.4, 0.5, 0.4, 0.4, 0.6, 0.7, 0.4, 0.1, 0.2], dtype=float).reshape((3, 4))  # peso de cada entrada para o neurônio
	b: np.array = np.array([1, 1, 1], dtype=float).reshape((3, 1))  # bias do neurônio

	t: int = 1  # contador de iterações
	E: float = 1  # erro global
	e: list[np.array] = []  # erro por instância
	ve: list[np.array] = []  # vetor de erros

	y: list[np.array] = []  # vetor de saída

	# como na leitura do csv temos uma instância em cada linha, preciamos transpor X
	# X = X.T

	# enquanto não atingirmos as épocas totais e o erro for maior que zero
	while t < max_it and E > 0:
		E = 0
		for index, value in enumerate(X):
			value = value.reshape((4, 1))
			# obentenção da saída prevista de acordo com os pessos da entrada
			y.append(activation_function(W.dot(value) + b))
			# cálculo do erro de predição
			e.append(np.array(D[index] - y[index], dtype=float))
			# atualização da matrix de pesos
			W = W + (alpha * (e[index].dot(value.T)))
			# atualização do bias
			b = b + (alpha * e[index])
			# atualização do erro global
			E = E + sum(e[index])
			# adicionando o erro no vetor de erros
			ve.append(E)
		t += 1

	return W, b, ve


def accuracy(W: np.array, b: bp.array, X: np.array, D: np.array) -> float:
	"""Realiza a predĩção e calcula a acurácia da rede neural treinada.

	Args:
		W: Matriz de pesos para as entradas dos neurônios.
		b: Vetor de bias dos neurônios.
		X: Dados usados para prever o modelo treinado.
		D: Classificação original da entrada X.

	Returns: Acurácia do modelo treinado.
	"""
	y: list[np.array] = []

	for index, value in enumerate(X):
		value = value.reshape((4, 1))
		# obtenção da saída prevista de acordo com os valores
		y.append(activation_function(W.dot(value) + b)



def main() -> None:
	"""Executa o código criado.

	Returns: None
	"""

	# lendo o arquivo csv
	dataset = pd.read_csv('data/iris_data.csv', header=None)
	# preparando os dados de D
	D = prepare_d(dataset[4])
	# preparando os dados de X
	X = dataset.drop(4, 1)
	X = X.drop(0, 0)
	# calculando o algoritmo e obtendo W
	W, b, ve = perceptron(2, 0.3, X.to_numpy(dtype=float), D)
	# exibindo
	print(f'Valor de W: {W}')
	print(f"Valores dos bias: {b}")
	# print(f"Vetor de erros: {ve}")


# Execução do código
main()