
class Audition:
    def __init__(self, actor, location, role):
        self.actor = actor
        self.location = location
        self.hired = False
        self.role = role
        role.add_audition(self)

    def call_back(self):
        self.hired = True

    def assign_role(self):
        return self.role