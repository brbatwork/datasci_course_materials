import sys
import json

def main():
   tweet_file = open(sys.argv[1])
   terms = {}
   tot_terms = 0

   # Scan each tweet and gather the terms 
   for line in tweet_file:
      tweet_data = json.loads(line)

      if 'text' in tweet_data:
         tweet = tweet_data['text']
         encoded_tweet = tweet.encode('utf-8')

         for term in encoded_tweet.split():
            tot_terms += 1

            if term in terms:
               terms[term] = terms[term] + 1
            else:
               terms[term] = 0


   if tot_terms > 0:
      for key in terms:
         freq = terms[key] / (tot_terms * 1.0)
         print key + " " + str(freq)
			#print key + " occurred  " + str(terms[key]) + " out of " + str(tot_terms) + " giving  freq " + str(freq)


if __name__ == '__main__':
    main()
