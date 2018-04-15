from docBot.PriaidDiagnosisClientDemo import PriaidDiagnosisClientDemo
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# Process whole documents
# text = ""
def run(userSymptom,userAge,userGender):

	doc = nlp(u'{0}'.format(userSymptom))
	noun_count = 0
	adj = []
	pushed_word = []
	temp = ""
	counter = 0
	while counter<len(doc):

		# if doc[counter].pos_ == "NOUN" and counter+2<len(doc) and doc[counter+1].lemma_=="be" and doc[counter+2]=="VERB":
		# 	print( "Found Noun Verb Verb", doc[counter],doc[counter+1])
		# 	result = "{0} {1}".format(doc[counter+2],doc[counter])
		# 	print("Result ",result)
		# 	adj.append(result)
		# 	counter+=3
		# 	continue

		if doc[counter].pos_ == "NOUN" and counter+1<len(doc) and doc[counter+1].pos_=="NOUN":
			print( "Found Noun Noun", doc[counter],doc[counter+1])
			result = "{0} {1}".format(doc[counter],doc[counter+1])
			print(result)
			adj.append(result)
			counter+=2
			continue
		if doc[counter].pos_ == "ADJ" and counter+1<len(doc) and doc[counter+1].pos_=="NOUN":
			print( "Found ADJ Noun", doc[counter],doc[counter+1])
			result = "{0} {1}".format(doc[counter],doc[counter+1])
			print(result)
			adj.append(result)
			counter+=2
			continue

		if doc[counter].pos_ == "NOUN":
			print("Found Noun ", doc[counter].lemma_) 
			adj.append(doc[counter].lemma_)
			counter+=1
			continue
		counter+=1

	    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
	    #       token.shape_, token.is_alpha, token.is_stop)

	diagnosisClient = PriaidDiagnosisClientDemo()
	all_symptoms = diagnosisClient.loadSymptoms()
	print(adj)
	symptoms = []
	if len(adj) == 0:
		temp="We did not recognize anything!"
		return temp

	symptoms.append(adj[0])



	# Getting ID for the Given Diagnosis
	def getId(targets,all_symptoms=all_symptoms):
		all_targetID = []
		for  target in targets:
			for symptom in all_symptoms:
				if symptom["Name"].lower() == target.lower():
					all_targetID.append(symptom["ID"])

		return all_targetID

	all_targetID = getId(symptoms)
	print(all_targetID)
	if len(all_targetID) == 0:
		temp = "Symptom Not Recognized"
		return temp
	print(all_targetID)

	gender = userGender
	dob = userAge
	print_items = []
	try:
		diagnoseDetail = diagnosisClient.loadDiagnosis(all_targetID,gender,dob)
	except:
		temp = "Couldn't Diagnose that symptom!"
		return temp





	count = 0
	for result in diagnoseDetail:
		x,y = result["Issue"]["IcdName"],result["Issue"]["Accuracy"]
		temp += ("You may have {0} with probability of {1} percent.".format(x, y))
		if len(diagnoseDetail) > 1 and count<len(diagnoseDetail)-1:
			temp+="\nOR\n"
			count+=1


	return temp



