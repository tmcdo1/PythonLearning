import urllib

def read_text():
    file_read = open("C:\Users\ThomasMcD\Desktop\movie_quotes.txt")
    text = file_read.read()
    #print(text)
    file_read.close()
    feedback = check_profanity(text)
    if(feedback):
        print("There is profanity!")
    else:
        print("No worries")

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    response = connection.read()
    connection.close()
    if(response == 'false'):
        return False
    else:
        return True

read_text()
