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
   