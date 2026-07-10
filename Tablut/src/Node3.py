"""
MCTS 
"""

import copy
import math
import random
from . import config
from . import makeMove
from . import saveBoardState
from .checkBoard import checkBoard2
from .config import init_pieces
from .evaluateFunction import eval


B = 'B'
W = 'W'
K = 'K'


def switchTurn(onTurn):
    if onTurn == 'White':
        return 'Black'
    return 'White'


def legal_moves(board, onTurn):
    all_Moves = makeMove.total_moves(board, onTurn)
    if not isinstance(all_Moves, dict):
        return {}

    return {
        startPos: moves
        for startPos, moves in all_Moves.items()
        if moves
    }


class Node:

    def __init__(self, onTurn):
        self.score_sum = 0
        self.visit_count = 0
        self.state = None
        self.children = {}
        self.onTurn = onTurn

    def expanded(self):
        return len(self.children) > 0

    def value(self):
        if self.visit_count == 0:
            return 0
        return self.score_sum / self.visit_count

    def expand(self, state, onTurn):
        if checkBoard2(state) != -2:
            return

        self.state = state
        self.onTurn = onTurn

        all_Moves = legal_moves(self.state, onTurn)

        for startPos, movesList in all_Moves.items():
            for goalPos in movesList:
                self.children[(startPos, goalPos)] = Node(switchTurn(onTurn))

    def avg_value(self):
        return self.value()

    def select_child(self):
        unvisited = [
            (move, child)
            for move, child in self.children.items()
            if child.visit_count == 0
        ]
        if unvisited:
            return random.choice(unvisited)

        best_score = -math.inf
        bestChild = None
        bestMove = None

        for move, child in self.children.items():
            score = -child.value()
            if score > best_score or (score == best_score and random.random() < 0.5):
                best_score = score
                bestChild = child
                bestMove = move

        return bestMove, bestChild

    def best_child(self):
        best_score = -math.inf
        bestChild = None
        bestMove = None

        for move, child in self.children.items():
            if child.visit_count == 0:
                continue

            score = -child.value()
            if score > best_score or (score == best_score and random.random() < 0.5):
                best_score = score
                bestChild = child
                bestMove = move

        if bestMove is None and self.children:
            bestMove, bestChild = max(
                self.children.items(),
                key=lambda item: item[1].visit_count
            )
            best_score = -bestChild.value()

        return bestMove, bestChild, best_score


class MCTS:

    def score_for_player(self, board, depth, onTurn):
        score = eval(board, depth)

        if onTurn == 'White':
            return score
        return -score

    def run(self, state, onTurn, number_simulations=10000):

        
        
        init_pieces(state)

        saved_state = saveBoardState.save_global_state()

        root = Node(onTurn)
        root.expand(state, onTurn)

        for _ in range(number_simulations):

            config.zugRegel = 0
            config.zugCounter= 0
            
            node = root
            searched_path = [node]

            while node.expanded():
                move, node = node.select_child()
                searched_path.append(node)

            parent = searched_path[-2]
            new_state = copy.deepcopy(parent.state)
            makeMove.updateBoard(new_state, move)

            init_pieces(new_state)

            score = self.simulate(new_state, node.onTurn)

            node.expand(new_state, node.onTurn)

            self.backpropagate(searched_path, score)

        saveBoardState.restore_global_state(saved_state)

        best_move, _, _ = root.best_child()

        if best_move is None and root.children:
            best_move = max(root.children.items(), key=lambda item: item[1].visit_count)[0]

        return root

    def backpropagate(self, searched_path, score):
        for node in reversed(searched_path):
            node.visit_count += 1
            node.score_sum += score
            score = -score

    def simulate(self, state, onTurn):
        saved_state = saveBoardState.save_global_state()
        currentPlayer = onTurn
        board = copy.deepcopy(state)
        i = 0

        while checkBoard2(board) == -2:
            if i == 30:
                saveBoardState.restore_global_state(saved_state)
                return 0

            all_Moves = legal_moves(board, currentPlayer)

            if not all_Moves:
                score = self.score_for_player(board, -i, onTurn)
                saveBoardState.restore_global_state(saved_state)
                return score

            startPos = random.choice(list(all_Moves.keys()))
            goalPos = random.choice(all_Moves[startPos])

            makeMove.updateBoard(board, (startPos, goalPos))

            currentPlayer = switchTurn(currentPlayer)
            i += 1

        score = self.score_for_player(board, -i, onTurn)

        saveBoardState.restore_global_state(saved_state)
        return score
