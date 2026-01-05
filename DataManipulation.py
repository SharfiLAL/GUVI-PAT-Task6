import string
'''
prebuilt python module


with open("dataDemo.txt","r",encoding="utf-8") as f :  


with > Automatically closes the file


open() > Opens the file
dataDemo.txt > file name
r > read
encoding="utf-8" > Supports all the characters \
fn > File object


 text = f.read()
reads the entire file and store in the string variable text


text=text.lower()

Python will become > python


for ch in string.punctuation:
   text=text.replace(ch,"")
Remove the Punctuation from my file

"python " > python
!" $%^Y&


words = text.split()


wordsOriginal = hello there am looking for personal one on one training in python selenium


words=["hello" , "there", "am"...]

word_count={} create an empty dictionary




word:count


"Python" : 3


for w in words:
   if w in word_count:
        word_count[w] += 1
   else:
        word_count[w]=1






'''




with open("dataDemo.txt","r",encoding="utf-8") as f :
 text = f.read()
text=text.lower()


for ch in string.punctuation:
   text=text.replace(ch,"")


words = text.split()


word_count={}
for w in words:
   if w in word_count:
        word_count[w] += 1
   else:
        word_count[w]=1


print(word_count)


most_word = max(word_count,key=word_count.get)
Most_count=word_count[most_word]


print("Most Repeated Word :", most_word)
print("Count :",Most_count)