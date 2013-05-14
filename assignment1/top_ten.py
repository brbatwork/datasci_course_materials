import sys
import json
import operator

def main():
   tweet_file = open(sys.argv[1])
   tags = {}

   # Scan each tweet and gather the hash tags 
   for line in tweet_file:
      tweet_data = json.loads(line)

      if 'entities' in tweet_data:
         entities = tweet_data['entities']

         if 'hashtags' in entities:
            hashtags = entities['hashtags']

            for i, val in enumerate(hashtags):
                        
               if 'text' in val:
                  ht = val['text']

                  if ht in tags:
                     tags[ht] = tags[ht] + 1
                  else:
                     tags[ht] = 1 


   sorted_tags = dict(sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])

   for key in sorted_tags:
         count = sorted_tags[key] * 1.0
         print key + " " + str(count)

if __name__ == '__main__':
    main()
