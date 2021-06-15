# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent RECOSIM,DQM --runUnscheduled -s RAW2DIGI,RECO:reconstruction_trackingOnly,VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

# import sys
# sys.path.insert(1, './MCs/')

from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
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

#L1 Tracks
options.register('l1extended',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"l1 extended")
options.register('nol1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"do not include l1tracks in generaltracks")

#Pixel setups
options.register('pixtrip',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pixel Triplets")
options.register('onlypixel',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"onlypixel")
options.register('protokin',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"using proto tracks kinematics")

#Patatrack
options.register('mkfit',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"running mkfit")
options.register('patatrack',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Patatrack Pixel Tracks")
options.register('clean',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Use Cleaned Patatrack Pixel Tracks")
options.register('allpata',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Seeding only from Patatrack Pixel Tracks")
options.register('doregion',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Seeding only from Patatrack Pixel Tracks")
options.register('rhoVtx',250,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx for region rho distance (x1000)")
options.register('zVtx',500,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx for region z distance (x1000)")
options.register('keepBad',99,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"keepBad")
options.register('keepDup',99,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"keepDup")

#Vetexing
options.register('davertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"da pixel vertexing")
options.register('fullvertex',True,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full vertexing")
options.register('patavertex',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pata vertexing")
options.register('fastl1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"fastl1 vertexing")
options.register('froml1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"froml1 vertexing")

#Files
options.register('T2',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"running on T2_Bari")

#EventContent
options.register('fullcontent',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"full content")
options.register('recosim',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"recosim content")

#Trimming&Vertexing
options.register('frac',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"vtx sum pt fraction (in %)")
options.register('nvtx',10,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"n trimmed vtx")
options.register('sumpt',10 ,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"minsumpt2 vtx")
options.register('zsep',5,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"z_sep (x1000)")
options.register('fromPV',True,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"fromPV for ininitial step")
options.register('fE',100,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"fixed Error for triplet (x1000)")
options.register('oR',250,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"half Lenght for triplet (x1000)")
options.register('rI',250,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"r vtx for initial (x1000)")
options.register('zI',500,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.int,"z vtx for initial (x1000)")

#MCs
options.register('susy',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"Susy")
options.register('dyll',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DY ll")
options.register('ztt',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"ZTT MC")
options.register('dstmmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DsTau3M MC")
options.register('bdksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BdToKstarMuMu MC")
options.register('b0ksmm',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"B0ToKstarMuMu")
options.register('bskkkk',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"BsToPhiPhi_KKKK MC")
options.register('withl1',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"loading files with l1 tracks already produced")
options.register('muons',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"DYMM MC")

options.register('noPU',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"noPU events")
options.register('pu140',False,VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.bool,"pu140 events")


#Miscs
options.register ('note','',VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.string, "noting")

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

if not options.T2:



    filelist = ["/store/group/phys_tracking/upgrade_ttbar/015FB6F1-59B4-304C-B540-2392A983A97D.root",
"/store/group/phys_tracking/upgrade_ttbar/049DEDCD-30D1-074F-B86C-9105C141BEFB.root",
"/store/group/phys_tracking/upgrade_ttbar/0DAE3770-0369-AB44-8955-4F2DD9A1D031.root",
"/store/group/phys_tracking/upgrade_ttbar/0E9C92B0-C40D-BF4B-B037-72CC40611286.root",
"/store/group/phys_tracking/upgrade_ttbar/0F6150D3-2B6F-A347-BEE3-EB8889352356.root",
"/store/group/phys_tracking/upgrade_ttbar/11A75A1C-68E0-6542-A6CB-A26B269F38D4.root",
"/store/group/phys_tracking/upgrade_ttbar/1234CB2C-12CE-7E46-BB4E-1CF46BF8134F.root",
"/store/group/phys_tracking/upgrade_ttbar/13CADEC6-EEE8-6245-B683-CBA5B2E5CC59.root",
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

from MCs.pu200 import *
filelist=pu200

if options.pu140:
   from MCs.pu140 import *
   filelist = pu140

if options.noPU:
   from MCs.noPU import *
   filelist = noPU
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
    filelist = ttbarl1
if options.muons:
    from MCs.muons import muon_files
    filelist = muon_files
if options.dyll:
    from MCs.dyll_50 import * 
    filelist = dyll
if options.susy:
    from MCs.susy import *
    filelist = susy

#if options.susy:
   
# filelist=["/store/mc/Phase2HLTTDRWinter20DIGI/DoubleElectron_FlatPt-1To100/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3-v2/20000/6BF09AEE-5B7E-1340-9529-9A0E5E0F9442.root"]
#filelist=["/store/relval/CMSSW_11_1_0_patch1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW-RECO/110X_mcRun4_realistic_v3_2026D49PU200_raw1100_ProdType1-v1/10000/AFD88583-675F-C14D-B057-6DD8121634D5.root"]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(filelist),
    secondaryFileNames = cms.untracked.vstring()
    )

process.source.inputCommands = cms.untracked.vstring("keep *")#,"drop *L1TkPrimaryVertex*_*_*RECO")
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
process.GlobalTag = GlobalTag(process.GlobalTag, '111X_mcRun4_realistic_T15_v2', '')

process.load('raw2digi_step_cff')
process.load("RecoJets.JetProducers.caloJetsForTrk_cff")
process.load("tracking_sequences")

if not options.timing:
    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")# import quickTrackAssociatorByHits
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")# import tpClusterProducer
    process.load("Validation.RecoTrack.TrackValidation_cff")# import trackingParticlesBHadron,trackingParticlesConversion,trackingParticleNumberOfLayersProducer
    process.load("SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi")# import simHitTPAssocProducer
    process.load("Validation.RecoTrack.associators_cff")

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

T = min(options.threads,options.n)

process.options.numberOfThreads=cms.untracked.uint32(T)
process.options.numberOfStreams=cms.untracked.uint32(T)

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

    if not options.timing:
    	process.hltPhase2PixelVertexAnalysisTrackingOnly.vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices","hltPhase2TrimmedPixelVertices")

    process.hltPhase2InitialStepSeeds.usePV = cms.bool(options.fromPV)
    process.hltPhase2PixelVerticesSequence = cms.Sequence(
        process.hltPhase2PixelVertices +
        process.hltPhase2TrimmedPixelVertices +
 	process.hltPhase2PixelTracksCleaner
    )
    #Minimal reasonable setup
    process.hltPhase2TrimmedPixelVertices.fractionSumPt2 = cms.double( 0.01 )
    process.hltPhase2TrimmedPixelVertices.minSumPt2 = cms.double( 10.0 )
    process.hltPhase2TrimmedPixelVertices.maxVtx = cms.uint32( 100 ) # > 200 # previous 100



if options.onlypixel:
    options.wf = -100
    suff = "pixelonly"

if options.wf == -5:
    customizeSingleIt(process,timing)
    suff = "m5"
  
    # customizeOriginalTrimmingInitial_v6(process,timing,fraction=0.05,numVertex=30,minSumPt2=20)
    #process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0
    if options.clean: 
	process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger") 
   #process.hltPhase2PixelVertices.TrackCollection = cms.InputTag("hltPhase2PixelQuadrupletsSelector")
if options.wf == -8:
    customizeL1SingleIt(process,timing)
    suff = "m8"
    # customizeOriginalTrimmingInitial_v6(process,timing,fraction=0.05,numVertex=30,minSumPt2=20)
    #process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0
    if options.clean: 
        process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger")
    #process.hltPhase2PixelVertices.TrackCollection = cms.InputTag("hltPhase2PixelQuadrupletsSelector")

if options.wf == -6:
    l1_pixel_recovery_triplets(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    suff = "m6_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
if options.wf == -7:
    l1_pixel_recovery_triplets(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    suff = "m7_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    process.hltPhase2InitialStepSeeds.InputVertexCollection = cms.InputTag("hltPhase2L1PrimaryVertex")
    hltPhase2TrimmedVertexTrackingRegions.VertexCollection = cms.InputTag( "hltPhase2L1PrimaryVertex" )
    
if options.wf == -4:
    suff = "m4_0p%d_%d_%d"%(options.frac,options.nvtx,options.sumpt)
    customizeOriginal_v6(process,timing)
    customizeOriginalTrimmingInitial_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)
    customizeOriginalTrimmingTriplet_v6(process,timing,fraction=options.frac/100.,numVertex=options.nvtx,minSumPt2=options.sumpt)

    process.hltPhase2PixelTracksCleaner.rhoVtx = options.rI / 1000.
    process.hltPhase2PixelTracksCleaner.zetaVtx = options.zI / 1000.
    process.hltPhase2HighPtTripletStepTrackingRegions.RegionPSet.fixedError = options.fE /1000.0
    process.hltPhase2HighPtTripletStepTrackingRegions.RegionPSet.originRadius = options.oR / 1000.0

    suff = suff + "_I_%d_%d_H_%d_%d"%(options.rI,options.zI,options.fE,options.oR)

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

if options.allpata and options.patatrack:
    suff = suff + "_tripFromTracks"
    process.hltPhase2PixelTracksCleaner.rhoVtx = 100.0 
    process.hltPhase2PixelTracksCleaner.useVtx = False
    process.hltPhase2PixelTracksCleaner.zetaVtx = 100.0
	
    process.hltPhase2PixelTripletsCleaner.rhoVtx = 100.0 
    process.hltPhase2PixelTripletsCleaner.useVtx = False
    process.hltPhase2PixelTripletsCleaner.zetaVtx = 100.0
   
    process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksCleaner")#hltPhase2PixelQuadrupletsSelector")#hltPhase2PixelTracksCleaner")#hltPhase2PixelQuadrupletsSelector")
    process.hltPhase2HighPtTripletStepSeeds = process.hltPhase2InitialStepSeeds.clone()
    process.hltPhase2HighPtTripletStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTripletsCleaner")
    process.hltPhase2HighPtTripletStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    process.hltPhase2HighPtTripletStepSeeds.mixed= cms.bool(False)
 
	
    if hasattr(process,"hltPhase2HighPtTripletStepHitDoublets"):
	delattr(process,"hltPhase2HighPtTripletStepHitDoublets")
    if hasattr(process,"hltPhase2HighPtTripletStepHitTriplets"):
 	delattr(process,"hltPhase2HighPtTripletStepHitTriplets")

if options.allpata and options.clean and options.patatrack:

	process.hltPhase2PixelTracksCleaner.rhoVtx = options.rhoVtx /1000.0
        process.hltPhase2PixelTracksCleaner.zetaVtx = options.zVtx / 1000.0
        process.hltPhase2PixelTripletsCleaner.useVtx = True
        process.hltPhase2PixelTracksCleaner.useVtx = False
        if options.fromPV:
		process.hltPhase2PixelTracksCleaner.nVertices = 10
        process.hltPhase2PixelTripletsCleaner.rhoVtx = options.rhoVtx /1000.0
        process.hltPhase2PixelTripletsCleaner.zetaVtx = options.zVtx / 1000.0

        if options.froml1:
		process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")	
		process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")
	if options.wf == -4:
		process.hltPhase2PixelTripletsCleaner.vertexTag = cms.InputTag("hltPhase2TrimmedPixelVertices")
		process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2TrimmedPixelVertices")

if options.patatrack and options.clean and not options.allpata:
	
	process.hltPhase2PixelTracksCleaner.rhoVtx = options.rhoVtx /1000.0
        process.hltPhase2PixelTracksCleaner.zetaVtx = options.zVtx / 1000.0
        process.hltPhase2PixelTripletsCleaner.useVtx = True
        process.hltPhase2PixelTracksCleaner.useVtx = False
	process.hltPhase2PixelTripletsCleaner.rhoVtx = options.rhoVtx /1000.0
        process.hltPhase2PixelTripletsCleaner.zetaVtx = options.zVtx / 1000.0

        process.hltPhase2InitialStepSeeds.InputCollection = cms.InputTag("hltPhase2PixelTracksMerger")
	
	if options.froml1:
                process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")
                process.hltPhase2PixelTracksCleaner.vertexTag = cms.InputTag("hltPhase2L1PrimaryVertex")
else:
	process.hltPhase2PixelTracksMerger = process.hltPhase2PixelTracksCleaner.clone()	
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
elif options.susy:
    suff = suff + "_susy"
elif options.dyll:
    suff = suff + "_dyll"
elif options.noPU:
    suff = suff + "_noPU"
elif options.pu140:
    suff = suff + "_pu140"
else:
    suff = suff + "_ttb"
  
    # if not timing and not options.onlypixel:
    #     process.prevalidation_startup = process.prevalidation_startup_offline
    #     process.dqm_vertex = process.dqm_vertex_offline
    # elif not timing:
    #     process.prevalidation_startup = process.prevalidation_startup_offline
    #     process.dqm_commons = process.dqm_commons_offline

suff = suff + "_skip_" + str(options.skip) + "_n_" + str(options.n)

if options.clean:
    suff = suff + "_zVtx" + str(options.zVtx)
    suff = suff + "_rhoVtx" + str(options.rhoVtx)
if options.l1extended:
    process.hltPhase2L1TrackSeedsFromL1Tracks.InputCollection = cms.InputTag("TTTracksFromExtendedTrackletEmulation","Level1TTTracks")
if options.fullvertex or not options.timing:
    process.schedule.extend([process.vertexing])
    suff = suff + "_fullvertexing"

if options.fastl1:
    process.hltPhase2L1PrimaryVertex.TrackLabel = cms.InputTag("hltPhase2TrackFromL1")
    suff = suff + "_fastl1vertex"
elif options.froml1 and not options.timing:
    process.hltPhase2VertexAnalysisL1.vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex","hltPhase2VertexFromL1")
    suff = suff + "_froml1vertex"
if options.patavertex:
    suff = suff + "_patavertex"
if options.patatrack:
    customizePixelTracksSoAonCPU(process,options.patavertex)
#    if options.wf == -5:
 #       process.hltPhase2InitialStepSeeds = process.hltPhase2SoAPixelSeeds.clone()
    process.hltPhase2PixelTrackSoA.doRegion = options.doregion
    process.hltPhase2PixelTracks.keepBad = options.keepBad
    process.hltPhase2PixelTracks.keepDup = options.keepDup
    if options.clean:
	suff = suff + "_clean"
    if options.keepBad < 99:
	suff = suff + "_keepBad_"+str(options.keepBad)
    if options.keepDup <99:
	 suff = suff + "_keepDup_"+str(options.keepDup)
    if options.doregion:  
	if options.froml1:
		process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
		suff = suff + "_regionFomL1"
	##process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
		#process.pixelVertexCoordinates.src = "hltPhase2L1PrimaryVertex"
    	else:
		suff = suff + "_regionL1"
    
    if options.pixtrip:
        process.hltPhase2PixelTrackSoA.minHitsPerNtuplet = 3
	suff = suff + "_pixtrips"
    suff = suff + "_pata"
    process.quickTrackAssociatorByHits.Purity_SimToReco = cms.double(0.65)
if options.davertex:
    process.hltPhase2PixelVertices = process.hltPhase2DAPrimaryVerticesUnsorted.clone()
    suff = suff + "_da"
elif not options.patavertex:
    process.hltPhase2PixelVertices.ZSeparation = float(options.zsep) / 1000.0

if hasattr(process,"hltPhase2InitialStepSeeds"):	
	process.hltPhase2InitialStepSeeds.useProtoTrackKinematics = cms.bool(options.protokin)
if hasattr(process,"hltPhase2HighPtTripletStepSeeds"):
	if options.allpata==True or options.wf <=-5:
		process.hltPhase2HighPtTripletStepSeeds.useProtoTrackKinematics = cms.bool(options.protokin)

if not options.patatrack:
	process.hltPhase2PixelVertices.TrackCollection = cms.InputTag( "hltPhase2PixelTracks")
	
if options.protokin:
	suff = suff + "_protokin"

suff = suff + "_zsep_" + str(options.zsep)

suff = suff + "_" + options.note

if options.nol1:
	process.hltPhase2InitialStepTrackCandidates.phase2clustersToSkip = cms.InputTag("hltPhase2InitialStepClusters")
	process.hltPhase2HighPtTripletStepSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
    	process.hltPhase2HighPtTripletStepSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2HighPtTripletStepClusters")
	process.hltPhase2HighPtTripletStepClusters.oldClusterRemovalInfo = cms.InputTag("hltPhase2InitialStepClusters")
	
	process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','highPtTripletStep')
    	process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTracksSelectionHighPurity","hltPhase2HighPtTripletStepTracksSelectionHighPurity")
    	process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0,0)
    	process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    	process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2HighPtTripletStepTracksSelectionHighPurity"))
	process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

	suff = suff + "_nol1"

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")
	if not options.timing:
		process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks","hltPhase2CutsRecoTracksHighPtTripletStepHp",
    "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp","hltPhase2CutsRecoTracksHighPtTripletStep",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo","hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp",
    "hltPhase2CutsRecoTracksL1StepByOriginalAlgo","hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp")

if options.patatrack and not options.timing:
	process.hltPhase2PixelVertexAnalysisTrackingOnly.vertexRecoCollections.append("vertexFromL1") # = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices","hltPhase2TrimmedPixelVertices")
	
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

if options.timing:
	suff = suff + "_timing_nthreads_" + str(options.threads)

process.FastTimerService.jsonFileName = cms.untracked.string('wf_' + suff + '.json')

process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dumper = cms.Path(process.dump)


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

if options.timing:
   open('step3_dump.py', 'w').write(process.dumpPython())
# Customisation from command line
process = customise_aging_1000(process)

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
