import sys
import json

def lines(fp):
    return str(fp.readlines())

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #Load up scores
   scores = {}
   states = {'AL':0, 'AK':0, 'AZ':0, 'AR':0, 'CA':0, 'CO':0, 'CT':0, 'DC':0, 'DE':0, 'FL':0,'GA':0,'HI':0,'ID':0,'IL':0, 'IN':0, 'IA':0, 'KA':0, 'KY':0, 'LA':0, 'ME':0, 'MD':0, 'MS':0, 'MO':0, 'MT':0, 'NB':0, 'NV':0, 'NH':0, 'NJ':0, 'NM':0, 'NY':0, 'NC':0, 'ND':0, 'OH':0, 'OK':0, 'OR':0, 'PA':0, 'RI':0, 'SC':0, 'SD':0, 'TN':0, 'TX':0, 'UT':0, 'VT':0, 'VA':0, 'WA':0, 'WV':0, 'WI':0, 'WY':0, 'AS':0, 'GU':0, 'MP':0, 'PR':0, 'VI':0} 

   for l in sent_file:
      term,score = l.split("\t")
      scores[term] = int(score)

   # Scan each tweet and get a score
   for line in tweet_file:
      tweet_data = json.loads(line)

      if 'text' in tweet_data:
         tweet = tweet_data['text']
         encoded_tweet = tweet.encode('utf-8')

         total = 0
         for w in encoded_tweet.split(" "):
            if w in scores:
               total += scores[w]

         sentiment_score = total 
      
         if 'user' in tweet_data:
            user = tweet_data['user']

            if 'location' in user:
               loc = user['location']
            
               if "," in loc:
                  loc_data = user['location'].split(",")
                  state = ""

                  if len(loc_data) >= 2:
                     state = loc_data[1]
                  
                  if state in states:
                     states[state] = states[state] + sentiment_score

   print max(states.iterkeys(), key=(lambda key: states[key])) 

if __name__ == '__main__':
    main()
