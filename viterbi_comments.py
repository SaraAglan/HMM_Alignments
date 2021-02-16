def viterbi(seq,HMMT,HMMG):
	l = len(seq)
########Initialization
	#Dictionary/List comprehension, we create a dictionary with a key for each state of the HMM and a list of length seq+2 (here we write +1 because we already included an extra character in the sequence that we pass to this function)
	#Note that in this way we obtain a representation for the matrix V
	V = {key:[(0,'?') for i in range(l+1)] for key in HMMT.keys()}
	#Initialize the first value for the state 'BEGIN' to 1
	V['BEGIN'][0] = (1,'^')

########Iteration
	#Iterate through every character of the sequence
	for c in range(l):
		#Iterate through every key of F (aka columns of the matrix)
		for row in V.keys():
			#Iterate through every state of the HMM
			for state in HMMT.keys():
				#Calculate the iteration step, where
					#V[state][c][0] is the probability of being in a state on the previous step
					#HMMT[state].get(row,0) is the transition probability from that state to the current one
					#HMMG[row].get(seq[c],0) is the probability of generating the character at position c from the current state
				P = V[state][c][0] * HMMT[state].get(row,0) * HMMG[row].get(seq[c],0)
				#If the computed value is higher than the one previously stored, save it alongside the state from which it comes
				if P > V[row][c+1][0]:
					V[row][c+1] = (P, state)

	#Backtracking
	S = []
	Pi = []
	i = l
	state = V['END'][i][1]
	#Simply iterate through the columns of the matrix, jumping to the right row according to the states we stored during the forward step and appending them
	while state != 'BEGIN':
		Pi.append(state)
		S.append(seq[i-2])
		i -= 1
		state = V[state][i][1]
	#Reverse both strings and return them alongside the probability
	S.reverse()
	Pi.reverse()

	return S, Pi, V['END'][l][0]

#Note that for the algorithm to perform its function, we need to have a proper input
#seq must contain a terminal character at the end
#HMMT contains the transition probability for each state
#HMMG contains the probability of generating a character from a state (BEGIN can't generate any state, but END should have probability 1 of generating the terminal character of the string)
seq = "ATGCG$"
HMMT = {
'BEGIN':{'Y':0.2,'N':0.8},
'Y':{'Y':0.7,'N':0.2,'END':0.1},
'N':{'Y':0.1,'N':0.8,'END':0.1},
'END':{}
}
HMMG = {
'BEGIN':{},
'Y':{'A':0.1,'T':0.1,'C':0.4,'G':0.4},
'N':{'A':0.25,'T':0.25,'C':0.25,'G':0.25},
'END':{'$':1}
}

result = viterbi(seq,HMMT,HMMG)
print result[0]
print result[1]
print "Probability = " + str(result[2])
