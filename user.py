class User:   
  
    user_list = [] # empty user list static variable    

    def __init__(self, user_name, email, password):
        '''
        __init__ method that helps us define the property of our object
        '''
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        save_user method save user object and appends it user_list
        '''
        User.user_list.append(self)
   
    @classmethod
    def display_users(cls):
        '''
        display_users is a class method that returns the class list
        '''
        return cls.user_list

    @classmethod
    def display_credential(cls):
        '''
        this method that retuns the list of credential_list
        '''
        return cls.credential_list    
