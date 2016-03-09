import webbrowser
import time

break_count = 0
total_break = 3
print "This program started on " + time.ctime()
while(count<total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=uzeSOqGrCEQ")
    break_count +=1

