# NFA: Non-Deterministic Finite Automation

# This automata accepts all strings with 01.
states = ("0", "1", "2", "3")
input_symbols = ("0", "1")
transition_function = {
                        "0" : [("ε" , "1"), ("ε" , "2")],
                        "1" : [("0" , "1"), ("1" , "3")],
                        "2" : [("0" , "3"), ("1" , "2")],
                        "3" : []
                        }
initial_state = ["0"]
final_states = ["3"]

class NFA:
    def __init__(self, _states, _input_symbols, _transition_function, _initial_state, _final_states):
        self.states = _states # estados
        self.input_symbols = _input_symbols # alfabeto
        self.transition_function = _transition_function # funções de transição 
        self.initial_state = _initial_state # estado inicial
        self.final_states = _final_states # estados finais
        self.current_states = set(initial_state)

    def process_word(self, word):
        for input in word:
            if input not in self.input_symbols:
                return False
                
            next_curr_states = set()
            # Attempt to grow a set while it's being iterated. Maybe it can be used to solve Epsilon cases.
            # i = 0
            # while i < len(self.current_states):
            #     current_state = self.current_states[i]
            
            for current_state in self.current_states:
                transitions_from_curr_state = self.transition_function.get(current_state)
                if transitions_from_curr_state is not None:
                    # If there's an Epsilon coming out from the current state, put the addressed state from the epsilon in the current_states.
                    # if "E" in transitions_from_curr_state:
                    #     new_state = transitions_from_curr_state.get("E")
                    #     self.current_states.extend(new_state)

                    new_states = set()
                    for transicao in transitions_from_curr_state:
                        if input == transicao[0]: # Se há uma transição para aquela letra 
                            new_states.add(transicao[1]) # Adicione esse estado a lista de estados que podem ser visitados
                    
                    if new_states is not None:
                        next_curr_states = next_curr_states.union(new_states)

            # If there's no more current states, reject word
            if len(next_curr_states) == 0:
                return False
            
            self.current_states = next_curr_states

        # After parsing all the word, check if there's any current state as an accepting state.
        for current_state in self.current_states:
            if current_state in self.final_states:
                return True

        return False
    
    def removeTransicaoVazia(self):
        transicoes_finais = dict()
        transicoes_finais = transition_function.copy()
        transicoes_nao_vazias = dict()
        transicoes_vazias = dict()
        # Para cada estado do automato
        for estado in transition_function:
            transicoes_finais[estado] = []
            transicoes_vazias[estado] = []
            transicoes_nao_vazias[estado] = []
            for transicao in transition_function.get(estado):
                if transicao[0] != "ε":
                    transicoes_finais[estado].append(transicao)
                    transicoes_nao_vazias[estado].append(transicao)
                else:
                    transicoes_vazias[estado].append(transicao)
                        
        for estado in transition_function:
            transicoes_nao_vazia_no_vertice = transicoes_nao_vazias.get(estado)
            # Enquanto houverem transições vazias daquele estado para outro
            while len(transicoes_nao_vazia_no_vertice) != 0:
                # Analisando a Transição feita
                transicao_analisada = transicoes_nao_vazia_no_vertice.pop()
            
                # Para cada transicao que o estado destino da transição possui
                for transicao_do_estado_destino in transition_function.get(transicao_analisada[1]):
                    if transicao_do_estado_destino[0] == "ε":
                        if transicao_do_estado_destino not in transicoes_finais[estado]:
                            nova_transicao = (transicao_analisada[0], transicao_do_estado_destino[1])
                            transicoes_finais[estado].append(nova_transicao)
                            transicoes_nao_vazia_no_vertice.append(nova_transicao)
                        
        for estado in transition_function:
            transicoes_vazia_no_vertice = transicoes_vazias.get(estado)
            # Enquanto houverem transições vazias daquele estado para outro
            while len(transicoes_vazia_no_vertice) != 0:
                # Analisando a Transição feita
                transicao_analisada = transicoes_vazia_no_vertice.pop()
                # Atualiza Estados Inciais e Estados Finais
                if estado in initial_state:
                    initial_state.append(transicao_analisada[1])
                if transicao_analisada[1] in final_states:
                    final_states.append(estado)
                # Para cada transicao que o estado destino da transição possui
                for transicao_do_estado_destino in transition_function.get(transicao_analisada[1]):
                    if transicao_do_estado_destino[0] != "ε":
                        if transicao_do_estado_destino not in transicoes_finais[estado]:
                            transicoes_finais[estado].append(transicao_do_estado_destino)
                    elif transicao_do_estado_destino not in transicoes_finais[estado]:
                        transicoes_vazia_no_vertice.append(transicao_do_estado_destino)
        
        self.transition_function = transicoes_finais
            



def main():
    automata = NFA(states, input_symbols, transition_function, initial_state, final_states)
    word = "00000000001"
    automata.removeTransicaoVazia() # Função para transformar o AFNe em AFN
    print(automata.final_states)
    accepted = automata.process_word(word)
    
    if accepted:
        print(f"\"{word}\" was accepted")

    else:
        print(f"\"{word}\" was rejected")

if __name__ == "__main__":
    main()