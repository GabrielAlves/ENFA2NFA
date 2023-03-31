# NFA: Non-Deterministic Finite Automation

# This automata accepts all strings with 01.
states = ("1", "2", "3")
input_symbols = ("a", "b", "c")
transition_function = {
                        "1" : [("a" , "3"), ("a" , "2")],
                        "2" : [("b" , "3"), ("ε", "3"), ("ε", "2")],
                        "3" : [("c" , "3")]
                        }
initial_state = ("1")
final_states = ("3")

transicoes_finais = dict()
transicoes_finais = transition_function.copy()
transicoes_vazias = dict()
for estado in transition_function:
    transicoes_finais[estado] = []
    transicoes_vazias[estado] = [] 
    for transicao in transition_function.get(estado):
        if transicao[0] != "ε":
            transicoes_finais[estado].append(transicao)
        else:
            transicoes_vazias[estado].append(transicao)     

transicoes_finais = dict()
print(transicoes_vazias)
while transicoes_vazias:
    for estado in transicoes_vazias:
        transicoes_finais[estado] = []
        if len(transicoes_vazias.get(estado)) != 0:
            for transicoes in transicoes_vazias.get(estado): # para cada transição dentre as transições vazias do estado x   
                transicoes_do_destino = transition_function.get(transicoes[1]) # recebe todas as transições que um estado alcançavel y tem
                print(f"transicoes_do_destino = {transicoes_do_destino}")
                # Procure nas novas transições as que são vazias e então adicione-as a lista de transições vazias
                for transicao_destino in transicoes_do_destino:
                    if transicao_destino[0] == "ε":
                        #transicoes_vazias[estado].append(transicao_destino)
                        pass
                    else:
                        transicoes_finais[estado].append(transicoes_do_destino) # adicionando as novas transições ao conjunto de transições finais
                print(transicoes_finais)
    break
            
            
            
    # print(transicoes_vazias)
    # for estado_origem in transicoes_vazias:
        
    #     pass
    # break
    #(origem, destino) = transicoes_vazias.pop()
    # for (nova_origem, simbolo, nova_destino) in transicoes:
    #    if nova_destino == origem:
    #         nova_transition = (nova_origem, simbolo, destino)
    #         if nova_transition not in transicoes:
    #             transicoes.add(nova_transition)
    #             transicoes_vazias.add((nova_origem, destino))
                
def convert_afne_to_afn(transitions):
    afn_transitions = {}
    for state, transicoes in transitions.items():
        print(f"estado = {state}, transicoes = {transicoes}")
        for symbol, destination in transicoes:
            print(f"symbol = {symbol}, destinations = {destination}")
            # Remove as transições vazias
                # if symbol == "ε":
                #     continue
            if state not in afn_transitions:
                afn_transitions[state] = []
                # afn_transitions[state].append((symbol, destination))
            if destination not in afn_transitions:
                afn_transitions[destination] = []
            if "ε" in transicoes:
                for e_destination in transicoes["ε"]:
                    afn_transitions[state].append((symbol, e_destination))
                    if e_destination not in afn_transitions:
                        afn_transitions[e_destination] = []
                    afn_transitions[e_destination].append(("ε", destination))
            else:
                afn_transitions[destination].append(("ε", destination))
    return afn_transitions                
        
                
# print(convert_afne_to_afn(transition_function)) #             
                
                
              




def removeTransicaoVazia(transicoes_com_vazio, numero_de_estados):
    # Transforma um conjunto de transições de um AFNe em um conjunto de transições de um AFN, sem transições vazias.
    # Cria uma cópia das transições originais, sem as transições vazias
    transicoes = dict()

    transicoes = transition_function.copy()
    for estado in transition_function:
        transicoes[estado] = [] 
        for transicao in transition_function.get(estado):
            if transicao[0] != "ε":
                transicoes[estado].append(transicao)
    
    # Cria cópias das transições com transições vazias, conectando os estados de origem aos estados de destino diretamente
    transicao_vazia = {(origem, destino) for (origem, simbolo, destino) in transicao_vazia if simbolo == "e"}
    while transicao_vazia:
        (origem, destino) = transicao_vazia.pop()
        for (nova_origem, simbolo, nova_destino) in transicoes:
            if nova_destino == origem:
                nova_transition = (nova_origem, simbolo, destino)
                if nova_transition not in transicoes:
                    transicoes.add(nova_transition)
                    transicao_vazia.add((nova_origem, destino))
    
    return transicoes
    

class NFA:
    def __init__(self, _states, _input_symbols, _transition_function, _initial_state, _final_states):
        self.states = _states # estados
        self.input_symbols = _input_symbols # alfabeto
        self.transition_function = _transition_function # funções de transição 
        self.initial_state = _initial_state # estado inicial
        self.final_states = _final_states # estados finais
        self.current_states = set([_initial_state])

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



def main():
    automata = NFA(states, input_symbols, transition_function, initial_state, final_states)
    word = "acccccccccc"
    accepted = automata.process_word(word)

    if accepted:
        print(f"\"{word}\" was accepted")

    else:
        print(f"\"{word}\" was rejected")

if __name__ == "__main__":
    main()