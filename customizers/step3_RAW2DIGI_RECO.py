# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:C1485BE1-0EDC-1448-9C59-9F1102535604.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from offline_v6_1_customizer import *

process = cms.Process('RECO',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step2.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

#process.dump =cms.EDAnalyzer('EventContentAnalyzer')
#process.dumper = cms.EndPath(process.dump)

process=customize_TRK_v6_1(process)

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_full.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.load( "HLTrigger.Timer.FastTimerService_cfi" )
# print a text summary at the end of the job
process.FastTimerService.printEventSummary         = False
process.FastTimerService.printRunSummary           = False
process.FastTimerService.printJobSummary           = True


# enable DQM plots
process.FastTimerService.enableDQM                 = True

# enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
process.FastTimerService.enableDQMbyPath           = True

# enable per-module DQM plots
process.FastTimerService.enableDQMbyModule         = True

# enable per-event DQM plots vs lumisection
process.FastTimerService.enableDQMbyLumiSection    = True
process.FastTimerService.dqmLumiSectionsRange      = 2500

# set the time resolution of the DQM plots
process.FastTimerService.dqmTimeRange              = 5000.
process.FastTimerService.dqmTimeResolution         =    5.
process.FastTimerService.dqmPathTimeRange          = 5000.
process.FastTimerService.dqmPathTimeResolution     =    5.
process.FastTimerService.dqmModuleTimeRange        = 5000.
process.FastTimerService.dqmModuleTimeResolution   =    5.

# set the base DQM folder for the plots
process.FastTimerService.dqmPath                   = 'HLT/TimerService'
process.FastTimerService.enableDQMbyProcesses      = True

process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2GeneralTracks_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2PixelVertices_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2PixelTracks_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2HighPtTripletStepTracks_*_*')
process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2InitialStepTracks_*_*')
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.DQMoutput)
# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.DQMoutput_step,process.RECOSIMoutput_step)#)#process.FEVTDEBUGHLToutput_step)#,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
#process=convertToUnscheduled(process)

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
