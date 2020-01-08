## I am Sofya, a CS UWO student.This program computes hapiness score for 4 US timezones and creates a picture with smiley faces.
#

p1 = [49.189787, -67.444574]
p2 = [24.660845, -67.444574]
p3 = [49.189787, -87.518395]
p4 = [24.660845, -87.518395]
p5 = [49.189787, -101.998892]
p6 = [24.660845, -101.998892]
p7 = [49.189787, -115.236428]
p8 = [24.660845, -115.236428]
p9 = [49.189787, -125.242264]
p10 = [24.660845, -125.242264]
keywordsDictionary = {}
totalOfScoresForATweet = 0
countOfKeywordsForAtweet = 0
happyscoreForATweetListEasternList =[]
happyscoreForATweetListCentralList =[]
happyscoreForATweetListMountainList =[]
happyscoreForATweetListPacificList =[]

keywordsInputFile = input('Enter the file containing keywords:')
try:
  keywordsInfile = open(keywordsInputFile, 'r')
except IOError:
  print('Error: file not found.')
for line in keywordsInfile:
  keywordsList = line.split(',')
  aKeyword = keywordsList[0]
  aValue = float(keywordsList[1])
  keywordsDictionary[aKeyword] = aValue #Created a dictionary with keywords as keys and happy scores as values.
tweetsInputFile = input('Enter the file containing tweets:')
try:
  tweetsInfile = open(tweetsInputFile, 'r')
except IOError:
  print('Error: file not found.')
for line in tweetsInfile:
 wordlist = line.split(' ',5)
 tweetWords = wordlist[5].split()
 latitude = float(wordlist[0].strip("[,"))
 longtitude = float(wordlist[1].strip("]"))
 if latitude >= p2[0] and latitude <= p1[0] :
                        if longtitude <= p1[1] and longtitude >= p3[1] : #for East timezone
                            for word in tweetWords :
                              word = word.strip('/#@.,?!"')
                              word = word.lower()
                              if word in keywordsDictionary : #if a tweet has any keywords, collect its scores and count them
                               totalOfScoresForATweet = totalOfScoresForATweet + keywordsDictionary[word]
                               countOfKeywordsForAtweet = countOfKeywordsForAtweet + 1
                               happyscoreForATweet = totalOfScoresForATweet/countOfKeywordsForAtweet
                               happyscoreForATweetListEasternList.append(happyscoreForATweet)

                        elif longtitude < p3[1] and longtitude >= p5[1] : #for Central timezone
                              for word in tweetWords :
                               word = word.strip('/#@.,?!"')
                               word = word.lower()
                               if word in keywordsDictionary :
                                     totalOfScoresForATweet = totalOfScoresForATweet + keywordsDictionary[word]
                                     countOfKeywordsForAtweet = countOfKeywordsForAtweet + 1
                                     happyscoreForATweet = totalOfScoresForATweet/countOfKeywordsForAtweet
                                     happyscoreForATweetListCentralList.append(happyscoreForATweet)

                        elif longtitude < p5[1] and longtitude >= p7[1] : #for Mountain timezone
                            for word in tweetWords :
                               word = word.strip('/#@.,?!"')
                               word = word.lower()
                               if word in keywordsDictionary :
                                     totalOfScoresForATweet = totalOfScoresForATweet + keywordsDictionary[word]
                                     countOfKeywordsForAtweet = countOfKeywordsForAtweet + 1
                                     happyscoreForATweet = totalOfScoresForATweet/countOfKeywordsForAtweet
                                     happyscoreForATweetListMountainList.append(happyscoreForATweet)

                        elif longtitude < p7 [1] and longtitude >= p9[1] : #for Pacific timezone
                            for word in tweetWords :
                               word = word.strip('/#@.,?!"')
                               word = word.lower()
                               if word in keywordsDictionary :
                                     totalOfScoresForATweet = totalOfScoresForATweet + keywordsDictionary[word]
                                     countOfKeywordsForAtweet = countOfKeywordsForAtweet + 1
                                     happyscoreForATweet = totalOfScoresForATweet/countOfKeywordsForAtweet
                                     happyscoreForATweetListPacificList.append(happyscoreForATweet)

numberOfTweetsInEastern = len(happyscoreForATweetListEasternList)
numberOfTweetsInCentral = len(happyscoreForATweetListCentralList)
numberOfTweetsInMountain = len(happyscoreForATweetListMountainList)
numberOfTweetsInPacific = len(happyscoreForATweetListPacificList)
happyScoreEastern = sum(happyscoreForATweetListEasternList)/numberOfTweetsInEastern
happyScoreCentral = sum(happyscoreForATweetListCentralList)/numberOfTweetsInCentral
happyScoreMountain = sum(happyscoreForATweetListMountainList)/numberOfTweetsInMountain
happyScorePacific = sum(happyscoreForATweetListPacificList)/numberOfTweetsInPacific

print('The hapiness score for Eastern timesone is', happyScoreEastern)
print('The hapiness score for Central timesone is', happyScoreCentral)
print('The hapiness score for Mountain timesone is', happyScoreMountain)
print('The hapiness score for Pacific timesone is', happyScorePacific)
print('The number of tweets found in Eastern timezone is', numberOfTweetsInEastern)
print('The number of tweets found in Central timezone is', numberOfTweetsInCentral)
print('The number of tweets found in Mountain timezone is', numberOfTweetsInMountain)
print('The number of tweets found in Pacific timezone is', numberOfTweetsInPacific)
keywordsInfile.close()

from happy_histogram import drawSimpleHistogram
drawSimpleHistogram(happyScoreEastern, happyScoreCentral, happyScoreMountain, happyScorePacific)






