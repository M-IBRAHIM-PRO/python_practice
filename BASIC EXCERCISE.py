class electronic_devices:
    usage_in_life="VERY USEFUL"
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def print_details(self):
        return f"The device name is {self.name} and its role is {self.role}."
    @classmethod
    def from_dashes(cls,str):
        return cls(*str.split("-"))
    @staticmethod
    def working_of_device(string):
        print("THE DEVICE "+string+" IS WORKING PROPERLY")
class pocket_gagets(electronic_devices):
    usage_in_daily_life ="A DIRE NEED OF LIFE"
    pass
class phone(pocket_gagets):
    importance_in_life="VERY MUCH IMPORTANT"
fan=electronic_devices.from_dashes("CEILING FAN-TO PROVIDE AIR")
mini_tools=pocket_gagets.from_dashes("PAIR OF SCISSORS-TO CUT SOMETHING & USED IN SURGERY")
infinix=phone.from_dashes("HOT 9-LIKE A MINI COMPUTER")
print(fan.print_details())
print(mini_tools.role)
infinix.working_of_device("BATTERY")