class Location:

    def __init__(self,name, latitude, longitude): #创建旅行地点
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"{self.name}({self.latitude}, {self.longitude})"

class Trip:
    
    def __init__(self, name,startdate,enddate): #创建旅行计划
        self.name = name
        self.startdate=startdate
        self.enddate=enddate
        self.locations = []


    def add_location(self, location): #添加旅行地点
        if not location.name.strip():
            print("Location name cannot be empty.")
            return
        if not isinstance(location.latitude, (int, float)):
            print("Latitude must be a number.")
            return
        if not isinstance(location.longitude, (int, float)):
            print("Longitude must be a number.")
            return
        for existing_location in self.locations: #防止重复地点
            if location.name ==existing_location.name:
                
                print(f"{location.name} is already in the trip.")
                return
        self.locations.append(location)
        print(f"{location.name} has been added to the trip.")

    def show_locations(self): #查看地点
        print(f"Trip(name={self.name}）")
        for index, location in enumerate(self.locations, start=1):
            print(f"{index}. {location}")

    def remove_location(self, location_name): #删除旅行地点
        for location in self.locations:
            if location.name == location_name:
                self.locations.remove(location)
                print(f"{location_name} has been removed from the trip.")
                return
        print(f"{location_name} not found in the trip.")


    def find_location(self, location_name): #查找旅行地点
        for location in self.locations:
            if location.name == location_name:
                print(f"Found: {location}")
                return location
        else:
            print(f"You didn't add {location_name} to the trip yet. Please add it first.")
            return None