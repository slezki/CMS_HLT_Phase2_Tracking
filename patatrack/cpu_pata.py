# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase1_2018_realistic -n 10 --era Run2_2018 --eventcontent RECOSIM,DQM --runUnscheduled --procModifiers gpu -s RAW2DIGI:RawToDigi_pixelOnly,RECO:reconstruction_pixelTrackingOnly,VALIDATION:@pixelTrackingOnlyValidation,DQM:@pixelTrackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry DB:Extended --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.ProcessModifiers.pixelNtupleFit_cff import pixelNtupleFit
from RecoLocalTracker.SiPixelRecHits.siPixelRecHitHostSoA_cfi import siPixelRecHitHostSoA as _siPixelRecHitFromSOA

from ttbar_14_D49PU200 import *

def customizePixelTracksSoAonCPU(process) :

  process.load('RecoLocalTracker/SiPixelRecHits/siPixelRecHitHostSoA_cfi')
  process.load('RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi')
  #process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexCUDA_cfi')

  process.pixelTrackSoA = process.caHitNtupletCUDA.clone()
  process.pixelTrackSoA.onGPU = False
  process.pixelTrackSoA.pixelRecHitSrc = 'siPixelRecHitsPreSplitting'#'siPixelRecHitHostSoA'
  #process.pixelVertexSoA = process.pixelVertexCUDA.clone()
  #process.pixelVertexSoA.onGPU = False
  #process.pixelVertexSoA.pixelTrackSrc = 'pixelTrackSoA'

  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi')
  process.pixelTracks = process.pixelTrackProducerFromSoA.clone()
  #process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexFromSoA_cfi')
  #process.pixelVertices = process.pixelVertexFromSoA.clone()
  process.pixelTracks.pixelRecHitLegacySrc = 'siPixelRecHitsPreSplitting'#'siPixelRecHitHostSoA'

  #process.PixelCPEFastESProducer.isUpgrade = True
  #process.reconstruction_step += process.siPixelRecHitHostSoA #+process.pixelTrackSoA+process.pixelVertexSoA
  process.siPixelRecHitsPreSplitting = _siPixelRecHitFromSOA.clone()
  process.siPixelRecHitsPreSplittingTask = cms.Task(process.siPixelRecHitsPreSplitting)
  process.pixelTracksSeedLayers.BPix.HitProducer = 'siPixelRecHitsPreSplitting'#"siPixelRecHitHostSoA"
  process.pixelTracksSeedLayers.FPix.HitProducer = 'siPixelRecHitsPreSplitting'#"siPixelRecHitHostSoA"
  process.siPixelRecHitsPreSplitting.convertToLegacy = True
  
  process.PixelCPEFastESProducer.Upgrade = True 
  process.pixeltrackerlocalrecoTask = cms.Task(process.siPixelClustersPreSplittingTask,process.siPixelRecHitsPreSplittingTask)
  process.reconstruction_step += process.pixelTrackSoA 
  
  return process

process = cms.Process('RECO',Phase2C9,pixelNtupleFit)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("HeterogeneousCore.CUDAServices.CUDAService_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.MessageLogger = cms.Service("MessageLogger",
       destinations      = cms.untracked.vstring('myDebugOutputFile'),
       myDebugOutputFile = cms.untracked.PSet(
                                threshold = cms.untracked.string('DEBUG'),
                                default = cms.untracked.PSet(limit = cms.untracked.int32(-1))),
       debugModules      = cms.untracked.vstring('*')                               #7
) 

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(filelist[1]),
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

process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(1)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

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
    fileName = cms.untracked.string('file:step3_pata.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM_pata.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

#process.reconstruction_pixelTrackingOnly = cms.Sequence(
#    pixeltrackerlocalreco*
#    offlineBeamSpot*
#    siPixelClusterShapeCachePreSplitting*
#    recopixelvertexing
#)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi_pixelOnly)
process.reconstruction_step = cms.Path(process.reconstruction_pixelTrackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationPixelTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationPixelTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflinePixelTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)


process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dumper = cms.Path(process.dump)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.dumper,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RECOSIMoutput_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
customizePixelTracksSoAonCPU(process)
# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line
process.Timing = cms.Service("Timing",
  summaryOnly = cms.untracked.bool(False),
  useJobReport = cms.untracked.bool(True)
)

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
