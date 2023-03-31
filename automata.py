# NFA: Non-Deterministic Finite Automation

# This automata accepts all strings with 01.
states = ("1", "2", "3")
input_symbols = ("0", "1")
transition_function = {
                        "1" : {"0" : "2"},
                        "2" : {"1" : "3"},
                        "3" : {"0" : "3", "1" : "3"}
                        }
initial_state = "1"
final_states = ("3")

class NFA:
    def __init__(self, _states, _input_symbols, _transition_function, _initial_state, _final_states):
        self.states = _states
        self.input_symbols = _input_symbols
        self.transition_function = _transition_function
        self.initial_state = _initial_state
        self.final_states = _final_states
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

                    new_states = transitions_from_curr_state.get(input)
                    
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
    word = "0111100"
    accepted = automata.process_word(word)

    if accepted:
        print(f"\"{word}\" was accepted")

    else:
        print(f"\"{word}\" was rejected")

if __name__ == "__main__":
    main()