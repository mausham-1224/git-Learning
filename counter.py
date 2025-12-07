import time
timee=int( input("Enter the number for sleep:"))


for x in range( timee,0,-1):

    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times Up")