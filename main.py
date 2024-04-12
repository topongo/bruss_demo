import requests

CONFIG = {
    "schema": "http",
    "host": "localhost",
    "port": 8000,
    "base": "/api/v1"
}

def bruss_get(url, query):
    return requests.get("{schema}://{host}:{port}{base}{url}".format(url=url, **CONFIG), params=query).json()

def bruss_post(url, query):
    return requests.post("{schema}://{host}:{port}{base}{url}".format(url=url, **CONFIG), data=query).json()

def select_from_list(ls, q):
    while True:
            try:
                if 0 <= (index := int(input(q))) < len(ls):
                    return index 
                else:
                    print(0 >= index, index > len(ls))
                    print("Value out of range!")
            except ValueError:
                print("Not a number!")


if __name__ == "__main__":
    while (inp := input("Stop or route? ")) not in ("stop", "route"):
        pass
   
    if inp == "stop":
        search = input("Search for? ")
        stops_list = bruss_get("/map/stops", {})
        results = []
        for n, s in enumerate((s for s in stops_list if search.lower() in s["name"].lower())):
            print(f"{n:3d}: {s['name']} ({s['id']})")
            results.append(s)

        si = select_from_list(results, "Select a stop: ") 
        
        stop = results[si]
        print(f"Selected stop: {stop}")

        stops = {"u": {}, "e": {}}
        for s in stops_list:
            stops[s["type"]][s["id"]] = s

        trips = bruss_get(f"/map/trips_stop", {"stop": stop['id'], "type": stop['type']})
        for n, t in enumerate(trips):
            # print(t)
            print(f"{n:3d}: {t['headsign']} ({t['id']})")

        ti = select_from_list(trips, "Select a trip: ") 

        trip = trips[ti]




