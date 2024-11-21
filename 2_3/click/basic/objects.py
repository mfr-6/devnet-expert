class Router():
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    
    def __str__(self):
        return f"Router({self.name}, {self.ip})"
    
    def cmd(self, command):
        return f"I'm {self.name} and you just invoked <{command}> against me!"
    
    def show_version(self):
        return "Version: 16.12.1"
