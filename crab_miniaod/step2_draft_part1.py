# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step1 --fileout file:step2.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename step2.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 500
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2_timing)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(#NUMBEREVENTS#)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*("	
