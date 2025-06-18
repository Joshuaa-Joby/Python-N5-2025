TrainingSession = int(input("Enter how long is the training session in mintues: "))
SongDuration = [0]
HowManySongs = int(input("How many songs do you have? "))

for i in range(HowManySongs):
    SongDuration.append(int(input("Enter the duration of song " + str(i + 1) + ": ")))

while TrainingSession > 10 or TrainingSession < 30 :
    print("Invalid session length")
    TrainingSession = int(input("Enter how long is the training session in mintues: "))          