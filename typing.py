from wonderwords import RandomSentence

import random
import time 
sentence_list =[]
paragraph =[]
for i in range(0,10):
    sent = RandomSentence()
    random_sent = sent.sentence()
    sentence_list.append(random_sent)
    paragraph += random_sent +  " "
def error_rate(sentence_list,paragraph):
    error_count = 0
    length = len(sentence_list)
    for i in range(length):
        if sentence_list[i] != paragraph[i]:
            error_count+=1
        else:
            pass
    error_percent=error_count/length * 100
    return error_percent
print("Type the below paragraph as quickly as possible with as few mistakes to get a high score: \n")
print(sentence_list)
print("\n")

start_time = time.time()
typed_paragraph = input()
end_time = time.time()
time_taken = end_time - start_time
error_percent = error_rate(sentence_list, typed_paragraph)
print("\n")

if error_percent > 50:
    print(f"Your error rate {error_percent} was quite high and hence your accurate speed could not be computed.")

else:
    speed = len(typed_paragraph)/time_taken
    print("******YOUR SCORE REPORT******")
    print(f"Your speed is {speed} words/sec")
    print(f"The error rate is {error_percent}")
