#!/bin/bash

export CURDIR=`pwd`

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

if [ -r CMSSW_9_3_7/src ] ; then
 echo release CMSSW_9_3_7 already exists
else
scram p CMSSW CMSSW_9_3_7
fi
cd CMSSW_9_3_7/src
eval `scram runtime -sh`

echo "Copy pythia hadronisation file"

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-PhaseIISummer17wmLHEGENOnly-00020 --retry 2 --create-dirs -o Configuration/GenProduction/python/HIG-PhaseIISummer17wmLHEGENOnly-00020-fragment.py
[ -s Configuration/GenProduction/python/HIG-PhaseIISummer17wmLHEGENOnly-00020-fragment.py ] || exit $?;

scram b
echo "Copy python files and script to workdir"
cp -r $CURDIR/step1.py ./
cp -r $CURDIR/step2.py ./
cp -r $CURDIR/step3.py ./
cp -r $CURDIR/step4.py ./
cp -r $CURDIR/pu.py ./
cp -r $CURDIR/fake.py ./
cp -r $CURDIR/crab.py ./

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step2.log step2.py
echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step2.log step2.py
echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j GenSimAODSim_step3.log step3.py
echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -e -j FrameworkJobReport.xml step4.py
echo "================= CMSRUN finished ====================" | tee -a job.log
