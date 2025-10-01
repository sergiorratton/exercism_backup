def tally(rows):
    # Cabeçalho
    tab_final = [["Team", "MP", "W", "D", "L", "P"]]

    for item in rows:
        team1, team2, result = item.split(";")

        # Função auxiliar para atualizar ou criar time
        def atualizar_time(nome, is_winner=False, is_draw=False):
            # Procurar sublista do time
            sublista = next((s for s in tab_final if s[0] == nome), None)
            if not sublista:
                # Se não existir, criar nova sublista
                sublista = [nome, 0, 0, 0, 0, 0]
                tab_final.append(sublista)

            # Atualizar partidas
            sublista[1] += 1

            # Atualizar vitória/empate/derrota
            if is_draw:
                sublista[3] += 1
                sublista[5] += 1
            elif is_winner:
                sublista[2] += 1
                sublista[5] += 3
            else:
                sublista[4] += 1

        # Atualizar times conforme resultado
        if result == "win":
            atualizar_time(team1, is_winner=True)
            atualizar_time(team2, is_winner=False)
        elif result == "draw":
            atualizar_time(team1, is_draw=True)
            atualizar_time(team2, is_draw=True)
        else:  # loss
            atualizar_time(team1, is_winner=False)
            atualizar_time(team2, is_winner=True)
    # Transformar cada sublista em string formatada
    tab_retorno = []
    header = "Team                           | MP |  W |  D |  L |  P"
    tab_final[1:] = sorted(
        tab_final[1:], 
        key=lambda x: (-x[5], x[0])  # -x[5] = pontos desc / x[0] = nome asc
    )
    tab_retorno.append(header)
    for sublista in tab_final[1:]:
        linha = f"{sublista[0]:<30} | {sublista[1]:>2} | {sublista[2]:>2} | {sublista[3]:>2} | {sublista[4]:>2} | {sublista[5]:>2}"
        tab_retorno.append(linha)

    return tab_retorno