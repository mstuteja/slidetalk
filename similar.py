#natural language toolkit 
import nltk

# nltk.download() - To be used for installing necessary tools (first time only)

#string manipulation using nltk
from nltk.corpus import stopwords

#converting strings into vectors 
from nltk.tokenize import word_tokenize 

#Function to determine similarity between presentation content and speech recognized content.

def similarcheck(x,y):
	X = x
	Y = y

	# tokenization using nltk 
	X_list = word_tokenize(X) 
	Y_list = word_tokenize(Y) 

	# list of stopwords 
	sw = stopwords.words('english') 
	l1 =[];l2 =[] 

	# removing stop words from the string 
	X_set = {w for w in X_list if not w in sw} 
	Y_set = {w for w in Y_list if not w in sw} 

	# creation of a set from tokenized data 
	rvector = X_set.union(Y_set) 
	for w in rvector: 
		if w in X_set: l1.append(1) # create a vector 
		else: l1.append(0) 
		if w in Y_set: l2.append(1) 
		else: l2.append(0) 
	c = 0

	# cosine similarity formula 
	for i in range(len(rvector)): 
			c+= l1[i]*l2[i] 
	cosine = c / float((sum(l1)*sum(l2))**0.5) 
	return cosine
