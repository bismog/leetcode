#!/usr/bin/env python

garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel'


def rake(garden):
    particle = garden.split()
    # out = ''
    for i in range(len(particle)):
        if particle[i] != 'gravel' and particle[i] != 'rock':
            particle[i] = 'gravel'
            # out = out.join(' gravel ')
        # else:
        #     out = out.join(particle[i])
    return ' '.join(particle)

if __name__ == "__main__":
    out = rake(garden)
    print out
