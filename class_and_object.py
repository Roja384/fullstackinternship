class instagram():
    def __init__(self,title,description,creator_name,location,likes=0):
        self.title=title
        self.description=description
        self.likes=likes
        self.creator_name=creator_name
        self.location=location
        self.comments=[]
    def display_title(self):
        print("The title of the reel is:",self.title)
    def display_description(self):
        print("The description of the reel is:",self.description)
    def display_creator_name(self):
        print("The creator is:",self.creator_name)
    def display_location(self):
        print("The location is:",self.location)
    def liked(self):
        self.likes+=1
    def unliked(self):
        if self.likes>0:
            self.likes-=1
    def display_likes(self):
        print("The number of likes is:",self.likes)
    def add_comment(self,comment):
        self.comments=self.comments+[comment]
    def display_comments(self):
        print("The comments are :")
        for comment in self.comments:
            print(comment)
    def delete_comment(self):
        if len(self.comments)>0:
            self.comments.pop()

reel1=instagram("dance","dancing with my friends","Roja","Mysore")
reel1.liked()
reel1.add_comment("Good performance")
reel1.add_comment("Good to see")
reel2=instagram("speech","giving speech on republic day","Anil","Bangalore")
reel2.unliked()
reel1.liked()
reel2.add_comment("Very informative")
reel2.liked()
reel1.display_title()
reel1.display_description()
reel1.display_creator_name()
reel1.display_location()
reel1.display_likes()
reel1.display_comments()
reel2.display_title()
reel2.display_description()
reel2.display_creator_name()
reel2.display_location()
reel2.display_likes()
reel2.display_comments()
reel1.delete_comment()
        
    
        
