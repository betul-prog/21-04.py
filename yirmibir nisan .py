sentence=input("give me a sentence:")
words= sentence.split()
i=0
longest=0
while i < len (words):
  if len (words[i]) > longest:
    longest= len (words[i])
    i+=1
    print ("the length of the longest word is:")

give me a sentence:seni seviyorum
the length of the longest word is:
the length of the longest word is: