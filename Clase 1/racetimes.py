import json

runners = ["Hanna", "Jackie", "Kimberly"]
stats = {}
track_lenght = 100

for runner in runners:
	print(f"-------[{runner}]-------")
	new_runner = {}  # Init Runner's stats

	# Time fields to request from user and where to store that
	times = ["minutes", "seconds", "miliseconds"]
	store = {}

	# Request each runner's times and store them in store, then add to the "Times" field in runner's stat

	for time in times:
		store[time] = float(input(f"{runner}'s {time}: "))

	new_runner["times"] = store

	# Calculate total seconds for runner, store to "seconds" in stats
	new_runner["seconds"] = new_runner["times"]["minutes"] * 60 + new_runner["times"]["seconds"]

	# Calculate average speed in meters per second as per seconds / 100
	new_runner["avgSpd"] = new_runner["seconds"] / track_lenght
	# Upload stats to Runners
	stats[runner] = new_runner
	print("\n\n")

print("----->Race Times!<-----")
for i in stats:
	runner = stats[i]
	
	print(
	f"""
	---[{i}'s stats]---
	With an average speed of {runner["avgSpd"]} meters per second, she finished the {track_lenght} meters track in {runner["times"]["minutes"]} minutes, {runner["times"]["seconds"]} seconds and {runner["times"]["miliseconds"]} miliseconds
	
	That's {runner["seconds"]} whole seconds, ladies and gentlemen!

	"""
	)

