import time
import webbrowser

total_breaks=3
count=0
while(count<total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=lLEyW5zH4DM")
    count+=1
