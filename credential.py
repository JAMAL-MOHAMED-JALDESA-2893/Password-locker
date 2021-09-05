# Class Credentials class that create new instance of credential
class Credential:

    credential_list = [] # Empty list: credential static variable

    def __init__(self, first_name, last_name, user_name, password, email):
        '''
        __init__ method help us define the properties of our object        
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email
    
    def save_credential(self):        
        '''
       this method saves credential objects into credential_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        this method deletes credentials saved in the credential_list
        '''
        Credential.credential_list.remove(self)
    
