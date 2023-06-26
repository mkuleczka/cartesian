import itertools

def create_cartesian_product(in_data):
    dict_out = {}  # temporary dictionary
    for element in range(len(in_data)):
        dict_out[in_data[element]['name']] = []
        words_list = in_data[element]['words']  # reading words of list from dictionary

        for i in range(len(words_list)):
            if '#' in words_list[i]:  # needs decoding if string contains '#word'
                splitted_values = words_list[i].split()

                word_decoded = []
                for j in range(len(splitted_values)):
                    if splitted_values[j] in dict_out:
                        word_decoded.append(dict_out[splitted_values[j]])  # replace with decoded '#word'
                    else:
                        word_decoded.append([splitted_values[j]])  # keep original value without decoded '#word'

                cartesian_list = []  # create cartesian product
                for prod in itertools.product(*word_decoded):
                    cartesian_list.append(" ".join(prod))
                dict_out[in_data[element]['name']].extend(cartesian_list)  # add decoded data to temporary dictionary

            else:
                dict_out[in_data[element]['name']].append(words_list[i])  # added raw data without decoding

    return [{'name': k, 'words': v} for k, v in dict_out.items()]  # returning in required format


if __name__ == "__main__":
    """
    data1 = [{'name': '#hours',
              'words': [f'{str(hour)}:{minute}' for hour in range(24) for minute in ['00', '15', '30', '45']]},
             {'name': '#before', 'words': ['before #hours']}]
    data2 = [{'name': '#not',
              'words': ['not']},
             {'name': '#interested', 'words': ['interested']},
             {'name': '#not_interested', 'words': ['#not #interested', 'i\'am #not_interested']}]
    print(create_cartesian_product(data1))
    print(create_cartesian_product(data2))
    """

    in_data = eval(input())
    print(create_cartesian_product(in_data))