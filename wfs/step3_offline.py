# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process('RECO2',Phase2C9)

options = VarParsing.VarParsing('analysis')
options.register ('wf',-1, VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"wf number")
options.register('nopu',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"nopu")
options.register('pu140',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pu140")
options.register('timing',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"timing")

options.register('n',1,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"max events")
options.register('skip',0,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"events to skip")
options.register('threads',16,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"num of threads")

options.parseArguments()

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

from pu140 import *

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.n),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
suff = "offline"
if options.nopu:
	suff = "offline_nopu"
if options.pu140:
	suff = "offline_pu140"
suff = suff + "_skip_" + str(options.skip) + "_n_" + str(options.n)

pu200 =["/store/group/phys_tracking/upgrade_ttbar/015FB6F1-59B4-304C-B540-2392A983A97D.root",
"/store/group/phys_tracking/upgrade_ttbar/049DEDCD-30D1-074F-B86C-9105C141BEFB.root",
"/store/group/phys_tracking/upgrade_ttbar/0DAE3770-0369-AB44-8955-4F2DD9A1D031.root",
"/store/group/phys_tracking/upgrade_ttbar/0E9C92B0-C40D-BF4B-B037-72CC40611286.root",
"/store/group/phys_tracking/upgrade_ttbar/0F6150D3-2B6F-A347-BEE3-EB8889352356.root",
"/store/group/phys_tracking/upgrade_ttbar/11A75A1C-68E0-6542-A6CB-A26B269F38D4.root",
"/store/group/phys_tracking/upgrade_ttbar/1234CB2C-12CE-7E46-BB4E-1CF46BF8134F.root",
"/store/group/phys_tracking/upgrade_ttbar/13CADEC6-EEE8-6245-B683-CBA5B2E5CC59.root",
"/store/group/phys_tracking/upgrade_ttbar/145779D7-EFD0-3144-B0E0-CC5F4E86190F.root",
"/store/group/phys_tracking/upgrade_ttbar/14C2F5D4-FA8E-F942-A4A8-B429B9BB7482.root",
"/store/group/phys_tracking/upgrade_ttbar/1650078B-2AA9-0C48-8597-437E6585942E.root",
"/store/group/phys_tracking/upgrade_ttbar/18709C5D-26C2-F041-ACFA-F0791A80EB8E.root",
"/store/group/phys_tracking/upgrade_ttbar/20EAA798-0F84-8C4F-A1E3-9CAC1F424534.root",
"/store/group/phys_tracking/upgrade_ttbar/227B9AFA-2612-694B-A2E7-B566F92C4B55.root",
"/store/group/phys_tracking/upgrade_ttbar/262C96FF-3ACC-6F4B-BCB7-57CB9D7438BC.root",
"/store/group/phys_tracking/upgrade_ttbar/2CBFF496-D53B-7849-9326-DE18E0ED9853.root",
"/store/group/phys_tracking/upgrade_ttbar/328BFACA-A34B-FC47-8382-0FF75AA61ACD.root",
"/store/group/phys_tracking/upgrade_ttbar/33976E28-9C5B-7143-846C-95800C4D8CF3.root",
"/store/group/phys_tracking/upgrade_ttbar/365143CE-D92F-6D49-AA92-632E55342AAE.root",
"/store/group/phys_tracking/upgrade_ttbar/42D8E9C8-7563-CC4B-9706-E0CFF2822A65.root",
"/store/group/phys_tracking/upgrade_ttbar/451C0530-4D6E-F541-BB01-A2C22C3F9F6E.root",
"/store/group/phys_tracking/upgrade_ttbar/46AE5E92-4669-D24E-866D-A20BE8395F82.root",
"/store/group/phys_tracking/upgrade_ttbar/46DAED64-4C7A-B24D-9F1E-9CAD01A466D8.root",
"/store/group/phys_tracking/upgrade_ttbar/48A1FCC3-7710-094E-98B9-5C5C05CAED2B.root",
"/store/group/phys_tracking/upgrade_ttbar/4B086AFC-7701-944F-84F9-3F1671C26D63.root",
"/store/group/phys_tracking/upgrade_ttbar/4C3F94F2-1D13-5B44-8514-CF8FE9B971EE.root",
"/store/group/phys_tracking/upgrade_ttbar/4C6F706B-E226-4042-AA43-AEB4E72D1B7C.root",
"/store/group/phys_tracking/upgrade_ttbar/504FAC71-E325-084B-9984-D62FFA2E36F2.root",
"/store/group/phys_tracking/upgrade_ttbar/51127465-66ED-B94C-8B7B-6C663B32FCB1.root",
"/store/group/phys_tracking/upgrade_ttbar/529F0000-EB29-7F42-96C7-660B646F738A.root",
"/store/group/phys_tracking/upgrade_ttbar/536517C8-222F-584B-A5D8-C1B1D1F374CD.root",
"/store/group/phys_tracking/upgrade_ttbar/55891DB4-60C7-0644-9DD7-D66C0EF336A0.root",
"/store/group/phys_tracking/upgrade_ttbar/5594D9E5-CA79-C34E-A3BD-AD6BEC9B8CA7.root",
"/store/group/phys_tracking/upgrade_ttbar/5FCCEB41-738A-D34B-8D6E-8EA16A2C568C.root",
"/store/group/phys_tracking/upgrade_ttbar/61034CCA-B2AA-F04B-82D4-776B06F5549A.root",
"/store/group/phys_tracking/upgrade_ttbar/6516D6D5-8369-594A-9048-735AAF0E9EFB.root",
"/store/group/phys_tracking/upgrade_ttbar/6943DAAD-30E5-6E4B-A73F-89B072EEC05E.root",
"/store/group/phys_tracking/upgrade_ttbar/6A2973C6-ED1D-5948-B58C-1FECFEFD0627.root",
"/store/group/phys_tracking/upgrade_ttbar/6A57A034-925B-364F-A2B1-B8BDA14B0721.root",
"/store/group/phys_tracking/upgrade_ttbar/6B2C04CF-C82B-B94F-9057-90850F3ECCF7.root",
"/store/group/phys_tracking/upgrade_ttbar/6C09ECB0-DA16-8948-A5FC-D791171152AB.root",
"/store/group/phys_tracking/upgrade_ttbar/73EAEA3A-6234-3E40-B0D6-2806BFE6CDEC.root",
"/store/group/phys_tracking/upgrade_ttbar/7470BF91-3B12-5440-B27C-04FE427CC92F.root",
"/store/group/phys_tracking/upgrade_ttbar/784C9C63-F27E-5F43-A444-F490D8DFF51B.root",
"/store/group/phys_tracking/upgrade_ttbar/7CB075DA-719B-6A4D-AF60-7BC0EBEA5869.root",
"/store/group/phys_tracking/upgrade_ttbar/7D4B93AA-7FEF-4D40-BB7A-94C7CA27F480.root",
"/store/group/phys_tracking/upgrade_ttbar/844EAF21-9C25-7242-9610-CE2F873C26C3.root",
"/store/group/phys_tracking/upgrade_ttbar/8A0EC03A-7837-5A4A-BF3A-4AED18DABC2F.root",
"/store/group/phys_tracking/upgrade_ttbar/8ABD3088-0F95-6F48-837C-320AC7FFEDEF.root",
"/store/group/phys_tracking/upgrade_ttbar/8EF9A3F1-940F-9B40-A32B-0839BCA30BCF.root",
"/store/group/phys_tracking/upgrade_ttbar/8FE4EEEB-32F0-A14A-AE88-94E85D7A3199.root",
"/store/group/phys_tracking/upgrade_ttbar/9E38C617-9119-7A43-8579-7FEFC5783A76.root",
"/store/group/phys_tracking/upgrade_ttbar/9FD542C1-BF55-9342-A2B6-2514946379FC.root",
"/store/group/phys_tracking/upgrade_ttbar/A166FA37-3D98-E44F-95E4-D7D9B43AF11A.root",
"/store/group/phys_tracking/upgrade_ttbar/A43E41C4-24BA-104A-BE86-95E1FF9CE2F3.root",
"/store/group/phys_tracking/upgrade_ttbar/A568BC6B-5D5E-5F48-B2F2-E640FCF093AE.root",
"/store/group/phys_tracking/upgrade_ttbar/ACEB5B5B-537D-0C4F-BEBB-CD8771DD53C7.root",
"/store/group/phys_tracking/upgrade_ttbar/AEE102A8-E95A-8740-9983-17AF3C1329E9.root",
"/store/group/phys_tracking/upgrade_ttbar/B242ED9D-09EE-3D41-92E4-77062951D758.root",
"/store/group/phys_tracking/upgrade_ttbar/B678394F-8C24-B345-9A09-1DE2E8E13716.root",
"/store/group/phys_tracking/upgrade_ttbar/B758C6A6-A9E1-1A4E-A486-BB82ADE9C3A2.root",
"/store/group/phys_tracking/upgrade_ttbar/BD7C61A9-B7D9-2444-8645-BEA2E68D2060.root",
"/store/group/phys_tracking/upgrade_ttbar/BE04E6A0-1936-8D44-A0A1-EA76F70BAC89.root",
"/store/group/phys_tracking/upgrade_ttbar/C41F2167-DC8B-4045-A535-0D083499F6AD.root",
"/store/group/phys_tracking/upgrade_ttbar/C657316E-7A9E-A246-B1F6-972BC05C44F6.root",
"/store/group/phys_tracking/upgrade_ttbar/C7BA2638-BC46-A54E-86F3-137D3652A9CE.root",
"/store/group/phys_tracking/upgrade_ttbar/CC7C5560-9C25-464E-A454-141093649736.root",
"/store/group/phys_tracking/upgrade_ttbar/CC90651E-BB43-8B40-AD35-D046BBF45456.root",
"/store/group/phys_tracking/upgrade_ttbar/CCB6C333-0D6A-0E4C-8ED4-AE67C6177C41.root",
"/store/group/phys_tracking/upgrade_ttbar/D0B6D156-5143-2343-8D93-A5C44DEFB586.root",
"/store/group/phys_tracking/upgrade_ttbar/D5B9F0B4-CDD4-B14B-A0AB-5AA08C15B1B4.root",
"/store/group/phys_tracking/upgrade_ttbar/DFFB3465-8A25-1F4F-95C7-0F2A565DC371.root",
"/store/group/phys_tracking/upgrade_ttbar/E2A8D49E-A947-CB4F-ACDB-84D1D20C5206.root",
"/store/group/phys_tracking/upgrade_ttbar/F3B78BA1-3656-5541-A648-600BE38BF611.root",
"/store/group/phys_tracking/upgrade_ttbar/F6E4AA63-7B99-2D47-AE5D-C68745838A20.root",
"/store/group/phys_tracking/upgrade_ttbar/FB8D623F-5BED-F746-809B-76FD78F65279.root",
"/store/group/phys_tracking/upgrade_ttbar/FCFDFCC2-F905-C246-8827-E5FED5204905.root"]

nopu = ["/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/DAF55EAB-0B6F-C646-B7DE-2D54C8A62073.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/DF27D727-5F91-5748-B83B-9DB5CD85604E.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/DFE96256-6096-3741-8739-0EB64AB681C1.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/E21DD179-F13E-E543-A0B2-C1ABDAAAD7F8.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/E30D1362-CED7-974F-8930-782B23F11751.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/E486070C-A1D5-8B41-BA9A-686077807269.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/E5437AA8-386B-DB43-8B35-B6690CD5DD19.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/E7BA8C7B-A811-CA49-9582-33226BD76252.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/EEF49391-A7E3-9C41-AC3F-6B1A0F1B9DA0.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F0932A00-A9EB-1E42-A56F-C0C89754E73E.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F14A1F9D-BA98-1D43-9130-D66073D43469.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F3AABCB2-269C-644C-A09A-FBF7124D5B7E.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F6B21094-64EE-DD41-839A-28B159129F80.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F7E3C394-24D7-4046-989F-B7075DCB0BB0.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/F7ECC566-E0F5-754A-9465-FA24A4D67734.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/FE308DD9-D66F-4545-B0F2-9E44880D0054.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/FF0494EC-DE4E-3C46-BC68-2AEE51390533.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/FFD62905-0181-D44F-8BEF-2557BFF9F040.root"]

filelist = pu200
# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(filelist),
    secondaryFileNames = cms.untracked.vstring()
)

process.source.inputCommands = cms.untracked.vstring("keep *")
process.options = cms.untracked.PSet()
process.source.skipEvents=cms.untracked.uint32(options.skip)

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

T = min(options.threads,options.n)

process.options.numberOfThreads=cms.untracked.uint32(T)
process.options.numberOfStreams=cms.untracked.uint32(T)

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
    fileName = cms.untracked.string('file:step3_' + suff + ' .root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM'+ suff + '.root'),
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
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction_trackingOnly)
process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.pL1TkElectronsEllipticMatchHGC = cms.Path(process.L1TkElectronsEllipticMatchHGC)
process.pL1TkMuon = cms.Path(process.L1TkMuons+process.L1TkMuonsTP)
process.pL1TkIsoElectronsHGC = cms.Path(process.L1TkIsoElectronsHGC)
process.pL1TkIsoElectronsCrystal = cms.Path(process.L1TkIsoElectronsCrystal)
process.pL1TkPrimaryVertex = cms.Path(process.L1TkPrimaryVertex)
process.pL1TkElectronsLooseHGC = cms.Path(process.L1TkElectronsLooseHGC)
process.pL1TkPhotonsCrystal = cms.Path(process.L1TkPhotonsCrystal)
process.pL1TkElectronsEllipticMatchCrystal = cms.Path(process.L1TkElectronsEllipticMatchCrystal)
process.pL1TkElectronsHGC = cms.Path(process.L1TkElectronsHGC)
process.pL1TkPhotonsHGC = cms.Path(process.L1TkPhotonsHGC)
process.pL1TkElectronsCrystal = cms.Path(process.L1TkElectronsCrystal)
process.pL1TkElectronsLooseCrystal = cms.Path(process.L1TkElectronsLooseCrystal)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

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

process.FastTimerService.jsonFileName = cms.untracked.string('wf_' + suff + '.json')

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.DQMoutput_step)
if options.timing:
   process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.RECOSIMoutput_step)
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
process = customise_aging_1000(process)

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
