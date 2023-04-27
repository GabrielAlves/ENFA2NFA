# ENFA2NFA

Remove as transições vazias de um autômato finito não determinístico. Trabalho que valia qualitativo na disciplina de Teoria da computação. Feito com [Daniel](https://github.com/Flame2000). Estou atualizando atrasado o repositório :p. 

# Como usar

No topo do arquivo automata.py, defina os componentes do Autômato:

states é uma tupla de strings que representa o conjunto de estados do autômato. Os estados devem ser dígitos. 
Ex: `states = ("0", "1")` indica que o autômato possui dois estados 0 e 1.

input_symbols é uma tupla de strings que representa o alfabeto do autômato. A transição vazia reconhecida pelo autômato é ε.
Ex: `input_symbols = ("a", "b", "c")` indica que o autômato espera receber tais entradas durante uma leitura.

transition_function é um dicionário cujas chaves são estados do autômato e os valores são as transições a partir deles. Para ser mais específico, um valor do dicionário é uma lista que guarda um conjunto de tuplas, cada uma delas representando uma transição a partir do estado chave do dicionário. Essas tuplas estão na forma (entrada, estado) indicando que o autômato adquire tal estado após ler a dita entrada.

Ex: `transition_function = {
                        "0" : [("ε" , "1"), ("ε" , "2")], 
                        "1" : [("0" , "1"), ("1" , "3")],
                        "2" : [("0" , "3"), ("1" , "2")],
                        "3" : []
                        }`
                        
O trecho acima indica, por exemplo, que a partir do estado 1 saem duas transições: uma que vai para o estado 1 após ler a entrada "0" e outra para o estado 3 após ler a entrada "1"

initial_state é uma lista de strings que representa o conjunto de estados iniciais do autômato. Assim como em states, os estados 
devem ser dígitos em strings e eles devem estar listados na tupla states.
Ex: `initial_state = ["1"]` indica que o autômato possui o estado 1 como estado inicial

final_states é uma lista de strings que representa o conjunto de estados finais do autômato. Assim como em states, os estados devem
ser dígitos em strings e eles devem estar listados na tupla states.
Ex: `final_states = ["1", "3"]` indica que o autômato possui os estados 1 e 3 como estado final

word é uma string e representa a palavra que será processada pelo autômato definido.
Ex: `word = "aabcc"` indica que a palavra "aabcc" é a palavra que passará pelo autômato.

Após todos os parâmetros desejados terem sido definidos, basta executar o arquivo automata.py que o programa imprimirá uma mensagem no terminal indicando se a palavra foi aceita ou rejeitada.