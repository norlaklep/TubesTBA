import string

alphabet_list = list(string.ascii_lowercase) #mengubah semua huruf ke lowercase
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11','q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22','q23']


transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)]      = "error"
        transition_table[(state, "#")]      = "error"
        transition_table[(state, " ")]      = "error"
        transition_table[(state, "{")]      = "error"
        transition_table[(state, "}")]      = "error"
        transition_table[(state, "(")]      = "error"
        transition_table[(state, ")")]      = "error"
        transition_table[(state, "<")]      = "error"
        transition_table[(state, ">")]      = "error"
        transition_table[(state, "=")]      = "error"
        transition_table[(state, "+")]      = "error"
        transition_table[(state, "-")]      = "error"
        transition_table[(state, ";")]      = "error"

#Initial State (start)
transition_table["q0", " "]    = "q0"

#Finish State (FS)
transition_table[("q2", "#")] = "accept"
transition_table[("q2", " ")] = "q3"

transition_table[("q7", "#")] = "accept"
transition_table[("q7", " ")] = "q8"

transition_table[("q12", "#")] = "accept"
transition_table[("q12", " ")] = "q13"

transition_table[("q17", "#")] = "accept"
transition_table[("q17", " ")] = "q18"

transition_table[("q22", "#")] = "accept"
transition_table[("q22", " ")] = "q23"

#Subject
#String "if"
transition_table[("q0", "i")]  = "q1"
transition_table[("q1", "f")]  = "q2"

transition_table[("q3", "(")]  = "q4"

for alphabet in alphabet_list:
    transition_table[("q4", alphabet)] = "q5"
transition_table[("q4", " ")]  = "q4"

for alphabet in alphabet_list:
    transition_table[("q5", alphabet)] = "q5"
transition_table[("q5", ">")]  = "q6"
transition_table[("q5", "<")]  = "q6"
transition_table[("q5", "=")]  = "q6"
transition_table[("q5", "+")]  = "q6"
transition_table[("q5", "-")]  = "q6"
transition_table[("q5", ")")]  = "q7"
transition_table[("q5", " ")]  = "q5"


for alphabet in alphabet_list:
    transition_table[("q6", alphabet)] = "q5"
transition_table[("q6", "+")]  = "q5"
transition_table[("q6", "-")]  = "q5"
transition_table[("q6", "=")]  = "q6"
transition_table[("q6", " ")]  = "q6"

transition_table[("q8", "{")]  = "q9"

for alphabet in alphabet_list:
    transition_table[("q9", alphabet)] = "q10"
transition_table[("q9", " ")]  = "q9"

for alphabet in alphabet_list:
    transition_table[("q10", alphabet)] = "q10"
transition_table[("q10", ">")]  = "q11"
transition_table[("q10", "<")]  = "q11"
transition_table[("q10", "=")]  = "q11"
transition_table[("q10", "+")]  = "q11"
transition_table[("q10", "-")]  = "q11"
transition_table[("q10", ")")]  = "q11"
transition_table[("q10", "}")]  = "q12"
transition_table[("q10", " ")]  = "q10"


for alphabet in alphabet_list:
    transition_table[("q11", alphabet)] = "q10"
transition_table[("q11", "+")]  = "q10"
transition_table[("q11", "-")]  = "q10"
transition_table[("q11", "=")]  = "q11"
transition_table[("q11", " ")]  = "q11"

transition_table[("q13", "e")]  = "q14"

transition_table[("q14", "l")]  = "q15"

transition_table[("q15", "s")]  = "q16"

transition_table[("q16", "e")]  = "q17"

transition_table[("q17", " ")]  = "q18"

transition_table[("q18", "{")]  = "q19"
transition_table[("q18", "i")]  = "q1"

for alphabet in alphabet_list:
    transition_table[("q19", alphabet)] = "q10"
transition_table[("q19", " ")]  = "q19"

for alphabet in alphabet_list:
    transition_table[("q20", alphabet)] = "q20"
transition_table[("q20", ">")]  = "q21"
transition_table[("q20", "<")]  = "q21"
transition_table[("q20", "=")]  = "q21"
transition_table[("q20", "+")]  = "q21"
transition_table[("q20", "-")]  = "q21"
transition_table[("q20", ")")]  = "q21"
transition_table[("q20", "}")]  = "q22"
transition_table[("q20", " ")]  = "q20"

for alphabet in alphabet_list:
    transition_table[("q21", alphabet)] = "q20"
transition_table[("q21", "+")]  = "q20"
transition_table[("q21", "-")]  = "q20"
transition_table[("q21", "=")]  = "q21"
transition_table[("q21", " ")]  = "q21"

transition_table[("q23", " ")]  = "q13"

def display_transition_table(transition_table):
    print("Transition Table:")
    print("State\tSymbol\tNext State")
    print("------------------------")
    for key, value in transition_table.items():
        state, symbol = key
        next_state = value
        if next_state != "error":
          print(f"{state}\t{symbol}\t{next_state}")

display_transition_table(transition_table)

def lexical(sentence):

    #Initialization || menginialisasi semua state
    alphabet_list = list(string.ascii_lowercase) #mengubah semua huruf ke lowercase
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11',
                'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22',
                'q23','q24','q25']


    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)]      = "error"
            transition_table[(state, "#")]      = "error"
            transition_table[(state, " ")]      = "error"
            transition_table[(state, "{")]      = "error"
            transition_table[(state, "}")]      = "error"
            transition_table[(state, "(")]      = "error"
            transition_table[(state, ")")]      = "error"
            transition_table[(state, "<")]      = "error"
            transition_table[(state, ">")]      = "error"
            transition_table[(state, "=")]      = "error"
            transition_table[(state, "+")]      = "error"
            transition_table[(state, "-")]      = "error"

    #Initial State (start)
    transition_table["q0", " "]    = "q0"

    #Finish State (FS)
    transition_table[("q2", "#")] = "accept"
    transition_table[("q2", " ")] = "q3"

    transition_table[("q7", "#")] = "accept"
    transition_table[("q7", " ")] = "q8"

    transition_table[("q12", "#")] = "accept"
    transition_table[("q12", " ")] = "q13"

    transition_table[("q17", "#")] = "accept"
    transition_table[("q17", " ")] = "q18"

    transition_table[("q22", "#")] = "accept"
    transition_table[("q22", " ")] = "q23"

    #Subject
    #String "if"
    transition_table[("q0", "i")]  = "q1"
    transition_table[("q1", "f")]  = "q2"

    transition_table[("q3", "(")]  = "q4"

    for alphabet in alphabet_list:
        transition_table[("q4", alphabet)] = "q5"
    transition_table[("q4", " ")]  = "q4"

    for alphabet in alphabet_list:
        transition_table[("q5", alphabet)] = "q5"
    transition_table[("q5", ">")]  = "q6"
    transition_table[("q5", "<")]  = "q6"
    transition_table[("q5", "=")]  = "q6"
    transition_table[("q5", "+")]  = "q6"
    transition_table[("q5", "-")]  = "q6"
    transition_table[("q5", ")")]  = "q7"
    transition_table[("q5", " ")]  = "q5"


    for alphabet in alphabet_list:
        transition_table[("q6", alphabet)] = "q5"
    transition_table[("q6", "+")]  = "q5"
    transition_table[("q6", "-")]  = "q5"
    transition_table[("q6", "=")]  = "q6"
    transition_table[("q6", " ")]  = "q6"

    transition_table[("q8", "{")]  = "q9"

    for alphabet in alphabet_list:
        transition_table[("q9", alphabet)] = "q10"
    transition_table[("q9", " ")]  = "q9"

    for alphabet in alphabet_list:
        transition_table[("q10", alphabet)] = "q10"
    transition_table[("q10", ">")]  = "q11"
    transition_table[("q10", "<")]  = "q11"
    transition_table[("q10", "=")]  = "q11"
    transition_table[("q10", "+")]  = "q11"
    transition_table[("q10", "-")]  = "q11"
    transition_table[("q10", ")")]  = "q11"
    transition_table[("q10", " ")]  = "q10"
    transition_table[("q10", ";")]  = "q24"


    for alphabet in alphabet_list:
        transition_table[("q11", alphabet)] = "q10"
    transition_table[("q11", "+")]  = "q10"
    transition_table[("q11", "-")]  = "q10"
    transition_table[("q11", "=")]  = "q11"
    transition_table[("q11", " ")]  = "q11"

    transition_table[("q13", "e")]  = "q14"

    transition_table[("q14", "l")]  = "q15"

    transition_table[("q15", "s")]  = "q16"

    transition_table[("q16", "e")]  = "q17"

    transition_table[("q18", "{")]  = "q19"
    transition_table[("q18", "i")]  = "q1"

    for alphabet in alphabet_list:
        transition_table[("q19", alphabet)] = "q10"
    transition_table[("q19", " ")]  = "q19"

    for alphabet in alphabet_list:
        transition_table[("q20", alphabet)] = "q20"
    transition_table[("q20", ">")]  = "q21"
    transition_table[("q20", "<")]  = "q21"
    transition_table[("q20", "=")]  = "q21"
    transition_table[("q20", "+")]  = "q21"
    transition_table[("q20", "-")]  = "q21"
    transition_table[("q20", ")")]  = "q21"
    transition_table[("q20", " ")]  = "q20"
    transition_table[("q20", ";")]  = "q25"

    for alphabet in alphabet_list:
        transition_table[("q21", alphabet)] = "q20"
    transition_table[("q21", "+")]  = "q20"
    transition_table[("q21", "-")]  = "q20"
    transition_table[("q21", "=")]  = "q21"
    transition_table[("q21", " ")]  = "q21"

    transition_table[("q23", " ")]  = "q13"

    transition_table[("q24", "}")]  = "q12"
    transition_table[("q25", "}")]  = "q22"


    #Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        #print(current_char)
        #print(state,"\n")
        if state=='q28':
            print('CURRENT TOKEN  : ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print(current_token,"    \"",current_char,"\"<- error, tidak valid")
            break
        idx_char = idx_char + 1


    #Conclusion || state yang di accept
    if state == "accept":
        print('SEMUA TOKEN YANG DIINPUT : ', sentence, ', valid')

    return lexical

#Main Program Lexical
print("======== TERMINAL ========")
print("if ( a>b ) { a = a + b ; } else {a=a-b;}")
print("========================== \n ")
sentence = "if ( a>b ) { a = a + b ; } else {a=a-b;}"
input_string = sentence.lower()+'#'
lexical(input_string)
print("\n\n")

print("======== TERMINAL ========")
print("if (a<=f) { a=f; } else if (b<=f) {b=f;}")
print("========================== \n ")
sentence = "if (a<=f) { a=f; } else if (b<=f) {b=f;}"
input_string = sentence.lower()+'#'
lexical(input_string)
print("\n\n")

print("======== TERMINAL ========")
print("if (berat==batas) { berat--; }")
print("========================== \n ")
sentence = "if (berat==batas) { berat--; }"
input_string = sentence.lower()+'#'
lexical(input_string)
print("\n\n")

print("======== TERMINAL ========")
print("if (a>b) { a-b; }}")
print("========================== \n ")
sentence = "if (a>b) { a-b; }}"
input_string = sentence.lower()+'#'
lexical(input_string)
print("\n\n")

print("======== TERMINAL ========")
print("if (z>g)) { g++; } ")
print("========================== \n ")
sentence = "if (z>g)) { g++; }"
input_string = sentence.lower()+'#'
lexical(input_string)
print("\n\n")

