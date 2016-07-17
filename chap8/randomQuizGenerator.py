#!python3
#randomQuizGenerator.py-creates quizzes along with answers and provide in random order
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia' : 'Richmond', 'Washington' : 'Olympia' , 'West Virginia' : 'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
for Num in range(35):
	quizFile=open('Quiz%s.txt'%(Num+1),'w')
	answerFile=open('Answer%s.txt'%(Num+1),'w')
	quizFile.write('Name:\n\nDate:\n\n')
	quizFile.write((' '*20)+'State capitals Quiz (Form %s)'%(Num+1))
	quizFile.write('\n\n')
	states=list(capitals.keys())
	random.shuffle(states)
	for no in range(50):
		correct=capitals[states[no]]
		wrong=list(capitals.values())
		del wrong[wrong.index(correct)]
		wrong=random.sample(wrong,3)
		answerOptions=wrong+[correct]
		random.shuffle(answerOptions)
		quizFile.write('%s.What is the capital of %s?\n'%(no+1,states[no]))
		for i in range(4):
			quizFile.write('%s.%s\n'%('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')

		answerFile.write('%s.%s\n'%(no+1,'ABCD'[answerOptions.index(correct)]))
	quizFile.close()
	answerFile.close()
