import random
def hangman(word):
    wrong=0
    stages=["",
            "_______        ",
            "|      |       ",
            "|      |       ",
            "|      O       ",
            "|     /|\      ",
            "|     / \      ",
            "|______________",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ！")
    while wrong<len(stages)-1:
        print("\n")
        msg="１文字予想してね。"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("やったね！")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("残念。正解は{}".format(word))
    
wort=["cat","dog","snake","mouse","sheep","cow","horse","dragon","tiger","rabbit","monkey","bird","pig"]
i=random.randint(0,12)
wort_i=wort[i]
hangman(wort_i)
