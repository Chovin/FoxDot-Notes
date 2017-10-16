Clock.bpm=110 # make sure to set tempo FIRST
Scale.default = 'minor'
Clock.meter = (3,5) # this is needed in or else it goes off beat
from random import choice
chords = {
    'i'   : [0,2,4],
    'v'   : [-.5,1,4],  # are we in the wrong scale? :P
    'vi'  : [0,2,5],   
    'iv'  : [0,3,5],
    'viio': [-.5, 1, 3],
    'n6'  : [.5, 3, 5]
}
progression = {
 'i'   : ['v','iv','vi','viio','n6'], 
 'iv'  : ['i'],
 'vi'  : ['iv'],
 'v'   : ['i','vi'],
 'viio': ['i'],
 'n6'  : ['viio','i']
 # -3 : [0]
}
melodies = [{'note': [0,0], 'dur': [5/2, 1/2]}, 
            # {'note': [0,1], 'dur': [3/2, 3/2]}, 
            # {'note': [-2,1,1], 'dur': [1, 1, 1]},
            # {'note': [7], 'dur': [3]}
            ] 
cdeg = 'i'
chord = chords[cdeg]
def prog():
    global pat_i
    global chord
    global cdeg
    Clock.schedule(prog)
    cell = choice(melodies)
    print(chord)
    p2 >> piano(chord, room=1, verb=.3, oct=4)
    p3 >> pluck(chord[0], dur=cell['dur'], amp=.5, room=.5, oct=6).stop() + cell['note']
    cdeg = choice(progression[cdeg])
    chord = chords[cdeg]


Clock.schedule(prog)
