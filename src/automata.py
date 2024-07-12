from typing import List, Dict, Tuple, Any
import os

Automata = Tuple[List[str], List[str], Dict[str, Dict[str, List[str]]], str, List[str]]

def load_automata(filename: str) -> Automata:
    """
    Carrega um autômato a partir de um arquivo.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    Sigma = lines[0].strip().split()
    Q = lines[1].strip().split()
    F = lines[2].strip().split()
    q0 = lines[3].strip()
    delta = {}

    for line in lines[4:]:
        origem, simbolo, destino = line.strip().split()
        if origem not in delta:
            delta[origem] = {}
        if simbolo not in delta[origem]:
            delta[origem][simbolo] = []
        delta[origem][simbolo].append(destino)

    return (Q, Sigma, delta, q0, F)

def process(automata: Automata, word: List[str]) -> Dict[str, str]:
    """
    Processa uma palavra no autômato.
    """
    Q, Sigma, delta, q0, F = automata
    current_states = [q0]

    for symbol in word:
        if symbol not in Sigma:
            return {"result": "INVÁLIDA"}
        next_states = []
        for state in current_states:
            if state in delta and symbol in delta[state]:
                next_states.extend(delta[state][symbol])
        current_states = next_states

    if any(state in F for state in current_states):
        return {"result": "ACEITA"}
    else:
        return {"result": "REJEITA"}

def convert_to_dfa(automata: Automata) -> Automata:
    """
    Converte um AFN para um AFD.
    """
    Q, Sigma, delta, q0, F = automata
    new_states = {frozenset([q0]): 'S0'}
    dfa_delta = {}
    dfa_F = set()
    unmarked_states = [frozenset([q0])]
    state_count = 0

    while unmarked_states:
        current = unmarked_states.pop(0)
        current_state_name = new_states[current]
        dfa_delta[current_state_name] = {}

        for symbol in Sigma:
            next_state = frozenset(sum((delta[state][symbol] for state in current if state in delta and symbol in delta[state]), []))
            if not next_state:
                continue
            if next_state not in new_states:
                state_count += 1
                new_states[next_state] = f'S{state_count}'
                unmarked_states.append(next_state)
            dfa_delta[current_state_name][symbol] = new_states[next_state]

            if next_state & set(F):
                dfa_F.add(new_states[next_state])

    dfa_Q = list(new_states.values())
    dfa_q0 = 'S0'
    dfa_F = list(dfa_F)

    return (dfa_Q, Sigma, dfa_delta, dfa_q0, dfa_F)
