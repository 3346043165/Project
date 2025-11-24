import requests
class Base():
    def __init__(self):
        self.session = requests.session()

    def post(self,path,**k):
        return self.session.post(path,**k)
    def put(self,path,**k):
        return self.session.put(path,**k)

    def get(self,path,**k):
        return self.session.get(path,**k)

    def delete(self,path,**k):
        return self.session.delete(path,**k)