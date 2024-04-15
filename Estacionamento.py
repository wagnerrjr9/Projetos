#
#
# Integrante: Gabriel Rocha Aboboreira, RA: 10420207
# Integrante: Giovanni Coelho Birochi, RA: 10443452
#
#
# Menu que vai aparecer sempre que chamarem a função opc_do_menu()
from datetime import datetime
qtde_veiculos_entraram = 0
qtde_veiculos_sairam = 0
tempo_total_permanencia = 0
valor_total = 0
veiculo_moto = 0
veiculo_carro_pequeno = 0
veiculo_carro_grande = 0
moto_valor = 0
qt_moto = 0
carro_grande_valor = 0
qt_carro_grande = 0
carro_pequeno_valor = 0
qt_carro_pequeno = 0

def opc_do_menu():
    print("\n1. Cadastrar Tarifas")
    print("2. Registrar Entrada de Veiculo")
    print("3. Registrar Saida de Veiculo")
    print("4. Gerar Relatório diario")
    print("5. Gerar Relatório por tipo de veiculo")
    print("6. Sair")
    opc = int(input("Digite uma opção entre 1 e 6: "))
    return opc


# Loop onde o código estar em laço
while True:

    
# Sempre que uma opção for terminada opc vai chamar novamente a função opc_do_menu e o usuario pode escolher outro opção/valor para opc e continuar o programa
    opc = opc_do_menu()

   
# Para sair do laço opção tem que ser igual a 6   
    if opc == 6:
        break

    
# Na opção 1 deve ser inserido os dados de custo de horas por veiculo
    if opc == 1:
        print("\nColoque o valor fixo e adicional de cada veiculo.")
        carro_pequeno_3h = int(input("Valor fixo 3h carro pequeno: "))
        carro_pequeno_adicional = int(input("Valor horas adicional carro pequeno: "))
        carro_grande_3h = int(input("Valor fixo 3h carro grande: "))
        carro_grande_adicional = int(input("Valor horas adicional carro grande: "))
        moto_3h = int(input("Valor fixo 3h moto: "))
        moto_adicional = int(input("Valor horas adicional moto: "))

        
# Na opção 2 vai ser cadastrado a entrado do veiculo expecificando data/horario, tipo de veiculo, placa e gerando um recibo
    elif opc == 2:
        qtde_veiculos_entraram +=1
        print ("/nColoque as infomaçoes do veiculo de entrada")
        tipo_veiculo = input("Digite o tipo de veículo (carro_pequeno, carro_grande, moto): ")
        placa =(input("Digite a placa do veiculo: "))
        data_hora_entrada_str = input("Digite a data e hora entrada veiculo nesse formato(AAAA-MM-DD HH:MM): ")
        data_hora_entrada = datetime.strptime(data_hora_entrada_str, "%Y-%m-%d %H:%M")
        print("")
        print(f"\nRecibo de Entrada\nPlaca: {placa}\nTipo: {tipo_veiculo}\nData/Hora: {data_hora_entrada}")
        print("")
        if tipo_veiculo == "moto":
            veiculo_moto += 1
        elif tipo_veiculo == "carro_pequeno":
            veiculo_carro_pequeno += 1
        elif tipo_veiculo == "carro_grande":
            veiculo_carro_grande += 1
            
        
# Na opção 3 vai ser registrado a saida do veiculo expecificando o horario saida, onde a data de saida vai ser subtraida pela data de entrada, achando o tempo de permanencia do veiculo
# esse tempo de permanencia é dividido por 3600 que são os segundos em uma hora
# Ao escolher o tipo de veiculo sera comparado se o tempo estacionado é superior a 3 horas se não for sera cobrada apenas as 3 horas.
# Se o tempo for superior as 3 horas sera cobrado horas adicionais, onde sera somado ao valor final o custo fixo das 3 horas e subtraido do tempo de permanencia 3 horas
# desse modo só sera cobrado o tempo de permanencia após as 3 horas no valor do custo das horas adicionais para aquele veiculo.
# Sendo gerado um recibo de saida com as infomações da data/hora de saida, placa, tipo de veiculo, tempo de permanencia e valor pago.
    elif opc == 3:
        print ("\nColoque as infomaçoes do veiculo de saida")
        data_hora_saida_str = input("Digite a data e hora de saida desse veiculo nesse formato(AAAA-MM-DD HH:MM): ")
        data_hora_saida = datetime.strptime(data_hora_saida_str, "%Y-%m-%d %H:%M")
        tempo_permanencia = data_hora_saida - data_hora_entrada
        horas = tempo_permanencia.seconds / 3600
        qtde_veiculos_sairam += 1
        tempo_total_permanencia += float(horas)
        if tipo_veiculo == "carro_pequeno":
            if horas <= 3:
                valor = float(carro_pequeno_3h)
                valor_total += valor
                carro_pequeno_valor += valor
                qt_carro_pequeno += 1
            else:
                horas_adicionais = horas - 3
                valor = float(carro_pequeno_3h + (horas_adicionais * carro_pequeno_adicional))
                valor_total += valor
                carro_pequeno_valor += valor
                qt_carro_pequeno += 1
        elif tipo_veiculo == "carro_grande":
            if horas <= 3:
                valor = float(carro_grande_3h)
                valor_total += valor
                carro_grande_valor += valor
                qt_carro_grande += 1
            else:
                horas_adicionais = horas - 3
                valor = float(carro_grande_3h + (horas_adicionais * carro_grande_adicional))
                valor_total += valor
                carro_grande_valor += valor
                qt_carro_grande += 1
        elif tipo_veiculo == "moto":
            if horas <= 3:
                valor = float(moto_3h)
                valor_total += valor
                moto_valor += valor
                qt_moto += 1
            else:
                horas_adicionais = horas - 3
                valor = float(moto_3h + (horas_adicionais * moto_adicional))
                valor_total += valor
                moto_valor += valor
                qt_moto += 1
        else:
            print("\nTipo de veículo inválido.")
        print("")
        print(f"\nRecibo de Saida\nData/Hora: {data_hora_saida}\nPlaca: {placa}\nTipo: {tipo_veiculo}\nTempo de permanencia: {tempo_permanencia}\nValor pago R$ {valor}")
        print("")

        
# Na opção 4 séra feito relátorio geral com a quantidade de veiculos que entraram e sairam do estacionamento naquele dia, calculando o tempo medio que os veiculos ficam no estacionamento
# As constates que armazena esses valores que estão na opção 4 esta na opção 3
    elif opc == 4:
        tempo_medio_permanencia = tempo_total_permanencia / qtde_veiculos_sairam
        print("")
        print(f"\nRelatório\nTempo medio: {tempo_medio_permanencia}\nValor total arrecadado: {valor_total}\nQuantidade total de veiculos: {qtde_veiculos_entraram}\nQuantidade de veículos que entraram: {qtde_veiculos_entraram}\nQuantidade de veículos que saíram: {qtde_veiculos_sairam}")
        print("")

        
# Na opção 5 séra feito relátorio com a opção que o cliente escolheu mostrando o valor medio gasto por aquele veiculo e a horas medias que aquele veiculo estar estacionado
#As constates que contem as informações que sera usada para calcular o valor medio gasto e tempo medio de cada veiculo estar na opção 3
    elif opc == 5:
        veiculo_tipo = input("Digite o tipo de veículo (carro_pequeno, carro_grande, moto): ")
        if veiculo_tipo == "moto":
            moto_media = moto_valor/qt_moto
            print("")
            print(f"Relatório\nMédia de valor arrecadado moto: {moto_media}")
        elif veiculo_tipo == "carro_pequeno":
            carro_pequeno_media = carro_pequeno_valor/qt_carro_pequeno
            print("")
            print(f"Relatório\nMédia de valor arrecadado carro pequeno: {carro_pequeno_media}")
        elif veiculo_tipo == "carro_grande":
            carro_grande_media = carro_grande_valor/qt_carro_grande
            print("")
            print(f"Relatório\nMédia de valor arrecadado carro gradne: {carro_grande_media}")
            
        if veiculo_moto > veiculo_carro_pequeno or veiculo_carro_grande:
            print(f"Moto é o veiculo que mais entra no total de: {veiculo_moto}")
            print("")
        elif veiculo_carro_pequeno > veiculo_moto or veiculo_carro_grande:
            print(f"Carro pequeno é o veiculo que mais entra no total de: {veiculo_carro_pequeno}")
            print("")
        elif veiculo_carro_grande > veiculo_moto or veiculo_carro_pequeno:
            print(f"Carro grande é o veiculo que mais entra no total de: {veiculo_carro_grande}")
            print("")
        else:
          print("Tipo de veiculo invalido")
    else:
          print("Opção Invalida")



