# Takes number of stops: n and returns the
# list of all the route segments needed.
def get_stops(n):
	stops = range(n)
	midpoint = int(len(stops)/2)
	return get_stops_helper(stops[:midpoint])
		 + get_stops_helper(stops[midpoint:]) 


def get_stops_helper(stops):
	if len(stops) == 2: # base case from 1a.
		return (stops[0], stops[1])
	else:
		new_segments = []
		for i in range(len(stops): 
			# from 1b (O(n) stops) are added
			new_segments.append(stops[0], stops[i])
		midpoint = int(len(stops) / 2) 
		# only the lower half of the stops needs additional connectors!
		return new_segments + get_stops_helper(stops[:midpoint)
		# recursive add to list
