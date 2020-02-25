"""
Problem:
given a string return a list of strings that have character limit

1. strings should only contain whole words

"""

def getShortenedStrings(rawString,charLimit = 100):
    responses = []
    if not rawString:
        return responses
    i = 0
    limit = charLimit - 5
    word = ""

    while(i<len(rawString)):
        curStr = "" + word

        while(len(curStr) < charLimit and i< len(rawString)):
            start =  i
            if rawString[i] == ' ':
                while( i < len(rawString) and
                       rawString[i] == ' ' and
                      (i-start+len(curStr) < limit)):
                    i+=1
            else:
                while(i < len(rawString) and
                      rawString[i] != ' '):
                    i+=1

            word = rawString[start:i]
            if len(curStr) + len(word) <= limit:
                curStr += word
                word = ""
            else:
                break
        responses.append(curStr)

    if word:
        responses.append(word)

    return [response+"({}/{})".format(i+1,len(responses)) for i,response in enumerate(responses)]

rawString = "crap"
print(getShortenedStrings(rawString))

rawString = """On the day Virat Kohli watched New Zealand trample India by ten wickets in the Wellington Test and one that marks ten years since Sachin Tendulkar became the world's first ODI double-centurion, the two men were honoured like never before. US president Donald Trump, speaking at the inauguration of the massive Sardar Patel Stadium in Ahmedabad, acknowledged India's love for the "greatest cricket players, from Soo chin Tendolkerr to Virot Kohlee". Headline writers everywhere woke up to all the possibilities they hadn't considered before."""
print(getShortenedStrings(rawString))
