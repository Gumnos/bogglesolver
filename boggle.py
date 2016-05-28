import sys
from collections import defaultdict
from pprint import pprint

END_OF_WORD = object() # a sentinel

def load_board(fp):
    data = [
        row.rstrip("\r\n")
        for row
        in fp
        ]
    rows = len(data)
    assert all(len(row) == rows for row in data), "Board is not square"
    return data

def load_dict(fp, max_len, min_len=3):
    results = {}
    word_count = 0
    for word in fp:
        word = word.strip()
        if not word.islower(): continue
        if len(word) < min_len or len(word) > max_len: continue
        word_count += 1
        d = results
        for letter in word:
            if letter not in d:
                d[letter] = {}
            d = d[letter]
        d[END_OF_WORD] = True
    return word_count, results

def search(board, dictionary,
        x, y,
        used, # set of (x,y) pairs already used
        ):
    c = board[y][x]
    if c in dictionary:
        new_dict = dictionary[c]
        if END_OF_WORD in new_dict:
            yield [(x,y)]
        size = len(board)
        for dx in (-1, 0, +1):
            for dy in (-1, 0, +1):
                if dx == dy == 0: continue # skip the 0 offset
                (newx, newy) = test_loc = (x+dx, y+dy)
                if newx < 0 or newy < 0 or newx >= size or newy >= size:
                    continue
                if test_loc not in used:
                    for result in search(
                            board,
                            new_dict,
                            newx, newy,
                            used | set((test_loc,))
                            ):
                        yield [(x,y)] + result

def solve(board, dictionary):
    for y, row in enumerate(board):
        for x, c in enumerate(row):
            for solution in search(
                    board,
                    dictionary,
                    x, y,
                    set(((x,y),)),
                    ):
                # solution should be a list of (x,y)
                word = "".join(
                    board[y][x]
                    for x, y
                    in solution
                    )
                yield word, solution

def main(board_name, dict_name="/usr/share/dict/words"):
    board = load_board(file(board_name))
    word_count, dictionary = load_dict(
        file(dict_name),
        len(board) ** 2, # capped by the board-size
        )
    for word, locs in solve(board, dictionary):
        print("%i %s at %s" % (
            len(word),
            word,
            locs,
            ))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1], *sys.argv[2:])
    else:
        sys.stderr.write(
            "usage: %s bogglefile.txt [dictionaryfile.txt]\n" % sys.argv[0]
            )
