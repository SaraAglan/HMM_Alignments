#sequences, gap, submat
seq1,seq2="ACCA","ACAGAC"
gap= -2
submat= {'A':{'A':2,'C':-1,'T':-1,'G':0},
	 'C':{'A':-1,'C':2,'T':0,'G':-1},
	 'T':{'A':-1,'C':0,'T':2,'G':-1},
	 'G':{'A':0,'C':-1,'T':-1,'G':2}}

###########################################################################
def Print(M):
	for elem in M:
		print elem

def NW(seq1, seq2, submat, gap):
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
	
	for i in range(1,a):
		Matrix[i][0]=i*gap
		Traceback[i][0]= 'Up'
	for j in range(1,b):
		Matrix[0][j]=j*gap
		Traceback[0][j]= 'Left'
#Iteration
	for i in range(1, a):
		for j in range(1, b):
			diag=Matrix[i-1][j-1]+submat[seq1[i-1]][seq2[j-1]]
			up=Matrix[i-1][j]+gap
			left=Matrix[i][j-1]+gap
			Matrix[i][j]=max(diag, up, left)
			if Matrix[i][j]== diag:
				Traceback[i][j]= 'Diag'
			elif Matrix[i][j]==up:
				Traceback[i][j]= 'Up'
			else:
				Traceback[i][j]= 'Left'
	Align1=''
	Align2=''
	Alignment=''
	i=len(seq1)
	j=len(seq2)
	while Traceback[i][j]!= 0:
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
	print 'The optimal alignment score is:', Matrix[-1][-1]
	print 'Matrix is:'
	Print(Matrix)
	print 'Traceback is:'
	Print(Traceback)
	print 'Best alignment is:'
	Alignment= str(Align1+'\n')+str(Align2)
	return Alignment
	
#Backtracking

print(NW(seq1, seq2, submat, gap))
