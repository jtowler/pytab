line = [{6: 'l'}]
newline = line + [{6: 'N'}]

riff1a = [
    {6: 0},
    {5: '3h5'},
    {4: 3},
    {5: 5},
    {5: 3},
    {5: '0h3h0'},
    {6: 5},
    {5: 3},
    {6: 5},
    {6: 3}
]

riff1b = riff1a[:6] + [
    {5: 3, 4: 5},
    {6: 'r'},
    {5: 4, 4: 6},
    {6: 'r'}
]

riff1c = riff1a[:4] + [
    {4: 3},
    {4: '5b6r5'},
    {4: '3h5p3'},
    {5: 4}
]

riff1 = riff1a + line + riff1b + line + riff1a + line + riff1c + newline

riff2a = [
    {6: 0, 5: 0},
    {6: 'r'},
    {6: 'x'},
    {6: 'x'},
    {5: '3h5'},
    {6: 'r'},
    {6: 0},
    {6: 'r'},
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
    {4: '5b6r5'},
    {4: '3h5p3'},
    {5: 5}
]

riff2 = riff2a + line + riff2b + line + riff2a + line + riff2c + newline

riff3a = [
    {6: 5, 5: 5, 4: 5},
    {6: 5, 5: 5, 4: 5},
    {4: 'r'},
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

riff3 = riff3a + line + riff3b + line

