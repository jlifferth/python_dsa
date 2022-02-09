
def matching_strings(strings, queries):
    query_dict = {}
    for query in queries:
        query_dict[query] = 0
        for string in strings:
            if query == string:
                query_dict[query] += 1
            else:
                continue

    result = []
    for value in queries:
        result.append(query_dict[value])

    return result


strings0 = ['aba', 'baba', 'aba', 'xzxb']
queries0 = ['aba', 'xzxb', 'ab']

strings1 = ['lekgdisnsbfdzpqlkg', 'eagemhdygyv', 'jwvwwnrhuai', 'urcadmrwlqe', 'mpgqsvxrijpombyv', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'mpgqsvxrijpombyv', 'eagemhdygyv', 'eagemhdygyv', 'jwvwwnrhuai', 'urcadmrwlqe', 'jwvwwnrhuai', 'kvugevicpsdf', 'kvugevicpsdf', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'mpgqsvxrijpombyv', 'exdafbnobg', 'qhootohpnfvbl', 'suffrbmqgnln', 'exdafbnobg', 'exdafbnobg', 'eagemhdygyv', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'jwvwwnrhuai', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai', 'exdafbnobg', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'qhootohpnfvbl', 'urcadmrwlqe', 'kvugevicpsdf', 'mpgqsvxrijpombyv', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'qhootohpnfvbl', 'lxyqetmgdbmh', 'urcadmrwlqe', 'urcadmrwlqe', 'kvugevicpsdf', 'lxyqetmgdbmh', 'urcadmrwlqe', 'lxyqetmgdbmh', 'jwvwwnrhuai', 'qhootohpnfvbl', 'qhootohpnfvbl', 'jwvwwnrhuai', 'lekgdisnsbfdzpqlkg', 'kvugevicpsdf', 'mpgqsvxrijpombyv', 'exdafbnobg', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'qhootohpnfvbl', 'exdafbnobg', 'qhootohpnfvbl', 'exdafbnobg', 'mpgqsvxrijpombyv', 'suffrbmqgnln', 'mpgqsvxrijpombyv', 'qhootohpnfvbl', 'jwvwwnrhuai', 'mpgqsvxrijpombyv', 'qhootohpnfvbl', 'lekgdisnsbfdzpqlkg', 'eagemhdygyv', 'jwvwwnrhuai', 'kvugevicpsdf', 'eagemhdygyv', 'eagemhdygyv', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'lxyqetmgdbmh', 'exdafbnobg', 'qhootohpnfvbl', 'qhootohpnfvbl', 'exdafbnobg', 'suffrbmqgnln', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'eagemhdygyv', 'lxyqetmgdbmh', 'urcadmrwlqe', 'suffrbmqgnln', 'qhootohpnfvbl', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'lxyqetmgdbmh', 'mpgqsvxrijpombyv', 'jwvwwnrhuai', 'lxyqetmgdbmh', 'lxyqetmgdbmh', 'lekgdisnsbfdzpqlkg', 'qhootohpnfvbl']
queries1 = ['exdafbnobg', 'eagemhdygyv', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'kvugevicpsdf', 'exdafbnobg', 'qhootohpnfvbl', 'eagemhdygyv', 'kvugevicpsdf', 'suffrbmqgnln', 'jwvwwnrhuai', 'lekgdisnsbfdzpqlkg', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'jwvwwnrhuai', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'exdafbnobg', 'suffrbmqgnln', 'qhootohpnfvbl', 'eagemhdygyv', 'exdafbnobg', 'suffrbmqgnln', 'jwvwwnrhuai', 'qhootohpnfvbl', 'eagemhdygyv', 'exdafbnobg', 'exdafbnobg', 'jwvwwnrhuai', 'qhootohpnfvbl', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'suffrbmqgnln', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'eagemhdygyv', 'jwvwwnrhuai', 'eagemhdygyv', 'qhootohpnfvbl', 'mpgqsvxrijpombyv', 'qhootohpnfvbl', 'jwvwwnrhuai', 'exdafbnobg', 'eagemhdygyv', 'eagemhdygyv', 'kvugevicpsdf', 'kvugevicpsdf', 'jwvwwnrhuai', 'urcadmrwlqe', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'exdafbnobg', 'exdafbnobg', 'eagemhdygyv', 'qhootohpnfvbl', 'exdafbnobg', 'exdafbnobg', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai', 'eagemhdygyv', 'urcadmrwlqe', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai', 'eagemhdygyv', 'lekgdisnsbfdzpqlkg', 'exdafbnobg', 'kvugevicpsdf', 'jwvwwnrhuai', 'exdafbnobg', 'lxyqetmgdbmh', 'exdafbnobg', 'lxyqetmgdbmh', 'jwvwwnrhuai', 'mpgqsvxrijpombyv', 'eagemhdygyv', 'urcadmrwlqe', 'kvugevicpsdf', 'qhootohpnfvbl', 'jwvwwnrhuai', 'eagemhdygyv', 'urcadmrwlqe', 'urcadmrwlqe', 'exdafbnobg', 'qhootohpnfvbl', 'exdafbnobg', 'eagemhdygyv', 'exdafbnobg', 'jwvwwnrhuai', 'eagemhdygyv', 'jwvwwnrhuai', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'urcadmrwlqe', 'eagemhdygyv', 'eagemhdygyv', 'jwvwwnrhuai', 'suffrbmqgnln', 'eagemhdygyv']

print(matching_strings(strings1, queries1))
