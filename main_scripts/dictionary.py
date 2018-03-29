from PyDictionary import PyDictionary
from speak import say
def findMeaning(str):
	dictionary=PyDictionary()
	meaningDict=dictionary.meaning(str)
	if meaningDict!=None:
		meaningList = [elem[0] for elem in meaningDict.values()]
		return meaningList[0]
	else:
		return "Sorry no meaning found"

if __name__ == '__main__':
	findMeaning("Hotel")

