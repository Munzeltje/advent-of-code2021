import numpy as np


def read_input(filename, board_size):
    drawn_numbers = np.loadtxt(filename, delimiter=",", max_rows=1, dtype=int)
    boards = np.loadtxt(filename, skiprows=1, dtype=int)
    boards = np.reshape(
        boards, (int(boards.shape[0] / board_size), board_size, board_size)
    )
    return drawn_numbers, boards


def find_losing_boards(mask):
    losing_boards = []
    for index, board in enumerate(mask):
        if np.any(np.all(board, axis=0)) or np.any(np.all(board, axis=1)):
            continue
        losing_boards.append(index)
    return losing_boards


def search_losing_mask_number(drawn_numbers, losing_board):
    for i, _ in enumerate(drawn_numbers):
        mask = np.isin(losing_board, drawn_numbers[:i])
        if np.any(np.all(mask, axis=0)) or np.any(np.all(mask, axis=1)):
            return mask, drawn_numbers[i - 1]
    return None


def binary_search_losing_board(drawn_numbers, boards):
    pivot = int(drawn_numbers.shape[0] / 2)
    while 0 <= pivot < drawn_numbers.shape[0]:
        mask = np.isin(boards, drawn_numbers[:pivot])
        losing_boards = find_losing_boards(mask)
        if len(losing_boards) == 1:
            losing_board = boards[losing_boards[0]]
            losing_board_mask, losing_number = search_losing_mask_number(
                drawn_numbers, losing_board
            )
            return losing_board, losing_board_mask, losing_number
        if len(losing_boards) > 1:
            pivot = int(pivot + (drawn_numbers.shape[0] - pivot) / 2)
        else:
            pivot = int(np.floor(pivot / 2))
    return None


def calculate_score(board, mask, number):
    score = 0
    for index, truth_value in np.ndenumerate(mask):
        if not truth_value:
            score += board[index]
    score = score * number
    return score


def main():
    drawn_numbers, boards = read_input("../input.txt", 5)
    losing_board, losing_board_mask, losing_number = binary_search_losing_board(
        drawn_numbers, boards
    )
    score = calculate_score(losing_board, losing_board_mask, losing_number)
    print(score)


if __name__ == "__main__":
    main()
