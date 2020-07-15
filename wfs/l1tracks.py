# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from ttbar_14_D49PU200 import *
import FWCore.ParameterSet.VarParsing as VarParsing
from Configuration.StandardSequences.Reconstruction_cff import *
from L1Trigger.TrackFindingTracklet.Tracklet_cfi import *

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

process.load('raw2digi_step_cff')
process.load("tracking_sequences")

options = VarParsing.VarParsing('analysis')
options.register('n',0,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"file number")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
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
        fileNames = cms.untracked.vstring(filelist[options.n]),
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

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2_ttbar_pu200_d49_' + str(options.n) + '.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
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

process.l1emulations = TTTracksFromTrackletEmulation.clone()
process.hltPhase2L1TTTracksEmulation = cms.Path(process.l1emulations)
process.output_step = cms.EndPath( process.FEVTDEBUGHLToutput)

process.schedule = cms.Schedule(*[process.hltPhase2L1TTTracksEmulation,process.output_step])

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
# process=convertToUnschedule   d(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

# from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
# process = customizeHLTforAll(process,"Fake",_customInfo)
