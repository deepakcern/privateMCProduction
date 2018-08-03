import os
import json
import glob

path='/local-scratch/deepakk/monoH_gridpacks_2016/genproductions/bin/MadGraph5_aMCatNLO/*.log'

files=sorted(glob.glob(path))
fout=open('cross_section.txt','w')
fout.write('mA'+'        '+'ma'+'        '+'mchi'+'        '+'tanb'+'        '+'sinp'+'        '+'initial state'+'        '+'CS(pb)'+'        '+'Uncertainty'+'\n')
for file in files:
    mA=file.split('/')[-1].split('_')[7]
    ma=file.split('/')[-1].split('_')[9]
    mchi=file.split('/')[-1].split('_')[11].split('.')[0]
    tanbeta='1'
    sintheta='0.35'
    f=open(file,'read')
    if 'codegen.log' not in file.split('/')[-1]:
        isCross=False
        for line in f:
            if 'Cross-section' in line:
                xsec=line.split()[2]
                uncert=line.split()[4]
                fout.write(mA+'        '+ma+'        '+mchi+'        '+tanbeta+'        '+sintheta+'              '+'gg'+'              '+xsec+'         '+uncert+'\n')
                isCross=True
        if not isCross:
            print "==========================IncorrectGridpack======================"+'\n'
            print file.split('/')[-1]+'_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'


    f.close()
