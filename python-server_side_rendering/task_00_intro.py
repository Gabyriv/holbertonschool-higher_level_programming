#!/usr/bin/python3
"""Creating a Simple Templating Program"""

import os

def generate_invitations(template, attendees):
    """ Generates invitations for a list of attendees

    Args:
        template (str): The template to use for the invitations.
        attendees (list): A list of attendees.
    """

    try:
        if not isinstance(template, str):
            raise TypeError('template must be a string')

        if not isinstance(attendees, list):
            raise TypeError('attendees must be a list')

        if not all(isinstance(attendee, dict) for attendee in attendees):
            raise TypeError('attendees must be a list of dicts')

        if len(template) == 0:
            raise ValueError('Template is empty, no output files generated.')

        if len(attendees) == 0:
            raise ValueError('No data provided, no output files generated.')

        for i, attendee in enumerate(attendees, start=1):
            invitation = template

            invitation = invitation.replace('{name}', str(attendee.get('name', 'N/A')))
            invitation = invitation.replace('{event_title}', str(attendee.get('event_title', 'N/A')))
            invitation = invitation.replace('{event_date}',
                'N/A' if attendee.get('event_date') is None else str(attendee['event_date']))
            invitation = invitation.replace('{event_location}', str(attendee.get('event_location', 'N/A')))

            output_file = f'output_{i}.txt'

            if os.path.exists(output_file) == False:
                with open(output_file, 'w') as file:
                    file.write(invitation)

    except Exception as e:
        print(f"Error: {e}")
