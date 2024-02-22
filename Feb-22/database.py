
import json

class Database:
    contacts = {}
    
    def __init__(self, db_filename) -> None:
        self.db_filename = db_filename
        db = open(db_filename, encoding="utf8")
        self.contacts = json.load(db)
        db.close()
        
    def get_name(self, ip:str):
        for key, val in self.contacts.items():
            if ip == val:
                return key
        return None
    
    def get_ip(self, name:str):
        if name in self.contacts:
            return self.contacts[name]
        return None
        
if __name__ == '__main__':
    test = Database('contacts.json')
    print(test.get_name("192.168.110.205"))
    print(test.get_ip("аян"))
    