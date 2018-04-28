#sequences, gap, submat
seq1, seq2= 'ACCATA', 'ACATA'
gap= -2
submat= {'A':{'A':2,'C':-1,'T':-1,'G':0},
	 'C':{'A':-1,'C':2,'T':0,'G':-1},
	 'T':{'A':-1,'C':0,'T':2,'G':-1},
	 'G':{'A':0,'C':-1,'T':-1,'G':2}}

###########################################################################
def Print(M):
	for elem in M:
		print elem

def SW(seq1, seq2, submat, gap):
	a=len(seq1)+1
	b=len(seq2)+1
#Initialization
	Matrix=[]
	Traceback=[[0]*b for i in range(a)]
	for i in range(a):
		row=[]
		for j in range(b):
			row.append(0)
		Matrix.append(row)

#Iteration
	for i in range(1, a):
		for j in range(1, b):
			diag=Matrix[i-1][j-1]+submat[seq1[i-1]][seq2[j-1]]
			up=Matrix[i-1][j]+gap
			left=Matrix[i][j-1]+gap
			Matrix[i][j]=max(diag, up, left,0)
			if Matrix[i][j]>0:
				if Matrix[i][j]== diag:
					Traceback[i][j]= 'Diag'
				elif Matrix[i][j]== up:
					Traceback[i][j]= 'Up'
				elif Matrix[i][j]== left:
					Traceback[i][j]= 'Left'
				elif Matrix[i][j]<0:
					Matrix[i][j]=0

	Align1=''
	Align2=''
	Alignment=''
	i=len(seq1)
	j=len(seq2)
	while Traceback[i][j]>0:
		if Traceback[i][j]== 'Diag':
			Align1=	seq1[i-1]+Align1
			Align2= seq2[j-1]+Align2
			i-=1
			j-=1
		elif Traceback[i][j]== 'Up':
			Align1= seq1[i-1]+Align1
			Align2= '-'+Align2
			i-=1
		else:
			Align1= '-'+Align1
			Align2= seq2[j-1]+Align2
			j-=1
	max_value=0
	max_i=0
	max_j=0
	for i in range(a):
		for j in range(b):
			if Matrix[i][j] > max_value:
				max_i, max_j = i, j
				max_value= Matrix[i][j]


	print 'The optimal alignment score is:', max_value, max_i, max_j
	print 'Matrix is:'
	Print(Matrix)
	print 'Traceback is:'
	Print(Traceback)
	print 'Best alignment is:'
	Alignment= str(Align1+'\n')+str(Align2)
	return Alignment

print(SW(seq1, seq2, submat, gap))
