# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

# import sys
# sys.path.insert(1, './MCs/')

import FWCore.ParameterSet.VarParsing as VarParsing
from customize_steps import *
#from Configuration.StandardSequences.Reconstruction_cff import *

process = cms.Process('RECO2',Phase2C9)#,l1tracking)

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
process.load("FWCore.Services.DependencyGraph_cfi")

options = VarParsing.VarParsing('analysis')
options.register ('wf',-1, VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"wf number")

options.register('timing',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"only timing")
options.register('debug',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"debug")

options.register('n',1,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"max events")
options.register('skip',0,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"events to skip")
options.register('threads',16,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"num of threads")

options.register('pixtrip',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pixel Triplets")
options.register('onlypixel',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"onlypixel")
options.register('mkfit',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"running mkfit")
options.register('patatrack',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"patatrack Pixel Tracks")
options.register('davertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"da pixel vertexing")
options.register('fullvertex',True,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full vertexing")
options.register('patavertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pata vertexing")

options.register('T2',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"running on T2_Bari")

#EventContent
options.register('fullcontent',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full content")
options.register('recosim',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"recosim content")

#Trimming&Vertexing
options.register('frac',20,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx sum pt fraction (in %)")
options.register('nvtx',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"n trimmed vtx")
options.register('sumpt',20 ,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"minsumpt2 vtx")
options.register('zsep',5,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"z_sep (x1000)")

#MCs
options.register('ztt',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"ZTT MC")
options.register('dstmmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DsTau3M MC")
options.register('bdksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BdToKstarMuMu MC")
options.register('b0ksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"B0ToKstarMuMu")
options.register('bskkkk',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BsToPhiPhi_KKKK MC")
options.register('withl1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"loading files with l1 tracks already produced")

options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.n),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)


process.MessageLogger = cms.Service("MessageLogger",
       destinations      = cms.untracked.vstring('debug'),
       debug = cms.untracked.PSet(
                                threshold = cms.untracked.string('DEBUG'),
                                default = cms.untracked.PSet(limit = cms.untracked.int32(-1))),
       debugModules      = cms.untracked.vstring('*')                               #7
)                                                                       #8

from MCs.ttbar import ttbar
filelist = ttbar

if options.ztt:
    from MCs.b0kstarmumu import b0kstarmumu
    filelist = b0kstarmumu
if options.dstmmm:
    from MCs.dstmmm import dstmmm #bdksmm import bdksmm
    filelist = dstmmm
if options.bdksmm:
    from MCs.bdksmm import bdksmm #bsphikkkk import bsphikkkk
    filelist = bdksmm
if options.b0ksmm:
    from MCs.b0ksmm import b0ksmm #dstaumumumu import dstaumumumu
    filelist = b0ksmm
if options.bskkkk:
    from MCs.bskkkk import bskkkk
    filelist = bskkkk
if options.withl1:
    from MCs.ttbarl1 import ttbarl1
    filelist = ttbar

if not options.T2:
    filelist = [f[5:] for f in filelist]

print(filelist)

# filelist=["/store/mc/Phase2HLTTDRWinter20DIGI/DoubleElectron_FlatPt-1To100/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/20000/6BF09AEE-5B7E-1340-9529-9A0E5E0F9442.root"]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(filelist),
    secondaryFileNames = cms.untracked.vstring()
    )

process.source.inputCommands = cms.untracked.vstring("keep *")
process.options = cms.untracked.PSet()
process.source.skipEvents=cms.untracked.uint32(options.skip)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

process.load('raw2digi_step_cff')
if options.wf<=-1:
    process.load("tracking_sequences_nol1")
else:
    process.load("tracking_sequences")
process.load('validation_sequences')
process.load('prevalidation_sequences')
process.load('dqm_sequences')

# load the DQMStore and DQMRootOutputModule
# enable multithreading
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)
process.options.numberOfStreams = cms.untracked.uint32(options.threads)
process.options.numberOfThreads = cms.untracked.uint32(options.threads)

#######
# -1 - original v6
# 0 - l1tracks only
# 1 - pixeltracks + l1tracks
# 2 - pixelTracks + initial step + l1tracks
# 3 - initialstep + l1tracks
# 4 - pixelTracksTriplets + l1tracks
#

timing = options.timing


suff = str(options.wf)

#TRIMMING OPTIONS
if options.wf < -1:

    process.hltPhase2PixelVertexAnalysisTrackingOnly.vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices","hltPhase2TrimmedPixelVertices")
    process.hltPhase2PixelVerticesSequence = cms.Sequence(
        process.hltPhase2PixelVertices +
        process.hltPhase2TrimmedPixelVertices
    )
    #Minimal reasonable setup
    process.hltPhase2TrimmedPixelVertices.fractionSumPt2 = cms.double( 0.01 )
    process.hltPhase2TrimmedPixelVertices.minSumPt2 = cms.double( 10.0 )
    process.hltPhase2TrimmedPixelVertices.maxVtx = cms.uint32( 100 ) # > 200 # previous 100

    process.hltPhase2PSetPvClusterComparerForITTrimming.track_chi2_max = cms.double( 20.0 )
    process.hltPhase2PSetPvClusterComparerForITTrimming.track_pt_max = cms.double( 40.0 )
    process.hltPhase2PSetPvClusterComparerForITTrimming.track_prob_min = cms.double( -1.0 )
    process.hltPhase2PSetPvClusterComparerForITTrimming.track_pt_min = cms.double( 0.9 )

if options.onlypixel:
    options.wf = -100
    suff = "pixelonly"

if options.wf == -5:
    customizeSingleIt(process,timing)
    suff = "m5"
    # customizeOriginalTrimmingInitial_v6(process,timing,fraction=0.05,numVertex=30,minSumPt2=20)
    process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0

if options.wf == -4:
    suff = "m4_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginal_v6(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
if options.wf == -3:
    customizeOriginal_v6(process,timing)
    suff = "m3_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
if options.wf == -2:
    customizeOriginal_v6(process,timing)
    suff = "m2_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
# if options.wf == -5:
#     suff = "m5"
#     customizeOriginal_v6_withvertex(process,timing)

##ORIGINAL v6_1
if options.wf == -1:
    suff = "m1"
    customizeOriginal_v6(process,timing)
    process.hltPhase2TrimmedPixelVertices = process.MeasurementTrackerEvent.clone()

#L1 Customizing
if options.wf == 0:
    suff = "purel1"
    customizeGeneralTracksToPureL1TracksStep(process,timing)
if options.wf == 1:
    customizeGeneralTracksToPixelL1TracksStep(process,timing)
if options.wf == 2:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)
if options.wf == 3:
    customizeGeneralTracksToInitialL1TracksStep(process,timing)
if options.wf == 4:
    customizeTripletL1(process,timing)
if options.wf == 5:
    pixel_l1_recovery(process,timing)
if options.wf == 6:
    l1_pixel_recovery(process,timing)
if options.wf == 7:
    l1_pixel_recovery_triplets(process,timing)

if options.mkfit:
    customizeHighPtTripletForMkFit(process)
# if options.pixtrip:
#     pixelTriplets(process)

if options.onlypixel:
    customizePixelOnly(process,timing)

if options.debug:
    suff = suff + "_debug"
if options.ztt:
    suff = suff + "_ztt"
elif options.dstmmm:
    suff = suff + "_dstmmm"
elif options.bdksmm:
    suff = suff + "_bdksmm"
elif options.b0ksmm:
    suff = suff + "_b0ksmm"
elif options.bskkkk:
    suff = suff + "_bskkkk"
else:
    suff = suff + "_ttb"
    # if not timing and not options.onlypixel:
    #     process.prevalidation_startup = process.prevalidation_startup_offline
    #     process.dqm_vertex = process.dqm_vertex_offline
    # elif not timing:
    #     process.prevalidation_startup = process.prevalidation_startup_offline
    #     process.dqm_commons = process.dqm_commons_offline

suff = suff + "_skip_" + str(options.skip) + "_n_" + str(options.n)

if options.fullvertex or not options.timing:
    process.schedule.extend([process.vertexing])
    suff = suff + "_fullvertexing"

if options.patavertex:
    suff = suff + "_patavertex"
if options.patatrack:
    customizePixelTracksSoAonCPU(process,options.patavertex)

    if options.pixtrip:
        process.hltPhase2PixelTrackSoA.minHitsPerNtuplet = 3
    suff = suff + "_pata"
    process.quickTrackAssociatorByHits.Purity_SimToReco = cms.double(0.65)
if options.davertex:
    process.hltPhase2PixelVertices = process.hltPhase2DAPrimaryVerticesUnsorted.clone()
    suff = suff + "_da"
elif not options.patavertex:
    process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0

suff = suff + "_zsep_" + str(options.zsep)

#DependecyGraph
#from FWCore.ParameterSet.Utilities import moduleLabelsInSequences
process.DependencyGraph.highlightModules = ["hltPhase2PixelTracks","hltPhase2PixelVertices","hltPhase2InitialStepTracks","hltPhase2InitialStepTrackCandidates"]

process.DependencyGraph.showPathDependencies = True
process.DependencyGraph.fileName = 'dependency' + suff + '.gv'

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_' + suff + '.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM_' + suff + '.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_full_' + suff + '.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

if not timing:
    process.DQMoutput_step = cms.EndPath( process.DQMoutput)
    process.schedule.extend([process.DQMoutput_step])

if options.fullcontent:


    process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-RECO-HLTDEBUG'),
            filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string('file:step3_full_' + suff + '.root'),
        outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
        splitLevel = cms.untracked.int32(0)
    )

    # process.FEVTDEBUGHLToutput.outputCommands.append('keep *')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2GeneralTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2*PixelVertices_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2PixelTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2HighPtTripletStepTracks_*_*')
    process.FEVTDEBUGHLToutput.outputCommands.append('keep *_hltPhase2InitialStepTracks_*_*')
    process.full_output_step = cms.EndPath(process.FEVTDEBUGHLToutput)
    process.schedule.extend([process.full_output_step])

elif options.recosim:

    process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM-RECO'),
            filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string('file:step3_reco_' + suff + '.root'),
        outputCommands = process.RECOSIMoutput.outputCommands,
        splitLevel = cms.untracked.int32(0)
    )

    # process.FEVTDEBUGHLToutput.outputCommands.append('keep *')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2GeneralTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2*PixelVertices_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2PixelTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2HighPtTripletStepTracks_*_*')
    process.RECOSIMoutput.outputCommands.append('keep *_hltPhase2InitialStepTracks_*_*')

    process.full_output_step = cms.EndPath(process.RECOSIMoutput)
    process.schedule.extend([process.full_output_step])

if 'PrescaleService' in process.__dict__:
    for pset in reversed(process.PrescaleService.prescaleTable):
        if not hasattr(process,pset.pathName.value()):
            process.PrescaleService.prescaleTable.remove(pset)

### Tracking @ HLT: set up FastTimerService; analogous setting can be obtained with option --timing in hltGetConfiguration
# configure the FastTimerService
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
tr = 10000000000.
tp = 10000000000.
tm = 2000000000.
process.FastTimerService.dqmTimeRange              = tr
process.FastTimerService.dqmTimeResolution         = tr/100.0
process.FastTimerService.dqmPathTimeRange          = tp
process.FastTimerService.dqmPathTimeResolution     = tp/100.0
process.FastTimerService.dqmModuleTimeRange        = tm
process.FastTimerService.dqmModuleTimeResolution   = tm/100.0

# set the base DQM folder for the plots
process.FastTimerService.dqmPath                   = 'HLT/TimerService'
process.FastTimerService.enableDQMbyProcesses      = True


process.FastTimerService.dqmMemoryRange            = 1000000
process.FastTimerService.dqmMemoryResolution       =    5000
process.FastTimerService.dqmPathMemoryRange        = 1000000
process.FastTimerService.dqmPathMemoryResolution   =    5000
process.FastTimerService.dqmModuleMemoryRange      =  100000
process.FastTimerService.dqmModuleMemoryResolution =     500

process.FastTimerService.writeJSONSummary = cms.untracked.bool(True)
process.FastTimerService.jsonFileName = cms.untracked.string('wf_' + suff + '_timing.json')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')
#
#ustomizeGeneralTracksToPixelL1TracksStep(process)
#customizeGeneralTracksToPixelTripletL1TracksStep(process)
#customizeGeneralTracksToInitialL1TracksStep(process)
#customizeGeneralTracksToInitialL1TracksStepMasking(process)
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
