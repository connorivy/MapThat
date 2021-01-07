import pickle
class Evaluator():
	def __init__(self):
		self.filter = pickle.load('./filter.pkl')
	def evaluate(self, tweet):
		for problem, filt in self.filter:
			for go in filt['Go_Words']:
				if go
