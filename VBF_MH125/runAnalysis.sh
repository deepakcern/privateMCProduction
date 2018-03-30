#### FRAMEWORK SANDBOX SETUP ####
# Load cmssw_setup function
source cmssw_setup.sh
 
# Setup CMSSW Base
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
 
# Download sandbox
wget --no-check-certificate "http://stash.osgconnect.net/+deepakk/sandbox-CMSSW_9_3_7-7396694.tar.bz2"
 
# Setup framework from sandbox
cmssw_setup sandbox-CMSSW_9_3_7-7396694.tar.bz2
 
 
cd $CMSSW_BASE

cmsenv

#chmod +x scriptExe.sh

sleep 1.1

. scriptExe.sh

exitcode=$?
exit $exitcode
