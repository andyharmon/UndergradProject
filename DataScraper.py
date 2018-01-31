from GetVenues import get_venues
from GetTips import get_tips

CLIENT_ID = 'TL23INJGO0B40GXYB040G1LXKSQ0JSP5IE010VTWTCHWZEQO'
CLIENT_SECRET = 'UYZWK4UKLKPG2OY54M4MCKMRGVDZJHGRP0OCE5UV44FQF1C5'

venue_list = get_venues(CLIENT_ID, CLIENT_SECRET)
tip_list = []

for venue in venue_list:
    tip_list = tip_list + get_tips(CLIENT_ID, CLIENT_SECRET, venue.id)

print('there are ' + str(len(tip_list)) + ' tips')
