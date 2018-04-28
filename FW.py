
#FORWARD ALGORITHM

#sequence, states, transitions, emissions
seq='ATTCGGTGTTG'

states=['BEGIN','X','Y','END']

trans={('BEGIN','X'):0.8,('BEGIN','Y'):0.2,
	('X','X'):0.6,('X','Y'):0.2,('X','END'):0.2,
	('Y','Y'):0.2,('Y','X'):0.7,('Y','END'):0.1}

emiss={'X':{'A':0.1,'C':0.4,'T':0.1,'G':0.4},
	'Y':{'A':0.25,'C':0.25,'T':0.25,'G':0.25}}

###########################################################################################
def Print(N):
	for elem in N:
		print elem


def FW(states,trans,emiss,seq):
	Matrix=[[0 for x in range(len(seq)+2)] for y in states]
	Matrix[0][0]=1
	for i in range(1, len(states)-1):
		Matrix[i][1]=trans[(states[0],states[i])]*emiss[states[i]][seq[0]]

	for j in range(2, len(seq)+1):
		for i in range(1, len(states)-1):
			sum_prob = 0
			for k in range(1, len(states)-1):
				a=Matrix[k][j-1]
				b=trans[(states[k],states[i])]
				c=emiss[states[i]][seq[j-1]]
				sum_prob += a*b*c
			Matrix[i][j] = sum_prob
	sum_prob = 0
	for k in range(1, len(states)-1):
		sum_prob += Matrix[k][len(seq)]*trans[(states[k],states[-1])]
	Matrix[-1][-1]=sum_prob
	#print Matrix
	print 'Probability is:'
	return sum_prob


print(FW(states,trans,emiss,seq))
