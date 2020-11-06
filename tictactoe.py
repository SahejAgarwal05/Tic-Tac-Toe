X = "X"
O = "O"
EMPTY=None

def initial_state():    
    return [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]

def player(board):
    return [O,X][(len(actions(board)))%2]

def actions(board):
    action=set()
    for a in  range(0,3):
        for b in range(0,3):
            if board[a][b]==EMPTY:
                action.add((a,b))
    return action

def result(board, action):
    if  board[action[0]][action[1]]==EMPTY:
        board[action[0]][action[1]]=player(board)
        return board
    else:
        raise Exception 

def winner(board):
    y=[[],[],[]]
    for x in board:
        y[0].append(x[0])
        y[1].append(x[1])
        y[2].append(x[2])
        if len(set(x))==1 and x[0]!=EMPTY:
            return  {X:O,O:X}[player(board)]
    for x in y:
        if len(set(x))==1 and x[0]!=EMPTY:
            return {X:O,O:X}[player(board)]
    if board[0][0]==board[1][1]==board[2][2]!=EMPTY:
        return {X:O,O:X}[player(board)]
    elif board[0][2]==board[1][1]==board[2][0]!=EMPTY:
        return {X:O,O:X}[player(board)]
    return EMPTY

def terminal(board):
    return len(actions(board))==0 or winner(board) in [X,O]

def utility(board):
    return {X:1,O:-1,EMPTY:0}[winner(board)]


    
def minimax(board):
    def clean(board,action):
        board[action[0]][action[1]]=EMPTY
    def help_minimax(board,limit):
        alpha=0
        beta={X:-2,O:2}[player(board)]
        for m in actions(board):
            board=result(board,m)
            if terminal(board):
                alpha=utility(board)
            else:
                alpha=help_minimax(board,beta)
            clean(board,m)
            side=player(board)
            if side==X:
                if alpha>=limit:
                    return alpha    
                elif alpha>beta:
                    beta=alpha
            else:
                if alpha<=limit:
                     return alpha
                elif alpha<beta:
                     beta=alpha
        return beta
    if terminal(board):
        return None
    alpha=0
    move=()
    limit={X:-2,O:2}[player(board)]
    for m in actions(board):
        boardl=result(board,m)
        if terminal(board)==True:
            alpha=utility(board)
        else:
            alpha=help_minimax(board,limit)
        clean(board,m)
        side=player(board)
        if side==X and alpha>limit:
            limit=alpha
            move=m
        elif side==O and alpha<limit:
            limit=alpha
            move=m
    return move


