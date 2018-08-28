from TimeMoneyApp.models import TimeEvent
import datetime
import time

def create_min_list(events):
    ''' TODO:
        have ns be name of the event,
        color hue with event type,
    '''

    event_durations = []
    ns = []
    n = 0

    # process events
    for ue in events:
        time_str = ue.get_event_duration()
        time_str = time_str.split('.')[0]
        time_splt = time.strptime(time_str.split(',')[0], '%H:%M:%S')
        secs = datetime.timedelta(hours=time_splt.tm_hour,
                                  minutes=time_splt.tm_min,
                                  seconds=time_splt.tm_sec).total_seconds()
        mins = secs / 60.0
        event_durations.append(mins)
        ns.append(n)
        n += 1

    return (event_durations, ns)

def fetch_events(events, group):

    if group == 'Date':
        # organize events by date
        return ([],[])
    elif group == 'Day':
        # organize events by day of week
        return ([],[])
    else:
        # no organization
        return create_min_list(events)

