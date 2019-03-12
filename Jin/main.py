import numpy as np


def readAutomata(f):
    global states, inputs, final_states
    # deletes comments in file
    forg = open("testautomata.mat", "r")
    for s in forg:
        if (s[0] != '#'):
            f.write(s)
    f.close()
    f = open(".automata.mat", "r")

    number_inputs = int(f.readline())
    number_states = int(f.readline())

    # reads possible inputs of automaton
    inputs_line = f.readline()
    for i in range(number_inputs):
        inputs.append(inputs_line[i])

    # reads possible states of automaton
    states_line = f.readline()
    for i in range(number_states):
        states.append(states_line[i])
    # reads final states
    final_states_line = f.readline()
    for c in final_states_line:
        final_states.append(c)

    # fills automata_matrix
    mat = np.chararray((number_states, number_inputs), unicode=True)
    for i in range(number_states):
        s = f.readline()
        for j in range(number_inputs):
            mat[i][j] = s[j]
    return mat


def recSearchStates(start_state, mat, closure):
    if mat[start_state][mat[0].size - 1]:
        for i in range(mat[start_state][mat[0].size - 1]):
            recSearchStates(mat[start_state][mat[0].size - 1][i], mat, closure)

    closure.append(start_state)

    return closure


def insertClosures(state_NFA, mat, closure):
    for i in range(state_NFA):
        recSearchStates(i, mat, closure)

    return 0


def make_NFA_Closures(mat):
    closures = [mat.size]
    for i in range(mat.size):
        insertClosures(i, mat, closures[i])
    return closures


def formatPackge(pacakge):
    newPackge = np.chararray(pacakge.size, unicode=True)
    minAux = pacakge[0]
    index = 0

    while pacakge.size:
        for i in range(pacakge.size):
            if pacakge[i] <= minAux:
                minAux = pacakge[i]
                index = i

        newPackge.append(minAux)
        aux = [minAux]
        pacakge.delete(aux, index)
        minAux = pacakge[0]

    return newPackge


def transferClosures(closure, mat, input_NFA):
    newPackge = np.chararray(999, unicode=True)
    numElements = 0

    for i in range(closure.size):
        if closure[i].size:
            for j in range(mat[closure[i]][input_NFA].size):
                newPackge.append(mat[closure[i]][input_NFA][j])
                numElements += 1

    aux = np.chararray(numElements, unicode=True)

    while newPackge[0]:
        aux.append(newPackge[0])
        index = [newPackge[0]]
        newPackge.delete(index, 0)

    return formatPackge(aux)


def findPackges(closures):
    packges = []
    packges.append(closures[0])
    for i in range(closures.size):
        

def comparePackge(packge1, packge2):
    if packge1.size != packge2.size:
        return False
    else:
        for i in range(packge1.size):
            if packge1[i] == packge2[i]:
                continue
            else:
                return False

        return True


def locatePackge(packges, packge):
    for i in range(packges.size):
        if comparePackge(packges[i], packge):
            return i


def makeMatrix(packges, result_set):
    global num_inputs
    automaton = np.chararray((result_set.size, num_inputs), unicode=True)
    for i in range(automaton.size):
        for j in range(automaton[0].size):
            if result_set[i][j]:
                automaton[i][j] = locatePackge(packges, result_set[i][j])
            else:
                automaton[i][j] = '.'

    return automaton


# main
states = []
inputs = []
final_states = []
f = open(".automata.mat", "w")
automata = readAutomata(f)
print('inputs:')
print(inputs)
print('states:')
print(states)
print('automata:')
print(automata)