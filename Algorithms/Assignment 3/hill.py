from board import Board
import copy
import datetime


def HC(state, rowNumber):
    if rowNumber == 4:
        rowNumber = 0
    if state.get_fitness() == 0:
        endTime = datetime.datetime.now()
        runTime = endTime -startTime
        print("Running time: ", int(runTime.total_seconds() * 1000), "ms")
        state.show_map()
    else:

        queenPosition = state.map[rowNumber].index(1)
        potential = "01234"
        if queenPosition == int(potential[0]):
            candidateState1 = copy.deepcopy(state)
            candidateState1.flip(rowNumber, 1)
            candidateState1.flip(rowNumber, queenPosition)
            candidateState2 = copy.deepcopy(state)
            candidateState2.flip(rowNumber, 2)
            candidateState2.flip(rowNumber, queenPosition)
            candidateState3 = copy.deepcopy(state)
            candidateState3.flip(rowNumber, 3)
            candidateState3.flip(rowNumber, queenPosition)
            candidateState4 = copy.deepcopy(state)
            candidateState4.flip(rowNumber, 4)
            candidateState4.flip(rowNumber, queenPosition)
        elif queenPosition == int(potential[1]):
            candidateState1 = copy.deepcopy(state)
            candidateState1.flip(rowNumber, 0)
            candidateState1.flip(rowNumber, queenPosition)
            candidateState2 = copy.deepcopy(state)
            candidateState2.flip(rowNumber, 2)
            candidateState2.flip(rowNumber, queenPosition)
            candidateState3 = copy.deepcopy(state)
            candidateState3.flip(rowNumber, 3)
            candidateState3.flip(rowNumber, queenPosition)
            candidateState4 = copy.deepcopy(state)
            candidateState4.flip(rowNumber, 4)
            candidateState4.flip(rowNumber, queenPosition)
        elif queenPosition == int(potential[2]):
            candidateState1 = copy.deepcopy(state)
            candidateState1.flip(rowNumber, 0)
            candidateState1.flip(rowNumber, queenPosition)
            candidateState2 = copy.deepcopy(state)
            candidateState2.flip(rowNumber, 1)
            candidateState2.flip(rowNumber, queenPosition)
            candidateState3 = copy.deepcopy(state)
            candidateState3.flip(rowNumber, 3)
            candidateState3.flip(rowNumber, queenPosition)
            candidateState4 = copy.deepcopy(state)
            candidateState4.flip(rowNumber, 4)
            candidateState4.flip(rowNumber, queenPosition)
        elif queenPosition == int(potential[3]):
            candidateState1 = copy.deepcopy(state)
            candidateState1.flip(rowNumber, 0)
            candidateState1.flip(rowNumber, queenPosition)
            candidateState2 = copy.deepcopy(state)
            candidateState2.flip(rowNumber, 1)
            candidateState2.flip(rowNumber, queenPosition)
            candidateState3 = copy.deepcopy(state)
            candidateState3.flip(rowNumber, 2)
            candidateState3.flip(rowNumber, queenPosition)
            candidateState4 = copy.deepcopy(state)
            candidateState4.flip(rowNumber, 4)
            candidateState4.flip(rowNumber, queenPosition)
        elif queenPosition == int(potential[4]):
            candidateState1 = copy.deepcopy(state)
            candidateState1.flip(rowNumber, 0)
            candidateState1.flip(rowNumber, queenPosition)
            candidateState2 = copy.deepcopy(state)
            candidateState2.flip(rowNumber, 1)
            candidateState2.flip(rowNumber, queenPosition)
            candidateState3 = copy.deepcopy(state)
            candidateState3.flip(rowNumber, 2)
            candidateState3.flip(rowNumber, queenPosition)
            candidateState4 = copy.deepcopy(state)
            candidateState4.flip(rowNumber, 3)
            candidateState4.flip(rowNumber, queenPosition)

        if candidateState1.get_fitness() >= state.get_fitness() and candidateState2.get_fitness() >= state.get_fitness() and candidateState3.get_fitness() >= state.get_fitness() and candidateState4.get_fitness() >= state.get_fitness():
            state = Board(5)
            HC(state, 0)
        else:
            decider = [candidateState1.get_fitness(), candidateState2.get_fitness(), candidateState3.get_fitness(), candidateState4.get_fitness()]
            minValue = decider.index(min(decider))
            rowNumber += 1
            if minValue == 0:
                HC(candidateState1, rowNumber)
            elif minValue == 1:
                HC(candidateState2, rowNumber)
            elif minValue == 2:
                HC(candidateState3, rowNumber)
            else:
                HC(candidateState4, rowNumber)


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    state = Board(5)
    HC(state, 0)