import sys
import json

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #Load up scores
   scores = {}

   for l in sent_file:
      term,score = l.split("\t")
      scores[term] = int(score)

   newsentiments = {}

   # Scan each tweet and get a score
   for line in tweet_file:
      tweet_data = json.loads(line)
      tweet = tweet_data['text']
      encoded_tweet = tweet.encode('utf-8')

      total = 0
      temp = {}

      for w in encoded_tweet.split(" "):

         if w in scores:
            total += scores[w]
         else:
            temp[w] = 0

      for key in temp:
         newsentiments[key] = total      


      for key in newsentiments:
         print key + "\t" + str(newsentiments[key])

if __name__ == '__main__':
    main()
