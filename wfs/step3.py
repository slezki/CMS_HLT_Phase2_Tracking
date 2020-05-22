# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from ttbar_14_D49PU200 import *
from FWCore.ParameterSet.VarParsing import VarParsing
from customize_steps import *

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
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)


process.MessageLogger = cms.Service("MessageLogger",
       destinations      = cms.untracked.vstring('debug'),
       debug = cms.untracked.PSet(
                                threshold = cms.untracked.string('DEBUG'),
                                default = cms.untracked.PSet(limit = cms.untracked.int32(-1))),
       debugModules      = cms.untracked.vstring('*')                               #7
)                                                                       #8


LOCAL = True
RECAS = True
if not RECAS:
    if LOCAL:
        process.load("local_files")
    else:
        process.load("input_TTbar_Phase2HLTTDRWinter20-PU200_110X_upgrade2026D49_realistic_v3-v2_cff")
else:
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(filelist),
        secondaryFileNames = cms.untracked.vstring()
        )

process.options = cms.untracked.PSet()

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
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
"""
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
"""
process.load('raw2digi_step_cff')
process.load("tracking_sequences")
process.load('validation_sequences')
process.load('prevalidation_sequences')
process.load('dqm_sequences')

process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# load the DQMStore and DQMRootOutputModule
# enable multithreading
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( False )
)
process.options.numberOfStreams = cms.untracked.uint32(8)
process.options.numberOfThreads = cms.untracked.uint32(8)

###### PixelCPE issue
process.TrackProducer.TTRHBuilder = "WithTrackAngle"
process.PixelCPEGenericESProducer.UseErrorsFromTemplates = False
process.PixelCPEGenericESProducer.LoadTemplatesFromDB = False
process.PixelCPEGenericESProducer.TruncatePixelCharge = False
process.PixelCPEGenericESProducer.IrradiationBiasCorrection = False
process.PixelCPEGenericESProducer.DoCosmics = False
process.PixelCPEGenericESProducer.Upgrade = cms.bool(True)
######

process.Timing = cms.Service("Timing",
  summaryOnly = cms.untracked.bool(False),
  useJobReport = cms.untracked.bool(True)
)

# Schedule definition
process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                   process.vertexing, process.prevalidation_purel1,
                                   process.validation_purel1, process.dqm_purel1, process.DQMoutput_step])

#customizeGeneralTracksToPureL1TracksStep(process)
customizePixelSeedsEta4(process)
customizeGeneralTracksToPixelL1TracksStep(process)
#customizeL1TracksStepToMkFit(process)

# process.schedule = cms.Schedule(*[ process.raw2digi_step,process.original_v7,
#                                    process.vertexing, process.prevalidation_original,
#                                    process.validation_original, process.dqm_original, process.DQMoutput_step ])

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
