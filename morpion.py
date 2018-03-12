def morpion():
	global damierl1
	damierl1 = ["A 1","B 1","C 1","A 2","B 2","C 2","A 3","B 3","C 3"]
	global n
	global joueur
	joueur = 1
	n = 0
	global tour
	tour = 1
	while(n == 0):
		print(damierl1[0],damierl1[1],damierl1[2])
		print(damierl1[3],damierl1[4],damierl1[5])
		print(damierl1[6],damierl1[7],damierl1[8])
		play()
	victoire()


def actionjoueur():
	global joueur
	global cara
	if joueur == 1:
		cara = " X "
		joueur = 2
	elif joueur == 2:
		cara = " O "
		joueur = 1



def play():
	global cara
	case = raw_input("Quel case jouer ?\n")
	caseM = case.upper()
	if caseM == "A1" and damierl1[0] == "A 1" :
		actionjoueur()
		damierl1[0] = cara

	elif caseM == "B1" and damierl1[1] == "B 1" :
		actionjoueur()
		damierl1[1] = cara

	elif caseM == "C1" and damierl1[2] == "C 1" :
		actionjoueur()
		damierl1[2] = cara

	elif caseM == "A2" and damierl1[3] == "A 2" :
		actionjoueur()
		damierl1[3] = cara


	elif caseM == "B2" and damierl1[4] == "B 2" :
		actionjoueur()
		damierl1[4] = cara


	elif caseM == "C2" and damierl1[5] == "C 2" :
		actionjoueur()
		damierl1[5] = cara

	elif caseM == "A3" and damierl1[6] == "A 3" :
		actionjoueur()
		damierl1[6] = cara

	elif caseM == "B3" and damierl1[7] == "B 3" :
		actionjoueur()
		damierl1[7] = cara

	elif caseM == "C3" and damierl1[8] == "C 3" :
		actionjoueur()
		damierl1[8] = cara


	else:
		print"Inconnu"
		actionjoueur()
	global tour
	tour += 1
	testvictoire()

	

def testvictoire():
	global n
	n = 0

	if damierl1[0]==" X " and damierl1[1] == " X " and damierl1[2] == " X " or damierl1[0]==" O " and damierl1[1] == " O " and damierl1[2] == " O ":

		n = 1


	elif damierl1[3]==" X " and damierl1[4] == " X " and damierl1[5] == " X " or damierl1[3]==" O " and damierl1[4] == " O " and damierl1[5] == " O ":
	
		n = 1
		


	elif damierl1[6]==" X " and damierl1[7] == " X " and damierl1[8] == " X " or damierl1[6]==" O " and damierl1[7] == " O " and damierl1[8] == " O ":
		
		n = 1
		

	elif damierl1[0]==" X " and damierl1[3] == " X " and damierl1[6] == " X " or damierl1[0]==" O " and damierl1[3] == " O " and damierl1[6] == " O ":
		
		n = 1
		

	elif damierl1[1]==" X " and damierl1[4] == " X " and damierl1[7] == " X " or damierl1[1]==" O " and damierl1[4] == " O " and damierl1[7] == " O ":
		
		n = 1
		

	elif damierl1[2]==" X " and damierl1[5] == " X " and damierl1[8] == " X " or damierl1[2]==" O " and damierl1[5] == " O " and damierl1[8] == " O ":
		
		n = 1
		


	elif damierl1[0]==" X " and damierl1[4] == " X " and damierl1[8] == " X " or damierl1[0]==" O " and damierl1[4] == " O " and damierl1[8] == " O ":
		
		n = 1
		

	elif damierl1[2]==" X " and damierl1[4] == " X " and damierl1[6] == " X " or damierl1[2]==" O " and damierl1[4] == " O " and damierl1[6] == " O ":
		
		n = 1

	elif tour == 10:
		n = 1
		

def victoire():
	global joueur
	if joueur == 1:
		joueur = 2

	elif joueur == 2:
		joueur = 1

	if n == 1 and tour !=10:
		print(damierl1[0],damierl1[1],damierl1[2])
		print(damierl1[3],damierl1[4],damierl1[5])
		print(damierl1[6],damierl1[7],damierl1[8])
		score()
		print"Victoire"

	elif n == 1 and tour == 10:
		print"Egalite"
		
def score():
	global score
	global joueur
	
	scoretxt = open("score.txt","a")
	#scoretxt.write("Score\n")
	#scoretxt.write(str(score))
	scoretxt.write("\nJoueur :")
	scoretxt.write(str(joueur,))
	scoretxt.write("\nTour :")
	scoretxt.write(str(tour))
	scoretxt.close()
	


morpion()