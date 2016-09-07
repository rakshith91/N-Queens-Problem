# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, August 2016
#
# Solves the N-Queens problem too! 
#N-Queen specific functions written by Sairam Rakshith Bhyravabhotla 

# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.
 
#The N-queens problem is: Given an empty NxN chessboard, place N rooks on the board so that no queens
# can take any other, i.e. such that no two rooks share the same row or column or on the same diagonal.

# This is N, the size of the board.
N= 8

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 


# Idea of transformation for the below function taken from http://stackoverflow.com/a/6313407
# Get the count on two diagonals given row and column of a piece
def count_on_diagonals(board, row, col):
	diag_list=[]
	for x in range(0 , 2*N-1):
		forward_diag=[]
		backward_diag=[]
		for y in range(max(x-N+1, 0), min(x, N-1)+1):
			forward_diag.append(board[N-x+y-1][y])
			backward_diag.append(board[x-y][y])
			if N-x+y-1 == row and y== col:
				diag_list.append(forward_diag)
			if x-y == row and y == col:
				diag_list.append(backward_diag)
	return sum(diag_list[0])+sum(diag_list[1])-board[row][col]

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "Q" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

# Get a list of successors of given board state by checking total pieces on board and if a rook/queen is present or not
def successors2(board):
	return [add_piece(board,r,c) if count_pieces(add_piece(board,r,c))<=N and board[r][c]!=1 else None for r in range(0,N) for c in range (0,N)]


# Get a list of successors of given board state by checking total pieces on board and if a rook/queen is present or not 
# and also verify the number of pieces on each row and column 
def successors3(board): 
	return [add_piece(board, r,c) if count_on_row(add_piece(board,r,c), r)<=1 and count_on_col(add_piece(board,r,c), c) <=1 and board[r][c]!=1 else None for r in range(0,N) for c in range(0, N)] 

#Successor function for n - queens
def nqueens_successors(board):
	return [add_piece(board,r,c) if count_on_row(add_piece(board,r,c), r)<=1 and count_on_col(add_piece(board,r,c),c) <=1 and board[r][c]!=1 and count_on_diagonals(add_piece(board,r,c),r,c)<=1 else None for r in range(0,N) for c in range(0, N)]

# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] ) 

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors3( fringe.pop() ):
			if s != None:
				if is_goal(s):
					return(s) 
				fringe.append(s)
	
    return False

#Solve n queens
def nqueens_solve(initial_board):
	fringe = [initial_board]
	while len(fringe) > 0:
		for s in nqueens_successors( fringe.pop() ):
			if s != None:
				if is_goal(s):
					return(s)
				fringe.append(s)
	return False

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print "Starting to solve n-rooks"
print "Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution..."
solution = solve(initial_board)
print printable_board(solution) if solution else "Sorry, no solution found. :("


print "Starting to solve n queens"
initial_board = [[0]*N]*N
print "Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n"
solution = nqueens_solve(initial_board)
print printable_board(solution) if solution else "Sorry, no solution found. :("

