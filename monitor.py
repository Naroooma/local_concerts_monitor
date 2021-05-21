from event_parser import *
from monitor_file_handler import *

# returns list of url from file
def fetch_urls(file_name):
    return

# compares new events_list and list in monitor file, returns bool and possible new events
def check_update():
    return

# sends email if a concert was found
def notify_concert(event, name, url):
    return


while True:
    urls = fetch_urls()

    for name, url in urls:
        # if monitor file doesn't exist
        create_monitor_file()
        # else
        new_events = events_list_site(url)
        old_events = events_list_file(url)
        updated, new_events = check_update()

        # if site has been updated
        if updated:
            # update monitor file
            update_monitor_file(site_name, new_events)

            # iterate over new events
            for event in new_events:
                # if new event is concert
                if is_concert(event)
                    # notify me about the concert
                    notify_concert(event, name, url)
