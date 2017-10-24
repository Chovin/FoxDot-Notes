# Jam sesh 10/24/2017

print(SynthDefs)

Scale.default = 'minor'

Root.default.set(-1)

print(Clock)

Group(p1,p2,b2,z1,s2,r1,b1).lpf=0

Clock.bpm = 200


 # I imagine everyone in the club would be so confused

tip() # better

countDown(p1) # wtf ?

resume(p1)


# @nextBar # <-- you're nextbaring it you could try, but not sure if it'll work like that
def countDown(plyr):
    Clock.bpm = 120
    plyr.amplify=0
    s2.amplify=1.5
    Group(p1,p2,b2,z1,s2,r1,b1).lpf=800
    v1.every(16, 'stutter', 3, amp=0, degree=[9,8])
    p2 >> play("1 2 3 4 ") # nice # 8 beats  # it was an honor clubbing with you lol

def tip():
    #p2.stop() # why im not sure.. I think im hearing osmething # one at a time
    p2 >> play("1 2 1234") # 8 beats # make sure you match the beats okay

# not bad    # lol one more time and then lets start a new one
# we're going to be writing these from scratch right? building them up.
# we'll have notes out I assume # yup # we'll be...live

def resume(plyr):
    p2.stop()
    v1.every(16, 'stutter', 3, degree=[9,8])
    plyr.amplify=1 #nice ty
    Group(p1,p2,b2,z1,s2,r1,b1).lpf=0
    # play plyr why are you stopping it then # im stopping the count, then Im resuming a different player called plyr 
    # define resuming meaning that player object was stopped prior to countDown() you could not stop it huh?
# btw, we should do this at A-Club too
# sure if jasper's good with it

# you know, we have volume settings. we don't need to make everything amp 5 lol
# hey how do I resume a player object individually again? idk what you mean


p1 >> play(P["V x XYY "] & "V o XYY ", amp=5, verb=1, dur=.25, sample=var([1,2],[1])) # there a proper club beat # that was good .25 # naw the base need to stay the same # is that what you were trying to do? # oh my bad # not really but that sounds aight

p1 >> play(P["V o oXYo"], amp=5, verb=1, dur=.25, sample=var([1,2],[1])) # there a proper club beat # that was good .25 # naw the base need to stay the same # is that what you were trying to do? # oh my bad # not really but that sounds aight

p1.stop()

p1 >> play(P["V o oYYo"] & "V o XYY ", amp=5, verb=1, dur=.25, sample=var([1,2],[1])) # there a proper club beat # that was good .25 # naw the base need to stay the same # is that what you were trying to do? # oh my bad # not really but that sounds aight


p2 >> play(" J(WE)", dur=PDur(5,8), amp=5, verb=1)

# idk horrible :/

b2 >> blip(P[:8]/8, dur=.25, amp=5) #.stop()


p2 >> play("---")

# idk bout you, but I always just use the letter that the instrument starts with.
# I run out of letters otherwise

print(SynthDefs)

print(Player.Attributes())

z1 >> zap([0,2,3,4,3,2,3,2,1,4,2,0], dur=PDur([5,3],8), amp=5).every(4, 'stutter')

s1 >> dirt([[0,-1],1], dur=1, sus=var([0,1],[6]), oct=5) # we suck at club music
# kek

b1 >> bass([0,1], dur=4 ,vib=2)

v1 >> saw([6,7], chop=32, dur=[2,6],amp=10).every(16, 'stutter', 3, amp=0, degree=[9,8])

# i think it's the play2 object. Not sure where it is though

# there's a synth that's off time. Not sure which is that # I don't hear anything

s2 >> fuzz([5,3,3,5,8,5], dur=[1,.5,.5,1,.5,.5], amp=2.3) # haha

r1 >> rave([5,4,], dur=PDur([2,6],8)).stop() # lol # this is so bad # club for clowns


l1 >> crunch().follow(r1)  # sorry, zoning out :P # thinking of how to make a melodic but ballsy sound for club

d1 >> dub()
