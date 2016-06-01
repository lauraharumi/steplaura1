import itertools 
import random 

characters = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(16))
print "16 random characters are: " +  characters  

f = open('/usr/share/dict/words', 'r') #read existing file with all words of the English dictionary
dictpairs = {} #create an empty dictionary
for word in f:
	sortedword = ''.join(sorted(word))[1:]
	if sortedword in dictpairs: 
		dictpairs[sortedword].append(word[:-1]) #values with same letters are paired with same key 
	else:
		dictpairs[sortedword] = [word[:-1]] #eg. bkkooorw : ['bookwork', 'workbook']

combinations = [] 
pos = 0
for i in xrange(len(characters),1,-1): #insert from longest to shortest
	combinations.insert(pos,set([''.join(sorted(c)) for c in itertools.combinations(characters,i)]))
	pos+= 1 

anagramlist = []
for sets in combinations: 
	for c in sets: 
		try:
			anagramlist.append(dictpairs[c])
		except:
			pass

anagrams = [anagram for samelengthlist in anagramlist for anagram in samelengthlist]
print anagrams #printing answers 

#play the actual game: can you make an anagram using the 16 letters? 
check = raw_input("check if anagram: ")
if check in anagrams: 
	print "YES"
else: 
	print "NOPE"

