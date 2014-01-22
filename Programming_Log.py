'''This program logs, manipulates, and presents data tracking my programming
progress and the amount of time I have spent practicing. Almost a self-
fulfilling prophecy in itself!'''

#THINGS TO WORK ON. CREATE CLASS FOR STORING TIME. CONVERT ALL SESSION_TIMES IN LIST TO TIMECLASS.
#ONCE TIME CLASS IS INITIATED, ADD ALL SESSION_TIMES FROM LIST AND WRITE DAILY TOTAL TO FILE.
#CREATE A FUNCTION AND A CLASS THAT CREATES FILE PATHWAYS. SUBSTITUTE THIS FOR CODE IN FUNCTIONS.

#Import modules.
import os
from datetime import datetime, timedelta

#Start-up functions. Gets Clock-In time.
def start():
    start_time = datetime.now()
    print('Time-keeping is starting now. You clocked in at {}'.format(str(start_time)[0:19]))
    return start_time

#Create new host folder if none exist.
def createHostFolder():
    directory = r'C:\Users\owner\Desktop'
    full_path = os.path.join(directory, 'Python Logs')
    print('Host folder path is: {}'.format(full_path))
    if not os.path.exists(full_path):
        os.makedirs(full_path)

#Read file and create list of total times. Returns list to later calculate daily total time.
def getTotalTimes(start_time):
    directory = r'C:\Users\owner\Desktop\Python Logs'
    date = str(start_time)[0:10]
    log_name = date + '.txt'
    full_path = os.path.join(directory, log_name)
    session_times = []
    today_log = open(full_path, 'r')
    for line in today_log:
        if line.startswith('Total Time'):
            session_times.append(line.strip().split(' ')[2])
    return session_times

#Get user input for Subject.
def grabData():
    subject = input('What did you practice today, Colin? ')
    return subject

#Calculates the duration of time spent coding.
def duration(start_time, session_times):
    end_time = datetime.now()
    calculated_duration = end_time - start_time
    session_times.append(calculated_duration)
    return calculated_duration, end_time, session_times

#Write to File (logs time in an output file). FORMAT OUTPUT TO LOOK PRETTY.
def store(start_time, end_time, subject, duration):
    date = str(start_time)[0:10]
    directory = r'C:\Users\owner\Desktop\Python Logs'
    log_name = date + '.txt'
    full_path = os.path.join(directory, log_name)
    if not os.path.exists(full_path):
        today_log = open(full_path, 'w')
        today_log.write('Date: ' + date + '\n')
        today_log.write('Studied: ' + subject + '\n')
    else:
        today_log = open(full_path, 'a')
        today_log.write('\n\nContinued studying: ' + subject + '\n')
    today_log.write('Clock in: {} \nClock out: {} \nTotal Time: {}'.format(start_time, end_time, str(duration)))            
    print('Progress was logged in: {}'.format(full_path))
    return today_log

#Main Function.
#CREATE CLASS TO DISPLAY TIME CORRECTLY(NOT TOTAL TIME IN EACH CATEGORY) SYNTHESIZE TOTAL TIMES FROM SESSION_TIMES LIST
def main():
    start_time = start()
    createHostFolder()
    session_times = getTotalTimes(start_time)
    input('Press Enter when you are done programming.')
    subject = grabData()
    spent_time, end_time, session_times = duration(start_time, session_times)
    print(session_times)
    print('On {}, you spent {} hours, {} minutes, and {} seconds learning about {}. Congratulations!'.format(start_time.strftime("%B %d, %Y"), spent_time.seconds // 3600, spent_time.seconds // 60, spent_time.seconds, subject))
    today_log = store(start_time, end_time, subject, spent_time)
    if today_log:
        today_log.close()


main()
