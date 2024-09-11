# Jogo de Luta de Robôs - Projeto Final de Programação Orientada a Objetos

## Descrição

Este projeto implementa um jogo de luta de robôs utilizando conceitos de Programação Orientada a Objetos (POO) em Python. O jogo envolve três tipos de robôs: robôs básicos, robôs-médicos e robôs-lutadores, que podem lutar e interagir entre si de várias maneiras, como curar, atacar e se reproduzir.

## Funcionalidades

### 1. Classe Base: `Robo`

A classe `Robo` serve como base para todos os robôs e contém os seguintes elementos:

- **Atributos de Instância**:
  - `nome: str`: Nome do robô.
  - `vida: float`: Nível de vida do robô, gerado aleatoriamente entre 0 e 1.

- **Atributos de Classe**:
  - `nivel_critico: float`: Um valor crítico que define se o robô precisa de cuidados médicos. O valor padrão é 0.60, mas pode ser alterado pelo programador.

- **Métodos**:
  - `__init__(self, nome: str)`: Inicializa o robô com o nome passado como parâmetro e gera um valor de vida aleatório.
  - `__repr__(self)`: Retorna uma representação amigável do robô, mostrando seu nome e nível de vida.
  - `__add__(self, other)`: Permite que dois robôs se reproduzam, criando um "robô bebê" cujo nome será a combinação dos nomes dos pais.
  - `precisa_de_medico(self)`: Verifica se o nível de vida do robô está abaixo do `nivel_critico`. Retorna `True` se o robô precisar de médico e `False` caso contrário.

### 2. Classe `RoboMedico` (Subclasse de `Robo`)

Os robôs-médicos são especializados em curar outros robôs. Eles têm as seguintes características:

- **Atributo de Instância**:
  - `poder_de_cura: float`: Um valor aleatório entre 0 e 1, representando a capacidade de cura do robô-médico.

- **Métodos**:
  - `curar(self, outro_robo: Robo)`: Cura o robô passado como parâmetro, desde que o nível de vida do robô-médico seja maior ou igual ao do robô a ser curado.

### 3. Classe `RoboLutador` (Subclasse de `Robo`)

Robôs-lutadores são especializados em combate, com os seguintes atributos:

- **Atributo de Classe**:
  - `dano_maximo: float`: Valor que define o dano máximo que um robô-lutador pode causar, sendo um número fixo como 0.2.

- **Atributo de Instância**:
  - `poder: float`: Um valor aleatório entre `dano_maximo` e 1, representando a força de ataque do robô.

- **Métodos**:
  - `atacar(self, outro_robo: Robo)`: Realiza um ataque ao outro robô, reduzindo sua vida com base no poder de ataque. Se o outro robô for também um robô-lutador, haverá um contra-ataque.

## Exemplo de Uso

- Durante uma luta, se a vida de um robô cair abaixo de 0.1, ele pode chamar um robô-médico.
- O robô-médico pode ou não atender o chamado com uma chance de 50%.
- Robôs podem se reproduzir, e os filhos herdam o tipo dos pais (robô médico ou lutador).

## Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
## Estrutura do Projeto

- `robo.py`: Define a classe base `Robo`.
- `robomedico.py`: Define a classe `RoboMedico`.
- `robolutador.py`: Define a classe `RoboLutador`.
- `main.py`: Contém exemplos e simulação de batalhas e interações entre os robôs.

## Referências

- [Documentação sobre números aleatórios](https://docs.python.org/pt-br/3/library/random.html)
- [Documentação sobre split de strings](https://docs.python.org/pt-br/3/library/stdtypes.html#str.split)
