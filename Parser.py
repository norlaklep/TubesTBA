def parser(sentence):
    print("=========================================")
    print("=======       PROSES PARSER       =======")
    print("========================================= \n")

    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = []
    terminals = []

    parse_table = {}
    

    stack = []
    stack.append('#')
    stack.append('S')

    index_token = 0
    symbol = tokens[index_token]

    while(len(stack) > 0):
        top = stack[ len(stack) - 1 ]
        print('TOP    = ', top)
        print('SYMBOL = ', symbol)
        if top in terminals:
            print('TOP ADALAH SYMBOL TERMINAL')
            if top == symbol:
                stack.pop()
                index_token = index_token + 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('ISI STACK:', stack)
            else:
                print('ERROR')
                break;
        elif top in non_terminals:
            print('TOP ADALAH SYMBOL NON-TERMINAL')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                print('ERROR')
                break;
        else:
            print('ERROR')
            break;
        print('ISI STACK: ', stack)
        print()

    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Inputan String ', '"', sentence, '"', 'Diterima, Sesuai Grammar')
    else:
        print('ERROR, Inputan String:', '"', sentence, '"', ', Tidak Diterima, Tidak Sesuai Grammar')  
    
    return parser

#Main Program Parser
print("============= TERMINAL =============")
print("")
print("")
print("")
print("==================================== \n ")
sentence = input("MASUKKAN INPUT : ")
input_string = sentence.lower()+'#'
parser(sentence)
