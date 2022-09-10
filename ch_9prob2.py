def game():
 return 765
score=game()
with open("hisscore.txt") as f:
    hiSscoreStr=(f.read)
    if hiSscoreStr=='':
        with open("hiSscore.txt","w") as f:
                f.write(str(score))
    elif int(hiSscoreStr)<score:
        with open("hisscore.txt","w") as f:
            f.write(str(score))