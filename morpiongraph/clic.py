import pygame
from pygame.locals import *
def morpion():


	damierl1 = [1,2,3,4,5,6,7,8,9]

	global joueur
	joueur = 1
	global n
	n = 0
	global tour
	tour = 0


	def actionjoueur():
		global joueur
		global cara
		global tour
		if joueur == 1:
			joueur = 2
			cara = "1"
			tour +=1
			testvictoire()
		elif joueur == 2:
			joueur = 1
			cara = "2"
			tour +=1
			testvictoire()

	def testvictoire():
		global n
		n = 0
		if damierl1[0]== "1" and damierl1[1]== "1" and damierl1[2] == "1" or damierl1[0]== "2" and damierl1[1]== "2" and damierl1[2] == "2" :
			n = 1

		elif damierl1[3]== "1" and damierl1[4]== "1" and damierl1[5] == "1" or damierl1[3]== "2" and damierl1[4]== "2" and damierl1[5] == "2" :
			n = 1

		elif damierl1[6]== "1" and damierl1[7]== "1" and damierl1[8] == "1" or damierl1[6]== "2" and damierl1[7]== "2" and damierl1[8] == "2" :
			n = 1


		elif damierl1[0]== "1" and damierl1[3]== "1" and damierl1[6] == "1" or damierl1[0]== "2" and damierl1[3]== "2" and damierl1[6] == "2" :
			n = 1

		elif damierl1[1]== "1" and damierl1[4]== "1" and damierl1[7] == "1" or damierl1[1]== "2" and damierl1[4]== "2" and damierl1[7] == "2" :

			n = 1

		elif damierl1[2]== "1" and damierl1[5]== "1" and damierl1[8] == "1" or damierl1[2]== "2" and damierl1[5]== "2" and damierl1[8] == "2" :

			n = 1


		elif damierl1[0]== "1" and damierl1[4]== "1" and damierl1[8] == "1" or damierl1[0]== "2" and damierl1[4]== "2" and damierl1[8] == "2" :
			n = 1

		elif damierl1[2]== "1" and damierl1[4]== "1" and damierl1[6] == "1" or damierl1[2]== "2" and damierl1[4]== "2" and damierl1[6] == "2" :
			n = 1

		elif tour == 9:
			n =2	



	RED = (255,0,0)
	BLUE = (0,255,0)
	GREEN = (0,0,255)

	COLORS=(RED,BLUE,GREEN)

	color_index=0
	jeu_index=0
	jeu_index2=0
	jeu_index3=0
	jeu_index4=0
	jeu_index5=0
	jeu_index6=0
	jeu_index7=0
	jeu_index8=0
	jeu_index9=0
	indexR = 0
	indexC = 0
	pygame.init()
	fenetre = pygame.display.set_caption("Morpion")
	fenetre = pygame.display.set_mode((290,320))




	global continuer
	continuer = 1
	rejouer = pygame.image.load("rejouer.png").convert_alpha()
	fondgg = pygame.image.load("fondgg.png").convert_alpha()
	fond = pygame.image.load("fondm.png").convert_alpha()
	CROIX =pygame.image.load("croix.png").convert_alpha()
	ROND = pygame.image.load("rond.png").convert_alpha()
	BLANC = pygame.image.load("blanc.png").convert_alpha()
	NUL = pygame.image.load("nul.png").convert_alpha()
	COPY = pygame.image.load("mp.png")
	JEU1=(BLANC,ROND,BLANC,CROIX)
	JEU2=(BLANC,ROND,BLANC,CROIX)
	JEU3=(BLANC,ROND,BLANC,CROIX)
	JEU4=(BLANC,ROND,BLANC,CROIX)
	JEU5=(BLANC,ROND,BLANC,CROIX)
	JEU6=(BLANC,ROND,BLANC,CROIX)
	JEU7=(BLANC,ROND,BLANC,CROIX)
	JEU8=(BLANC,ROND,BLANC,CROIX)
	JEU9=(BLANC,ROND,BLANC,CROIX)
	ROND = (ROND)
	CROIX = (CROIX)
	"""
	Definition des zones cliquables
	"""
	fond = pygame.image.load("fondm.png").convert_alpha()

	fondmax = pygame.Rect((0,0),(290,290))
	rect_fondgg = pygame.Surface(fondmax.size)

	clickable_area = pygame.Rect((0,0),(90,90))
	rect_surf = pygame.Surface(clickable_area.size)


	clickable_area2 = pygame.Rect((0,100),(90,90))
	rect_surf2 = pygame.Surface(clickable_area2.size)

	clickable_area3 = pygame.Rect((0,200),(90,90))
	rect_surf3 = pygame.Surface(clickable_area3.size)

	clickable_area4 = pygame.Rect((100,0),(90,90))
	rect_surf4 = pygame.Surface(clickable_area4.size)

	clickable_area5 = pygame.Rect((100,100),(90,90))
	rect_surf5 = pygame.Surface(clickable_area5.size)

	clickable_area6 = pygame.Rect((100,200),(90,90))
	rect_surf6 = pygame.Surface(clickable_area6.size)

	clickable_area7 = pygame.Rect((200,0),(90,90))
	rect_surf7 = pygame.Surface(clickable_area7.size)

	clickable_area8 = pygame.Rect((200,100),(90,90))
	rect_surf8 = pygame.Surface(clickable_area8.size)

	clickable_area9 = pygame.Rect((200,200),(90,90))
	rect_surf9 = pygame.Surface(clickable_area9.size)

	score = pygame.Rect((0,290),(290,30))
	rect_score = pygame.Surface(score.size)

	fenetre.blit(BLANC, (0,0))
	fenetre.blit(fond, (0,0))
	pygame.display.flip()


	pygame.display.flip()

	rect_score.blit(COPY,((0,0),(100,100)))

	rect_surf.blit(JEU1[jeu_index],((0,0),(100,100)))

	rect_surf2.blit(JEU2[jeu_index2],((0,0),(100,100)))

	rect_surf3.blit(JEU2[jeu_index3],((0,0),(100,100)))

	rect_surf4.blit(JEU2[jeu_index4],((0,0),(100,100)))

	rect_surf5.blit(JEU2[jeu_index5],((0,0),(100,100)))

	rect_surf6.blit(JEU2[jeu_index6],((0,0),(100,100)))

	rect_surf7.blit(JEU2[jeu_index7],((0,0),(100,100)))

	rect_surf8.blit(JEU2[jeu_index8],((0,0),(100,100)))

	rect_surf9.blit(JEU2[jeu_index9],((0,0),(100,100)))



	while continuer:
		if n == 0:
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
					
				elif event.type == MOUSEBUTTONUP:
					if event.button == 1:
						if clickable_area.collidepoint(event.pos) and damierl1[0] == 1:
							if joueur == 1:
								rect_surf.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[0]= cara

							elif joueur == 2:
								rect_surf.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[0] = cara


						elif clickable_area2.collidepoint(event.pos) and damierl1[1] == 2:
							if joueur == 1:
								rect_surf2.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[1]= cara

							elif joueur == 2:
								rect_surf2.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[1]= cara

						elif clickable_area3.collidepoint(event.pos) and damierl1[2] == 3:
							if joueur == 1:
								rect_surf3.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[2]= cara

							elif joueur == 2:
								rect_surf3.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[2]= cara


						elif clickable_area4.collidepoint(event.pos)and damierl1[3] == 4:
							if joueur == 1:
								rect_surf4.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[3]= cara

							elif joueur == 2:
								rect_surf4.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[3]= cara

						elif clickable_area5.collidepoint(event.pos)and damierl1[4] == 5:
							if joueur == 1:
								rect_surf5.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[4]= cara

							elif joueur == 2:
								rect_surf5.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[4] = cara
								testvictoire()

						elif clickable_area6.collidepoint(event.pos)and damierl1[5] == 6:
							if joueur == 1:
								rect_surf6.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[5]= cara

							elif joueur == 2:
								rect_surf6.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[5]= cara



						elif clickable_area7.collidepoint(event.pos)and damierl1[6] == 7:
							if joueur == 1:
								rect_surf7.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[6]= cara


							elif joueur == 2:
								rect_surf7.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[6]= cara



						elif clickable_area8.collidepoint(event.pos)and damierl1[7] == 8:
							if joueur == 1:
								rect_surf8.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[7]= cara


							elif joueur == 2:
								rect_surf8.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[7]= cara



						elif clickable_area9.collidepoint(event.pos)and damierl1[8] == 9:
							if joueur == 1:
								rect_surf9.blit(ROND,((0,0),(100,100)))
								actionjoueur()
								damierl1[8] = cara

							elif joueur == 2:
								rect_surf9.blit(CROIX,((0,0),(100,100)))
								actionjoueur()
								damierl1[8] = cara
						testvictoire()
				






			fenetre.blit(rect_score,score)						
			fenetre.blit(rect_surf,clickable_area)
			fenetre.blit(rect_surf2,clickable_area2)
			fenetre.blit(rect_surf3,clickable_area3)
			fenetre.blit(rect_surf4,clickable_area4)
			fenetre.blit(rect_surf5,clickable_area5)
			fenetre.blit(rect_surf6,clickable_area6)
			fenetre.blit(rect_surf7,clickable_area7)
			fenetre.blit(rect_surf8,clickable_area8)
			fenetre.blit(rect_surf9,clickable_area9)


			pygame.display.flip()

		elif n==1:
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
				if event.type == MOUSEBUTTONUP:
					if event.button == 1:	
						if zone_rejouer.collidepoint(event.pos):

							morpion()

			fenetre.blit(fondgg,(0,0))
			zone_rejouer= pygame.Rect((100,180),(90,90))
			rect_rejouer = pygame.Surface(zone_rejouer.size)
			fenetre.blit(rejouer,(100,250))
			pygame.display.flip()

		elif n ==2:
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
				if event.type == MOUSEBUTTONUP:
					if event.button == 1:	
						if zone_rejouer.collidepoint(event.pos):

							morpion()
			fenetre.blit(NUL,(0,0))
			zone_rejouer= pygame.Rect((100,180),(90,90))
			rect_rejouer = pygame.Surface(zone_rejouer.size)
			fenetre.blit(rejouer,(100,250))
			pygame.display.flip()



	

morpion()