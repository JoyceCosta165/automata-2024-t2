"""Implementação de autômatos finitos."""

def load_automata():
    """
    Lê os dados de um autômato finito a partir de um arquivo.

    A estrutura do arquivo deve ser:

    <lista de símbolos do alfabeto, separados por espaço (' ')>
    <lista de nomes de estados>
    <lista de nomes de estados finais>
    <nome do estado inicial>
    <lista de regras de transição, com "origem símbolo destino">

    Um exemplo de arquivo válido é:

    ```
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    ```

    Caso o arquivo seja inválido uma exceção Exception é gerada.

    """
    file_path = '/home/nicolas/Documents/automata_2024_t1/examples/01-simples.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    Sigma = lines[0].strip().split(' ')
    Q = lines[1].strip().split(' ')
    F = lines[2].strip().split(' ')
    q0 = lines[3].strip()
    delta = {}

    for line in lines[4:]:
        origin, symbol, destination = line.strip().split(' ')
        if (origin, symbol) not in delta:
            delta[(origin, symbol)] = []
        delta[(origin, symbol)].append(destination)

    return (Q, Sigma, delta, q0, F)

def process(automata, word):
    """
    Processa uma palavra e retorna o resultado.
    
    Os resultados válidos são ACEITA, REJEITA, INVÁLIDA.
    """
    Q, Sigma, delta, q0, F = automata
    current_state = q0

    for symbol in word:
        if (current_state, symbol) in delta:
            current_state = delta[(current_state, symbol)][0]
        else:
            return {"status": "INVÁLIDA"}

    if current_state in F:
        return {"status": "ACEITA"}
    else:
        return {"status": "REJEITA"}

if __name__ == "__main__":
    automata = load_automata()
    print(automata)
    result = process(automata, ['a', 'b'])
    print(result)
