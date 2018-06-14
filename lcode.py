# -*- coding: utf-8 -*-
from questions import get_problems
import random

data = get_problems()
data = data.split("\n")

problems = {}
descriptions = {}
easy, medium, hard = [], [], []

def pre_process_questions():

	for s in data:
		s = s.split(" ")
	  	
	  	problem_num = s[0]
	  	difficulty = s[-1]
	  	problem_name = " ".join(s[1:len(s)-2])
	  	
	  	#capture problem frequency
		if problem_num in problems:
			problems[problem_num] += 1
		else:
			problems[problem_num] = 1
	  	
	  	
	  	if problem_num not in descriptions:
			descriptions[problem_num] = (problem_name, difficulty)

			if difficulty == "Easy":
				easy.append(problem_num)
			elif difficulty == "Medium":
				medium.append(problem_num)
			else:
				hard.append(problem_num)

def getIterableOfType(qType):
	iter_able = None
	if qType == "Easy":
		iter_able = easy
	elif qType == "Medium":
		iter_able = medium
	else:
		iter_able = hard
	return iter_able

def getQuestionOfType(qType):
	iter_able = getIterableOfType(qType)
	for num in iter_able:
		print num, descriptions[num][0]
	print "\nThere are a total of {} {} problems".format(len(iter_able), qType)

def getRandomQuestionOfType(qType):
	iter_able = getIterableOfType(qType)
	randnum = random.randint(0, len(iter_able)-1)
	print iter_able[randnum], descriptions[iter_able[randnum]]



if __name__ == "__main__":
	pre_process_questions()
	getRandomQuestionOfType("Easy")








  
