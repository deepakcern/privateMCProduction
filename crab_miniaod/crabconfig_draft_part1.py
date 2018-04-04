from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromSiteDB
config = Configuration()

name= 'VBFHbb_miniaod'
config.section_("General")
config.General.requestName = "privateMCProductionMiniAOD#REQUESTDATE##WHOAMI#"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
#config.JobType.pluginName = 'PrivateMC'
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_cfg.py'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.scriptExe = 'jobScript.sh'
config.JobType.outputFiles = ['MiniAOD.root','step2.log', 'step3.log', 'FrameworkJobReport.xml', 'job.log']
config.JobType.inputFiles = ['pu.py','jobScript.sh', 'step2_cfg.py', 'step3_cfg.py', 'step4_cfg.py']
config.JobType.maxMemoryMB = 2400
config.JobType.numCores = 4
config.section_("Data")
#config.Data.outputPrimaryDataset = 'privateMCProductionAODSIMMiniAOD'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 800
config.Data.unitsPerJob = 1
#config.Data.totalUnits = #NUMBEREVENTS#
config.Data.publication = True
config.Data.outputDatasetTag = 'eventMiniAOD-#BASENAME#'
config.Data.inputDBS = 'phys03'
## T3 Beijing
config.Data.ignoreLocality = True
config.Data.outLFNDirBase = '/store/user/%s/t3store2/VBFHbb_miniaod/' % (getUsernameFromSiteDB())
## T3 Beijing
#config.Data.userInputFiles =[
config.Data.inputDataset = ('
