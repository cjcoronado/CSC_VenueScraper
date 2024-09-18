def extract_event_name(event_name_lines, guest_lines):
    if event_name_lines is not None:
        full_name = event_name_lines.get_text().strip()
        location_and_event = full_name.split(" @", 1)
        events_and_guests = location_and_event[0].replace(' / ', ', ')

        if " w/ " in events_and_guests:
            event_and_guests_split = events_and_guests.split(" w/ ")
        elif " with " in events_and_guests:
            event_and_guests_split = events_and_guests.split(" with ")
        elif " feat. " in events_and_guests:
            event_and_guests_split = events_and_guests.split(" feat. ")
        else:
            event_and_guests_split = [events_and_guests]

        main_event = event_and_guests_split[0].replace(' Album Release Show', '')
        if ' – ' in main_event:  # new condition to handle ' – ' in the event name
            main_event = main_event.split(' – ')[0]

        guests = ', '.join([guest.strip() for guest in event_and_guests_split[1].split(", ") if guest.strip()]) if len(
            event_and_guests_split) > 1 else ''
        guests = guests.strip()

        if guest_lines is not None:
            extras = guest_lines.get_text().strip()
            if extras.startswith('w/ '):
                extras = extras[3:]
            if guests:
                guests += ', '
            guests += extras

        guests = guests.rstrip(', ')  # Remove any trailing commas and spaces

        event_name = f"{main_event}, {guests}" if guests else main_event

        if len(location_and_event) > 1:
            event_name += " @" + location_and_event[1]
    else:
        event_name = "Unknown Event"

    event_detail = f"{event_name} @ Local 506"
    return event_detail
