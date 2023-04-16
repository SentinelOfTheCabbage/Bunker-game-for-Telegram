class User():

    def __init__(self, user_id):
        self.user_id = user_id
        self.role = None

    def set_defaults(self, **kwargs):
        self.reproduction = kwargs['reporduction']
        self.phobies = kwargs['phobies']
        self.secure = kwargs['secure']
        self.earner = kwargs['earner']
        self.builder = kwargs['builder']
        self.engineer = kwargs['engineer']
        self.doctor = kwargs['doctor']
