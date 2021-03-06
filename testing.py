from Automata import *

def testAutomata(automata, states, inputs, final_states,input_string):
    accepted = True 
    for i in input_string:
        if (belongs_to_list(i, inputs) == False):
            return False
    ans = search_automata(automata, states, input_string, 0, 0, len(input_string) - 1, final_states)
    return ans


def search_automata(automata, states, inputs, s, i, max_i, final_states):
    cur_input = int(inputs[i])
    if i + 1 > max_i:
        if belongs_to_list(str(automata[s][cur_input]), final_states) == True:
            return True
        else:
            return False
    if automata[s][cur_input] == '.': return False
    s = states.index(automata[s][cur_input])
    return search_automata(automata, states, inputs, s, i + 1, max_i, final_states)


def belongs_to_list(char, test):
    belongs = False
    for c in test:
        if (c == char):
            belongs = True
    return belongs


def mirrorAutomata(a):
    print('Making mirror...')
    m = []
    #copies the dimensions of original automata matrix
    for i in range (len(a.matrix)):
        m.append([])
        for j in range (len(a.matrix[i])):
            m[i].append([])
    
    #find the mirrored indexes with its corresponding location
    #in the original automata and adds theem to a list
    indexes = []
    for i in range (len(a.matrix)): 
        indexes.append ( search_mirror(a.states[i],a) )
    

    #shows all the found indexes to be copied to mirror
    print('FOUND INDEXES FOR MIRROR:')
    printMatrix(indexes) 
    
    #puts the found indexes along with the appropiate state
    #in the mirror matrix
    for i in range( len(indexes) ):
        for j in range (len(indexes[i])):
            m[i][indexes[i][j][1]].append(indexes[i][j][0])
    #puts the corresponding '.' char in the empty lists
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (len(m[i][j]) == 0):
                m[i][j].append('.')
    return Automata(m,a.states,a.inputs,a.initial_state,a.final_states)

def search_mirror(target,a):
    res = []
    for i in range (len(a.matrix)):
        for j in range(len(a.matrix[i])):
            if a.matrix[i][j] == [ target ]:
                res.append([a.states[i],j])
    return res

def printAutomata(a):
    print('STATES:')
    print (a.states)
    print('INPUTS:')
    print (a.inputs)
    print('FINAL STATES:')
    print (a.final_states)
    print('INITIAL STATE:')
    print (a.initial_state)
    print('MATRIX:')
    printMatrix(a.matrix)

def printMatrix(m):
    mat = ''
    for i in range (len(m)):
        for j in range (len(m[i])):
            mat += str ( m[i][j] )
        mat += '\n'
    print (mat)

#MAIN
matrix =    [[['A'],['C'],['D'],['F']],\
            [['.'],['B'],['.'],['.']],\
            [['.'],['B'],['F'],['F']],\
            [['D'],['.'],['.'],['.']],\
            [['S'],['.'],['E'],['.']],\
            [['.'],['F'],['.'],['.']],\
            [['.'],['.'],['.'],['.']]]
        
states = ['S','A','B','C','D','E','F']
inputs = ['a','b','c','d']
final_states = ['F']
initial_state = ['S']
a = Automata(matrix,states,inputs,final_states,initial_state)
printAutomata(a)
m = mirrorAutomata(a)
printAutomata(m)
