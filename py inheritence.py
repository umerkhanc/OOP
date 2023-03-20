class father():
    def skills(self):
        print('gardening, programming')
        
class mother():
    def skills(self):
        print('cooking, art')

class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print('sport')
c=child()
c.skills()
        