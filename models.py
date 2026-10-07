class Location:

    def __init__(self,name, latitude, longitude): #创建旅行地点
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"{self.name}({self.latitude}, {self.longitude})"

class Trip:
    
    def __init__(self, userid,name,startdate,enddate): #创建旅行计划
        self.userid = userid
        self.name = name
        self.startdate=startdate
        self.enddate=enddate
        self.locations = []


    def add_location(self, location): #添加旅行地点
        if not location.name.strip():
            return "Location name cannot be empty."
        if not isinstance(location.latitude, (int, float)):
            return "Latitude must be a number."
        if not isinstance(location.longitude, (int, float)):
            return "Longitude must be a number."
        for existing_location in self.locations: #防止重复地点
            if location.name ==existing_location.name:
                return f"{location.name} is already in the trip."
        self.locations.append(location)
        return f"{location.name} has been added to the trip."

    def show_locations(self): #查看地点
        lines = [f"Trip(name={self.name})"]
        for index, location in enumerate(self.locations, start=1):
            lines.append(f"{index}. {location}")
        return "\n".join(lines)

    def remove_location(self, location_name): #删除旅行地点
        for location in self.locations:
            if location.name == location_name:
                self.locations.remove(location)
                return f"{location_name} has been removed from the trip."
        return f"{location_name} not found in the trip."


    def find_location(self, location_name): #查找旅行地点
        for location in self.locations:
            if location.name == location_name:
                return location
        return None
