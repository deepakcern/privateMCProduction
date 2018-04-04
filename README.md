# privateMCProduction

## PHASE-II VBFH Production:

### 1. CMSSW release
First we need to release required CMSSW. To release CMSSW , follow these commands:

```source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
scram p CMSSW CMSSW_9_3_7
cd CMSSW_9_3_7/src
eval `scram runtime -sh`
```
### 2. Copy Pythia Hadronization File
Pythia hadronization file will depend on your process and decay modes.Please use correct hadronization file.

```curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-PhaseIISummer17wmLHEGENOnly-00020 --retry 2 --create-dirs -o Configuration/GenProduction/python/HIG-PhaseIISummer17wmLHEGENOnly-00020-fragment.py```

(You can find official pythia hadronization file from McM page)
```
scram b
```
### 3. Generating GENSIM File
To get GENSIM file please follow these cammands:
```
cd ../../
cmsDriver Configuration/GenProduction/python/HIG-PhaseIISummer17wmLHEGENOnly-00020-fragment.py --fileout file:step1.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_upgrade2023_realistic_v5 --beamspot HLLHC14TeV --step LHE,GEN,SIM --geometry Extended2023D17 --era Phase2_timing --python_filename step1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cp step1.py CMSSW_9_3_7/src
cd CMSSW_9_3_7/src
cmsenv
cmsRun step1.py
```

After this step you will get GENSIM file for 10 events.

### 4. Generating DIGIRECO File
```
cd ../../
cmsDriver step1 --filein file:step1.root --fileout file:step2.root --mc --eventcontent FEVTDEBUGHLT --pileup NoPileUp --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW --conditions 93X_upgrade2023_realistic_v5 --beamspot HLLHC14TeV --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake --nThreads 4 --geometry Extended2023D17 --era Phase2_timing --python_filename step2.py --no_exec -n 10

cp step2.py CMSSW_9_3_7/src
cd CMSSW_9_3_7/src
cmsenv
cmsRun step2.py
```

After this step you will get step2.root file for 10 events.
```
cd ../../
cmsDriver step2 --filein file:step2.root --fileout file:step3.root --mc --eventcontent RECOSIM --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --conditions 93X_upgrade2023_realistic_v5 --beamspot HLLHC14TeV --step RAW2DIGI,L1Reco,RECO --nThreads 4 --geometry Extended2023D17 --era Phase2_timing --python_filename step3.py --no_exec -n 10

cp step3.py CMSSW_9_3_7/src
cd CMSSW_9_3_7/src
cmsenv
cmsRun step3.py
```

After this step you will get step3.root file for 10 events.

### 5. Generating MINIAOD File
```
cd ../../
cmsDriver step1 --filein file:step3.root --fileout file:MiniAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 93X_upgrade2023_realistic_v5 --step PAT --nThreads 4 --geometry Extended2023D17 --era Phase2_timing --python_filename MiniAod_10.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cp MiniAod_10.py CMSSW_9_3_7/src
cd CMSSW_9_3_7/src
cmsRun MiniAod_10.py
```
After this step you will get MINIAOD file for 10 events

# Submit Crab Job
## GENSIM production 
To produce GENSIM file, you need to modify two files `privateproduction.sh` and `crabconfig_draft.py` according to user.

To check script locally, do `USECRAB="False"` inside the script `privateproduction.sh` and run this command:
```
. privateproduction.sh
```
To submit crab job, do `USECRAB="True"` inside the script `privateproduction.sh` and run this command:
```
. privateproduction.sh
```
#### We will update soon for miniAOD production using crab job

# Submit Condor Job
## Optional step
Check locally using these commands:

```
git clone https://github.com/deepakcern/privateMCProduction.git
cd privateMCProduction
. runAnalysis.sh
```
# Submitting Condor Job
```
condor_submit analysis.submit
```
(We will update condor job script soon)

