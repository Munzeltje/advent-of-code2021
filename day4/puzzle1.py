import numpy as np


def read_input(filename, board_size):
    drawn_numbers = np.loadtxt(filename, delimiter=",", max_rows=1, dtype=int)
    boards = np.loadtxt(filename, skiprows=1, dtype=int)
    boards = np.reshape(
        boards, (int(boards.shape[0] / board_size), board_size, board_size)
    )
    return drawn_numbers, boards


def find_winning_boards(mask):
    winning_boards = []
    for index, board in enumerate(mask):
        if np.any(np.all(board, axis=0)) or np.any(np.all(board, axis=1)):
            winning_boards.append(index)
    return winning_boards


def search_winning_mask_number(drawn_numbers, winning_board, pivot):
    for i in range(1, pivot):
        mask = np.isin(winning_board, drawn_numbers[:i])
        if np.any(np.all(mask, axis=0)) or np.any(np.all(mask, axis=1)):
            return mask, drawn_numbers[i - 1]
    return None


def binary_search_winning_board(drawn_numbers, boards):
    pivot = int(drawn_numbers.shape[0] / 2)
    while 0 <= pivot < drawn_numbers.shape[0]:
        mask = np.isin(boards, drawn_numbers[:pivot])
        winning_boards = find_winning_boards(mask)
        if len(winning_boards) == 1:
            winning_board = boards[winning_boards[0]]
            winning_board_mask, winning_number = search_winning_mask_number(
                drawn_numbers, winning_board, pivot
            )
            return winning_board, winning_board_mask, winning_number
        if len(winning_boards) > 1:
            pivot = int(np.floor(pivot / 2))
        else:
            pivot = int(pivot + (drawn_numbers.shape[0] - pivot) / 2)
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
    winning_board, winning_board_mask, winning_number = binary_search_winning_board(
        drawn_numbers, boards
    )
    score = calculate_score(winning_board, winning_board_mask, winning_number)
    print(score)


if __name__ == "__main__":
    main()
