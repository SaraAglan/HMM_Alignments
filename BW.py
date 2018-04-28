
#BACKWARD ALGORITHM

#sequence, states, transitions, emissions
seq='ATTCG'

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


def BW(states,trans,emiss,seq):
	Matrix=[[0 for x in range(len(seq)+2)] for y in states]
	Matrix[-1][-1]=1
	for i in range(1, len(states)-1):
		Matrix[i][-2]=trans[(states[i],states[-1])]

	for j in range(len(seq)-1,0,-1):
		for i in range(1, len(states)-1):
			sum_prob = 0
			for k in range(1, len(states)-1):
				a=Matrix[k][j+1]
				b=trans[(states[i],states[k])]
				c=emiss[states[k]][seq[j]]
				sum_prob += a*b*c
			Matrix[i][j] = sum_prob
	sum_prob = 0
	for k in range(1, len(states)-1):
		sum_prob += Matrix[k][1]*trans[(states[0],states[k])]*emiss[states[k]][seq[0]]

	print 'Probability is:'
	return sum_prob


print(BW(states,trans,emiss,seq))
