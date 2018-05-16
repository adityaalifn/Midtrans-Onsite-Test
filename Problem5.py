bus_schedule = [
    "Bus 1 A 10:00 D 10:05",
    "Bus 2 A 10:05 D 10:15",
    "Bus 3 A 10:10 D 10:30",
    "Bus 4 A 10:25 D 10:40",
    "Bus 5 A 10:45 D 10:50"
]

inside_station = []

for schedule in bus_schedule:
    depature = schedule.split("D")[-1]
    arrival = schedule.split("D")[-0].split("A")[-1]
    bus_name = schedule.split("A")[0]
    inside_station.append({"B": bus_name, "A":arrival, "D": depature})
print(inside_station)