
import FWCore.ParameterSet.Config as cms


process = cms.Process("TEST")
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.DQM.collectorHost = ''
process.load("FWCore.Modules.logErrorHarvester_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cff")
process.load("Configuration/StandardSequences/RawToDigi_cff")
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/Reconstruction_cff")

process.GlobalTag.globaltag = "STARTUP31X_V1::All"
process.prefer("GlobalTag")
#process.Tracer = cms.Service("Tracer")

process.load("DQMServices.Components.DQMLogError_cfi.py")

process.dqmSaver.workflow = cms.untracked.string('/workflow/for/mytest')



process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)


process.source = cms.Source("PoolSource",                          
                            fileNames = cms.untracked.vstring(
    "rfio:/castor/cern.ch/cms/store/relval/CMSSW_3_1_1/RelValTTbar/GEN-SIM-DIGI-RAW-HLTDEBUG/STARTUP31X_V1-v2/0002/8AFB2138-ED6B-DE11-AC45-000423D6A6F4.root"

    )
                            
)



process.p = cms.Path(process.RawToDigi*process.reconstruction*process.logErrorHarvester*process.logErrorDQM + process.dqmSaver)

