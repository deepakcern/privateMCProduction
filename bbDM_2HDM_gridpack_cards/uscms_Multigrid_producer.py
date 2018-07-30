# import ROOT
# from math import pi, sqrt, copysign
# from ROOT import TH1F, TFile, TTree, TString, gSystem, gROOT, AddressOf, TLorentzVector, TVector, TMath
import sys
import os
# import numpy as np

verbose = False
#cardsPath = sys.argv[1]
# model = sys.argv[1] # either 2hdm or zpb

cardsPath = 'cards/examples/'
# gridpoint = 'MH3_600_MH4_XX_Mchi_YY'
prefix    = 'bbDM_2HDMa_MH3_600_MH4_XX_Mchi_YY'

d_cardspath = os.path.join(cardsPath, prefix)


if verbose: print (d_cardspath)

d_run_card       = os.path.join(d_cardspath, prefix +'_run_card.dat')
d_proc_card      = os.path.join(d_cardspath, prefix +'_proc_card.dat')
d_extramodels    = os.path.join(d_cardspath, prefix +'_extramodels.dat')
d_customizecards = os.path.join(d_cardspath, prefix +'_customizecards.dat')
d_cutcards       = os.path.join(d_cardspath, prefix +'_cuts.f')

# print ()

#
if verbose: print (d_run_card, d_proc_card, d_extramodels, d_customizecards)




def change_cards(d_cardname, cardname, MH4, Mchi):
    f    = open(d_cardname, 'r')
    fout = open (cardname, 'w')
    for line in f:
        line = line.replace('XX', str(MH4))
        line = line.replace('YY', str(Mchi))
        fout.write(line)
    fout.close()
    print ("Cardname",cardname)




def submitgrid(MH4, Mchi):
    cardspath = d_cardspath.replace("XX",str(MH4)).replace("YY",str(Mchi))
    print ("cardpath",cardspath)
    os.system('mkdir '+cardspath)

    run_card       = d_run_card.replace("XX",str(MH4)).replace("YY",str(Mchi))
    proc_card      = d_proc_card.replace("XX",str(MH4)).replace("YY",str(Mchi))
    extramodels    = d_extramodels.replace("XX",str(MH4)).replace("YY",str(Mchi))
    customizecards = d_customizecards.replace("XX",str(MH4)).replace("YY",str(Mchi))
    cutcards = d_cutcards.replace("XX",str(MH4)).replace("YY",str(Mchi))

    change_cards(d_run_card, run_card, MH4, Mchi)
    change_cards(d_proc_card, proc_card, MH4, Mchi)
    change_cards(d_extramodels, extramodels, MH4, Mchi)
    change_cards(d_customizecards, customizecards, MH4, Mchi)
    change_cards(d_cutcards, cutcards, MH4, Mchi)

    outdir = prefix.replace("XX",str(MH4)).replace("YY",str(Mchi))
    print ("output dir",outdir)
    os.system('nohup ./submit_cmsconnect_gridpack_generation.sh  '+ outdir +' '+ cardspath +'  4 "4 Gb" > mysubmit_'+outdir+'.debug 2>&1 &')
    #print ("12000 12000 2nw  outdir  cardspath   8nh")


MH4=[50,100,350,400,500,900]
Mchi=[1,10]

for i in Mchi:
    for j in MH4:
        mh4=j
        mchi=i
        print ("Mchi= ", mchi, "MH4= ",mh4)
        submitgrid(mh4, mchi)
