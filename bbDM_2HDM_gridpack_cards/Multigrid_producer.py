# import ROOT
# from math import pi, sqrt, copysign
# from ROOT import TH1F, TFile, TTree, TString, gSystem, gROOT, AddressOf, TLorentzVector, TVector, TMath
import sys
import os
# import numpy as np

verbose = False
#cardsPath = sys.argv[1]
# model = sys.argv[1] # either 2hdm or zpb

old_cardsPath = 'Templet'
# gridpoint = 'MH3_600_MH4_XX_Mchi_YY'

prefix    = 'bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY'
os.system('mkdir '+ old_cardsPath+'/'+prefix)

os.system('cp '+old_cardsPath+'/'+'run_card.dat'+' '+  old_cardsPath+'/'+prefix+'/bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY_run_card.dat' )
os.system('cp '+old_cardsPath+'/'+'proc_card.dat'+' '+  old_cardsPath+'/'+prefix+'/bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY_proc_card.dat' )
os.system('cp '+old_cardsPath+'/'+'extramodels.dat'+' '+  old_cardsPath+'/'+prefix+'/bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY_extramodels.dat' )
os.system('cp '+old_cardsPath+'/'+'customizecards.dat'+' '+  old_cardsPath+'/'+prefix+'/bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY_customizecards.dat' )
os.system('cp '+old_cardsPath+'/'+'cuts.f'+' '+  old_cardsPath+'/'+prefix+'/bbDM_2HDMa_MH3_AA_MH4_XX_Mchi_YY_cuts.f' )

#cardsPath = os.path.join(old_cardsPath,prefix)
d_cardspath = os.path.join(old_cardsPath, prefix)


if verbose: print (d_cardspath)

d_run_card       = os.path.join(d_cardspath,prefix+'_run_card.dat')
d_proc_card      = os.path.join(d_cardspath,prefix+'_proc_card.dat')
d_extramodels    = os.path.join(d_cardspath,prefix+'_extramodels.dat')
d_customizecards = os.path.join(d_cardspath,prefix+'_customizecards.dat')
d_cutcards       = os.path.join(d_cardspath,prefix+'_cuts.f')

# print ()

#
if verbose: print (d_run_card, d_proc_card, d_extramodels, d_customizecards)




def change_cards(d_cardname, cardname,MH3, MH4, Mchi):
    f    = open(d_cardname, 'r')
    fout = open (cardname, 'w')
    for line in f:
        line = line.replace('AA', str(MH3))
        line = line.replace('XX', str(MH4))
        line = line.replace('YY', str(Mchi))
        fout.write(line)
    fout.close()
    print ("Cardname",cardname)




def submitgrid(MH3, MH4, Mchi):
    cardspath = d_cardspath.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    print ("cardpath",cardspath)
    os.system('mkdir '+cardspath)

    run_card       = d_run_card.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    proc_card      = d_proc_card.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    extramodels    = d_extramodels.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    customizecards = d_customizecards.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    cutcards = d_cutcards.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))

    change_cards(d_run_card, run_card, MH3, MH4, Mchi)
    change_cards(d_proc_card, proc_card,MH3 , MH4, Mchi)
    change_cards(d_extramodels, extramodels, MH3, MH4, Mchi)
    change_cards(d_customizecards, customizecards, MH3, MH4, Mchi)
    change_cards(d_cutcards, cutcards, MH3,MH4, Mchi)

    outdir = prefix.replace("AA",str(MH3)).replace("XX",str(MH4)).replace("YY",str(Mchi))
    print ("output dir",outdir)
    # os.system('nohup ./submit_cmsconnect_gridpack_generation.sh  '+ outdir +' '+ cardspath +'  4 "4 Gb" > mysubmit_'+outdir+'.debug 2>&1 &')
    #print ("12000 12000 2nw  outdir  cardspath   8nh")


MH4=[100,150,200,250,300,350,400,500]
Mchi=[1,10]
MH3=[600,800,1000,1200]

for k in MH3:
    for i in Mchi:
        for j in MH4:
            mh3=k
            mh4=j
            mchi=i
            print ("Mchi= ", mchi, "MH4= ",mh4, "MH3=",mh3)
            submitgrid(mh3, mh4, mchi)
