filename=input("Enter filename:")
with open(filename,"r") as file:
    text=file.read()
text=text.lower()
words=text.split()
freq={}
for word in words:
    word=word.strip("':;,.?{[(')!]}")
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sorted_words=sorted(freq.items(),key=lambda x:x[1])
for word,count in sorted_words[:10]:
    print(word,":",count)
