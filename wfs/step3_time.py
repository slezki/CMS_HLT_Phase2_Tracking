# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from ttbar_14_D49PU200 import *
import FWCore.ParameterSet.VarParsing as VarParsing
from customize_steps import *
#from Configuration.StandardSequences.Reconstruction_cff import *

process = cms.Process('RECO',Phase2C9)#,l1tracking)

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

options = VarParsing.VarParsing('analysis')
options.register ('wf',
                  -1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Wf number")

options.parseArguments()

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
# process.load('timing')
# process.load('validation_sequences')
# process.load('prevalidation_sequences')
# process.load('dqm_sequences')
# process.load("tracking_modules")
# process.load('validation_modules')
# process.load('prevalidation_modules')
# process.load('dqm_modules')


# load the DQMStore and DQMRootOutputModule
# enable multithreading
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
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


# ### For timing
# ### Tracking @ HLT: set up FastTimerService; analogous setting can be obtained with option --timing in hltGetConfiguration
# # configure the FastTimerService
# process.load( "HLTrigger.Timer.FastTimerService_cfi" )
# # print a text summary at the end of the job
# process.FastTimerService.printEventSummary         = False
# process.FastTimerService.printRunSummary           = False
# process.FastTimerService.printJobSummary           = True
#
#
# # enable DQM plots
# process.FastTimerService.enableDQM                 = True
#
# # enable per-path DQM plots (starting with CMSSW 9.2.3-patch2)
# process.FastTimerService.enableDQMbyPath           = True
#
# # enable per-module DQM plots
# process.FastTimerService.enableDQMbyModule         = True
#
# # enable per-event DQM plots vs lumisection
# process.FastTimerService.enableDQMbyLumiSection    = True
# process.FastTimerService.dqmLumiSectionsRange      = 2500
#
# # set the time resolution of the DQM plots
# process.FastTimerService.dqmTimeRange              = 80000.
# process.FastTimerService.dqmTimeResolution         =    10.0
# process.FastTimerService.dqmPathTimeRange          = 80000.
# process.FastTimerService.dqmPathTimeResolution     =    10.0
# process.FastTimerService.dqmModuleTimeRange        = 80000.
# process.FastTimerService.dqmModuleTimeResolution   =    10.0
#
# # set the base DQM folder for the plots
# process.FastTimerService.dqmPath                   = 'HLT/TimerService'
# process.FastTimerService.enableDQMbyProcesses      = True

#process.FastTimerOutput = cms.EndPath( process.dqmOutput )


# Schedule definition
#process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
#                                   process.vertexing, process.prevalidation_purel1,
#                                   process.validation_purel1, process.dqm_purel1, process.DQMoutput_step])

# process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks,
#                                    process.vertexing, process.prevalidation_l1initial,
#                                    process.validation_purel1, process.dqm_l1initial, process.DQMoutput_step])

# process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks_mask,
#                                    process.vertexing, process.prevalidation_l1initial,
#                                    process.validation_l1initial, process.dqm_l1initial, process.DQMoutput_step])


# FastTimerService client
# process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
# process.fastTimerServiceClient.dqmPath = "HLT/TimerService"
#
# # DQM file saver
# process.load('DQMServices.Components.DQMFileSaver_cfi')
# process.dqmSaver.workflow = "/HLT/FastTimerService/All"
#
# process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient + process.dqmSaver )


#######
# -1 - original v7
# 0 - l1tracks only
# 1 - pixeltracks + l1tracks
# 2 - pixelTracks + initial step + l1tracks
# 3 - initialstep + l1tracks
# 4 - pixelTracksTriplets + l1tracks
#

# customizeGeneralTracksToPureL1TracksStep(process)
# customizePixelSeedsEta4(process)
# customizeGeneralTracksToPixelL1TracksStep(process)
# customizeGeneralTracksToInitialL1TracksStep(process)
# customizeGeneralTracksToInitialL1TracksStepMasking(process)
# customizeL1TracksStepToMkFit(process)

timing = True

if options.wf == -2:
    customizeOriginal(process,timing)
if options.wf == 0:
    customizeGeneralTracksToPureL1TracksStep(process,timing)
if options.wf == 1:
    customizeGeneralTracksToPixelL1TracksStep(process,timing)
if options.wf == 2:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)
if options.wf == 3:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)

if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

### Tracking @ HLT: set up FastTimerService; analogous setting can be obtained with option --timing in hltGetConfiguration
# configure the FastTimerService


if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True


process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)
process.options.numberOfStreams = cms.untracked.uint32(8) #overwritten to 4 for timing
process.options.numberOfThreads = cms.untracked.uint32(8)

############################################### for timing studies

process.load( "HLTrigger.Timer.FastTimerService_cfi" )
process.load("timing")

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

#process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLTriggerFirstPath = cms.Path( process.hltGetRaw + process.hltBoolFalse )

process.HLTriggerFinalPath = cms.Path( process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.HLTAnalyzerEndpath = cms.EndPath( process.hltTrigReport )

### final path for timing
process.DQMoutput_step = cms.EndPath(process.DQMoutput)
