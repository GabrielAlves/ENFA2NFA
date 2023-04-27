# NFA: Non-Deterministic Finite Automation

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

word = "000000000001"

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
            
            for current_state in self.current_states:
                transitions_from_curr_state = self.transition_function.get(current_state)
                if transitions_from_curr_state is not None:

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
    
    def remove_empty_movements(self):
        final_transitions = dict()
        final_transitions = transition_function.copy()
        non_empty_transitions = dict()
        empty_transitions = dict()
        # Para cada estado do automato
        for state in transition_function:
            final_transitions[state] = []
            empty_transitions[state] = []
            non_empty_transitions[state] = []
            for transition in transition_function.get(state):
                if transition[0] != "ε":
                    final_transitions[state].append(transition)
                    non_empty_transitions[state].append(transition)
                else:
                    empty_transitions[state].append(transition)
                        
        for state in transition_function:
            non_empty_on_vertice_transitions = non_empty_transitions.get(state)
            # Enquanto houverem transições vazias daquele estado para outro
            while len(non_empty_on_vertice_transitions) != 0:
                # Analisando a Transição feita
                analysed_transition = non_empty_on_vertice_transitions.pop()
            
                # Para cada transicao que o estado destino da transição possui
                for destine_state_transition in transition_function.get(analysed_transition[1]):
                    if destine_state_transition[0] == "ε":
                        if destine_state_transition not in final_transitions[state]:
                            new_transition = (analysed_transition[0], destine_state_transition[1])
                            final_transitions[state].append(new_transition)
                            non_empty_on_vertice_transitions.append(new_transition)
                        
        for state in transition_function:
            on_vertice_empty_transition = empty_transitions.get(state)
            # Enquanto houverem transições vazias daquele estado para outro
            while len(on_vertice_empty_transition) != 0:
                # Analisando a Transição feita
                analysed_transition = on_vertice_empty_transition.pop()
                # Atualiza Estados Inciais e Estados Finais
                if state in initial_state:
                    initial_state.append(analysed_transition[1])
                if analysed_transition[1] in final_states:
                    final_states.append(state)
                # Para cada transicao que o estado destino da transição possui
                for destine_state_transition in transition_function.get(analysed_transition[1]):
                    if destine_state_transition[0] != "ε":
                        if destine_state_transition not in final_transitions[state]:
                            final_transitions[state].append(destine_state_transition)
                    elif destine_state_transition not in final_transitions[state]:
                        on_vertice_empty_transition.append(destine_state_transition)
        
        self.transition_function = final_transitions

def main():
    automata = NFA(states, input_symbols, transition_function, initial_state, final_states)
    automata.remove_empty_movements()
    #automata.removeTransicaoVazia() # Função para transformar o AFNe em AFN
    accepted = automata.process_word(word)
    
    if accepted:
        print(f"\"{word}\" was accepted")

    else:
        print(f"\"{word}\" was rejected")

if __name__ == "__main__":
    main()