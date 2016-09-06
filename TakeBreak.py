import webbrowser
import time

numRep = 3
count = 0

print("This program started on "+time.ctime())
while (count<numRep):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=VbfpW0pbvaU")
    count+=1
