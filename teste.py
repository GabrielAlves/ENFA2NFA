# Para cada estado do automato
for estado in transition_function:
    transicoes_finais[estado] = []
    transicoes_vazias[estado] = [] 
    for transicao in transition_function.get(estado):
        if transicao[0] != "ε":
            transicoes_finais[estado].append(transicao)
        else:
            transicoes_vazias[estado].append(transicao)
    # Se esse estado não possuir nenhuma transição vazia ignore
    # if len(transicoes_vazias.get(estado)) == 0:
    #     continue
    transicoes_vazia_no_vertice = transicoes_vazias.get(estado)
    iteracao = 0
    # Enquanto houverem transições vazias daquele estado para outro
    while len(transicoes_vazia_no_vertice) != 0:
        print(f" iteração {iteracao} = {transicoes_vazia_no_vertice}")
        # Analisando a Transição feita
        transicao_analisada = transicoes_vazia_no_vertice.pop()
        print(transicao_analisada)
        if estado in initial_state:
            initial_state.append(transicao_analisada[1])
            print(f"Estados Iniciais Atualizados! : {initial_state}")
        if transicao_analisada[1] in final_states:
            final_states.append(estado)
        
            print(f"Estados Finais Atualizados! : {final_states}")
        for transicao_do_estado_destino in transition_function.get(transicao_analisada[1]):
            if transicao_do_estado_destino[0] != "ε":
                if transicao_do_estado_destino not in transicoes_finais[estado]:
                    print(f"Transição Nova Adicionada! {transicao_do_estado_destino}")
                    transicoes_finais[estado].append(transicao_do_estado_destino)
                else:
                    print("Essa Transição já está no Estado!")
            elif transicao_do_estado_destino not in transicoes_finais[estado]:
                print(f"Transição vazia a mais! {transicao_do_estado_destino}")
                transicoes_vazia_no_vertice.append(transicao_do_estado_destino)
        iteracao += 1