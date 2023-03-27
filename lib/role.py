from .audition import Audition

class Role:
    def __init__(self, character_name):
        self.character_name = character_name
        self.auditions = []

    def add_audition(self, audition):
        self.auditions.append(audition)

    def actors(self):
        return [audition.actor for audition in self.auditions]
    
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition
        print('no actor has been hired for this role.')
    
    def understudy(self):
        hired_auditions =[]
        for audition in self.auditions:
            if audition.hired:
                hired_auditions.append(audition)
        if len(hired_auditions) == 0:
            print('no actor has been hired for understudy for this role')
        if len(hired_auditions) == 1:
            print('no understudy has been hired for this role')
        else:
            return hired_auditions[1]