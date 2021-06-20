import calendar
from datetime import datetime
import webbrowser

subjects = {'monday' : ['DCCN', 'MPMC', 'WT','LUNCH BREAK', 'DMAA', 'CP', 'DCCN'],
                'tuesday' : ['UNIX', 'DCCN', 'WT', 'LUNCH BREAK', 'RA', 'MPMC', 'WT'],
                'wednesday' : ['WT', 'UNIX', 'DCCN', 'LUNCH BREAK', 'MPMC', 'DMAA', 'UNIX'],
                'thursday' : ['MPMC', 'SS', 'DMMA', 'LUNCH BREAK', 'UNIX', 'DCCN', 'MPMC'],
                'friday' : ['WT', 'DMAA', 'DCCN', 'LUNCH BREAK', 'MPMC', 'UNIX', 'DMAA'],
                'saturday' : ['DMAA', 'WT', 'UNIX','LUNCH BREAK', 'UNIXLAB'],
                'sunday' : ['WTLAB', 'AELSLAB', 'LUNCH BREAK', 'MPMCLAB']
              }
classes = { 'DCCN':	'https://meet.google.com/lookup/filgrqri3s',
            'MPMC' : 'https://meet.google.com/lookup/c2h3bvthzx',
            'WT' : 'https://meet.google.com/lookup/frcfytzqw2',
            'DMAA' : 'https://meet.google.com/lookup/ggjkhdmcfp',
            'CP' :'',	
            'UNIX' : 'https://meet.google.com/lookup/bziccis7kc',
            'RA' : 'https://meet.google.com/lookup/hiexncufwt',
            'SS' : 'https://meet.google.com/lookup/hw7pxhpgv3',
            'WTLAB' : 'https://meet.google.com/lookup/brzpz3qiql',
            'ELCS'	: 'https://meet.google.com/lookup/hdlj3ho6u2',
            'MPMCLAB' :	'https://meet.google.com/lookup/hvdgtwo2yd',
            'UNIXLAB' : 'https://meet.google.com/lookup/evfhggazrc'
          }

def find_day():
    date_and_time = datetime.now()
    date = str(date_and_time.day) + ' ' + str(date_and_time.month) + ' ' + str(date_and_time.year)
    date = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[date]
    return day.lower()

def find_classes():
    subs = []
    day = find_day()
    classes = subjects[day]
    if day != 'saturday' and day != 'sunday':
        timings = ['09:15 am - 10:15 am','10:30 am - 11:30 am', '11:45 am - 12:45 pm', '12:45 pm - 14:00 pm', '14:00 pm - 15:00 pm', '15:15 pm - 16:15 pm', '16:30 pm - 17:30 pm']
        for i in range(7):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    if day == 'saturday':
        timings = ['09:15 am - 10:15 am','10:30 am - 11:30 am', '11:45 am - 12:45 pm', '12:45 pm - 14:00 pm', '14:00 pm - 17:30 pm']
        for i in range(5):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    if day == 'sunday':
        timings = ['07:30 am - 10:30 am', '10:45 am - 13:45 pm', '14:15 pm', '14:15 pm - 17:15 pm']
        for i in range(4):
            formatted = '{} {}'.format(timings[i],classes[i])
            subs.append(formatted)
    return subs

def classes_today():
    subs = find_classes()
    for i in subs:
        time = datetime.now().time()
        time = str(time).split(":")
        if time[0] == i[0:2] and time[1] >= i[3:5]:
            print('\n' + '\t' + i,' <-- Present Session')
        elif time[0] == i[11:13] and time[1] < i[14:16]:
            print('\n' + '\t' + i,' <-- Present Session')
        else:
            print('\n' + '\t' + i)

def help_menu():
    print('\n\t --->>> AUTOMATING GOOGLE CLASSROOM V 1.0 <<<---')
    print('\n\t COMMAND                  DESCRIPTION')
    print('\n\t class [-a or automate]   To automate')
    print('\n\t class [-h or help]       To see this menu')
    print('\n\t class [subject_name]     To open subject_name\'s link')
    print('\n\t class [-t or today]      To see today\'s classes')

def open_link(url):
    webbrowser.open(url)
    print('opened requested page')
