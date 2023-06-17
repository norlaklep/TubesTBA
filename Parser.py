def parser(sentence):
    print("=========================================")
    print("=======       PROSES PARSER       =======")
    print("========================================= \n")

    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['Statement','kondisi','aksi','ekspresi','variable']
    terminals = ['if', ':' , 'else', '>', 'c', '=', '*', '+', 'a', 'b']

    parse_table = {}

    parse_table[('Statement', 'if')]    = ['if','kondisi',':','aksi','else',':','aksi']
    parse_table[('Statement', 'else')]  = ['if','kondisi',':','aksi','else',':','aksi'] 
    parse_table[('Statement', ':')]     = ['if','kondisi',':','aksi','else',':','aksi'] 
    parse_table[('Statement', '>')]     = ['error']
    parse_table[('Statement', '=')]     = ['error']
    parse_table[('Statement', '*')]     = ['error'] 
    parse_table[('Statement', '+')]     = ['error'] 
    parse_table[('Statement', 'a')]     = ['error']
    parse_table[('Statement', 'b')]     = ['error']
    parse_table[('Statement', 'c')]     = ['error']  
    parse_table[('Statement', 'EOS')]   = ['error']

    parse_table[('kondisi', 'if')]      = ['error']
    parse_table[('kondisi', 'else')]    = ['error']
    parse_table[('kondisi', ':')]       = ['error']
    parse_table[('kondisi', '>')]       = ['variable','>','variable'] 
    parse_table[('kondisi', '=')]       = ['error']
    parse_table[('kondisi', '*')]       = ['error'] 
    parse_table[('kondisi', '+')]       = ['error'] 
    parse_table[('kondisi', 'a')]       = ['error']
    parse_table[('kondisi', 'b')]       = ['error']
    parse_table[('kondisi', 'c')]       = ['error']  
    parse_table[('kondisi', 'EOS')]     = ['error']

    parse_table[('aksi', 'if')]         = ['error']
    parse_table[('aksi', 'else')]       = ['error']
    parse_table[('aksi', ':')]          = ['error']
    parse_table[('aksi', '>')]          = ['error']
    parse_table[('aksi', '=')]          = ['c','=','ekspresi']
    parse_table[('aksi', '*')]          = ['error'] 
    parse_table[('aksi', '+')]          = ['error'] 
    parse_table[('aksi', 'a')]          = ['error']
    parse_table[('aksi', 'b')]          = ['error']
    parse_table[('aksi', 'c')]          = ['c','=','ekspresi']
    parse_table[('aksi', 'EOS')]        = ['error']

    parse_table[('ekspresi', 'if')]     = ['error']
    parse_table[('ekspresi', 'else')]   = ['error']
    parse_table[('ekspresi', ':')]      = ['error']
    parse_table[('ekspresi', '>')]      = ['error'] 
    parse_table[('ekspresi', '=')]      = ['error']
    parse_table[('ekspresi', '*')]      = ['variable', '*','variable'] 
    parse_table[('ekspresi', '+')]      = ['variable', '+','variable'] 
    parse_table[('ekspresi', 'a')]      = ['error']
    parse_table[('ekspresi', 'b')]      = ['error']
    parse_table[('ekspresi', 'c')]      = ['error']  
    parse_table[('ekspresi', 'EOS')]    = ['error']

    parse_table[('variable', 'if')]     = ['error']
    parse_table[('variable', 'else')]   = ['error']
    parse_table[('variable', ':')]      = ['error']
    parse_table[('variable', '>')]      = ['error']
    parse_table[('variable', '=')]      = ['error']
    parse_table[('variable', '*')]      = ['error'] 
    parse_table[('variable', '+')]      = ['error'] 
    parse_table[('variable', 'a')]      = ['a']
    parse_table[('variable', 'b')]      = ['b']
    parse_table[('variable', 'c')]      = ['error']  
    parse_table[('variable', 'EOS')]    = ['error']


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
print("==================================== \n ")
sentence = input("MASUKKAN INPUT : ")
input_string = sentence.lower()+'#'
parser(sentence)
