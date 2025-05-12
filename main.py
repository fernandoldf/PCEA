def list_analyzer(input_list: list) ->  None:
    total_sum = sum(input_list)
    number_values = len(input_list)
    mean_value = total_sum / number_values
    max_value = max(input_list)
    min_value = min(input_list)
    even_num = 0
    for number in input_list:
        if number % 2 == 0:
            even_num += 1
    print(f"Média: {mean_value:.2f}")
    print(f"Maior número: {max_value}")
    print(f"Menor número: {min_value}")
    print(f"Quantidade de números pares: {even_num}")