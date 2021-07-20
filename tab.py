from tab_helper import *


riff1a = [
    {6: 0},
    {5: '3h5'},
    {4: 3},
    {5: 5},
    {5: 3},
    {5: '0h3h0'},
    {6: 5},
    {5: 0},
    {6: 5},
    {6: 3}
]

riff1b = riff1a[:6] + [
    {5: 3, 4: 5}, REST,
    {5: 4, 4: 6}, REST
]

riff1c = riff1a[:4] + [
    {4: 3},
    {4: '5b6r5p3'},
    {4: '5p3'},
    {5: 4}
]

riff1 = section_builder([riff1a, riff1b, riff1a, riff1c], title='\nIntro Riff\n')

riff2a = [
    {6: 0, 5: 0}, REST,
    {6: 'x'},
    {6: 'x'},
    {5: '3h5'}, REST,
    {6: 0}, REST,
    {6: 'x'},
    {6: '3h5'},
    {5: '3p0'},
    {6: 3, 5: 3, 4: 3}
]

riff2b = riff2a[:9] + [
    {5: 3, 4: 5},
    {5: 2, 4: 5},
    {6: 3, 5: 3, 4: 3},
]

riff2c = riff2a[:9] + [
    {4: '5b6r5p3'},
    {4: '5p3'},
    {5: 5}
]

riff2 = section_builder([riff2a, riff2b, riff2a, riff2c], title='\nVerse Riff\n')

riff3a = [
    {6: 5, 5: 5, 4: 5},
    {6: 5, 5: 5, 4: 5}, REST,
    {4: 5},
    {4: 3},
    {5: 5},
    {4: 3},
    {5: 5},
    {5: 3}
]

riff3b = riff3a[:6] + [
    {5: 3},
    {5: 0},
    {6: 3, 5: 3},
]

riff3 = section_builder([riff3a, riff3b], title='\nPre Chorus Riff\n')

chorus1 = [
    {6: 0, 5: 0, 4: 0},
    {4: 0, 3: 2, 2: 3, 1: 2}, REST,
    {5: 3, 4: 2, 3: 0, 2: 3, 1: 3}, REST,
    {5: 2, 4: 0, 3: 0, 2: 3, 1: 3},
    {6: 3, 5: 3, 4: 3}
]

chorus2 = chorus1[:-1] + [
    {5: 3, 4: 2, 3: 0, 2: 3, 1: 3}
]

chorus = section_builder([chorus1, chorus2, chorus1, chorus1[:4] ], title='\nChorus Chords\n')

bridge1 = [
    {-1: '\nBridge Guitar 1\n'},
    {5: 5, 4: 7, 3: 7}, REST,
    {5: 3, 4: 5, 3: 5}, REST,
    {5: 5, 4: 7, 3: 7}, REST
]

bridge2 = [
    {-1: '\nBridge Guitar 2\n'},
    {3: 10, 2: 10, 1: 10}, REST,
    {3: 7, 2: 8, 1: 8}, REST,
    {3: 10, 2: 10, 1: 10}, REST
]

riff4a = [
    {6: 0}, REST,
    {5: '3h5'},
    {5: '3h5'}, REST,
    {6: '0h3h5'},
    {5: '0h3p0'},
    {6: 5},
    {6: 0},
    {6: 3}
]

riff4b = riff4a[:5] + [
    {4: 3},
    {5: 5},
    {4: 5},
    {4: 3},
    {5: 5},
    {5: 3},
    {5: 0},
    {6: 3}
]

riff4 = section_builder([riff4a, riff4b], title='\nBridge End Riff\n')

riff5 = section_builder([riff1a, riff1b, [{5: 5, 4: 7}]], title='\nOutro Riff\n')

full_tab = riff1 + riff2 + riff3 + chorus + bridge1 + bridge2 + riff4 + riff5
