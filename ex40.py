#initializing class
class Song(object):
    #initializing newly created empty object
    def __init__(self, lyrics):
        #assigning the parameter to instance variable. so that every instance of song will have a attribute store the lyrics passed
        self.lyrics = lyrics
     #fuction to print the lines   
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
#first instance creating and passing few lines
happy_bday = Song(["Happy birthday to you", 
                   "I don't want to get sued", 
                   "So I'll stop right there"])

# second instance creating and passing the string
bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

##calling the method
happy_bday.sing_me_a_song()

#calling the second method
bulls_on_parade.sing_me_a_song()