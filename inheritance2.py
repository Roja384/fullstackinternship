#program for a Smartphone System using Multiple Inheritance

class camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality
    def display_camera_details(self):
        print("The camera quality is:",self.camera_quality)

class musicplayer():
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality
    def display_music_details(self):
        print("The quality of the music player is:",self.sound_quality)
class smartphone(camera,musicplayer):
    def __init__(self,brand,camera_quality,sound_quality):
        self.brand=brand
        camera.__init__(self,camera_quality)
        musicplayer.__init__(self,sound_quality)

    def display_smartphone_details(self):
        print("the brand of phone is:",self.brand)
        self.display_camera_details()
        self.display_music_details()
myphone=smartphone("samsung","good","high")
myphone.display_smartphone_details()