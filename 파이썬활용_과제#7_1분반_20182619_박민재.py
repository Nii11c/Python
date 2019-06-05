str1='''Time is
Too Slow for those who Wait
Too Swift for those who Fear
Too Long for those who Grieve
Too short for those who Rejoice
But for those who love
Time is not'''

word=str1.split()
print("문장: \n",str1,"\n")

dicti = {}

for k in word:
    if k not in dicti:
        dicti[k]=1
    else:
        dicti[k]+=1

for k,n in dicti.items():
    print(k,":",n,"회")
