###
# 04-12-2020
# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.
###
def word_search(matrix, word):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            word_right = build_word_right(matrix, r, c, len(word))
            word_down = build_word_down(matrix, r, c, len(word))
            if word in (word_right, word_down):
                return True
    return False


def build_word_right(matrix, r, c, length):
    return ''.join([matrix[r][i] for i in range(c, len(matrix[0]))])[:length]


def build_word_down(matrix, r, c, length):
    return ''.join([matrix[i][c] for i in range(r, len(matrix))])[:length]


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
# True
