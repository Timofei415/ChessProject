from graphics import *
import math
import random
import time
import numpy as np
win = GraphWin("My window", 1200, 700)
win.setBackground (color_rgb(245, 245, 245))



def sigmoid(x):
	return(1/(1+np.exp(-x)))


def fromNumberToLetter(x):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	return (alphabet[x-1])
def board():
	Rectangle (Point(30,30), Point(670,670)).draw(win)
	j = 0
	i = 0
	while j < 8:
		shift = j % 2
		shift1 = (j+1) % 2
		while i < 4:
			cell = Rectangle (Point (30+160*i+80*shift,590-80*j), Point (110+160*i+80*shift,670-80*j))
			cell.setFill(color_rgb(50, 120, 50))
			cell.draw(win)
			wcell = Rectangle (Point (30+160*i+80*shift1,590-80*j), Point (110+160*i+80*shift1,670-80*j))
			wcell.setFill(color_rgb(255, 255, 255))
			wcell.draw(win)
			i = i+1
		j = j+1
		i = 0
	i = 0
	while i < 8:
		number = Text (Point (15, 630-80*i), str(i+1))
		number.setSize(15)
		number.setStyle('bold')
		number.draw(win)
		letter = Text (Point (70+80*i, 685), fromNumberToLetter(i+1))
		letter.setSize(15)
		letter.setStyle('bold')
		letter.draw(win)
		i = i + 1
board()

def wcheckmate():
	m = Rectangle (Point(100,100), Point(600,500))
	m.setFill(color_rgb(245, 245, 245))
	m.setWidth(5)
	t = Text(Point (350,130), 'Checkmate')
	t.setSize(35)
	t.setStyle('bold')
	a = Text(Point (350,200), 'White won')
	a.setSize(30)
	b = Text(Point (350,400), 'New Game')
	b.setSize(25)
	b.setStyle('italic')
	c = Text(Point (590,110), 'x')
	c.setSize(20)
	d = Rectangle (Point(580,100), Point(600,122))
	e = Rectangle (Point(250,370), Point(450,430))
	m.draw(win)
	t.draw(win)
	a.draw(win)
	b.draw(win)
	c.draw(win)
	d.draw(win)
	e.draw(win)
	time.sleep(1)
	m.undraw()
	t.undraw()
	a.undraw()
	b.undraw()
	c.undraw()
	d.undraw()
	e.undraw()
def bcheckmate():
	m = Rectangle (Point(100,100), Point(600,500))
	m.setFill(color_rgb(245, 245, 245))
	m.setWidth(5)
	t = Text(Point (350,130), 'Checkmate')
	t.setSize(35)
	t.setStyle('bold')
	a = Text(Point (350,200), 'Black won')
	a.setSize(30)
	b = Text(Point (350,400), 'New Game')
	b.setSize(25)
	b.setStyle('italic')
	c = Text(Point (590,110), 'x')
	c.setSize(20)
	d = Rectangle (Point(580,100), Point(600,122))
	e = Rectangle (Point(250,370), Point(450,430))
	m.draw(win)
	t.draw(win)
	a.draw(win)
	b.draw(win)
	c.draw(win)
	d.draw(win)
	e.draw(win)
	time.sleep(1)
	m.undraw()
	t.undraw()
	a.undraw()
	b.undraw()
	c.undraw()
	d.undraw()
	e.undraw()
def stalemate():
	m = Rectangle (Point(100,100), Point(600,500))
	m.setFill(color_rgb(245, 245, 245))
	m.setWidth(5)
	t = Text(Point (350,130), 'Stalemate')
	t.setSize(35)
	t.setStyle('bold')
	a = Text(Point (350,200), 'Draw')
	a.setSize(30)
	b = Text(Point (350,400), 'New Game')
	b.setSize(25)
	b.setStyle('italic')
	c = Text(Point (590,110), 'x')
	c.setSize(20)
	d = Rectangle (Point(580,100), Point(600,122))
	e = Rectangle (Point(250,370), Point(450,430))
	m.draw(win)
	t.draw(win)
	a.draw(win)
	b.draw(win)
	c.draw(win)
	d.draw(win)
	e.draw(win)
	time.sleep(1)
	m.undraw()
	t.undraw()
	a.undraw()
	b.undraw()
	c.undraw()
	d.undraw()
	e.undraw()
def threefoldrepetition():
	m = Rectangle (Point(100,100), Point(600,500))
	m.setFill(color_rgb(245, 245, 245))
	m.setWidth(5)
	t = Text(Point (350,130), 'Threefold repetition')
	t.setSize(35)
	t.setStyle('bold')
	a = Text(Point (350,200), 'Draw')
	a.setSize(30)
	b = Text(Point (350,400), 'New Game')
	b.setSize(25)
	b.setStyle('italic')
	c = Text(Point (590,110), 'x')
	c.setSize(20)
	d = Rectangle (Point(580,100), Point(600,122))
	e = Rectangle (Point(250,370), Point(450,430))
	m.draw(win)
	t.draw(win)
	a.draw(win)
	b.draw(win)
	c.draw(win)
	d.draw(win)
	e.draw(win)
	time.sleep(1)
	m.undraw()
	t.undraw()
	a.undraw()
	b.undraw()
	c.undraw()
	d.undraw()
	e.undraw()


def whitePromotionChosing(f,j,position):
	a = Rectangle (Point(20+80*j,25), Point(120+80*j,355))
	a.setFill ('white')
	a.setWidth(5)
	a.draw(win)
	whiteQueen = Image(Point(70+80*j,70), 'whiteQueen.png')
	whiteQueen.draw(win)
	whiteRook = Image(Point(70+80*j,150), 'whiteRook.png')
	whiteRook.draw(win)
	whiteBishop = Image(Point(70+80*j,233), 'whiteBishop.png')
	whiteBishop.draw(win)
	whiteKnight = Image(Point(73+80*j,313), 'whiteKnight.png')
	whiteKnight.draw(win)
	while True:
		p = win.getMouse()
		i1 = rowNumber(p)
		j1 = columnNumber(p)
		if (j1 == j):
			if (i1 == 7):
				f = f[0] + 'Q' + f[1:3]
				break
			if (i1 == 6):
				f = f[0] + 'R' + f[1:3]
				break
			if (i1 == 5):
				f = f[0] + 'B' + f[1:3]
				break
			if (i1 == 4):
				f = f[0] + 'N' + f[1:3]
				break
	newRow = (position[7])[0:j] + [f] + (position[7])[j+1:8]
	position1 = position[0:7] + [newRow]
	a.undraw()
	whiteQueen.undraw()
	whiteKnight.undraw()
	whiteRook.undraw()
	whiteBishop.undraw()
	return (position1)
def blackPromotionChosing(f,j,position):
	a = Rectangle (Point(20+80*j,345), Point(120+80*j,675))
	a.setFill ('white')
	a.setWidth(5)
	a.draw(win)
	blackQueen = Image(Point(70+80*j,390), 'blackQueen.png')
	blackQueen.draw(win)
	blackRook = Image(Point(72+80*j,473), 'blackRook.png')
	blackRook.draw(win)
	blackBishop = Image(Point(71+80*j,552), 'blackBishop.png')
	blackBishop.draw(win)
	blackKnight = Image(Point(70+80*j,632), 'blackKnight.png')
	blackKnight.draw(win)
	while True:
		p = win.getMouse()
		i1 = rowNumber(p)
		j1 = columnNumber(p)
		if (j1 == j):
			if (i1 == 3):
				f = f[0] + 'Q' + f[1:3]
				break
			if (i1 == 2):
				f = f[0] + 'R' + f[1:3]
				break
			if (i1 == 1):
				f = f[0] + 'B' + f[1:3]
				break
			if (i1 == 0):
				f = f[0] + 'N' + f[1:3]
				break
	newRow = (position[0])[0:j] + [f] + (position[0])[j+1:8]
	position1 = [newRow] + position[1:8]
	a.undraw()
	blackQueen.undraw()
	blackKnight.undraw()
	blackRook.undraw()
	blackBishop.undraw()
	return (position1)


def movedrawer(moves, movenumber, shortcastles, longcastles):
	x = moves[len(moves)-1] #x = 1122wQ
	l = x[3]
	if (l == '0'):
		letter = 'a'
	elif (l == '1'):
		letter = 'b'
	elif (l == '2'):
		letter = 'c'
	elif (l == '3'):
		letter = 'd'
	elif (l == '4'):
		letter = 'e'
	elif (l == '5'):
		letter = 'f'
	elif (l == '6'):
		letter = 'g'
	elif (l == '7'):
		letter = 'h'
	move = x[5] + letter + str(int(x[2]) + 1)
	column = (movenumber - 1) // 22
	j = 10 + 30*movenumber - 30*22*column
	if (x[4] == 'w'):
		i = 720 + 120*column
		m = Text(Point(690 + 120*column,j), str(movenumber) + '. ')
		m.setSize(13)
		m.setStyle('bold')
		m.draw(win)
	else:
		i = 765 + 120*column
	if shortcastles:
		a = Text(Point(i,j), 'O-O')
	elif longcastles:
		a = Text(Point(i,j), 'O-O-O')
	else:
		a = Text(Point(i,j), move)
	a.setSize(13)
	a.draw(win)
#white starting position
 #pawns
whitePawn1 = Image(Point(69,552), 'whitePawn.png')
whitePawn1.draw(win)
whitePawn2 = Image(Point(149,552), 'whitePawn.png')
whitePawn2.draw(win)
whitePawn3 = Image(Point(229,552), 'whitePawn.png')
whitePawn3.draw(win)
whitePawn4 = Image(Point(309,552), 'whitePawn.png')
whitePawn4.draw(win)
whitePawn5 = Image(Point(389,552), 'whitePawn.png')
whitePawn5.draw(win)
whitePawn6 = Image(Point(469,552), 'whitePawn.png')
whitePawn6.draw(win)
whitePawn7 = Image(Point(549,552), 'whitePawn.png')
whitePawn7.draw(win)
whitePawn8 = Image(Point(629,552), 'whitePawn.png')
whitePawn8.draw(win)
 #Knights
whiteKnight1 = Image(Point(153,633), 'whiteKnight.png')
whiteKnight1.draw(win)
whiteKnight2 = Image(Point(553,633), 'whiteKnight.png')
whiteKnight2.draw(win)
 #Bishops
whiteBishop1 = Image(Point(230,633), 'whiteBishop.png')
whiteBishop1.draw(win)
whiteBishop2 = Image(Point(470,633), 'whiteBishop.png')
whiteBishop2.draw(win)
 #Rooks
whiteRook1 = Image(Point(70,630), 'whiteRook.png')
whiteRook1.draw(win)
whiteRook2 = Image(Point(630,630), 'whiteRook.png')
whiteRook2.draw(win)
 #Queen
whiteQueen = Image(Point(310,630), 'whiteQueen.png')
whiteQueen.draw(win)
 #King
whiteKing = Image(Point(390,636), 'whiteKing.png')
whiteKing.draw(win)
#black starting position
 #pawns
blackPawn1 = Image(Point(70,152), 'blackPawn.png')
blackPawn1.draw(win)
blackPawn2 = Image(Point(150,152), 'blackPawn.png')
blackPawn2.draw(win)
blackPawn3 = Image(Point(230,152), 'blackPawn.png')
blackPawn3.draw(win)
blackPawn4 = Image(Point(310,152), 'blackPawn.png')
blackPawn4.draw(win)
blackPawn5 = Image(Point(390,152), 'blackPawn.png')
blackPawn5.draw(win)
blackPawn6 = Image(Point(470,152), 'blackPawn.png')
blackPawn6.draw(win)
blackPawn7 = Image(Point(550,152), 'blackPawn.png')
blackPawn7.draw(win)
blackPawn8 = Image(Point(630,152), 'blackPawn.png')
blackPawn8.draw(win)
 #Rooks
blackRook1 = Image(Point(72,73), 'blackRook.png')
blackRook1.draw(win)
blackRook2 = Image(Point(632,73), 'blackRook.png')
blackRook2.draw(win)
 #Knights
blackKnight1 = Image(Point(150,72), 'blackKnight.png')
blackKnight1.draw(win)
blackKnight2 = Image(Point(550,72), 'blackKnight.png')
blackKnight2.draw(win)
 #Bishops
blackBishop1 = Image(Point(231,72), 'blackBishop.png')
blackBishop1.draw(win)
blackBishop2 = Image(Point(471,72), 'blackBishop.png')
blackBishop2.draw(win)
 #Queen
blackQueen = Image(Point(310,70), 'blackQueen.png')
blackQueen.draw(win)
 #King
blackKing = Image(Point(389,72), 'blackKing.png')
blackKing.draw(win)
 #checks if the element is in the list

def elem (e,l):
	i = 0
	m = False
	while i < len(l):
		if e == l[i]:
			m = True 
		i = i + 1
	return (m)

def elemnumber (e,l):
	i = 0
	m = 0
	while i < len(l):
		if e == l[i]:
			m = m + 1 
		i = i + 1
	return (m)
def delete (i, s):
	return (s[0:i] + s[i+1:len(s)])
#changes the position after making a move. If taking happens, undraws the taken piece
# produce taking of one piece by another (drawing)
def threefold(positionrecord):
	i = 0
	k = 0
	result = False
	while i < len(positionrecord):
		k = 0
		j = i
		while j < len(positionrecord):
			if (positionrecord[i] == positionrecord[j]):
				k = k + 1
			if (k == 3):
				result = True
				break
			j = j + 1
		if (result == True):
			break
		i = i + 1
	return(result)
def taking (p,i1,j1,i2,j2):
	element1 = (p[i1])[j1]
	element2 = (p[i2])[j2]
	if (element2 == 'bP1') or (element2[0] + element2[2:4] == 'bP1'):
		blackPawn1.undraw()
	elif (element2 == 'bP2') or (element2[0] + element2[2:4] == 'bP2'):
		blackPawn2.undraw()
	elif (element2 == 'bP3') or (element2[0] + element2[2:4] == 'bP3'):
		blackPawn3.undraw()
	elif (element2 == 'bP4') or (element2[0] + element2[2:4] == 'bP4'):
		blackPawn4.undraw()
	elif (element2 == 'bP5') or (element2[0] + element2[2:4] == 'bP5'):
		blackPawn5.undraw()
	elif (element2 == 'bP6') or (element2[0] + element2[2:4] == 'bP6'):
		blackPawn6.undraw()
	elif (element2 == 'bP7') or (element2[0] + element2[2:4] == 'bP7'):
		blackPawn7.undraw()
	elif (element2 == 'bP8') or (element2[0] + element2[2:4] == 'bP8'):
		blackPawn8.undraw()
	if (element2 == 'bR1'):
		blackRook1.undraw()
	elif (element2 == 'bR2'):
		blackRook2.undraw()
	elif (element2 == 'bN1'):
		blackKnight1.undraw()
	elif (element2 == 'bN2'):
		blackKnight2.undraw()
	elif (element2 == 'bB1'):
		blackBishop1.undraw()
	elif (element2 == 'bB2'):
		blackBishop2.undraw()
	elif (element2 == 'bQ'):
		blackQueen.undraw()
	if (element2 == 'wP1') or (element2[0] + element2[2:4] == 'wP1'):
		whitePawn1.undraw()
	elif (element2 == 'wP2') or (element2[0] + element2[2:4] == 'wP2'):
		whitePawn2.undraw()
	elif (element2 == 'wP3') or (element2[0] + element2[2:4] == 'wP3'):
		whitePawn3.undraw()
	elif (element2 == 'wP4') or (element2[0] + element2[2:4] == 'wP4'):
		whitePawn4.undraw()
	elif (element2 == 'wP5') or (element2[0] + element2[2:4] == 'wP5'):
		whitePawn5.undraw()
	elif (element2 == 'wP6') or (element2[0] + element2[2:4] == 'wP6'):
		whitePawn6.undraw()
	elif (element2 == 'wP7') or (element2[0] + element2[2:4] == 'wP7'):
		whitePawn7.undraw()
	elif (element2 == 'wP8') or (element2[0] + element2[2:4] == 'wP8'):
		whitePawn8.undraw()
	if (element2 == 'wR1'):
		whiteRook1.undraw()
	elif (element2 == 'wR2'):
		whiteRook2.undraw()
	elif (element2 == 'wN1'):
		whiteKnight1.undraw()
	elif (element2 == 'wN2'):
		whiteKnight2.undraw()
	elif (element2 == 'wB1'):
		whiteBishop1.undraw()
	elif (element2 == 'wB2'):
		whiteBishop2.undraw()
	elif (element2 == 'wQ'):
		whiteQueen.undraw()
# changes the position

def swapping(p,i1,j1,i2,j2):
	element1 = (p[i1])[j1]
	element2 = (p[i2])[j2]
	if (element2 == 'e'):
		newRow1 = (p[i1])[0:j1] + [element2] + (p[i1])[j1+1:8] 
	else:
		newRow1 = (p[i1])[0:j1] + ['e'] + (p[i1])[j1+1:8]
	if i1 == i2:
		newRow2 = newRow1[0:j2] + [element1] + newRow1[j2+1:8] 
	else:
		newRow2 = (p[i2])[0:j2] + [element1] + (p[i2])[j2+1:8] 
	if i1 < i2:
		newPosition = p[0:i1] + [newRow1] + p[i1+1:i2] + [newRow2] + p[i2+1:8]
	elif i1 == i2:
		newPosition = p[0:i1] + [newRow2] + p[i2+1:8]
	else:
		newPosition = p[0:i2] + [newRow2] + p[i2+1:i1] + [newRow1] + p[i1+1:8]
	return (newPosition)
# list of all cells attacked by white

def whiteAttack (position):
	i = 0
	j = 0
	moves = set()
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f[0] == 'w'):
				if (f == 'wP1') or (f == 'wP2') or (f == 'wP3') or (f == 'wP4') or (f == 'wP5') or (f == 'wP6') or (f == 'wP7') or (f == 'wP8'):
					if (i < 7) and (j < 7):
						moves.add((i+1,j+1))
					if (i < 7) and (j > 0):
						moves.add((i+1,j-1))
				elif (f[0:2] == 'wN'):
						if (i < 6) and (j < 7):
							moves.add((i+2,j+1))
						if (i < 6) and (j > 0):
							moves.add((i+2,j-1))
						if (i > 1) and (j < 7):
							moves.add((i-2,j+1))
						if (i > 1) and (j > 0):
							moves.add((i-2,j-1))
						if (i < 7) and (j < 6):
							moves.add((i+1,j+2))
						if (i < 7) and (j > 1):
							moves.add((i+1,j-2))
						if (i > 0) and (j < 6):
							moves.add((i-1,j+2))
						if (i > 0) and (j > 1):
							moves.add((i-1,j-2))
				elif (f[0:2] == 'wB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								moves.add((i+x,j+y))
							else:
								moves.add((i+x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								moves.add((i-x,j+y))
							else:
								moves.add((i-x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								moves.add((i+x,j-y))
							else:
								moves.add((i+x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								moves.add((i-x,j-y))
							else:
								moves.add((i-x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'wR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								moves.add((i+x,j))
							else:
								moves.add((i+x,j))
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								moves.add((i-x,j))
							else:
								moves.add((i-x,j))
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								moves.add((i,j-x))
							else:
								moves.add((i,j-x))
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								moves.add((i,j+x))
							else:
								moves.add((i,j+x))
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'wQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								moves.add((i+x,j+y))
							else:
								moves.add((i+x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								moves.add((i-x,j+y))
							else:
								moves.add((i-x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								moves.add((i+x,j-y))
							else:
								moves.add((i+x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								moves.add((i-x,j-y))
							else:
								moves.add((i-x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								moves.add((i+x,j))
							else:
								moves.add((i+x,j))
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								moves.add((i-x,j))
							else:
								moves.add((i-x,j))
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								moves.add((i,j-x))
							else:
								moves.add((i,j-x))
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								moves.add((i,j+x))
							else:
								moves.add((i,j+x))
								break
							x = x + 1
						x = 1 
				elif (f == 'wK'):
					if (j < 7) and (i < 7):
						moves.add((i+1,j+1))
					if (j > 0) and (i < 7):
						moves.add((i+1,j-1))
					if (j < 7) and (i > 0):
						moves.add((i-1,j+1))
					if (j > 0) and (i > 0):
						moves.add((i-1,j-1))
					if (i < 7):
						moves.add((i+1,j))
					if (i > 0):
						moves.add((i-1,j))
					if (j < 7):
						moves.add((i,j+1))
					if (j > 0):
						moves.add((i,j-1))
			j = j + 1
		i = i + 1
	return (moves)        
# list of all cells attacked by black

def blackAttack (position):
	i = 0
	j = 0
	moves = set()
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f[0] == 'b'):
				if (f == 'bP1') or (f == 'bP2') or (f == 'bP3') or (f == 'bP4') or (f == 'bP5') or (f == 'bP6') or (f == 'bP7') or (f == 'bP8'):
					if (i > 0) and (j < 7):
						moves.add((i-1,j+1))
					if (i > 0) and (j > 0):
						moves.add((i-1,j-1))
				elif (f[0:2] == 'bN'):
						if (i < 6) and (j < 7):
							moves.add((i+2,j+1))
						if (i < 6) and (j > 0):
							moves.add((i+2,j-1))
						if (i > 1) and (j < 7):
							moves.add((i-2,j+1))
						if (i > 1) and (j > 0):
							moves.add((i-2,j-1))
						if (i < 7) and (j < 6):
							moves.add((i+1,j+2))
						if (i < 7) and (j > 1):
							moves.add((i+1,j-2))
						if (i > 0) and (j < 6):
							moves.add((i-1,j+2))
						if (i > 0) and (j > 1):
							moves.add((i-1,j-2))
				elif (f[0:2] == 'bB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								moves.add((i+x,j+y))
							else:
								moves.add((i+x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								moves.add((i-x,j+y))
							else:
								moves.add((i-x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								moves.add((i+x,j-y))
							else:
								moves.add((i+x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								moves.add((i-x,j-y))
							else:
								moves.add((i-x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'bR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								moves.add((i+x,j))
							else:
								moves.add((i+x,j))
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								moves.add((i-x,j))
							else:
								moves.add((i-x,j))
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								moves.add((i,j-x))
							else:
								moves.add((i,j-x))
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								moves.add((i,j+x))
							else:
								moves.add((i,j+x))
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'bQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								moves.add((i+x,j+y))
							else:
								moves.add((i+x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								moves.add((i-x,j+y))
							else:
								moves.add((i-x,j+y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								moves.add((i+x,j-y))
							else:
								moves.add((i+x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								moves.add((i-x,j-y))
							else:
								moves.add((i-x,j-y))
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								moves.add((i+x,j))
							else:
								moves.add((i+x,j))
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								moves.add((i-x,j))
							else:
								moves.add((i-x,j))
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								moves.add((i,j-x))
							else:
								moves.add((i,j-x))
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								moves.add((i,j+x))
							else:
								moves.add((i,j+x))
								break
							x = x + 1
						x = 1 
				elif (f == 'bK'):
					if (j < 7) and (i < 7):
						moves.add((i+1,j+1))
					if (j > 0) and (i < 7):
						moves.add((i+1,j-1))
					if (j < 7) and (i > 0):
						moves.add((i-1,j+1))
					if (j > 0) and (i > 0):
						moves.add((i-1,j-1))
					if (i < 7):
						moves.add((i+1,j))
					if (i > 0):
						moves.add((i-1,j))
					if (j < 7):
						moves.add((i,j+1))
					if (j > 0):
						moves.add((i,j-1))
			j = j + 1
		i = i + 1
	return (moves)

 # determines which piece is in the chosen cell
# all possible position that white can make next move
def whitepossiblePositions (position,moverecord):
	bAttacked = blackAttack(position)
	i = 0
	j = 0
	possibilities = []
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f[0] == 'w'):
				if (f == 'wP1') or (f == 'wP2') or (f == 'wP3') or (f == 'wP4') or (f == 'wP5') or (f == 'wP6') or (f == 'wP7') or (f == 'wP8'):
					if (i == 1) and ((position[2])[j] == 'e') and ((position[3])[j] == 'e'):
						if not whiteCheck(swapping (position,i,j,i+2,j)):
							possibilities.append(swapping (position,i,j,i+2,j))
					if (i < 6) and ((position[i+1])[j] == 'e'):
						if not whiteCheck(swapping (position,i,j,i+1,j)):
							possibilities.append(swapping (position,i,j,i+1,j))
					if (j < 7) and (i < 6) and (colour((position[i+1])[j+1]) == 'black'):
						if not whiteCheck(swapping (position,i,j,i+1,j+1)):
							possibilities.append(swapping (position,i,j,i+1,j+1))
					if (i < 6) and (j > 0) and (colour((position[i+1])[j-1]) == 'black'):
						if not whiteCheck(swapping (position,i,j,i+1,j-1)):
							possibilities.append(swapping (position,i,j,i+1,j-1))
					if (i == 4) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
						position1 = swapping (position,i,j-1,i+1,j-1)
						if not whiteCheck(swapping (position,i,j,i+1,j-1)):
							possibilities.append(swapping (position,i,j,i+1,j-1))
					if (i == 4) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
						position1 = swapping (position,i,j+1,i+1,j+1)
						if not whiteCheck(swapping (position,i,j,i+1,j+1)):
							possibilities.append(swapping (position,i,j,i+1,j+1))
					if (i == 6) and ((position[i+1])[j] == 'e'):
						position1 = swapping (position,i,j,i+1,j)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j] + [wQ] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j] + [wR] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j] + [wB] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						possibilities.append(position2)
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j] + [wN] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
					if (i == 6) and (j > 0) and (colour((position[i+1])[j-1]) == 'black'):
						position1 = swapping (position,i,j,i+1,j-1)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wQ] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities.append(position2)
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wR] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wB] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities.append(position2)
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wN] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
					if (i == 6) and (j < 7) and (colour((position[i+1])[j+1]) == 'black'):
						position1 = swapping (position,i,j,i+1,j+1)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wQ] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wR] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wB] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wN] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						if not whiteCheck(position2):
							possibilities.append(position2)
				elif (f[0:2] == 'wN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i+2,j+1)):
								possibilities.append(swapping (position,i,j,i+2,j+1))
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i+2,j-1)):
								possibilities.append(swapping (position,i,j,i+2,j-1))
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i-2,j+1)):
								possibilities.append(swapping (position,i,j,i-2,j+1))
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i-2,j-1)):
								possibilities.append(swapping (position,i,j,i-2,j-1))
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i+1,j+2)):
								possibilities.append(swapping (position,i,j,i+1,j+2))
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i+1,j-2)):
								possibilities.append(swapping (position,i,j,i+1,j-2))
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i-1,j+2)):
								possibilities.append(swapping (position,i,j,i-1,j+2))
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'white'):
							if not whiteCheck(swapping (position,i,j,i-1,j-2)):
								possibilities.append(swapping (position,i,j,i-1,j-2))
				elif (f[0:2] == 'wB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
							if (colour((position[i+x])[j+y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
							if (colour((position[i-x])[j+y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
							if (colour((position[i+x])[j-y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
							if (colour((position[i-x])[j-y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'wR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
							if (colour((position[i+x])[j]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
							if (colour((position[i-x])[j]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								if not whiteCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
							if (colour((position[i])[j-x]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								if not whiteCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
							if (colour((position[i])[j+x]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'wQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
							if (colour((position[i+x])[j+y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
							if (colour((position[i-x])[j+y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
							if (colour((position[i+x])[j-y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
							if (colour((position[i-x])[j-y]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								if not whiteCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
							if (colour((position[i+x])[j]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								if not whiteCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
							if (colour((position[i-x])[j]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								if not whiteCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
							if (colour((position[i])[j-x]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								if not whiteCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
							if (colour((position[i])[j+x]) == 'black'):
								if not whiteCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
				elif (f == 'wK'):
					if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i+1,j+1)):
							possibilities.append(swapping (position,i,j,i+1,j+1))
					if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i+1,j-1)):
							possibilities.append(swapping (position,i,j,i+1,j-1))
					if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i-1,j+1)):
							possibilities.append(swapping (position,i,j,i-1,j+1))
					if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i-1,j-1)):
							possibilities.append(swapping (position,i,j,i-1,j-1))
					if (i < 7) and (colour((position[i+1])[j]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i+1,j)):
							possibilities.append(swapping (position,i,j,i+1,j))
					if (i > 0) and (colour((position[i-1])[j]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i-1,j)):
							possibilities.append(swapping (position,i,j,i-1,j))
					if (j < 7) and (colour((position[i])[j+1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i,j+1)):
							possibilities.append(swapping (position,i,j,i,j+1))
					if (j > 0) and (colour((position[i])[j-1]) != 'white'):
						if not whiteCheck(swapping (position,i,j,i,j-1)):
							possibilities.append(swapping (position,i,j,i,j-1))	
					if ((position[0])[5] == 'e') and ((position[0])[6] == 'e') and ((position[0])[7] == 'wR2') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,5) in bAttacked) or ((0,6) in bAttacked)):
						position1 = swapping (position,0,7,0,5)
						possibilities.append(swapping (position1,0,4,0,6))
					if ((position[0])[3] == 'e') and ((position[0])[2] == 'e') and ((position[0])[1] == 'e') and ((position[0])[0] == 'wR1') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,3) in bAttacked) or ((0,2) in bAttacked)):
						position1 = swapping (position,0,0,0,3)
						possibilities.append(swapping (position1,0,4,0,2))
			j = j + 1
		i = i + 1
	return (possibilities)


def whitepossiblePositionsEst (position,moverecord):
	bAttacked = blackAttack(position)
	i = 0
	j = 0
	possibilities = []
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f[0] == 'w'):
				if (f == 'wP1') or (f == 'wP2') or (f == 'wP3') or (f == 'wP4') or (f == 'wP5') or (f == 'wP6') or (f == 'wP7') or (f == 'wP8'):
					if (i == 1) and ((position[2])[j] == 'e') and ((position[3])[j] == 'e'):
						possibilities = possibilities + [swapping (position,i,j,i+2,j)]
					if (i < 6) and ((position[i+1])[j] == 'e'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j)]
					if (j < 7) and (i < 6) and (colour((position[i+1])[j+1]) == 'black'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j+1)]
					if (i < 6) and (j > 0) and (colour((position[i+1])[j-1]) == 'black'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j-1)]
					if (i == 4) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
						position1 = swapping (position,i,j-1,i+1,j-1)
						possibilities = possibilities + [swapping (position1,i,j,i+1,j-1)]
					if (i == 4) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
						position1 = swapping (position,i,j+1,i+1,j+1)
						possibilities = possibilities + [swapping (position1,i,j,i+1,j+1)]
					if (i == 6) and ((position[i+1])[j] == 'e'):
						position1 = swapping (position,i,j,i+1,j)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j] + [wQ] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j] + [wR] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j] + [wB] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j] + [wN] + (position1[7])[j+1:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
					if (i == 6) and (j > 0) and (colour((position[i+1])[j-1]) == 'black'):
						position1 = swapping (position,i,j,i+1,j-1)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wQ] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wR] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wB] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j-1] + [wN] + (position1[7])[j:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
					if (i == 6) and (j < 7) and (colour((position[i+1])[j+1]) == 'black'):
						position1 = swapping (position,i,j,i+1,j+1)
						wQ = 'wQ' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wQ] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wR = 'wR' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wR] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wB = 'wB' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wB] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
						wN = 'wN' + f[1:3]
						newRow = (position1[7])[0:j+1] + [wN] + (position1[7])[j+2:8]
						position2 = position1[0:7] + [newRow] 
						possibilities = possibilities + [position2]
				elif (f[0:2] == 'wN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i+2,j+1)]
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i+2,j-1)]
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i-2,j+1)]
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i-2,j-1)]
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i+1,j+2)]
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i+1,j-2)]
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i-1,j+2)]
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'white'):
							possibilities = possibilities + [swapping (position,i,j,i-1,j-2)]	 
				elif (f[0:2] == 'wB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
							if (colour((position[i+x])[j+y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
							if (colour((position[i-x])[j+y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
							if (colour((position[i+x])[j-y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
							if (colour((position[i-x])[j-y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'wR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
							if (colour((position[i+x])[j]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
							if (colour((position[i-x])[j]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
							if (colour((position[i])[j-x]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
							if (colour((position[i])[j+x]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'wQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
							if (colour((position[i+x])[j+y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
							if (colour((position[i-x])[j+y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
							if (colour((position[i+x])[j-y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
							if (colour((position[i-x])[j-y]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
							if (colour((position[i+x])[j]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
							if (colour((position[i-x])[j]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
							if (colour((position[i])[j-x]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
							if (colour((position[i])[j+x]) == 'black'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
				elif (f == 'wK'):
					if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j+1)]
					if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j-1)]
					if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j+1)]
					if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j-1)]
					if (i < 7) and (colour((position[i+1])[j]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j)]
					if (i > 0) and (colour((position[i-1])[j]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j)]
					if (j < 7) and (colour((position[i])[j+1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i,j+1)]
					if (j > 0) and (colour((position[i])[j-1]) != 'white'):
						possibilities = possibilities + [swapping (position,i,j,i,j-1)]		
					if ((position[0])[5] == 'e') and ((position[0])[6] == 'e') and ((position[0])[7] == 'wR2') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,5) in bAttacked) or ((0,6) in bAttacked)):
						position1 = swapping (position,0,7,0,5)
						possibilities = possibilities + [swapping (position1,0,4,0,6)]
					if ((position[0])[3] == 'e') and ((position[0])[2] == 'e') and ((position[0])[1] == 'e') and ((position[0])[0] == 'wR1') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,3) in bAttacked) or ((0,2) in bAttacked)):
						position1 = swapping (position,0,0,0,3)
						possibilities = possibilities + [swapping (position1,0,4,0,2)]
			j = j + 1
		i = i + 1
	return (possibilities)



# all possible position that black can make next move	
def blackpossiblePositions (position,moverecord):
	wAttacked = whiteAttack(position)
	i = 0
	j = 0
	possibilities = []
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f[0] == 'b'):
				if (f == 'bP1') or (f == 'bP2') or (f == 'bP3') or (f == 'bP4') or (f == 'bP5') or (f == 'bP6') or (f == 'bP7') or (f == 'bP8'):
					if (i == 6) and ((position[5])[j] == 'e') and ((position[4])[j] == 'e'):
						if not blackCheck(swapping (position,i,j,i-2,j)):
							possibilities.append(swapping (position,i,j,i-2,j))
					if (i > 1) and ((position[i-1])[j] == 'e'):
						if not blackCheck(swapping (position,i,j,i-1,j)):
							possibilities.append(swapping (position,i,j,i-1,j))
					if (j < 7) and (i > 1) and (colour((position[i-1])[j+1]) == 'white'):
						if not blackCheck(swapping (position,i,j,i-1,j+1)):
							possibilities.append(swapping (position,i,j,i-1,j+1))
					if (i > 1) and (j > 0) and (colour((position[i-1])[j-1]) == 'white'):
						if not blackCheck(swapping (position,i,j,i-1,j-1)):
							possibilities.append(swapping (position,i,j,i-1,j-1))
					if (i == 3) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
						position1 = swapping (position,i,j-1,i-1,j-1)
						if not blackCheck(swapping (position,i,j,i-1,j-1)):
							possibilities.append(swapping (position,i,j,i-1,j-1))
					if (i == 3) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
						position1 = swapping (position,i,j+1,i-1,j+1)
						if not blackCheck(swapping (position,i,j,i-1,j+1)):
							possibilities.append(swapping (position,i,j,i-1,j+1))
					if (i == 1) and ((position[i-1])[j] == 'e'):
						position1 = swapping (position,i,j,i-1,j)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j] + [bQ] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j] + [bR] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j] + [bB] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j] + [bN] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
					if (i == 1) and (j > 0) and (colour((position[i-1])[j-1]) == 'white'):
						position1 = swapping (position,i,j,i-1,j-1)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bQ] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bR] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bB] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bN] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
					if (i == 1) and (j < 7) and (colour((position[i-1])[j+1]) == 'white'):
						position1 = swapping (position,i,j,i-1,j+1)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bQ] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bR] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8] 
						if not blackCheck(position2):
							possibilities.append(position2)
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bB] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bN] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8]
						if not blackCheck(position2):
							possibilities.append(position2)
				elif (f[0:2] == 'bN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'black'):
							if not blackCheck(swapping (position,i,j,i+2,j+1)):
								possibilities.append(swapping (position,i,j,i+2,j+1))
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'black'):
							if not blackCheck(swapping (position,i,j,i+2,j-1)):
								possibilities.append(swapping (position,i,j,i+2,j-1))
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'black'):
							if not blackCheck(swapping (position,i,j,i-2,j+1)):
								possibilities.append(swapping (position,i,j,i-2,j+1))
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'black'):
							if not blackCheck(swapping (position,i,j,i-2,j-1)):
								possibilities.append(swapping (position,i,j,i-2,j-1))
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'black'):
							if not blackCheck(swapping (position,i,j,i+1,j+2)):
								possibilities.append(swapping (position,i,j,i+1,j+2))
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'black'):
							if not blackCheck(swapping (position,i,j,i+1,j-2)):
								possibilities.append(swapping (position,i,j,i+1,j-2))
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'black'):
							if not blackCheck(swapping (position,i,j,i-1,j+2)):
								possibilities.append(swapping (position,i,j,i-1,j+2))
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'black'):
							if not blackCheck(swapping (position,i,j,i-1,j-2)):
								possibilities.append(swapping (position,i,j,i-1,j-2))	 
				elif (f[0:2] == 'bB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
							if (colour((position[i+x])[j+y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
							if (colour((position[i-x])[j+y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
							if (colour((position[i+x])[j-y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
							if (colour((position[i-x])[j-y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'bR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
							if (colour((position[i+x])[j]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
							if (colour((position[i-x])[j]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								if not blackCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
							if (colour((position[i])[j-x]) == 'white'):
								if not blackCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								if not blackCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
							if (colour((position[i])[j+x]) == 'white'):
								if not blackCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'bQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
							if (colour((position[i+x])[j+y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j+y)):
									possibilities.append(swapping (position,i,j,i+x,j+y))
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
							if (colour((position[i-x])[j+y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j+y)):
									possibilities.append(swapping (position,i,j,i-x,j+y))
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
							if (colour((position[i+x])[j-y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j-y)):
									possibilities.append(swapping (position,i,j,i+x,j-y))
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
							if (colour((position[i-x])[j-y]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j-y)):
									possibilities.append(swapping (position,i,j,i-x,j-y))
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								if not blackCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
							if (colour((position[i+x])[j]) == 'white'):
								if not blackCheck(swapping (position,i,j,i+x,j)):
									possibilities.append(swapping (position,i,j,i+x,j))
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								if not blackCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
							if (colour((position[i-x])[j]) == 'white'):
								if not blackCheck(swapping (position,i,j,i-x,j)):
									possibilities.append(swapping (position,i,j,i-x,j))
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								if not blackCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
							if (colour((position[i])[j-x]) == 'white'):
								if not blackCheck(swapping (position,i,j,i,j-x)):
									possibilities.append(swapping (position,i,j,i,j-x))
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								if not blackCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
							if (colour((position[i])[j+x]) == 'white'):
								if not blackCheck(swapping (position,i,j,i,j+x)):
									possibilities.append(swapping (position,i,j,i,j+x))
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				elif (f == 'bK'):
					if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i+1,j+1)):
							possibilities.append(swapping (position,i,j,i+1,j+1))
					if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i+1,j-1)):
							possibilities.append(swapping (position,i,j,i+1,j-1))
					if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i-1,j+1)):
							possibilities.append(swapping (position,i,j,i-1,j+1))
					if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i-1,j-1)):
							possibilities.append(swapping (position,i,j,i-1,j-1))
					if (i < 7) and (colour((position[i+1])[j]) != 'black'):
						if not blackCheck(swapping (position,i,j,i+1,j)):
							possibilities.append(swapping (position,i,j,i+1,j))
					if (i > 0) and (colour((position[i-1])[j]) != 'black'):
						if not blackCheck(swapping (position,i,j,i-1,j)):
							possibilities.append(swapping (position,i,j,i-1,j))
					if (j < 7) and (colour((position[i])[j+1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i,j+1)):
							possibilities.append(swapping (position,i,j,i,j+1))
					if (j > 0) and (colour((position[i])[j-1]) != 'black'):
						if not blackCheck(swapping (position,i,j,i,j-1)):
							possibilities.append(swapping (position,i,j,i,j-1))	
					if ((position[7])[5] == 'e') and ((position[7])[6] == 'e') and ((position[7])[7] == 'bR2') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,5) in wAttacked) or ((7,6) in wAttacked)):
						position1 = swapping (position,7,7,7,5)
						possibilities.append(swapping (position1,7,4,7,6))
					if ((position[7])[3] == 'e') and ((position[7])[2] == 'e') and ((position[7])[1] == 'e') and ((position[7])[0] == 'bR1') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,3) in wAttacked) or ((7,2) in wAttacked)):
						position1 = swapping (position,7,0,7,3)
						possibilities.append(swapping (position1,7,4,7,2))
			j = j + 1
		i = i + 1	
	return (possibilities)


def blackpossiblePositionsEst (position,moverecord):
	wAttacked = whiteAttack(position)
	i = 0
	j = 0
	possibilities = []
	while (i < 8):
		j = 0
		while (j < 8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f != 'e'):			
				if (f == 'bP1') or (f == 'bP2') or (f == 'bP3') or (f == 'bP4') or (f == 'bP5') or (f == 'bP6') or (f == 'bP7') or (f == 'bP8'):
					if (i == 6) and ((position[5])[j] == 'e') and ((position[4])[j] == 'e'):
						possibilities = possibilities + [swapping (position,i,j,i-2,j)]
					if (i > 1) and ((position[i-1])[j] == 'e'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j)]
					if (j < 7) and (i > 1) and (colour((position[i-1])[j+1]) == 'white'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j+1)]
					if (i > 1) and (j > 0) and (colour((position[i-1])[j-1]) == 'white'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j-1)]
					if (i == 3) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
						position1 = swapping (position,i,j-1,i-1,j-1)
						possibilities = possibilities + [swapping (position1,i,j,i-1,j-1)]
					if (i == 3) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
						position1 = swapping (position,i,j+1,i-1,j+1)
						possibilities = possibilities + [swapping (position1,i,j,i-1,j+1)]
					if (i == 1) and ((position[i-1])[j] == 'e'):
						position1 = swapping (position,i,j,i-1,j)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j] + [bQ] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j] + [bR] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j] + [bB] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j] + [bN] + (position1[0])[j+1:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
					if (i == 1) and (j > 0) and (colour((position[i-1])[j-1]) == 'white'):
						position1 = swapping (position,i,j,i-1,j-1)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bQ] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bR] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bB] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j-1] + [bN] + (position1[0])[j:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
					if (i == 1) and (j < 7) and (colour((position[i-1])[j+1]) == 'white'):
						position1 = swapping (position,i,j,i-1,j+1)
						bQ = 'bQ' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bQ] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bR = 'bR' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bR] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8] 
						possibilities = possibilities + [position2]
						bB = 'bB' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bB] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
						bN = 'bN' + f[1:3]
						newRow = (position1[0])[0:j+1] + [bN] + (position1[0])[j+2:8]
						position2 = [newRow] + position1[1:8]
						possibilities = possibilities + [position2]
				elif (f[0:2] == 'bN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i+2,j+1)]
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i+2,j-1)]
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i-2,j+1)]
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i-2,j-1)]
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i+1,j+2)]
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i+1,j-2)]
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i-1,j+2)]
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'black'):
							possibilities = possibilities + [swapping (position,i,j,i-1,j-2)]	 
				elif (f[0:2] == 'bB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
							if (colour((position[i+x])[j+y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
							if (colour((position[i-x])[j+y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
							if (colour((position[i+x])[j-y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
							if (colour((position[i-x])[j-y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				elif (f[0:2] == 'bR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
							if (colour((position[i+x])[j]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
							if (colour((position[i-x])[j]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
							if (colour((position[i])[j-x]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
							if (colour((position[i])[j+x]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				elif (f[0:2] == 'bQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
							if (colour((position[i+x])[j+y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j+y)]
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
							if (colour((position[i-x])[j+y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j+y)]
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
							if (colour((position[i+x])[j-y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j-y)]
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
							if (colour((position[i-x])[j-y]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j-y)]
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
							if (colour((position[i+x])[j]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i+x,j)]
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
							if (colour((position[i-x])[j]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i-x,j)]
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
							if (colour((position[i])[j-x]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i,j-x)]
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
							if (colour((position[i])[j+x]) == 'white'):
								possibilities = possibilities + [swapping (position,i,j,i,j+x)]
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				elif (f == 'bK'):
					if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j+1)]
					if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j-1)]
					if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j+1)]
					if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j-1)]
					if (i < 7) and (colour((position[i+1])[j]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i+1,j)]
					if (i > 0) and (colour((position[i-1])[j]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i-1,j)]
					if (j < 7) and (colour((position[i])[j+1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i,j+1)]
					if (j > 0) and (colour((position[i])[j-1]) != 'black'):
						possibilities = possibilities + [swapping (position,i,j,i,j-1)]		
					if ((position[7])[5] == 'e') and ((position[7])[6] == 'e') and ((position[7])[7] == 'bR2') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,5) in wAttacked) or ((7,6) in wAttacked)):
						position1 = swapping (position,7,7,7,5)
						possibilities = possibilities + [swapping (position1,7,4,7,6)]
					if ((position[7])[3] == 'e') and ((position[7])[2] == 'e') and ((position[7])[1] == 'e') and ((position[7])[0] == 'bR1') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,3) in wAttacked) or ((7,2) in wAttacked)):
						position1 = swapping (position,7,0,7,3)
						possibilities = possibilities + [swapping (position1,7,4,7,2)]
			j = j + 1
		i = i + 1
	return (possibilities)	


# checks if white king is under attack

def whiteCheck(position):
	return (whiteKingFinder(position) in blackAttack(position))
# checks if black king is under attack 

def blackCheck(position):
	return (blackKingFinder(position) in whiteAttack(position))
# records the move done
def moveslist(position,i,j,i1,j1):
	f = piece(i,j,position)
	i1 = str(i1)
	j1 = str(j1)
	i = str(i)
	j = str(j)
	return (i + j + i1 + j1 + f)
#determining the piece, its row and column numbers

def piece (i,j, position):
	return ((position[i])[j])
 #determines coordinates of the cell

def rowNumber (point):
	y = point.y
	i = int ((700-y-30) // 80)
	return(i)

def columnNumber (point):
	x = point.x
	j = int ((x-30) // 80)
	return(j)
 #draws the cell where chosen piece is allowed to move
#drawing and undrawing possible moves on the board 
def possibleMove (i,j):
	x = 70 + 80*j
	y = 700 - (70 + i*80)
	m = Rectangle (Point(x-36,y-36), Point(x+37,y+37))
	m.setWidth(6)
	m.setOutline ('yellow')
	m.draw(win)
	return(m)
def cleardots (dots):
	i = 0
	while i < len(dots):
		dots[i].undraw()
		i = i + 1
 #Determines the colour of the piece 
#determines the colour of the chosen piece

def colour (x):
	if x[0] == 'w':
		return('white')
	elif x[0] == 'b':
		return('black')
	else:
		return('empty')
 #Function makeMove moves the piece from cell (i,j) to cell(i1,j1)
# determines the position of white and black kings

def whiteKingFinder (position):
	found = False
	for i in range(8):
		j = 0
		for j in range(8):
			if ((position[i])[j] == 'wK'):
				s = (i,j)
				found = True
				break
		if found:
			break
	return (s)

def blackKingFinder (position):
	found = False
	i = 7
	j = 7
	while (i >= 0):
		j = 7
		while (j >= 0):
			if (position[i])[j] == 'bK':
				s = (i,j)
				found = True
				break
			j = j - 1
		if found:
			break
		i = i - 1
	return (s)
# check if white or black kings made any movements

def whiteKingMoves(moverecord):
	i = 0
	p = True
	while (i < len(moverecord)):
		if ((moverecord[i])[4:len(moverecord)] == 'wK'):
			p = False
			break
		i = i + 1
	return(p)

def blackKingMoves(moverecord):
	i = 0
	p = True
	while (i < len(moverecord)):
		if ((moverecord[i])[4:len(moverecord)] == 'bK'):
			p = False
			break
		i = i + 1
	return(p)

def piecenumber(position):
	i = 0
	j = 0
	wK = 0
	wQ = 0
	wR = 0
	wB = 0
	wN = 0
	wP = 0
	bK = 0
	bQ = 0
	bR = 0
	bB = 0
	bN = 0
	bP = 0
	while (i < 8):
		j = 0
		while (j < 8):
			f = (position[i])[j]
			if (f == 'wK'):
				wK = wK + 1
			if (f == 'wQ'):
				wQ = wQ + 1
			if (f == 'wR1') or (f == 'wR2'):
				wR = wR + 1
			if (f == 'wB1') or (f == 'wB2'):
				wB = wB + 1
			if (f == 'wN1') or (f == 'wN2'):
				wN = wN + 1
			if (f[0:2] == 'wP'):
				wP = wP + 1
			if (len(f) > 2) and (f[0] + f[2] == 'wP'):
				wP = wP + 1			
			if (f == 'bK'):
				bK = bK + 1
			if (f == 'bQ'):
				bQ = bQ + 1
			if (f == 'bR1') or (f == 'bR2'):
				bR = bR + 1
			if (f == 'bB1') or (f == 'bB2'):
				bB = bB + 1
			if (f == 'bN1') or (f == 'bN2'):
				bN = bN + 1
			if (f[0:2] == 'bP'):
				bP = bP + 1
			if (len(f) > 2) and (f[0] + f[2] == 'bP'):
				bP = bP + 1	
			j = j + 1
		i = i + 1
	return (wK,wQ,wR,wB,wN,wP,bK,bQ,bR,bB,bN,bP)

# making a move (drawing on the board)
def makeMove (position,i,j,i1,j1):
	y = -(i1-i)*80
	x = (j1-j)*80
	delay = 0.002
	frames = 16
	if piece(i,j,position) == 'wR1':
		d = 0
		while (d < frames):
			whiteRook1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wR2':
		d = 0
		while (d < frames):
			whiteRook2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wN1':
		d = 0
		while (d < frames):
			whiteKnight1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wN2':
		d = 0
		while (d < frames):
			whiteKnight2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wB1':
		d = 0
		while (d < frames):
			whiteBishop1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wB2':
		d = 0
		while (d < frames):
			whiteBishop2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wQ':
		d = 0
		while (d < frames):
			whiteQueen.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'wK':
		d = 0
		while (d < frames):
			whiteKing.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP1') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP1'):
		d = 0
		while (d < frames):
			whitePawn1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP2') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP2'):
		d = 0
		while (d < frames):
			whitePawn2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP3') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP3'):
		d = 0
		while (d < frames):
			whitePawn3.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP4') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP4'):
		d = 0
		while (d < frames):
			whitePawn4.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP5') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP5'):
		d = 0
		while (d < frames):
			whitePawn5.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP6') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP6'):
		d = 0
		while (d < frames):
			whitePawn6.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP7') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP7'):
		d = 0
		while (d < frames):
			whitePawn7.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if (piece(i,j,position) == 'wP8') or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'wP8'):
		d = 0
		while (d < frames):
			whitePawn8.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bR1':
		d = 0
		while (d < frames):
			blackRook1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bR2':
		d = 0
		while (d < frames):
			blackRook2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bN1':
		d = 0
		while (d < frames):
			blackKnight1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bN2':
		d = 0
		while (d < frames):
			blackKnight2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bB1':
		d = 0
		while (d < frames):
			blackBishop1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bB2':
		d = 0
		while (d < frames):
			blackBishop2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bQ':
		d = 0
		while (d < frames):
			blackQueen.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bK':
		d = 0
		while (d < frames):
			blackKing.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP1' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP1'):
		d = 0
		while (d < frames):
			blackPawn1.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP2' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP2'):
		d = 0
		while (d < frames):
			blackPawn2.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP3' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP3'):
		d = 0
		while (d < frames):
			blackPawn3.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP4' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP4'):
		d = 0
		while (d < frames):
			blackPawn4.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP5' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP5'):
		d = 0
		while (d < frames):
			blackPawn5.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP6' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP6'):
		d = 0
		while (d < frames):
			blackPawn6.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP7' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP7'):
		d = 0
		while (d < frames):
			blackPawn7.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	if piece(i,j,position) == 'bP8' or (piece(i,j,position)[0] + piece(i,j,position)[2:4] == 'bP8'):
		d = 0
		while (d < frames):
			blackPawn8.move(x/frames,y/frames)
			time.sleep(delay)
			d = d + 1
	
#ComputerPlays functions
def whitecomputerMove (position,position1):
	i = 0
	j = 0
	enpassant1 = False
	enpassant2 = False
	shortcastles = False
	longcastles = False
	promotion = False
	while (i < 8):
		j = 0
		while (j < 8):
			if ((position[i])[j] != ((position1[i])[j])) and (colour((position1[i])[j]) == 'white'): 
				i2 = i
				j2 = j
			if ((position[i])[j] != ((position1[i])[j])) and (colour((position1[i])[j]) != 'white'): 
				i1 = i
				j1 = j
			j = j + 1
		i = i + 1
	i = 0
	while (i < 8):
		if (((position1[7])[i])[0:3] == 'wQP') or (((position1[7])[i])[0:3] == 'wRP') or (((position1[7])[i])[0:3] == 'wBP') or (((position1[7])[i])[0:3] == 'wNP'):
			if (((position[6])[i])[0:2] == 'wP'):
				promotion = True
				break
			if (i > 0) and (((position[6])[i-1])[0:2] == 'wP'):
				promotion = True
				break
			if (i < 7) and (((position[6])[i+1])[0:2] == 'wP'):
				promotion = True
				break
		i = i + 1
	i = 0
	if (((position[0])[4]) == 'wK') and (((position[0])[7]) == 'wR2') and (((position1[0])[5]) == 'wR2') and (((position1[0])[6]) == 'wK'):
		shortcastles = True
		i1 = 0
		j1 = 4
		i2 = 0
		j2 = 6
	if (((position[0])[4]) == 'wK') and (((position[0])[0]) == 'wR1') and (((position1[0])[3]) == 'wR1') and (((position1[0])[2]) == 'wK'):
		longcastles = True
		i1 = 0
		j1 = 4
		i2 = 0
		j2 = 2
	while (i < 8):
		if (i > 0) and (((position[4])[i])[0:2] == 'wP') and (((position[4])[i-1])[0:2] == 'bP') and (((position1[4])[i])[0:2] == 'e') and (((position1[5])[i-1])[0:2] == 'wP') and (((position1[4])[i-1]) == 'e'):
			enpassant1 = True
			i1 = 4
			j1 = i
			i2 = 5
			j2 = i-1
		if (i < 7) and (((position[4])[i])[0:2] == 'wP') and (((position[4])[i+1])[0:2] == 'bP') and (((position1[4])[i])[0:2] == 'e') and (((position1[5])[i+1])[0:2] == 'wP') and (((position1[4])[i+1]) == 'e'):
			enpassant2 = True
			i1 = 4
			j1 = i
			i2 = 5
			j2 = i+1
		i = i + 1
	return (i1,j1,i2,j2,promotion,enpassant1,enpassant2,shortcastles,longcastles)

def blackcomputerMove (position,position1):
	i = 0
	j = 0
	enpassant1 = False
	enpassant2 = False
	shortcastles = False
	longcastles = False
	promotion = False
	while (i < 8):
		j = 0
		while (j < 8):
			if ((position[i])[j] != ((position1[i])[j])) and (colour((position1[i])[j]) == 'black'): 
				i2 = i
				j2 = j
			if ((position[i])[j] != ((position1[i])[j])) and (colour((position1[i])[j]) != 'black'): 
				i1 = i
				j1 = j
			j = j + 1
		i = i + 1
	i = 0
	while (i < 8):
		if (((position1[0])[i])[0:3] == 'bQP') or (((position1[0])[i])[0:3] == 'bRP') or (((position1[0])[i])[0:3] == 'bBP') or (((position1[0])[i])[0:3] == 'bNP'):
			if (((position[1])[i])[0:2] == 'bP'):
				promotion = True
				break
			if (i > 0) and (((position[1])[i-1])[0:2] == 'bP'):
				promotion = True
				break
			if (i < 7) and (((position[1])[i+1])[0:2] == 'bP'):
				promotion = True
				break
		i = i + 1
	i = 0
	if (((position[7])[4]) == 'bK') and (((position[7])[7]) == 'bR2') and (((position1[7])[5]) == 'bR2') and (((position1[7])[6]) == 'bK'):
		shortcastles = True
		i1 = 7
		j1 = 4
		i2 = 7
		j2 = 6
	if (((position[7])[4]) == 'bK') and (((position[7])[0]) == 'bR1') and (((position1[7])[3]) == 'bR1') and (((position1[7])[2]) == 'bK'):
		longcastles = True
		i1 = 7
		j1 = 4
		i2 = 7
		j2 = 2
	while (i < 8):
		if (i > 0) and (((position[3])[i])[0:2] == 'bP') and (((position[3])[i-1])[0:2] == 'wP') and (((position1[3])[i])[0:2] == 'e') and (((position1[2])[i-1])[0:2] == 'bP') and (((position1[3])[i-1]) == 'e'):
			enpassant1 = True
			i1 = 3
			j1 = i
			i2 = 2
			j2 = i-1
		if (i < 7) and (((position[3])[i])[0:2] == 'bP') and (((position[3])[i+1])[0:2] == 'wP') and (((position1[3])[i])[0:2] == 'e') and (((position1[2])[i+1])[0:2] == 'bP') and (((position1[3])[i+1]) == 'e'):
			enpassant2 = True
			i1 = 3
			j1 = i
			i2 = 2
			j2 = i+1
		i = i + 1
	return (i1,j1,i2,j2,promotion,enpassant1,enpassant2,shortcastles,longcastles)

def materialcounter (position):
	s = 0
	i = 0
	j = 0
	while i < 8:
		j = 0
		while j < 8:
			f = (position[i])[j]
			if (f != 'e'):
				if (f[0:2] == 'wP'):
					s = s + 1
				if (f[0:2] == 'wR'):
					s = s + 5
				if (f[0:2] == 'wN'):
					s = s + 3
				if (f[0:2] == 'wB'):
					s = s + 3
				if (f[0:2] == 'wQ'):
					s = s + 9
				if (f[0:2] == 'bP'):
					s = s - 1
				if (f[0:2] == 'bR'):
					s = s - 5
				if (f[0:2] == 'bN'):
					s = s - 3
				if (f[0:2] == 'bB'):
					s = s - 3
				if (f[0:2] == 'bQ'):
					s = s - 9
			j = j + 1
		i = i + 1
	return(s)


def maxnumber (x):
	m = -3000
	i = 0
	k = 0
	while i < len(x):
		if x[i] > m:
			m = x[i]
			k = [i]
		i = i + 1
	return(k)

def minnumber (x):
	m = 3000
	i = 0
	k = 0
	while i < len(x):
		if x[i] < m:
			m = x[i]
			k = [i]
		i = i + 1
	return(k)



def maxvalue (x):
	m = np.array([-3000])
	i = 0
	k = 0
	while i < len(x):
		if x[i] > m:
			m = x[i]
			k = [i]
		i = i + 1
	return(m)

def minvalue (x):
	m = np.array([3000])
	i = 0
	k = 0
	while i < len(x):
		if x[i] < m:
			m = x[i]
			k = [i]
		i = i + 1
	return(m)



def positionvector2(position):

	i = 0
	j = 0

	wP1moves = set()
	wP2moves = set()
	wP3moves = set()
	wP4moves = set()
	wP5moves = set()
	wP6moves = set()
	wP7moves = set()
	wP8moves = set()

	wN1moves = set()
	wN2moves = set()
	wB1moves = set()
	wB2moves = set()
	wR1moves = set()
	wR2moves = set()
	wQmoves = set()
	wKmoves = set()

	bP1moves = set()
	bP2moves = set()
	bP3moves = set()
	bP4moves = set()
	bP5moves = set()
	bP6moves = set()
	bP7moves = set()
	bP8moves = set()

	bN1moves = set()
	bN2moves = set()
	bB1moves = set()
	bB2moves = set()
	bR1moves = set()
	bR2moves = set()
	bQmoves = set()
	bKmoves = set()

	array = []

	# 0-31 the existense of pieces (0-15 white pieces, 16-31 black pieces)
	# 


	pieces = set(position[0] + position[1] + position[2] + position[3] + position[4] + position[5] + position[6] + position[7])

	if 'wK' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wQ' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wR1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wR2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wB1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wB2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wN1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wN2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wP1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wP2' in pieces:
		array.append(1)
	else:
		array.append(0)		
	if 'wP3' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP4' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP5' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP6' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP7' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP8' in pieces:
		array.append(1)
	else:
		array.append(0)	

	if 'bK' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bQ' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bR1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bR2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bB1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bB2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bN1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bN2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP2' in pieces:
		array.append(1)
	else:
		array.append(0)		
	if 'bP3' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP4' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP5' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP6' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP7' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP8' in pieces:
		array.append(1)
	else:
		array.append(0)	



	for i in range(8):
		for j in range(8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f == 'wP1'):
				if (j < 7):
					wP1moves.add((i+1,j+1))
				if (j > 0):
					wP1moves.add((i+1,j-1))
			elif (f == 'wP2'):
				if (j < 7):
					wP2moves.add((i+1,j+1))
				if (j > 0):
					wP2moves.add((i+1,j-1))
			elif (f == 'wP3'):
				if (j < 7):
					wP3moves.add((i+1,j+1))
				if (j > 0):
					wP3moves.add((i+1,j-1))
			elif (f == 'wP4'):
				if (j < 7):
					wP4moves.add((i+1,j+1))
				if (j > 0):
					wP4moves.add((i+1,j-1))
			elif (f == 'wP5'):
				if (j < 7):
					wP5moves.add((i+1,j+1))
				if (j > 0):
					wP5moves.add((i+1,j-1))
			elif (f == 'wP6'):
				if (j < 7):
					wP6moves.add((i+1,j+1))
				if (j > 0):
					wP6moves.add((i+1,j-1))
			elif (f == 'wP7'):
				if (j < 7):
					wP7moves.add((i+1,j+1))
				if (j > 0):
					wP7moves.add((i+1,j-1))
			elif (f == 'wP8'):
				if (j < 7):
					wP8moves.add((i+1,j+1))
				if (j > 0):
					wP8moves.add((i+1,j-1))
			elif (f == 'wN1'):
				if (i < 6) and (j < 7):
					wN1moves.add((i+2,j+1))
				if (i < 6) and (j > 0):
					wN1moves.add((i+2,j-1))
				if (i > 1) and (j < 7):
					wN1moves.add((i-2,j+1))
				if (i > 1) and (j > 0):
					wN1moves.add((i-2,j-1))
				if (i < 7) and (j < 6):
					wN1moves.add((i+1,j+2))
				if (i < 7) and (j > 1):
					wN1moves.add((i+1,j-2))
				if (i > 0) and (j < 6):
					wN1moves.add((i-1,j+2))
				if (i > 0) and (j > 1):
					wN1moves.add((i-1,j-2))	
			elif (f == 'wN2'):
				if (i < 6) and (j < 7):
					wN2moves.add((i+2,j+1))
				if (i < 6) and (j > 0):
					wN2moves.add((i+2,j-1))
				if (i > 1) and (j < 7):
					wN2moves.add((i-2,j+1))
				if (i > 1) and (j > 0):
					wN2moves.add((i-2,j-1))
				if (i < 7) and (j < 6):
					wN2moves.add((i+1,j+2))
				if (i < 7) and (j > 1):
					wN2moves.add((i+1,j-2))
				if (i > 0) and (j < 6):
					wN2moves.add((i-1,j+2))
				if (i > 0) and (j > 1):
					wN2moves.add((i-1,j-2))	 	 
			elif (f == 'wB1'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wB1moves.add((i+x,j+y))
					else:
						wB1moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wB1moves.add((i-x,j+y))
					else:
						wB1moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wB1moves.add((i+x,j-y))
					else:
						wB1moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wB1moves.add((i-x,j-y))
					else:
						wB1moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1	
			elif (f == 'wB2'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wB2moves.add((i+x,j+y))
					else:
						wB2moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wB2moves.add((i-x,j+y))
					else:
						wB2moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wB2moves.add((i+x,j-y))
					else:
						wB2moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wB2moves.add((i-x,j-y))
					else:
						wB2moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1		
			elif (f == 'wR1'):
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wR1moves.add((i+x,j))
					else:
						wR1moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wR1moves.add((i-x,j))
					else:
						wR1moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wR1moves.add((i,j-x))
					else:
						wR1moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wR1moves.add((i,j+x))
					else:
						wR1moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wR2'):
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wR2moves.add((i+x,j))
					else:
						wR2moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wR2moves.add((i-x,j))
					else:
						wR2moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wR2moves.add((i,j-x))
					else:
						wR2moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wR2moves.add((i,j+x))
					else:
						wR2moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wQ'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wQmoves.add((i+x,j+y))
					else:
						wQmoves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wQmoves.add((i-x,j+y))
					else:
						wQmoves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wQmoves.add((i+x,j-y))
					else:
						wQmoves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wQmoves.add((i-x,j-y))
					else:
						wQmoves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wQmoves.add((i+x,j))
					else:
						wQmoves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wQmoves.add((i-x,j))
					else:
						wQmoves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wQmoves.add((i,j-x))
					else:
						wQmoves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wQmoves.add((i,j+x))
					else:
						wQmoves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wK'):
				if (j < 7) and (i < 7):
					wKmoves.add((i+1,j+1))
				if (j > 0) and (i < 7):
					wKmoves.add((i+1,j-1))
				if (j < 7) and (i > 0):
					wKmoves.add((i-1,j+1))
				if (j > 0) and (i > 0):
					wKmoves.add((i-1,j-1))
				if (i < 7):
					wKmoves.add((i+1,j))
				if (i > 0):
					wKmoves.add((i-1,j))
				if (j < 7):
					wKmoves.add((i,j+1))
				if (j > 0):
					wKmoves.add((i,j-1))
			elif (f == 'bP1'):
				if (j < 7):
					bP1moves.add((i-1,j+1))
				if (j > 0):
					bP1moves.add((i-1,j-1))
			elif (f == 'bP2'):
				if (j < 7):
					bP2moves.add((i-1,j+1))
				if (j > 0):
					bP2moves.add((i-1,j-1))
			elif (f == 'bP3'):
				if (j < 7):
					bP3moves.add((i-1,j+1))
				if (j > 0):
					bP3moves.add((i-1,j-1))
			elif (f == 'bP4'):
				if (j < 7):
					bP4moves.add((i-1,j+1))
				if (j > 0):
					bP4moves.add((i-1,j-1))
			elif (f == 'bP5'):
				if (j < 7):
					bP5moves.add((i-1,j+1))
				if (j > 0):
					bP5moves.add((i-1,j-1))
			elif (f == 'bP6'):
				if (j < 7):
					bP6moves.add((i-1,j+1))
				if (j > 0):
					bP6moves.add((i-1,j-1))
			elif (f == 'bP7'):
				if (j < 7):
					bP7moves.add((i-1,j+1))
				if (j > 0):
					bP7moves.add((i-1,j-1))
			elif (f == 'bP8'):
				if (j < 7):
					bP8moves.add((i-1,j+1))
				if (j > 0):
					bP8moves.add((i-1,j-1))
			elif (f == 'bN1'):
				if (i < 6) and (j < 7):
					bN1moves.add((i+2,j+1))
				if (i < 6) and (j > 0):
					bN1moves.add((i+2,j-1))
				if (i > 1) and (j < 7):
					bN1moves.add((i-2,j+1))
				if (i > 1) and (j > 0):
					bN1moves.add((i-2,j-1))
				if (i < 7) and (j < 6):
					bN1moves.add((i+1,j+2))
				if (i < 7) and (j > 1):
					bN1moves.add((i+1,j-2))
				if (i > 0) and (j < 6):
					bN1moves.add((i-1,j+2))
				if (i > 0) and (j > 1):
					bN1moves.add((i-1,j-2))	
			elif (f == 'bN2'):
				if (i < 6) and (j < 7):
					bN2moves.add((i+2,j+1))
				if (i < 6) and (j > 0):
					bN2moves.add((i+2,j-1))
				if (i > 1) and (j < 7):
					bN2moves.add((i-2,j+1))
				if (i > 1) and (j > 0):
					bN2moves.add((i-2,j-1))
				if (i < 7) and (j < 6):
					bN2moves.add((i+1,j+2))
				if (i < 7) and (j > 1):
					bN2moves.add((i+1,j-2))
				if (i > 0) and (j < 6):
					bN2moves.add((i-1,j+2))
				if (i > 0) and (j > 1):
					bN2moves.add((i-1,j-2))	 	 
			elif (f == 'bB1'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bB1moves.add((i+x,j+y))
					else:
						bB1moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bB1moves.add((i-x,j+y))
					else:
						bB1moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bB1moves.add((i+x,j-y))
					else:
						bB1moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bB1moves.add((i-x,j-y))
					else:
						bB1moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1	
			elif (f == 'bB2'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bB2moves.add((i+x,j+y))
					else:
						bB2moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bB2moves.add((i-x,j+y))
					else:
						bB2moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bB2moves.add((i+x,j-y))
					else:
						bB2moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bB2moves.add((i-x,j-y))
					else:
						bB2moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1		
			elif (f == 'bR1'):
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bR1moves.add((i+x,j))
					else:
						bR1moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bR1moves.add((i-x,j))
					else:
						bR1moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bR1moves.add((i,j-x))
					else:
						bR1moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bR1moves.add((i,j+x))
					else:
						bR1moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bR2'):
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bR2moves.add((i+x,j))
					else:
						bR2moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bR2moves.add((i-x,j))
					else:
						bR2moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bR2moves.add((i,j-x))
					else:
						bR2moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bR2moves.add((i,j+x))
					else:
						bR2moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bQ'):
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bQmoves.add((i+x,j+y))
					else:
						bQmoves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bQmoves.add((i-x,j+y))
					else:
						bQmoves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bQmoves.add((i+x,j-y))
					else:
						bQmoves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bQmoves.add((i-x,j-y))
					else:
						bQmoves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bQmoves.add((i+x,j))
					else:
						bQmoves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bQmoves.add((i-x,j))
					else:
						bQmoves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bQmoves.add((i,j-x))
					else:
						bQmoves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bQmoves.add((i,j+x))
					else:
						bQmoves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bK'):
				if (j < 7) and (i < 7):
					bKmoves.add((i+1,j+1))
				if (j > 0) and (i < 7):
					bKmoves.add((i+1,j-1))
				if (j < 7) and (i > 0):
					bKmoves.add((i-1,j+1))
				if (j > 0) and (i > 0):
					bKmoves.add((i-1,j-1))
				if (i < 7):
					bKmoves.add((i+1,j))
				if (i > 0):
					bKmoves.add((i-1,j))
				if (j < 7):
					bKmoves.add((i,j+1))
				if (j > 0):
					bKmoves.add((i,j-1))



	attackingvector = []

	i = 0
	j = 0

	for i in range(8):
		j = 0
		for j in range(8):
			if (i,j) in wP1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP3moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP4moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP5moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP6moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP7moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wP8moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wN1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wN2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wB1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wB2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wR1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wR2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wQmoves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in wKmoves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			
			if (i,j) in bP1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP3moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP4moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP5moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP6moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP7moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bP8moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bN1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bN2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bB1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bB2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bR1moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bR2moves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bQmoves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)
			if (i,j) in bKmoves:
				attackingvector.append(1)
			else:
				attackingvector.append(0)

	i = 0
	j = 0

	wP1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP3Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP4Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP5Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP6Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP7Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wP8Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wN1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wN2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wB1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wB2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wR1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wR2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wQAttacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	wKAttacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP3Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP4Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP5Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP6Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP7Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bP8Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bN1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bN2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bB1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bB2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bR1Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bR2Attacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bQAttacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	bKAttacked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for i in range(8):
		for j in range(8):
			f = (position[i])[j]
			k = (i*8+j)*32
			if (f == 'wP1'):
				wP1Attacked = attackingvector[k:k+32]
			elif (f == 'wP2'):
				wP2Attacked = attackingvector[k:k+32]
			elif (f == 'wP3'):
				wP3Attacked = attackingvector[k:k+32]
			elif (f == 'wP4'):
				wP4Attacked = attackingvector[k:k+32]
			elif (f == 'wP5'):
				wP5Attacked = attackingvector[k:k+32]
			elif (f == 'wP6'):
				wP6Attacked = attackingvector[k:k+32]
			elif (f == 'wP7'):
				wP7Attacked = attackingvector[k:k+32]
			elif (f == 'wP8'):
				wP8Attacked = attackingvector[k:k+32]
			elif (f == 'wN1'):
				wN1Attacked = attackingvector[k:k+32]
			elif (f == 'wN2'):
				wN2Attacked = attackingvector[k:k+32]
			elif (f == 'wB1'):
				wB1Attacked = attackingvector[k:k+32]
			elif (f == 'wB2'):
				wB2Attacked = attackingvector[k:k+32]
			elif (f == 'wR1'):
				wR1Attacked = attackingvector[k:k+32]
			elif (f == 'wR2'):
				wR2Attacked = attackingvector[k:k+32]
			elif (f == 'wQ'):
				wQAttacked = attackingvector[k:k+32]
			elif (f == 'wK'):
				wKAttacked = attackingvector[k:k+32]
			elif (f == 'bP1'):
				bP1Attacked = attackingvector[k:k+32]
			elif (f == 'bP2'):
				bP2Attacked = attackingvector[k:k+32]
			elif (f == 'bP3'):
				bP3Attacked = attackingvector[k:k+32]
			elif (f == 'bP4'):
				bP4Attacked = attackingvector[k:k+32]
			elif (f == 'bP5'):
				bP5Attacked = attackingvector[k:k+32]
			elif (f == 'bP6'):
				bP6Attacked = attackingvector[k:k+32]
			elif (f == 'bP7'):
				bP7Attacked = attackingvector[k:k+32]
			elif (f == 'bP8'):
				bP8Attacked = attackingvector[k:k+32]
			elif (f == 'bN1'):
				bN1Attacked = attackingvector[k:k+32]
			elif (f == 'bN2'):
				bN2Attacked = attackingvector[k:k+32]
			elif (f == 'bB1'):
				bB1Attacked = attackingvector[k:k+32]
			elif (f == 'bB2'):
				bB2Attacked = attackingvector[k:k+32]
			elif (f == 'bR1'):
				bR1Attacked = attackingvector[k:k+32]
			elif (f == 'bR2'):
				bR2Attacked = attackingvector[k:k+32]
			elif (f == 'bQ'):
				bQAttacked = attackingvector[k:k+32]
			elif (f == 'bK'):
				bKAttacked = attackingvector[k:k+32]



	attacked = wP1Attacked + wP2Attacked + wP3Attacked + wP4Attacked + wP5Attacked + wP6Attacked + wP7Attacked + wP8Attacked + wN1Attacked + wN2Attacked + wB1Attacked + wB2Attacked + wR1Attacked + wR2Attacked + wQAttacked + wKAttacked + bP1Attacked + bP2Attacked + bP3Attacked + bP4Attacked + bP5Attacked + bP6Attacked + bP7Attacked + bP8Attacked + bN1Attacked + bN2Attacked + bB1Attacked + bB2Attacked + bR1Attacked + bR2Attacked + bQAttacked + bKAttacked

	i = 0
	attackingvector2 = []
	for i in range(128):
		s = 16*i
		m = 0.8*sum(attackingvector[s:s+8]) + 0.5*sum(attackingvector[s+8:s+12]) + 0.3*sum(attackingvector[s+12:s+14]) + 0.1*sum(attackingvector[s+14:s+15])
		attackingvector2 = attackingvector2 + [m]

	i = 0
	attacked2 = []
	for i in range(40):
		s = 16*i
		m = 0.8*sum(attacked[s:s+8]) + 0.5*sum(attacked[s+8:s+12]) + 0.3*sum(attacked[s+12:s+14]) + 0.1*sum(attacked[s+14:s+15])
		attacked2 = attacked2 + [m]

	output = array + attackingvector2


	return(output)


def positionvector(position):
		
	centre = {(3,2),(3,3),(3,4),(3,5),
		  	(4,2),(4,3),(4,4),(4,5)}
	
	i = 0
	j = 0

	wP1moves = set()
	wP2moves = set()
	wP3moves = set()
	wP4moves = set()
	wP5moves = set()
	wP6moves = set()
	wP7moves = set()
	wP8moves = set()

	wN1moves = set()
	wN2moves = set()
	wB1moves = set()
	wB2moves = set()
	wR1moves = set()
	wR2moves = set()
	wQmoves = set()
	wKmoves = set()

	bP1moves = set()
	bP2moves = set()
	bP3moves = set()
	bP4moves = set()
	bP5moves = set()
	bP6moves = set()
	bP7moves = set()
	bP8moves = set()

	bN1moves = set()
	bN2moves = set()
	bB1moves = set()
	bB2moves = set()
	bR1moves = set()
	bR2moves = set()
	bQmoves = set()
	bKmoves = set()

	array = []

	# 0-31 the existense of pieces (0-15 white pieces, 16-31 black pieces)
	# 


	pieces = set(position[0] + position[1] + position[2] + position[3] + position[4] + position[5] + position[6] + position[7])

	if 'wQ' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wR1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wR2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wB1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wB2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wN1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wN2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wP1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'wP2' in pieces:
		array.append(1)
	else:
		array.append(0)		
	if 'wP3' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP4' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP5' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP6' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP7' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'wP8' in pieces:
		array.append(1)
	else:
		array.append(0)	

	if 'bQ' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bR1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bR2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bB1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bB2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bN1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bN2' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP1' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP2' in pieces:
		array.append(1)
	else:
		array.append(0)		
	if 'bP3' in pieces:
		array.append(1)
	else:
		array.append(0)
	if 'bP4' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP5' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP6' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP7' in pieces:
		array.append(1)
	else:
		array.append(0)	
	if 'bP8' in pieces:
		array.append(1)
	else:
		array.append(0)	

	wPstructure = []
	bPstructure = []

	#piecePositions

	wP1pos = (-1,-1)
	wP2pos = (-1,-1)
	wP3pos = (-1,-1)
	wP4pos = (-1,-1)
	wP5pos = (-1,-1)
	wP6pos = (-1,-1)
	wP7pos = (-1,-1)
	wP8pos = (-1,-1)
	wR1pos = (-1,-1)
	wR2pos = (-1,-1)
	wN1pos = (-1,-1)
	wN2pos = (-1,-1)
	wB1pos = (-1,-1)
	wB2pos = (-1,-1)
	wQpos = (-1,-1)
	wKpos = (-1,-1)


	bP1pos = (-1,-1)
	bP2pos = (-1,-1)
	bP3pos = (-1,-1)
	bP4pos = (-1,-1)
	bP5pos = (-1,-1)
	bP6pos = (-1,-1)
	bP7pos = (-1,-1)
	bP8pos = (-1,-1)
	bR1pos = (-1,-1)
	bR2pos = (-1,-1)
	bN1pos = (-1,-1)
	bN2pos = (-1,-1)
	bB1pos = (-1,-1)
	bB2pos = (-1,-1)
	bQpos = (-1,-1)
	bKpos = (-1,-1)



	for i in range(8):
		for j in range(8):
			x = 1
			y = 1
			f = (position[i])[j]
			if (f == 'wP1'):
				wP1pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP1moves.add((i+1,j+1))
				if (j > 0):
					wP1moves.add((i+1,j-1))
			elif (f == 'wP2'):
				wP2pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP2moves.add((i+1,j+1))
				if (j > 0):
					wP2moves.add((i+1,j-1))
			elif (f == 'wP3'):
				wP3pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP3moves.add((i+1,j+1))
				if (j > 0):
					wP3moves.add((i+1,j-1))
			elif (f == 'wP4'):
				wP4pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP4moves.add((i+1,j+1))
				if (j > 0):
					wP4moves.add((i+1,j-1))
			elif (f == 'wP5'):
				wP5pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP5moves.add((i+1,j+1))
				if (j > 0):
					wP5moves.add((i+1,j-1))
			elif (f == 'wP6'):
				wP6pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP6moves.add((i+1,j+1))
				if (j > 0):
					wP6moves.add((i+1,j-1))
			elif (f == 'wP7'):
				wP7pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP7moves.add((i+1,j+1))
				if (j > 0):
					wP7moves.add((i+1,j-1))
			elif (f == 'wP8'):
				wP8pos = (i,j)
				wPstructure.append(j)
				if (j < 7):
					wP8moves.add((i+1,j+1))
				if (j > 0):
					wP8moves.add((i+1,j-1))
			elif (f == 'wN1'):
				wN1pos = (i,j)
				if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'white'):
					wN1moves.add((i+2,j+1))
				if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'white'):
					wN1moves.add((i+2,j-1))
				if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'white'):
					wN1moves.add((i-2,j+1))
				if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'white'):
					wN1moves.add((i-2,j-1))
				if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'white'):
					wN1moves.add((i+1,j+2))
				if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'white'):
					wN1moves.add((i+1,j-2))
				if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'white'):
					wN1moves.add((i-1,j+2))
				if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'white'):
					wN1moves.add((i-1,j-2))	
			elif (f == 'wN2'):
				wN2pos = (i,j)
				if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'white'):
					wN2moves.add((i+2,j+1))
				if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'white'):
					wN2moves.add((i+2,j-1))
				if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'white'):
					wN2moves.add((i-2,j+1))
				if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'white'):
					wN2moves.add((i-2,j-1))
				if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'white'):
					wN2moves.add((i+1,j+2))
				if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'white'):
					wN2moves.add((i+1,j-2))
				if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'white'):
					wN2moves.add((i-1,j+2))
				if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'white'):
					wN2moves.add((i-1,j-2))	
			elif (f == 'wB1'):
				wB1pos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wB1moves.add((i+x,j+y))
					else:
						wB1moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wB1moves.add((i-x,j+y))
					else:
						wB1moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wB1moves.add((i+x,j-y))
					else:
						wB1moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wB1moves.add((i-x,j-y))
					else:
						wB1moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1	
			elif (f == 'wB2'):
				wB2pos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wB2moves.add((i+x,j+y))
					else:
						wB2moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wB2moves.add((i-x,j+y))
					else:
						wB2moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wB2moves.add((i+x,j-y))
					else:
						wB2moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wB2moves.add((i-x,j-y))
					else:
						wB2moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1		
			elif (f == 'wR1'):
				wR1pos = (i,j)
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wR1moves.add((i+x,j))
					else:
						wR1moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wR1moves.add((i-x,j))
					else:
						wR1moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wR1moves.add((i,j-x))
					else:
						wR1moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wR1moves.add((i,j+x))
					else:
						wR1moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wR2'):
				wR2pos = (i,j)
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wR2moves.add((i+x,j))
					else:
						wR2moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wR2moves.add((i-x,j))
					else:
						wR2moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wR2moves.add((i,j-x))
					else:
						wR2moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wR2moves.add((i,j+x))
					else:
						wR2moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wQ'):
				wQpos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						wQmoves.add((i+x,j+y))
					else:
						wQmoves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						wQmoves.add((i-x,j+y))
					else:
						wQmoves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						wQmoves.add((i+x,j-y))
					else:
						wQmoves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						wQmoves.add((i-x,j-y))
					else:
						wQmoves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						wQmoves.add((i+x,j))
					else:
						wQmoves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						wQmoves.add((i-x,j))
					else:
						wQmoves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						wQmoves.add((i,j-x))
					else:
						wQmoves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						wQmoves.add((i,j+x))
					else:
						wQmoves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'wK'):
				wKpos = (i,j)
				if (j < 7) and (i < 7):
					wKmoves.add((i+1,j+1))
				if (j > 0) and (i < 7):
					wKmoves.add((i+1,j-1))
				if (j < 7) and (i > 0):
					wKmoves.add((i-1,j+1))
				if (j > 0) and (i > 0):
					wKmoves.add((i-1,j-1))
				if (i < 7):
					wKmoves.add((i+1,j))
				if (i > 0):
					wKmoves.add((i-1,j))
				if (j < 7):
					wKmoves.add((i,j+1))
				if (j > 0):
					wKmoves.add((i,j-1))
			elif (f == 'bP1'):
				bP1pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP1moves.add((i-1,j+1))
				if (j > 0):
					bP1moves.add((i-1,j-1))
			elif (f == 'bP2'):
				bP2pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP2moves.add((i-1,j+1))
				if (j > 0):
					bP2moves.add((i-1,j-1))
			elif (f == 'bP3'):
				bP3pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP3moves.add((i-1,j+1))
				if (j > 0):
					bP3moves.add((i-1,j-1))
			elif (f == 'bP4'):
				bP4pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP4moves.add((i-1,j+1))
				if (j > 0):
					bP4moves.add((i-1,j-1))
			elif (f == 'bP5'):
				bP5pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP5moves.add((i-1,j+1))
				if (j > 0):
					bP5moves.add((i-1,j-1))
			elif (f == 'bP6'):
				bP6pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP6moves.add((i-1,j+1))
				if (j > 0):
					bP6moves.add((i-1,j-1))
			elif (f == 'bP7'):
				bP7pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP7moves.add((i-1,j+1))
				if (j > 0):
					bP7moves.add((i-1,j-1))
			elif (f == 'bP8'):
				bP8pos = (i,j)
				bPstructure.append(j)
				if (j < 7):
					bP8moves.add((i-1,j+1))
				if (j > 0):
					bP8moves.add((i-1,j-1))
			elif (f == 'bN1'):
				bN1pos = (i,j)
				if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'black'):
					bN1moves.add((i+2,j+1))
				if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'black'):
					bN1moves.add((i+2,j-1))
				if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'black'):
					bN1moves.add((i-2,j+1))
				if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'black'):
					bN1moves.add((i-2,j-1))
				if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'black'):
					bN1moves.add((i+1,j+2))
				if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'black'):
					bN1moves.add((i+1,j-2))
				if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'black'):
					bN1moves.add((i-1,j+2))
				if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'black'):
					bN1moves.add((i-1,j-2))	
			elif (f == 'bN2'):
				bN2pos = (i,j)
				if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'black'):
					bN2moves.add((i+2,j+1))
				if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'black'):
					bN2moves.add((i+2,j-1))
				if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'black'):
					bN2moves.add((i-2,j+1))
				if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'black'):
					bN2moves.add((i-2,j-1))
				if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'black'):
					bN2moves.add((i+1,j+2))
				if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'black'):
					bN2moves.add((i+1,j-2))
				if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'black'):
					bN2moves.add((i-1,j+2))
				if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'black'):
					bN2moves.add((i-1,j-2))	
			elif (f == 'bB1'):
				bB1pos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bB1moves.add((i+x,j+y))
					else:
						bB1moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bB1moves.add((i-x,j+y))
					else:
						bB1moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bB1moves.add((i+x,j-y))
					else:
						bB1moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bB1moves.add((i-x,j-y))
					else:
						bB1moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1	
			elif (f == 'bB2'):
				bB2pos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bB2moves.add((i+x,j+y))
					else:
						bB2moves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bB2moves.add((i-x,j+y))
					else:
						bB2moves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bB2moves.add((i+x,j-y))
					else:
						bB2moves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bB2moves.add((i-x,j-y))
					else:
						bB2moves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1		
			elif (f == 'bR1'):
				bR1pos = (i,j)
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bR1moves.add((i+x,j))
					else:
						bR1moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bR1moves.add((i-x,j))
					else:
						bR1moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bR1moves.add((i,j-x))
					else:
						bR1moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bR1moves.add((i,j+x))
					else:
						bR1moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bR2'):
				bR2pos = (i,j)
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bR2moves.add((i+x,j))
					else:
						bR2moves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bR2moves.add((i-x,j))
					else:
						bR2moves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bR2moves.add((i,j-x))
					else:
						bR2moves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bR2moves.add((i,j+x))
					else:
						bR2moves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bQ'):
				bQpos = (i,j)
				while (i+x < 8) and (j+y < 8): 
					if ((position[i+x])[j+y] == 'e'):
						bQmoves.add((i+x,j+y))
					else:
						bQmoves.add((i+x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j+y < 8): 
					if ((position[i-x])[j+y] == 'e'):
						bQmoves.add((i-x,j+y))
					else:
						bQmoves.add((i-x,j+y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8) and (j-y >= 0): 
					if ((position[i+x])[j-y] == 'e'):
						bQmoves.add((i+x,j-y))
					else:
						bQmoves.add((i+x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i-x >= 0) and (j-y >= 0): 
					if ((position[i-x])[j-y] == 'e'):
						bQmoves.add((i-x,j-y))
					else:
						bQmoves.add((i-x,j-y))
						break
					x = x + 1
					y = y + 1
				x = 1 
				y = 1
				while (i+x < 8): 
					if ((position[i+x])[j] == 'e'):
						bQmoves.add((i+x,j))
					else:
						bQmoves.add((i+x,j))
						break
					x = x + 1
				x = 1 
				while (i-x >= 0): 
					if ((position[i-x])[j] == 'e'):
						bQmoves.add((i-x,j))
					else:
						bQmoves.add((i-x,j))
						break
					x = x + 1
				x = 1 
				while (j-x >= 0): 
					if ((position[i])[j-x] == 'e'):
						bQmoves.add((i,j-x))
					else:
						bQmoves.add((i,j-x))
						break
					x = x + 1
				x = 1 
				while (j+x < 8): 
					if ((position[i])[j+x] == 'e'):
						bQmoves.add((i,j+x))
					else:
						bQmoves.add((i,j+x))
						break
					x = x + 1
				x = 1 
			elif (f == 'bK'):
				bKpos = (i,j)
				if (j < 7) and (i < 7):
					bKmoves.add((i+1,j+1))
				if (j > 0) and (i < 7):
					bKmoves.add((i+1,j-1))
				if (j < 7) and (i > 0):
					bKmoves.add((i-1,j+1))
				if (j > 0) and (i > 0):
					bKmoves.add((i-1,j-1))
				if (i < 7):
					bKmoves.add((i+1,j))
				if (i > 0):
					bKmoves.add((i-1,j))
				if (j < 7):
					bKmoves.add((i,j+1))
				if (j > 0):
					bKmoves.add((i,j-1))





	#wN1mobility 
	array.append(len(wN1moves)/8)
	#wN2mobility
	array.append(len(wN2moves)/8)
	#wB1mobility
	array.append(len(wB1moves)/15)
	#wB2mobility 
	array.append(len(wB2moves)/15)
	#wR1mobility
	array.append(len(wR1moves)/16)
	#wR2mobility 
	array.append(len(wR2moves)/16)

	#bN1mobility 
	array.append(len(bN1moves)/8)
	#bN2mobility 
	array.append(len(bN2moves)/8)
	#bB1mobility 
	array.append(len(bB1moves)/15)
	#bB2mobility 
	array.append(len(bB2moves)/15)
	#bR1mobility
	array.append(len(bR1moves)/16)
	#bR2mobility 
	array.append(len(bR2moves)/16)

	#Pawn structure
	doublewhitePawns = len(wPstructure) - len(set(wPstructure))
	doubleblackPawns = len(bPstructure) - len(set(bPstructure))

	array.append(doublewhitePawns)
	array.append(doubleblackPawns)
	
	wPcentered = 0
	bPcentered = 0

	if (wP1pos in centre):
		wPcentered += 1
	if (wP2pos in centre):
		wPcentered += 1
	if (wP3pos in centre):
		wPcentered += 1
	if (wP4pos in centre):
		wPcentered += 1
	if (wP5pos in centre):
		wPcentered += 1
	if (wP6pos in centre):
		wPcentered += 1
	if (wP7pos in centre):
		wPcentered += 1
	if (wP8pos in centre):
		wPcentered += 1
	if (bP1pos in centre):
		bPcentered += 1
	if (bP2pos in centre):
		bPcentered += 1
	if (bP3pos in centre):
		bPcentered += 1
	if (bP4pos in centre):
		bPcentered += 1
	if (bP5pos in centre):
		bPcentered += 1
	if (bP6pos in centre):
		bPcentered += 1
	if (bP7pos in centre):
		bPcentered += 1
	if (bP8pos in centre):
		bPcentered += 1

	array.append(wPcentered)
	array.append(bPcentered)


	wNcentered = 0
	bNcentered = 0

	if (wN1pos in centre):
		wNcentered += 1
	if (wN2pos in centre):
		wNcentered += 1

	if (bN1pos in centre):
		bNcentered += 1
	if (bN2pos in centre):
		bNcentered += 1

	array.append(wNcentered)
	array.append(bNcentered)






	output = array 

	return(output)




def networkPosEstimation(position,synaptic_weights,moverecord):
	return(sigmoid(np.dot(positionvector(position), synaptic_weights)))

def NetworkELOcomparison(positions,synaptic_weights,moverecord):
	i = 0
	m = []
	while i < len(positions):
		m = m + [networkPosEstimation(positions[i],synaptic_weights,moverecord)]
		i = i + 1
	return(m)





def whitebestpositions(position,synaptic_weights,moverecord):
	positions = whitepossiblePositions(position,moverecord)
	estimation = NetworkELOcomparison(positions,synaptic_weights,moverecord)
	poss = []
	bestnumber = 20
	if bestnumber < len(positions):
		for i in range(bestnumber):
			m = maxnumber(estimation)
			m = random.choice(m)
			poss.append(positions[m])
			estimation = estimation[0:m] + estimation[m+1:len(estimation)]
	else:
		poss = positions
	return(poss)

def blackbestpositions(position,synaptic_weights,moverecord):
	positions = blackpossiblePositions(position,moverecord)
	estimation = NetworkELOcomparison(positions,synaptic_weights,moverecord)
	poss = []
	bestnumber = 20
	if bestnumber < len(positions):
		for i in range(bestnumber):
			m = minnumber(estimation)
			m = random.choice(m)
			poss.append(positions[m])
			estimation = estimation[0:m] + estimation[m+1:len(estimation)]
	else:
		poss = positions
	return(poss)







def blackprunning1(position,synaptic_weights,moverecord):
	poss = whitepossiblePositions(position,moverecord) 
	alpha = 1
	i = 0
	for i in range(len(poss)):
		betterposition = True
		blackrespond = blackpossiblePositions(poss[i],moverecord)
		for j in range(len(blackrespond)):
			if (networkPosEstimation(blackrespond[j],synaptic_weights,moverecord) < alpha):
				betterposition = False
				break
		if betterposition:
			alpha = minvalue(NetworkELOcomparison(blackrespond,synaptic_weights,moverecord))
	return(alpha)


def whitealphabetaprunning(position,synaptic_weights,moverecord):
	poss = whitepossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		alpha = 0
		i = 0
		for i in range(len(poss)):
			betterposition = True
			blackrespond = blackpossiblePositions(poss[i],moverecord)
			for j in range(len(blackrespond)):
				if (networkPosEstimation(blackrespond[j],synaptic_weights,moverecord) <= alpha):
					betterposition = False
					break
			if betterposition:
				alpha = minvalue(NetworkELOcomparison(blackrespond,synaptic_weights,moverecord))
				h = i
		return(poss[h]) 


def whitealphabetaprunning1(position,synaptic_weights,moverecord):
	poss = whitepossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		beta = 0
		i = 0
		for i in range(len(poss)):
			alpha = 1
			betterposition2 = True
			blackrespond = blackpossiblePositions(poss[i],moverecord)
			for j in range(len(blackrespond)):
				betterposition = True
				whiterespond = whitepossiblePositions(blackrespond[j],moverecord)
				for k in range(len(whiterespond)):
					if (networkPosEstimation(whiterespond[k],synaptic_weights,moverecord) >= alpha):
						betterposition = False
						break
				if betterposition:
					alpha = maxvalue(NetworkELOcomparison(whiterespond,synaptic_weights,moverecord))

				if alpha <= beta:
					betterposition2 = False
					break

			if betterposition2:
				beta = alpha
				h = i

		return(poss[h]) 


def whitealphabetaprunning2(position,synaptic_weights,moverecord):
	poss = whitepossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		gamma = 0
		i = 0
		for i in range(len(poss)):
			beta = 1
			betterposition2 = True
			blackrespond = blackpossiblePositions(poss[i],moverecord)
			for j in range(len(blackrespond)):
				alpha = 0
				betterposition1 = True
				whiterespond = whitepossiblePositions(blackrespond[j],moverecord)
				for k in range(len(whiterespond)):
					betterposition = True
					blackrespond2 = blackpossiblePositions(whiterespond[k],moverecord)
					for z in range(len(blackrespond2)):
						if (networkPosEstimation(blackrespond2[z],synaptic_weights,moverecord) <= alpha):
							betterposition = False
							break
					if betterposition:
						alpha = minvalue(NetworkELOcomparison(blackrespond,synaptic_weights,moverecord))

					if alpha >= beta:
						betterposition1 = False
						break

				if betterposition1:
					beta = alpha
				
				if beta <= gamma:
					betterposition2 = False
					break				

			if betterposition2:
				gamma = beta
				h = i

		return(poss[h]) 

def alphabetaprunningRec(position,synaptic_weights,moverecord,depth,whiteToMove):
	if (depth == 0):
		return (networkPosEstimation(position,synaptic_weights,moverecord))
	elif (depth == 1):
		if whiteToMove:
			poss = whitepossiblePositions(position,moverecord)
			alpha = np.array([0])
			for i in range(len(poss)):
				m = networkPosEstimation(poss[i],synaptic_weights,moverecord)
				if (m >= alpha):
					alpha = m
			return (alpha)
		else:
			poss = blackpossiblePositions(position,moverecord)
			alpha = np.array([1])
			for i in range(len(poss)):
				m = networkPosEstimation(poss[i],synaptic_weights,moverecord)
				if (m <= alpha):
					alpha = m
			return (alpha)
	else:
		n = 0
		start_time = time.time()
		if whiteToMove:
			alpha = 0
			poss = whitepossiblePositions(position,moverecord)
			h = [['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']]
		else:
			alpha = 1
			poss = blackpossiblePositions(position,moverecord)
			h = [['wR1', 'wN1', 'wB1', 'wQ', 'wK', 'wB2', 'wN2', 'wR2'], ['wP1', 'wP2', 'wP3', 'wP4', 'e', 'wP6', 'wP7', 'wP8'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'wP5', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'bK', 'e', 'e', 'e']]
		for i in range(len(poss)):
			#if (depth == 3):
			#	print(round(100*i/len(poss)))
			betterposition = True
			if whiteToMove:
				blackrespond = blackpossiblePositions(poss[i],moverecord)
				for j in range(len(blackrespond)):
					n = n + 1
					if (alphabetaprunningRec(blackrespond[j],synaptic_weights,moverecord,depth-2, whiteToMove)[0] <= alpha):
						betterposition = False
						break
		
				if betterposition:
					alpha = alphabetaprunningRec(poss[i],synaptic_weights,moverecord,depth-1, not whiteToMove)[0]
					h = poss[i]
			else:
				whiterespond = whitepossiblePositions(poss[i],moverecord)
				for j in range(len(whiterespond)):
					n = n + 1
					if (alphabetaprunningRec(whiterespond[j],synaptic_weights,moverecord,depth-2, whiteToMove)[0] >= alpha):
						betterposition = False
						break
		
				if betterposition:
					alpha = alphabetaprunningRec(poss[i],synaptic_weights,moverecord,depth-1, not whiteToMove)[0]
					h = poss[i]
		#print(n)
		if (depth == 3):
			print ("Time", time.time() - start_time)
		return(alpha,h) 





def blackalphabetaprunning(position,synaptic_weights,moverecord):
	poss = blackpossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		alpha = 1
		i = 0
		for i in range(len(poss)):
			betterposition = True
			whiterespond = whitepossiblePositions(poss[i],moverecord)
			for j in range(len(whiterespond)):
				if (networkPosEstimation(whiterespond[j],synaptic_weights,moverecord) >= alpha):
					betterposition = False
					break
			if betterposition:
				alpha = maxvalue(NetworkELOcomparison(whiterespond,synaptic_weights,moverecord))
				h = i
		return(poss[h])


def blackalphabetaprunning1(position,synaptic_weights,moverecord):
	poss = blackpossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		h = 0
		beta = 1
		i = 0
		for i in range(len(poss)):
			alpha = 0
			betterposition2 = True
			whiterespond = whitepossiblePositions(poss[i],moverecord)
			for j in range(len(whiterespond)):
				betterposition = True
				blackrespond = blackpossiblePositions(whiterespond[j],moverecord)
				for k in range(len(blackrespond)):
					if (networkPosEstimation(blackrespond[k],synaptic_weights,moverecord) <= alpha):
						betterposition = False
						break
				if betterposition:
					alpha = minvalue(NetworkELOcomparison(blackrespond,synaptic_weights,moverecord))

				if alpha >= beta:
					betterposition2 = False
					break

			if betterposition2:
				beta = alpha
				h = i

		return(poss[h]) 

def blackalphabetaprunning2(position,synaptic_weights,moverecord):
	poss = blackpossiblePositions(position,moverecord) 
	if (poss == []):
		return([['e', 'e', 'e', 'e', 'wK', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8'], ['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2']])
	else:
		gamma = 1
		i = 0
		for i in range(len(poss)):
			beta = 0
			betterposition2 = True
			whiterespond = whitepossiblePositions(poss[i],moverecord)
			for j in range(len(whiterespond)):
				alpha = 1
				betterposition1 = True
				blackrespond = blackpossiblePositions(whiterespond[j],moverecord)
				for k in range(len(blackrespond)):
					betterposition = True
					whiterespond2 = whitepossiblePositions(blackrespond[k],moverecord)
					for z in range(len(whiterespond2)):
						if (networkPosEstimation(whiterespond2[z],synaptic_weights,moverecord) >= alpha):
							betterposition = False
							break
					if betterposition:
						alpha = maxvalue(NetworkELOcomparison(whiterespond,synaptic_weights,moverecord))

					if alpha <= beta:
						betterposition1 = False
						break

				if betterposition1:
					beta = alpha
				
				if beta >= gamma:
					betterposition2 = False
					break				

			if betterposition2:
				gamma = beta
				h = i

		return(poss[h]) 



def whitepositionchooser(position,synaptic_weights,moverecord):
	depth = 0
	poss = whitepossiblePositions(position,moverecord)
	num = len(poss)
	n = 0
	wrespond = poss
	i = 0 
	brespond = []
	for i in range(num):
		brespond = brespond + [blackalphabetaprunning(wrespond[i],synaptic_weights,moverecord)]
	
	u = maxnumber(NetworkELOcomparison(brespond,synaptic_weights,moverecord))
	u = random.choice(u)
	return(poss[u])

	

def blackpositionchooser(position,synaptic_weights,moverecord):
	depth = 0
	poss = blackpossiblePositions(position,moverecord)
	num = len(poss)
	n = 0
	brespond = poss
	i = 0 
	wrespond = []
	for i in range(num):
		wrespond = wrespond + [whitealphabetaprunning(brespond[i],synaptic_weights,moverecord)]

	u = minnumber(NetworkELOcomparison(wrespond,synaptic_weights,moverecord))
	u = random.choice(u)
	return(poss[u])

	


outF = open('datanumbers.py', 'w')

#synaptic weights
synaptic_weights = np.array([
[12], #white Queen value
[6], #white Rook value
[6],#white Rook value
[4],#white Bishop value
[4],#white Bishop value
[4],#white Knight value
[4],#white Knight value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[1],#white Pawn value
[-12], #black Queen value
[-6], #black Rook value
[-6],#black Rook value
[-4],#black Bishop value
[-4],#black Bishop value
[-4],#black Knight value
[-4],#black Knight value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[-1],#black Pawn value
[0.2], #white Knight1 mobility
[0.2], #white Knight2 mobility
[0.6], #white Bishop1 mobility
[0.6], #white Bishop2 mobility
[0.4], #white Rook1 mobility
[0.4], #white Rook2 mobility
[-0.2], #black Knight1 mobility
[-0.2], #black Knight2 mobility
[-0.6], #black Bishop1 mobility
[-0.6], #black Bishop2 mobility
[-0.4], #black Rook1 mobility
[-0.4], #black Rook2 mobility
[-0.1], #double white Pawns
[0.1], #double black Pawns
[0.1], #white Pawns centered
[-0.1], #black Pawns centered
[0.2], #white Knights centered
[-0.2], #black Knights centered

 ])




#Starting position
whitePlayer = True
blackPlayer = False

position = [['wR1','wN1','wB1','wQ','wK','wB2','wN2','wR2'],
	['wP1','wP2','wP3','wP4','wP5','wP6','wP7','wP8'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['bP1','bP2','bP3','bP4','bP5','bP6','bP7','bP8'],
	['bR1','bN1','bB1','bQ','bK','bB2','bN2','bR2']]

training_inputs = np.array([positionvector(position)])

while True:
	
	whitePawn1.undraw()
	whitePawn2.undraw()
	whitePawn3.undraw()
	whitePawn4.undraw()
	whitePawn5.undraw()
	whitePawn6.undraw()
	whitePawn7.undraw()
	whitePawn8.undraw()
	whiteKnight1.undraw()
	whiteKnight2.undraw()
	whiteBishop1.undraw()
	whiteBishop2.undraw()
	whiteRook1.undraw()
	whiteRook2.undraw()
	whiteQueen.undraw()
	whiteKing.undraw()
	blackPawn1.undraw()
	blackPawn2.undraw()
	blackPawn3.undraw()
	blackPawn4.undraw()
	blackPawn5.undraw()
	blackPawn6.undraw()
	blackPawn7.undraw()
	blackPawn8.undraw()
	blackRook1.undraw()
	blackRook2.undraw()
	blackKnight1.undraw()
	blackKnight2.undraw()
	blackBishop1.undraw()
	blackBishop2.undraw()
	blackQueen.undraw()
	blackKing.undraw()

	whitePawn1 = Image(Point(69,552), 'whitePawn.png')
	whitePawn1.draw(win)
	whitePawn2 = Image(Point(149,552), 'whitePawn.png')
	whitePawn2.draw(win)
	whitePawn3 = Image(Point(229,552), 'whitePawn.png')
	whitePawn3.draw(win)
	whitePawn4 = Image(Point(309,552), 'whitePawn.png')
	whitePawn4.draw(win)
	whitePawn5 = Image(Point(389,552), 'whitePawn.png')
	whitePawn5.draw(win)
	whitePawn6 = Image(Point(469,552), 'whitePawn.png')
	whitePawn6.draw(win)
	whitePawn7 = Image(Point(549,552), 'whitePawn.png')
	whitePawn7.draw(win)
	whitePawn8 = Image(Point(629,552), 'whitePawn.png')
	whitePawn8.draw(win)
	 #Knights
	whiteKnight1 = Image(Point(153,633), 'whiteKnight.png')
	whiteKnight1.draw(win)
	whiteKnight2 = Image(Point(553,633), 'whiteKnight.png')
	whiteKnight2.draw(win)
	 #Bishops
	whiteBishop1 = Image(Point(230,633), 'whiteBishop.png')
	whiteBishop1.draw(win)
	whiteBishop2 = Image(Point(470,633), 'whiteBishop.png')
	whiteBishop2.draw(win)
	 #Rooks
	whiteRook1 = Image(Point(70,630), 'whiteRook.png')
	whiteRook1.draw(win)
	whiteRook2 = Image(Point(630,630), 'whiteRook.png')
	whiteRook2.draw(win)
	 #Queen
	whiteQueen = Image(Point(310,630), 'whiteQueen.png')
	whiteQueen.draw(win)
	 #King
	whiteKing = Image(Point(390,636), 'whiteKing.png')
	whiteKing.draw(win)
	#black starting position
	 #pawns
	blackPawn1 = Image(Point(70,152), 'blackPawn.png')
	blackPawn1.draw(win)
	blackPawn2 = Image(Point(150,152), 'blackPawn.png')
	blackPawn2.draw(win)
	blackPawn3 = Image(Point(230,152), 'blackPawn.png')
	blackPawn3.draw(win)
	blackPawn4 = Image(Point(310,152), 'blackPawn.png')
	blackPawn4.draw(win)
	blackPawn5 = Image(Point(390,152), 'blackPawn.png')
	blackPawn5.draw(win)
	blackPawn6 = Image(Point(470,152), 'blackPawn.png')
	blackPawn6.draw(win)
	blackPawn7 = Image(Point(550,152), 'blackPawn.png')
	blackPawn7.draw(win)
	blackPawn8 = Image(Point(630,152), 'blackPawn.png')
	blackPawn8.draw(win)
	 #Rooks
	blackRook1 = Image(Point(72,73), 'blackRook.png')
	blackRook1.draw(win)
	blackRook2 = Image(Point(632,73), 'blackRook.png')
	blackRook2.draw(win)
	 #Knights
	blackKnight1 = Image(Point(150,72), 'blackKnight.png')
	blackKnight1.draw(win)
	blackKnight2 = Image(Point(550,72), 'blackKnight.png')
	blackKnight2.draw(win)
	 #Bishops
	blackBishop1 = Image(Point(231,72), 'blackBishop.png')
	blackBishop1.draw(win)
	blackBishop2 = Image(Point(471,72), 'blackBishop.png')
	blackBishop2.draw(win)
	 #Queen
	blackQueen = Image(Point(310,70), 'blackQueen.png')
	blackQueen.draw(win)
	 #King
	blackKing = Image(Point(389,72), 'blackKing.png')
	blackKing.draw(win)


	position = [['wR1','wN1','wB1','wQ','wK','wB2','wN2','wR2'],
	['wP1','wP2','wP3','wP4','wP5','wP6','wP7','wP8'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['e','e','e','e','e','e','e','e'],
	['bP1','bP2','bP3','bP4','bP5','bP6','bP7','bP8'],
	['bR1','bN1','bB1','bQ','bK','bB2','bN2','bR2']]



	position1 = position
	moverecord = []
	movenumber = 1
	positionrecord = [position]
	training_inputs = np.array([positionvector(position)])
	while True:
		dots = []
		newpiece = True
		enpassant1 = False
		enpassant2 = False
		shortcastles = False
		longcastles = False
		promotion = False
		#White move
		if whitePlayer:
			#White player move
			if (len(whitepossiblePositions(position,moverecord)) == 0) and (not whiteCheck(position)):
				stalemate()
				break
			if whiteCheck(position) and (len(whitepossiblePositions(position,moverecord)) == 0):
				print ('Checkmate')
				bcheckmate()
				break
			if threefold(positionrecord):
				threefoldrepetition()
				break
			while (position1 == position):           
				bAttacked = blackAttack(position1)   
				moves = []                    
				while (len(moves) == 0):
					x = 1
					y = 1
					if newpiece:
						p = win.getMouse()
					else:
						p = p1
					j = columnNumber(p)
					i = rowNumber (p)
					f = piece(i,j,position)
				#White pawns possible moves
					if (f == 'wP1') or (f == 'wP2') or (f == 'wP3') or (f == 'wP4') or (f == 'wP5') or (f == 'wP6') or (f == 'wP7') or (f == 'wP8'):
						if (i == 1) and ((position[2])[j] == 'e') and ((position[3])[j] == 'e'):
							dots = dots + [possibleMove(i+1,j)]
							dots = dots + [possibleMove(i+2,j)]
							moves = moves + [[i+1,j],[i+2,j]]
						elif (i < 7) and ((position[i+1])[j] == 'e'):
							dots = dots + [possibleMove(i+1,j)]
							moves = moves + [[i+1,j]]
						if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) == 'black'):
							dots = dots + [possibleMove(i+1,j+1)]
							moves = moves + [[i+1,j+1]]
						if (i < 7) and (j > 0) and (colour((position[i+1])[j-1]) == 'black'):
							dots = dots + [possibleMove(i+1,j-1)]
							moves = moves + [[i+1,j-1]]
						if (i == 4) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
							dots = dots + [possibleMove(i+1,j-1)]
							moves = moves + [[i+1,j-1]]
							enpassant1 = True
						if (i == 4) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '6') and ((moverecord[len(moverecord)-1])[2] == '4') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
							dots = dots + [possibleMove(i+1,j+1)]
							moves = moves + [[i+1,j+1]]
							enpassant2 = True
						if (i == 6) and (((position[i+1])[j] == 'e') or (colour((position[i+1])[j-1]) == 'black') or (colour((position[i+1])[j+1]) == 'black')):
							promotion = True
				#White Knights possible moves
					if (f != 'e') and (f[0:2] == 'wN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'white'):
							dots = dots + [possibleMove(i+2,j+1)]
							moves = moves + [[i+2,j+1]]
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'white'):
							dots = dots + [possibleMove(i+2,j-1)]
							moves = moves + [[i+2,j-1]]
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'white'):
							dots = dots + [possibleMove(i-2,j+1)]
							moves = moves + [[i-2,j+1]]
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'white'):
							dots = dots + [possibleMove(i-2,j-1)]
							moves = moves + [[i-2,j-1]]
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'white'):
							dots = dots + [possibleMove(i+1,j+2)]
							moves = moves + [[i+1,j+2]]
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'white'):
							dots = dots + [possibleMove(i+1,j-2)]
							moves = moves + [[i+1,j-2]]
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'white'):
							dots = dots + [possibleMove(i-1,j+2)]
							moves = moves + [[i-1,j+2]]
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'white'):
							dots = dots + [possibleMove(i-1,j-2)]
							moves = moves + [[i-1,j-2]]	 
				#White Bishops possible moves
					if (f != 'e') and (f[0:2] == 'wB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
							if (colour((position[i+x])[j+y]) == 'black'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
							if (colour((position[i-x])[j+y]) == 'black'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
							if (colour((position[i+x])[j-y]) == 'black'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
							if (colour((position[i-x])[j-y]) == 'black'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				#White Rooks possible moves
					if (f != 'e') and (f[0:2] == 'wR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
							if (colour((position[i+x])[j]) == 'black'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
							if (colour((position[i-x])[j]) == 'black'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
							if (colour((position[i])[j-x]) == 'black'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
							if (colour((position[i])[j+x]) == 'black'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
				#White Queen possible moves
					if (f != 'e') and (f[0:2] == 'wQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
							if (colour((position[i+x])[j+y]) == 'black'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
								break
							if (colour((position[i+x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
							if (colour((position[i-x])[j+y]) == 'black'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
								break
							if (colour((position[i-x])[j+y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
							if (colour((position[i+x])[j-y]) == 'black'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
								break
							if (colour((position[i+x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
							if (colour((position[i-x])[j-y]) == 'black'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
								break
							if (colour((position[i-x])[j-y]) == 'white'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
							if (colour((position[i+x])[j]) == 'black'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
								break
							if (colour((position[i+x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
							if (colour((position[i-x])[j]) == 'black'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
								break
							if (colour((position[i-x])[j]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
							if (colour((position[i])[j-x]) == 'black'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
								break
							if (colour((position[i])[j-x]) == 'white'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
							if (colour((position[i])[j+x]) == 'black'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
								break
							if (colour((position[i])[j+x]) == 'white'):
								break
							x = x + 1
						x = 1 
					newpiece = True
				#White King possible moves
					if (f == 'wK'):
						if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'white') and (not ((i+1,j+1) in bAttacked)):
							dots = dots + [possibleMove(i+1,j+1)]
							moves = moves + [[i+1,j+1]]
						if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'white') and (not ((i+1,j-1) in bAttacked)):
							dots = dots + [possibleMove(i+1,j-1)]
							moves = moves + [[i+1,j-1]]
						if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'white') and (not ((i-1,j+1) in bAttacked)):
							dots = dots + [possibleMove(i-1,j+1)]
							moves = moves + [[i-1,j+1]]
						if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'white') and (not ((i-1,j-1) in bAttacked)):
							dots = dots + [possibleMove(i-1,j-1)]
							moves = moves + [[i-1,j-1]]
						if (i < 7) and (colour((position[i+1])[j]) != 'white') and (not ((i+1,j) in bAttacked)):
							dots = dots + [possibleMove(i+1,j)]
							moves = moves + [[i+1,j]]
						if (i > 0) and (colour((position[i-1])[j]) != 'white') and (not ((i-1,j) in bAttacked)):
							dots = dots + [possibleMove(i-1,j)]
							moves = moves + [[i-1,j]]
						if (j < 7) and (colour((position[i])[j+1]) != 'white') and (not ((i,j+1) in bAttacked)):
							dots = dots + [possibleMove(i,j+1)]
							moves = moves + [[i,j+1]]
						if (j > 0) and (colour((position[i])[j-1]) != 'white') and (not ((i,j-1) in bAttacked)):
							dots = dots + [possibleMove(i,j-1)]
							moves = moves + [[i,j-1]]
						if ((position[0])[5] == 'e') and ((position[0])[6] == 'e') and ((position[0])[7] == 'wR2') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,5) in bAttacked) or ((0,6) in bAttacked)):
							dots = dots + [possibleMove(0,6)]
							moves = moves + [[0,6]]
							shortcastles = True
						if ((position[0])[3] == 'e') and ((position[0])[2] == 'e') and ((position[0])[1] == 'e') and ((position[0])[0] == 'wR1') and whiteKingMoves(moverecord) and not (((0,4) in bAttacked) or ((0,3) in bAttacked) or ((0,2) in bAttacked)):
							dots = dots + [possibleMove(0,2)]
							moves = moves + [[0,2]]
							longcastles = True
				p1 = win.getMouse()
				i1 = rowNumber (p1)
				j1 = columnNumber(p1)
				if (elem ([i1,j1],moves)) and (not (whiteKingFinder(swapping (position,i,j,i1,j1)) in blackAttack(swapping (position,i,j,i1,j1)))):
					cleardots (dots)
					if enpassant1 and (j1 == j-1):
						position = swapping (position,i,j-1,i+1,j-1)
					if enpassant2 and (j1 == j+1):
						position = swapping (position,i,j+1,i+1,j+1)
					if shortcastles and (j1 == 6):
						makeMove (position,0,7,0,5)
						position = swapping (position,0,7,0,5)
					if longcastles and (j1 == 2):
						makeMove (position,0,0,0,3)
						position = swapping (position,0,0,0,3)
					makeMove (position,i,j,i1,j1)
					taking (position,i,j,i1,j1)
					moverecord = moverecord + [moveslist(position,i,j,i1,j1)]
					movedrawer(moverecord,movenumber,shortcastles,longcastles)
					position1 = swapping (position,i,j,i1,j1)
				if promotion and (i1 == 7) and (not (whiteKingFinder(swapping (position,i,j,i1,j1)) in blackAttack(swapping (position,i,j,i1,j1)))):
					if (f == 'wP1'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn1.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn1 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn1 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn1 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn1 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn1.draw(win)
					if (f == 'wP2'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn2.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn2 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn2 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn2 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn2 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn2.draw(win)
					if (f == 'wP3'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn3.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn3 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn3 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn3 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn3 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn3.draw(win)
					if (f == 'wP4'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn4.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn4 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn4 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn4 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn4 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn4.draw(win)
					if (f == 'wP5'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn5.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn5 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn5 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn5 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn5 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn5.draw(win)
					if (f == 'wP6'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn6.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn6 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn6 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn6 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn6 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn6.draw(win)
					if (f == 'wP7'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn7.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn7 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn7 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn7 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn7 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn7.draw(win)
					if (f == 'wP8'):
						position1 = whitePromotionChosing(f,j1,position1)
						whitePawn8.undraw()
						if (((position1[i1])[j1])[0:2] == 'wQ'):
							whitePawn8 = Image(Point(70+80*j1,70), 'whiteQueen.png')
						if ((position1[i1])[j1])[0:2] == 'wR':
							whitePawn8 = Image(Point(70+80*j1,70), 'whiteRook.png')
						if ((position1[i1])[j1])[0:2] == 'wB':
							whitePawn8 = Image(Point(70+80*j1,73), 'whiteBishop.png')
						if ((position1[i1])[j1])[0:2] == 'wN':
							whitePawn8 = Image(Point(73+80*j1,73), 'whiteKnight.png')
						whitePawn8.draw(win)
				cleardots (dots)
				newpiece = False
				enpassant1 = False
				enpassant2 = False
				shortcastles = False
				longcastles = False
				promotion = False
			if sum(piecenumber(position)) != sum(piecenumber(position1)):
				positionrecord = []
			position = position1
			positionrecord = positionrecord + [position]
			positionarray = positionvector(position)
			outF.write(str(positionarray) + ',')
			outF.write('\n')

		else:
			if (len(whitepossiblePositions(position,moverecord)) == 0) and (not whiteCheck(position)):
				stalemate()
				whitewon = False
				blackwon = False
				break
			if whiteCheck(position) and (len(whitepossiblePositions(position,moverecord)) == 0):
				print ('Checkmate')
				bcheckmate()
				whitewon = False
				blackwon = True
				break
			if threefold(positionrecord):
				threefoldrepetition()
				whitewon = False
				blackwon = False
				break
			#poss = whitepossiblePositions(position,moverecord) 
			#respond = []
			#h = 0
			#for h in range(len(poss)):
			#	resp = blackpossiblePositions(poss[h],moverecord)
			#	respond = respond + [minvalue(NetworkELOcomparison(resp,synaptic_weights,moverecord))]
			#u = maxnumber(respond)
			#u = random.choice(u)
			
		
			#position2 = whitealphabetaprunning1(position,synaptic_weights,moverecord)
			position2 = alphabetaprunningRec(position,synaptic_weights,moverecord,3,True)[1]


			i = whitecomputerMove(position,position2)[0]
			j = whitecomputerMove(position,position2)[1]
			i1 = whitecomputerMove(position,position2)[2]
			j1 = whitecomputerMove(position,position2)[3]
			if whitecomputerMove(position,position2)[5] and (j1 == j-1): #enpassant1
				position = swapping (position,i,j-1,i+1,j-1)
			if whitecomputerMove(position,position2)[6] and (j1 == j+1): #enpassant2
				position = swapping (position,i,j+1,i+1,j+1)
			if whitecomputerMove(position,position2)[7]: #shortcastles
				makeMove (position,0,7,0,5)
				position = swapping (position,0,7,0,5)
			if whitecomputerMove(position,position2)[8]: #longcastles
				makeMove (position,0,0,0,3)
				position = swapping (position,0,0,0,3)
			makeMove (position,i,j,i1,j1)
			taking (position,i,j,i1,j1)
			moverecord = moverecord + [moveslist(position,i,j,i1,j1)]
			movedrawer(moverecord,movenumber,shortcastles,longcastles)
			if whitecomputerMove(position,position2)[4]:
				f = (position[i])[j]
				if (f == 'wP1'):
					whitePawn1.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn1 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn1 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn1 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn1 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn1.draw(win)
				if (f == 'wP2'):
					whitePawn2.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn2 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn2 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn2 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn2 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn2.draw(win)
				if (f == 'wP3'):
					whitePawn3.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn3 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn3 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn3 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn3 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn3.draw(win)
				if (f == 'wP4'):
					whitePawn4.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn4 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn4 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn4 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn4 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn4.draw(win)
				if (f == 'wP5'):
					whitePawn5.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn5 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn5 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn5 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn5 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn5.draw(win)
				if (f == 'wP6'):
					whitePawn6.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn6 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn6 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn6 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn6 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn6.draw(win)
				if (f == 'wP7'):
					whitePawn7.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn7 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn7 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn7 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn7 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn7.draw(win)
				if (f == 'wP8'):
					whitePawn8.undraw()
					if (((position2[i1])[j1])[0:2] == 'wQ'):
						whitePawn8 = Image(Point(70+80*j1,70), 'whiteQueen.png')
					if ((position2[i1])[j1])[0:2] == 'wR':
						whitePawn8 = Image(Point(70+80*j1,70), 'whiteRook.png')
					if ((position2[i1])[j1])[0:2] == 'wB':
						whitePawn8 = Image(Point(70+80*j1,73), 'whiteBishop.png')
					if ((position2[i1])[j1])[0:2] == 'wN':
						whitePawn8 = Image(Point(73+80*j1,73), 'whiteKnight.png')
					whitePawn8.draw(win)
			if sum(piecenumber(position)) != sum(piecenumber(position2)):
				positionrecord = []
			position = position2  
			position1 = position
			positionrecord = positionrecord + [position]
			if sum(piecenumber(position)) == sum(piecenumber(position2)):
				newarray = np.array([positionvector(position)]) 
				training_inputs = np.concatenate((training_inputs,newarray), axis = 0)


		if blackPlayer:
			#Black player move
			if (len(blackpossiblePositions(position,moverecord)) == 0) and (not blackCheck(position)):
				stalemate()
				break
			if blackCheck(position) and (len(blackpossiblePositions(position,moverecord)) == 0):
				print ('Checkmate')
				wcheckmate()
				break
			if threefold(positionrecord):
				threefoldrepetition()
				break
			if threefold(positionrecord):
				threefoldrepetition()
				break
			while (position1 == position):
				wAttacked = whiteAttack(position1)
				moves = []
				while (len(moves) == 0):
					x = 1
					y = 1
					if newpiece:
						p = win.getMouse()
					else:
						p = p1
					j = columnNumber(p)
					i = rowNumber (p)
					f = piece(i,j,position)
				#Black pawns possible moves 
					if (f == 'bP1') or (f == 'bP2') or (f == 'bP3') or (f == 'bP4') or (f == 'bP5') or (f == 'bP6') or (f == 'bP7') or (f == 'bP8'):
						if (i == 6) and ((position[5])[j] == 'e') and ((position[4])[j] == 'e'):
							dots = dots + [possibleMove(i-1,j)]
							dots = dots + [possibleMove(i-2,j)]
							moves = moves + [[i-1,j],[i-2,j]]
						elif (i > 0) and ((position[i-1])[j] == 'e'):
							dots = dots + [possibleMove(i-1,j)]
							moves = moves + [[i-1,j]]
						if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) == 'white'):
							dots = dots + [possibleMove(i-1,j+1)]
							moves = moves + [[i-1,j+1]]
						if (i > 0) and (j > 0) and (colour((position[i-1])[j-1]) == 'white'):
							dots = dots + [possibleMove(i-1,j-1)]
							moves = moves + [[i-1,j-1]]
						if (i == 3) and (j > 0) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j-1)):
							dots = dots + [possibleMove(i-1,j-1)]
							moves = moves + [[i-1,j-1]]
							enpassant1 = True
						if (i == 3) and (j < 7) and ((moverecord[len(moverecord)-1])[0] == '1') and ((moverecord[len(moverecord)-1])[2] == '3') and ((moverecord[len(moverecord)-1])[5] == 'P') and ((moverecord[len(moverecord)-1])[3] == str(j+1)):
							dots = dots + [possibleMove(i-1,j+1)]
							moves = moves + [[i-1,j+1]]
							enpassant2 = True
						if (i == 1) and (((position[i-1])[j] == 'e') or (colour((position[i-1])[j-1]) == 'white') or (colour((position[i-1])[j+1]) == 'white')):
							promotion = True
				#Black Knights possible moves
					if (f != 'e') and (f[0:2] == 'bN'):
						if (i < 6) and (j < 7) and (colour((position[i+2])[j+1]) != 'black'):
							dots = dots + [possibleMove(i+2,j+1)]
							moves = moves + [[i+2,j+1]]
						if (i < 6) and (j > 0) and (colour((position[i+2])[j-1]) != 'black'):
							dots = dots + [possibleMove(i+2,j-1)]
							moves = moves + [[i+2,j-1]]
						if (i > 1) and (j < 7) and (colour((position[i-2])[j+1]) != 'black'):
							dots = dots + [possibleMove(i-2,j+1)]
							moves = moves + [[i-2,j+1]]
						if (i > 1) and (j > 0) and (colour((position[i-2])[j-1]) != 'black'):
							dots = dots + [possibleMove(i-2,j-1)]
							moves = moves + [[i-2,j-1]]
						if (i < 7) and (j < 6) and (colour((position[i+1])[j+2]) != 'black'):
							dots = dots + [possibleMove(i+1,j+2)]
							moves = moves + [[i+1,j+2]]
						if (i < 7) and (j > 1) and (colour((position[i+1])[j-2]) != 'black'):
							dots = dots + [possibleMove(i+1,j-2)]
							moves = moves + [[i+1,j-2]]
						if (i > 0) and (j < 6) and (colour((position[i-1])[j+2]) != 'black'):
							dots = dots + [possibleMove(i-1,j+2)]
							moves = moves + [[i-1,j+2]]
						if (i > 0) and (j > 1) and (colour((position[i-1])[j-2]) != 'black'):
							dots = dots + [possibleMove(i-1,j-2)]
							moves = moves + [[i-1,j-2]]
				#Black Bishops possible moves
					if (f != 'e') and (f[0:2] == 'bB'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
							if (colour((position[i+x])[j+y]) == 'white'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
							if (colour((position[i-x])[j+y]) == 'white'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
							if (colour((position[i+x])[j-y]) == 'white'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
							if (colour((position[i-x])[j-y]) == 'white'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
				#Black Rooks possible moves
					if (f != 'e') and (f[0:2] == 'bR'):
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
							if (colour((position[i+x])[j]) == 'white'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
							if (colour((position[i-x])[j]) == 'white'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
							if (colour((position[i])[j-x]) == 'white'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
							if (colour((position[i])[j+x]) == 'white'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				#Black Queen possible moves
					if (f != 'e') and (f[0:2] == 'bQ'):
						while (i+x < 8) and (j+y < 8): 
							if ((position[i+x])[j+y] == 'e'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
							if (colour((position[i+x])[j+y]) == 'white'):
								dots = dots + [possibleMove(i+x,j+y)]
								moves = moves + [[i+x,j+y]]
								break
							if (colour((position[i+x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j+y < 8): 
							if ((position[i-x])[j+y] == 'e'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
							if (colour((position[i-x])[j+y]) == 'white'):
								dots = dots + [possibleMove(i-x,j+y)]
								moves = moves + [[i-x,j+y]]
								break
							if (colour((position[i-x])[j+y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8) and (j-y >= 0): 
							if ((position[i+x])[j-y] == 'e'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
							if (colour((position[i+x])[j-y]) == 'white'):
								dots = dots + [possibleMove(i+x,j-y)]
								moves = moves + [[i+x,j-y]]
								break
							if (colour((position[i+x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i-x >= 0) and (j-y >= 0): 
							if ((position[i-x])[j-y] == 'e'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
							if (colour((position[i-x])[j-y]) == 'white'):
								dots = dots + [possibleMove(i-x,j-y)]
								moves = moves + [[i-x,j-y]]
								break
							if (colour((position[i-x])[j-y]) == 'black'):
								break
							x = x + 1
							y = y + 1
						x = 1 
						y = 1
						while (i+x < 8): 
							if ((position[i+x])[j] == 'e'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
							if (colour((position[i+x])[j]) == 'white'):
								dots = dots + [possibleMove(i+x,j)]
								moves = moves + [[i+x,j]]
								break
							if (colour((position[i+x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (i-x >= 0): 
							if ((position[i-x])[j] == 'e'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
							if (colour((position[i-x])[j]) == 'white'):
								dots = dots + [possibleMove(i-x,j)]
								moves = moves + [[i-x,j]]
								break
							if (colour((position[i-x])[j]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j-x >= 0): 
							if ((position[i])[j-x] == 'e'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
							if (colour((position[i])[j-x]) == 'white'):
								dots = dots + [possibleMove(i,j-x)]
								moves = moves + [[i,j-x]]
								break
							if (colour((position[i])[j-x]) == 'black'):
								break
							x = x + 1
						x = 1 
						while (j+x < 8): 
							if ((position[i])[j+x] == 'e'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
							if (colour((position[i])[j+x]) == 'white'):
								dots = dots + [possibleMove(i,j+x)]
								moves = moves + [[i,j+x]]
								break
							if (colour((position[i])[j+x]) == 'black'):
								break
							x = x + 1
						x = 1 
				#Black King possible moves
					if (f == 'bK'):
						if (j < 7) and (i < 7) and (colour((position[i+1])[j+1]) != 'black') and (not ((i+1,j+1) in wAttacked)):
							dots = dots + [possibleMove(i+1,j+1)]
							moves = moves + [[i+1,j+1]]
						if (j > 0) and (i < 7) and (colour((position[i+1])[j-1]) != 'black') and (not ((i+1,j-1) in wAttacked)):
							dots = dots + [possibleMove(i+1,j-1)]
							moves = moves + [[i+1,j-1]]
						if (j < 7) and (i > 0) and (colour((position[i-1])[j+1]) != 'black') and (not ((i-1,j+1) in wAttacked)):
							dots = dots + [possibleMove(i-1,j+1)]
							moves = moves + [[i-1,j+1]]
						if (j > 0) and (i > 0) and (colour((position[i-1])[j-1]) != 'black') and (not ((i-1,j-1) in wAttacked)):
							dots = dots + [possibleMove(i-1,j-1)]
							moves = moves + [[i-1,j-1]]
						if (i < 7) and (colour((position[i+1])[j]) != 'black') and (not ((i+1,j) in wAttacked)):
							dots = dots + [possibleMove(i+1,j)]
							moves = moves + [[i+1,j]]
						if (i > 0) and (colour((position[i-1])[j]) != 'black') and (not ((i-1,j) in wAttacked)):
							dots = dots + [possibleMove(i-1,j)]
							moves = moves + [[i-1,j]]
						if (j < 7) and (colour((position[i])[j+1]) != 'black') and (not ((i,j+1) in wAttacked)):
							dots = dots + [possibleMove(i,j+1)]
							moves = moves + [[i,j+1]]
						if (j > 0) and (colour((position[i])[j-1]) != 'black') and (not ((i,j-1) in wAttacked)):
							dots = dots + [possibleMove(i,j-1)]
							moves = moves + [[i,j-1]]
						if ((position[7])[5] == 'e') and ((position[7])[6] == 'e') and ((position[7])[7] == 'bR2') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,5) in wAttacked) or ((7,6) in wAttacked)):
							dots = dots + [possibleMove(7,6)]
							moves = moves + [[7,6]]
							shortcastles = True
						if ((position[7])[3] == 'e') and ((position[7])[2] == 'e') and ((position[7])[1] == 'e') and ((position[7])[0] == 'bR1') and blackKingMoves(moverecord) and not (((7,4) in wAttacked) or ((7,3) in wAttacked) or ((7,2) in wAttacked)):
							dots = dots + [possibleMove(7,2)]
							moves = moves + [[7,2]]
							longcastles = True
					newpiece = True
				p1 = win.getMouse()
				i1 = rowNumber (p1)
				j1 = columnNumber(p1)
				if elem ([i1,j1],moves) and (not (blackKingFinder(swapping (position,i,j,i1,j1)) in whiteAttack(swapping (position,i,j,i1,j1)))):
					cleardots (dots)
					if enpassant1 and (j1 == j-1):
						position = swapping (position,i,j-1,i-1,j-1)
					if enpassant2 and (j1 == j+1):
						position = swapping (position,i,j+1,i-1,j+1)
					if shortcastles and (j1 == 6):
						makeMove (position,7,7,7,5)
						position = swapping (position,7,7,7,5)
					if longcastles and (j1 == 2):
						makeMove (position,7,0,7,3)
						position = swapping (position,7,0,7,3)
					makeMove (position,i,j,i1,j1)
					taking (position,i,j,i1,j1)
					moverecord = moverecord + [moveslist(position,i,j,i1,j1)]
					movedrawer(moverecord,movenumber,shortcastles,longcastles)
					position1 = swapping (position,i,j,i1,j1) 
				if promotion and (i1 == 0) and (not (elem (blackKingFinder(swapping (position,i,j,i1,j1)),whiteAttack(swapping (position,i,j,i1,j1))[0]))):
					if (f == 'bP1'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn1.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn1 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn1 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn1 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn1 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn1.draw(win)
					if (f == 'bP2'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn2.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn2 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn2 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn2 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn2 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn2.draw(win)
					if (f == 'bP3'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn3.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn3 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn3 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn3 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn3 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn3.draw(win)
					if (f == 'bP4'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn4.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn4 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn4 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn4 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn4 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn4.draw(win)
					if (f == 'bP5'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn5.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn5 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn5 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn5 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn5 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn5.draw(win)
					if (f == 'bP6'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn6.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn6 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn6 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn6 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn6 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn6.draw(win)
					if (f == 'bP7'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn7.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn7 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn7 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn7 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn7 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn7.draw(win)
					if (f == 'bP8'):
						position1 = blackPromotionChosing(f,j1,position1)
						blackPawn8.undraw()
						if (((position1[i1])[j1])[0:2] == 'bQ'):
							blackPawn8 = Image(Point(70+80*j1,630), 'blackQueen.png')
						if ((position1[i1])[j1])[0:2] == 'bR':
							blackPawn8 = Image(Point(72+80*j1,633), 'blackRook.png')
						if ((position1[i1])[j1])[0:2] == 'bB':
							blackPawn8 = Image(Point(71+80*j1,632), 'blackBishop.png')
						if ((position1[i1])[j1])[0:2] == 'bN':
							blackPawn8 = Image(Point(70+80*j1,632), 'blackKnight.png')
						blackPawn8.draw(win)
				cleardots (dots)
				newpiece = False
				enpassant1 = False
				enpassant2 = False
				shortcastles = False
				longcastles = False
				promotion = False
			if sum(piecenumber(position)) != sum(piecenumber(position1)):
				positionrecord = []
			position = position1
			positionrecord = positionrecord + [position]
			movenumber = movenumber + 1
			positionarray = positionvector(position)
			outF.write(str(positionarray) + ',')
			outF.write('\n')
			#Black computer move
		else:
			if (len(blackpossiblePositions(position,moverecord)) == 0) and (not blackCheck(position)):
				stalemate()
				whitewon = False
				blackwon = False
				break
			if blackCheck(position) and (len(blackpossiblePositions(position,moverecord)) == 0):
				print ('Checkmate')
				wcheckmate()
				whitewon = True
				blackwon = False
				break
			if threefold(positionrecord):
				threefoldrepetition()
				whitewon = False
				blackwon = False
				break
			#poss = blackpossiblePositions(position,moverecord) 
			#respond = []
			#h = 0
			#for h in range(len(poss)):
			#	resp = whitepossiblePositions(poss[h],moverecord)
			#	respond = respond + [maxvalue(NetworkELOcomparison(resp,synaptic_weights,moverecord))]
			#u = minnumber(respond)
			#u = random.choice(u)
			#position2 = poss[u]
			



			position2 = blackalphabetaprunning1(position,synaptic_weights,moverecord)
			#position2 = alphabetaprunningRec(position,synaptic_weights,moverecord,3,False)[1]


			i = blackcomputerMove(position,position2)[0]
			j = blackcomputerMove(position,position2)[1]
			i1 = blackcomputerMove(position,position2)[2]
			j1 = blackcomputerMove(position,position2)[3]
			if blackcomputerMove(position,position2)[5]: #enpassant1
				position = swapping (position,i,j-1,i-1,j-1)
			if blackcomputerMove(position,position2)[6]: #enpassant2
				position = swapping (position,i,j+1,i-1,j+1)
			if blackcomputerMove(position,position2)[7]: #shortcatles
				makeMove (position,7,7,7,5)
				position = swapping (position,7,7,7,5)
			if blackcomputerMove(position,position2)[8]: #longcastles
				makeMove (position,7,0,7,3)
				position = swapping (position,7,0,7,3)
			makeMove (position,i,j,i1,j1)
			taking (position,i,j,i1,j1)
			moverecord = moverecord + [moveslist(position,i,j,i1,j1)]
			movedrawer(moverecord,movenumber,shortcastles,longcastles)
			if blackcomputerMove(position,position2)[4]:
				f = (position[i])[j]
				if (f == 'bP1'):
					blackPawn1.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn1 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn1 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn1 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn1 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn1.draw(win)
				if (f == 'bP2'):
					blackPawn2.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn2 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn2 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn2 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn2 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn2.draw(win)
				if (f == 'bP3'):
					blackPawn3.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn3 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn3 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn3 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn3 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn3.draw(win)
				if (f == 'bP4'):
					blackPawn4.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn4 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn4 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn4 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn4 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn4.draw(win)
				if (f == 'bP5'):
					blackPawn5.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn5 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn5 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn5 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn5 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn5.draw(win)
				if (f == 'bP6'):
					blackPawn6.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn6 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn6 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn6 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn6 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn6.draw(win)
				if (f == 'bP7'):
					blackPawn7.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn7 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn7 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn7 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn7 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn7.draw(win)
				if (f == 'bP8'):
					blackPawn8.undraw()
					if (((position2[i1])[j1])[0:2] == 'bQ'):
						blackPawn8 = Image(Point(70+80*j1,630), 'blackQueen.png')
					if ((position2[i1])[j1])[0:2] == 'bR':
						blackPawn8 = Image(Point(72+80*j1,633), 'blackRook.png')
					if ((position2[i1])[j1])[0:2] == 'bB':
						blackPawn8 = Image(Point(71+80*j1,632), 'blackBishop.png')
					if ((position2[i1])[j1])[0:2] == 'bN':
						blackPawn8 = Image(Point(70+80*j1,632), 'blackKnight.png')
					blackPawn8.draw(win)
			if sum(piecenumber(position)) != sum(piecenumber(position2)):
				positionrecord = []
			position = position2 
			position1 = position 
			positionrecord = positionrecord + [position]
			movenumber = movenumber + 1
			if sum(piecenumber(position)) == sum(piecenumber(position2)):
				newarray = np.array([positionvector(position)]) 
				training_inputs = np.concatenate((training_inputs,newarray), axis = 0)


	x = 1
	training_outputslist = []
	if whitewon:
		for x in range(len(training_inputs)):
			training_outputslist = training_outputslist + [sigmoid(np.dot(training_inputs[x],synaptic_weights))+0.1]
	elif blackwon:
		for x in range(len(training_inputs)):
			training_outputslist = training_outputslist + [sigmoid(np.dot(training_inputs[x],synaptic_weights))-0.1]
	else:
		for x in range(len(training_inputs)):
			est = np.asscalar(sigmoid(np.dot(training_inputs[x],synaptic_weights)))
			training_outputslist = training_outputslist + [est+0.05]

	training_outputs = np.array([training_outputslist]).T
	i = 0
	for i in range(30000): 
		input_layer = training_inputs
		outputs = sigmoid(np.dot(input_layer, synaptic_weights))

		err = training_outputs - outputs
		adjustment = np.dot(input_layer.T, 0.001*err * (1 - outputs)*outputs)

		synaptic_weights = synaptic_weights + adjustment 

		if i % 3000 == 0:
			print(str(10*i / 3000) + '%')
	print(training_outputs - sigmoid(np.dot(training_inputs,synaptic_weights)))
	print(synaptic_weights[0:24])
	outF.write(str(synaptic_weights))

win.getMouse()
win.closeWin()