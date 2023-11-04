def unpack(**dic):
    pair_strings = []
    for key, value in dic.items():
        pair_strings.append(f"{key} = {value}")

    result_string = ", ".join(pair_strings)
    print(result_string)

unpack(**parms)