# Documentação do projeto Calculadora

## Pré-requisitos para rodar o projeto

Para rodar o projeto na sua maquina certifique-se de ter os seguintes itens instalados em sua máquina:

- **Python 3**: necessário para executar o projeto.
- **Pip**: usado para instalar as bibliotecas do projeto.
    - Obs: Certifique-se de ter o Pyhon adicionado ao PATH do seu computador.
- **Bibliotecas necessárias**: 
  - Sympy
  - Numpy
  - Matplotlib
  - Plotly

## Passos para Rodar o Código

### 1. Crie um ambiente virtual do Python
```bash
# Criar o ambiente virtual
python -m venv venv
```
### 2. Entre no ambiente virtual
```bash
# Ativar o ambiente virtual (Linux):
source venv/bin/activate

# Ativar o ambiente virtual (Windows)
.\venv\Scripts\activate
```
### 3. Baixe as dependencias no ambiente virtual
```bash
pip install -r requirements.txt
```
### 4. Apos instalar as dependencias no ambiente virtual use o comando abaixo para execultar a Aplicação
```bash
python main.py
```            
## Interação com a Calculadora
**Quando a Calculadora estiver em excução terá um menu:**
```bash
    [1] - DERIVAR FUNÇÕES
    [2] - MOSTRAR GRÁFICOS/IMAGEM/DOMINIO
    [3] - MOSTRAR AMBOS
```
**Aqui o usuário podera escolher qual opção seguir.**
### Após escolher a opção será possível digitar a função até a ordem que deseja derivar (da 1º a 3º ordem).
```bash
 Digite uma função (em termos de x e y): 
 Até qual ordem você quer calcular as derivadas? 
```
**Após digitar os dados a aplicação será capaz de mostrar a derivada, o grafico, imagem, dominio ao depender da escolha feita.**

### Exemplos de input de função:
```bash
    7(x**5)*(y**4) - 8(x**3)*(y**4)  
    1/x
    2x + 2y
    cos(x) + sin(y)
    tan(x) + tan(y)
```

