#program for an Instagram Account System using Encapsulation.
class InstagramAccount:
    def __init__(self,account_name,password):
        self.account_name=account_name
        self._private_reels=[]
        self.__archived_reels=[]
        self.__password=password

    def add_private_reels(self,reel):
         self._private_reels.append(reel)

    def display_private_reels(self,isfollower):
        if isfollower:
            print("private reels are")
            for reel in self._private_reels:
                print(reel)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reels(self,reel):
        self.__archived_reels.append(reel)

    def display_archived_reels(self,password):
        if password==self.__password:
            print("archived reels are:")
            for reel in self.__archived_reels:
                print(reel)
        else:
            print("Access Denied! Only account holder can view archived reels")
    def get_archived_reels(self,password):
        if password==self.__password:
            return self.__archived_reels
        else:
            print("Access denied")
    def set_password(self,old_password,new_password):
        if old_password==self.__password:
            self.__password=new_password
            print("Password updated")
        else:
            print("Cannot update password")

account=InstagramAccount("Roja",1234)
account.add_private_reels("singing reels")
account.add_private_reels("Dancing reels")

account.add_archived_reels("School reels")
account.add_archived_reels("College reels")

account.display_private_reels(True)
account.display_private_reels(False)

account.display_archived_reels(1234)
account.display_archived_reels(12345)

account.set_password(1234,4321)
account.display_archived_reels(4321)



