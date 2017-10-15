# prog huh. We doing progressive metal?
# kek. chord progressions, btw
# so where's your transcription?

Scale.default = 'minor'
Clock.bpm = 110

from random import choice, randint

pat_i = 0
                                                      # v and this one starts with 0 instead of 2
p1 >> piano([0,2,4, 0,3,5, -3, -2, 0]) # wtf  # "ii" : [0,3,5]  # "i" : [0,2,4] # "?" : [3,5,7.5] #< like this is outside our scale

# anyways, I gotta call it a night. :thumbsup:. gnight o/ 
# okay. I'll try to read up and learn more tomorrow
p
# if you're still there, do you hear it going up as well?
# -1.5 gets really high # ugh... >.>
# definitely. What are u up to?
# trying to get the notes of the chords. cause it's not playing the right note just by playing the base note +2, +4
pat = [[-2,-3], [5,3,1,0], PTri([0,3])]
pats = ['Marco', 'is', 'salty']
# dude. This is the best representation for the key of the song. 
# Like 1 chord: [1,2,3], 5 chord; [1,64]
# the [1,2,3] lists aren't chords though, they are the next chord to play.
# I broke it cause I took out 2

progression = {
 0  : [3,-3, -2, 4, 5], 
 3  : [0],
 4  : [0, 5],
 5  : [3],
 -2 : [0, -3], #what does -3 play? -3 chord. which is... 7-3 == 4 chord, but cause programming is 0 indexed, it's the 5th chord "V" mm i see
 -3 : [0]
}
melodies = [{'note': [0,0], 'dur': [5/2, 1/2]}, # sets? # naw, jus tnot done writing lol :P uno momento
            {'note': [0,1], 'dur': [3/2, 3/2]}, 
            {'note': [-2,1,1], 'dur': [1, 1, 1]}] # I'mma look back at that video :P

# we can make it more complicated. instead of using this to determine base note movement,
# we can use this to determine MOVEMENTS
# prelude > [chorus, blah blah, blah, flourish, blah] > finale
# yeah thats a great idea. That way we can just sit back
# I mean it's cool, but for the performance, we probably wanna be a little more active in its development.
# lol # sorry I kinda took over the sesh. this has been on my mind for the whole weekend
# it's cool I learned alot. Well..about patterns and stuff. Idk what's happening right now
# lol want me to explain? Nah it's fine. Got enough to think about haha
# aight. You should rewatch the Codemania vid w/ andrew once you feel like you wanna take the next step :3
# yeah. And Imma finish the FoxDot tutorial videos. I feel a lack of impromptu coding
# I learned a lof from those foxdot tuts. they're a bit dry though
# brb just gonna prepare for bed :thumbsup: .... I just bought more gear... pshhhh
chord = 0 # < 1st chord is 0
# basically the keys in the dict are played first and the values follow?
# let's walk through it.
# he's a rockstar and we're not yet # close
# pretty good actually
# eya # darnit! I was trying to recreate Andrew's :P
def prog():
    global pat_i
    global chord
    # Clock.schedule(prog, beat=Clock.now() + 3) # what's 4? # good question, thank you
    cell = choice(melodies)
    p2 >> piano(chord, room=1, verb=.3).stop() + [0,2,4]
    p3 >> pluck(cell['note'], dur=cell['dur'], amp=.5, room=.5).stop() + 7 # play the chord
    # choose the next chord. # progression[0] is..? random.choice([1]) is 1
    # it's the exact same thing that the Andrew guy did. It's a Markov Chain of sorts  
    chord = choice(progression[chord])
    print("{}: {}".format(chord,pats[pat_i]))
    pat_i = (pat_i+1)%len(pat)

print(dir(p1))

prog() # < you have to start it

print('hi. my text box is stuck saying marco is salty')

p3.stop()


# haha whoahhhhh. Dictionary jam!
# dude yes! first time it worked
# Temporal Recursion
#lol
# YES!
# what just happened. I froze
# that was basically time travel
# yo check this out (if it works kek)
# niiice!!!
# piano recital :O
# well I just did that to have varying times. no rhyme or reason
# oohhhhhhh. Yeah but what I mean is, it's recursive because it schedule itself again
# and again since you're adding something to current time
# yup!
# does that count as LiveCoding graphics? kek
# oh shoot we could
# we could have scrolling lyrics
# anyways, let's make some music

# woah dude. Idea


var.chords = var([0,1,2,11,15,20], [20,10,30,])

durs = Pvar([[1,.5],[.25]], [8,4]) # hmmm



patterns = Pvar([[(2,4,8),0],[[7,(5,7)],8,9]],[4,8])


p2 >> pluck(var.chords, dur=durs).stop() + patterns # add it to the main chord and dur
# shoot let's just improv for now with patterns
# aight

# aight, gonna clean up the screen




