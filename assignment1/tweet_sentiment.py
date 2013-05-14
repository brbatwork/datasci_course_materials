import sys
import json

def lines(fp):
    return str(fp.readlines())

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #Load up scores
   scores = {}

   for l in sent_file:
      term,score = l.split("\t")
      scores[term] = int(score)

   # Scan each tweet and get a score
   for line in tweet_file:
      tweet_data = json.loads(line)
      tweet = tweet_data['text']
      encoded_tweet = tweet.encode('utf-8')

      total = 0
      for w in encoded_tweet.split(" "):
         if w in scores:
            total += scores[w]

      print str(total)

if __name__ == '__main__':
    main()
