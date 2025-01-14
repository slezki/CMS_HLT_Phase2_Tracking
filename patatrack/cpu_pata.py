# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --conditions auto:phase1_2018_realistic -n 10 --era Run2_2018 --eventcontent RECOSIM,DQM --runUnscheduled --procModifiers gpu -s RAW2DIGI:RawToDigi_pixelOnly,RECO:reconstruction_pixelTrackingOnly,VALIDATION:@pixelTrackingOnlyValidation,DQM:@pixelTrackingOnlyDQM --datatier GEN-SIM-RECO,DQMIO --geometry DB:Extended --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

from Configuration.ProcessModifiers.pixelNtupleFit_cff import pixelNtupleFit
import FWCore.ParameterSet.VarParsing as VarParsing

from DQM.SiTrackerPhase2.Phase2TrackerMonitorDigi_cff import *
from DQM.SiTrackerPhase2.Phase2ITMonitorRecHit_cff import *

from Validation.SiTrackerPhase2V.Phase2TrackerValidateDigi_cff import *
from Validation.SiTrackerPhase2V.Phase2ITValidateRecHit_cff import *


#from ttbar import ttbar

def customizePixelTracksSoAonCPU(process) :

  from RecoLocalTracker.SiPixelRecHits.siPixelRecHitHostSoA_cfi import siPixelRecHitHostSoA as _siPixelRecHitFromSOA
  #from RecoPixelVertexing.PixelVertexFinding.pixelVertexCoordinates_cfi import pixelVertexCoordinates as _pixelVertexCoordinates

  process.load('RecoLocalTracker/SiPixelRecHits/siPixelRecHitHostSoA_cfi')
  process.load('RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi')
  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexFromSoA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexCUDA_cfi')

  process.pixelTrackSoA = process.caHitNtupletCUDA.clone()
  process.pixelTrackSoA.onGPU = False
  process.pixelTrackSoA.pixelRecHitSrc = 'siPixelRecHitsPreSplitting'#'siPixelRecHitHostSoA'

  # process.pixelTrackSoA.earlyFishbone = False
  process.pixelTrackSoA.lateFishbone = True

  #process.pixelTrackSoA.CAThetaCutBarrel  = 0.0020 * 2
  #process.pixelTrackSoA.CAThetaCutForward = 0.0025 * 2

  process.pixelTrackSoA.trackQualityCuts.tripletMinPt = 0.5
  process.pixelTrackSoA.trackQualityCuts.tripletMaxTip = 0.22
  process.pixelTrackSoA.trackQualityCuts.tripletMaxZip = 13.0

  process.pixelTrackSoA.trackQualityCuts.quadrupletMinPt = 0.5
  process.pixelTrackSoA.trackQualityCuts.quadrupletMaxTip = 0.15
  process.pixelTrackSoA.trackQualityCuts.quadrupletMaxZip = 11.5

  #process.pixelTrackSoA.trackQualityCuts.upgrade = True
  #process.pixelTrackSoA.trackQualityCuts.tripletChi2MaxPt = 2.5
  #process.pixelTrackSoA.trackQualityCuts.chi2MaxPt = 2.5

  process.pixelVertexSoA = process.pixelVertexCUDA.clone()
  process.pixelTrackSoA.isUpgrade = True
  process.pixelTrackSoA.doClusterCut= False

  #process.pixelVertexSoA.eps = 0.01
#  process.pixelVertexSoA.onGPU = False
#  process.pixelVertexSoA.pixelTrackSrc = 'pixelTrackSoA'
  process.pixelTracks = process.pixelTrackProducerFromSoA.clone()
  process.pixelTracks.pixelRecHitLegacySrc = 'siPixelRecHitsPreSplitting'#'siPixelRecHitHostSoA'

  process.siPixelRecHitsPreSplitting = _siPixelRecHitFromSOA.clone()
  process.siPixelRecHitsPreSplitting.Upgrade = True
  process.siPixelRecHitsPreSplittingTask = cms.Task(process.siPixelRecHitsPreSplitting)
  process.siPixelRecHitsPreSplitting.convertToLegacy = True
  
  #process.vertexFromL1 = cms.EDProducer("L1ToVertex")
  #process.pixelVertexCoordinates = _pixelVertexCoordinates.clone()
  #process.pixelVertexCoordinates.src = "vertexFromL1"

  process.PixelCPEFastESProducer.Upgrade = True
  process.pixeltrackerlocalrecoTask = cms.Task(process.siPixelClustersPreSplittingTask,process.siPixelRecHitsPreSplittingTask)
  process.reconstruction_step += process.pixelTrackSoA

  return process

def customizePixelTracksSoAonGPU(process) :

  from RecoLocalTracker.SiPixelRecHits.siPixelRecHitHostSoA_cfi import siPixelRecHitHostSoA as _siPixelRecHitFromSOA

  process.load('RecoLocalTracker/SiPixelRecHits/siPixelRecHitHostSoA_cfi')
  process.load('RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi')
  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackSoA_cfi')
  process.load('RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexFromSoA_cfi')
  process.load('RecoPixelVertexing.PixelVertexFinding.pixelVertexCUDA_cfi')

  from RecoLocalTracker.SiPixelClusterizer.siPixelClusterDigisCUDA_cfi import siPixelClusterDigisCUDA
  from RecoLocalTracker.SiPixelClusterizer.siPixelDigisClustersFromSoA_cfi import siPixelDigisClustersFromSoA
  from RecoLocalTracker.SiPixelRecHits.siPixelRecHitCUDA_cfi import siPixelRecHitCUDA
  from RecoLocalTracker.SiPixelRecHits.siPixelRecHitFromSOA_cfi import siPixelRecHitFromSOA

  #from RecoPixelVertexing.PixelTriplets.caHitNtupletCUDA_cfi import caHitNtupletCUDA
  #from RecoPixelVertexing.PixelTrackFitting.pixelTrackSoA_cfi import pixelTrackSoA
  #from RecoPixelVertexing.PixelTrackFitting.pixelTrackProducerFromSoA_cfi import pixelTrackProducerFromSoA as _pixelTrackFromSoA

  process.pixelTrackCUDA = process.caHitNtupletCUDA.clone()
  process.pixelTrackCUDA.onGPU = True
  process.pixelTrackCUDA.pixelRecHitSrc = 'siPixelRecHitCUDA'#'siPixelRecHitHostSoA'

  # process.pixelTrackSoA.earlyFishbone = False
  # process.pixelTrackSoA.lateFishbone = True

  process.pixelTrackCUDA.trackQualityCuts.tripletMinPt = 0.5
  process.pixelTrackCUDA.trackQualityCuts.tripletMaxTip = 0.1
  process.pixelTrackCUDA.trackQualityCuts.tripletMaxZip = 7.5
  process.pixelTrackCUDA.trackQualityCuts.quadrupletMinPt = 0.5
  process.pixelTrackCUDA.trackQualityCuts.quadrupletMaxTip = 0.09
  process.pixelTrackCUDA.trackQualityCuts.quadrupletMaxZip = 9.0
  #process.pixelTrackCUDA.trackQualityCuts.upgrade = True
  #process.pixelTrackCUDA.trackQualityCuts.tripletChi2MaxPt = 2.5
  #process.pixelTrackCUDA.trackQualityCuts.chi2MaxPt = 1.8

  process.pixelVertexSoA = process.pixelVertexCUDA.clone()
  process.pixelTrackCUDA.isUpgrade = True

  process.pixelTrackSoA.src = 'pixelTrackCUDA'
  process.pixelTrackCUDA.doClusterCut= False

  #process.pixelVertexSoA.eps = 0.01
  process.pixelVertexSoA.onGPU = True
  process.pixelVertexSoA.pixelTrackSrc = 'pixelTrackSoA'
  
  
  process.pixelTracks = process.pixelTrackProducerFromSoA.clone()
  process.pixelTracks.pixelRecHitLegacySrc = 'siPixelRecHitsPreSplitting'#'siPixelRecHitFromSOA'#'siPixelRecHitHostSoA'

  #process.pixelVertices = process.pixelVertexFromSoA.clone()

  process.siPixelRecHitsPreSplitting = _siPixelRecHitFromSOA.clone()
  process.siPixelRecHitsPreSplitting.Upgrade = True
  process.siPixelRecHitsPreSplittingTask = cms.Task(process.siPixelRecHitsPreSplitting)
  process.siPixelRecHitsPreSplitting.convertToLegacy = True

  process.PixelCPEFastESProducer.Upgrade = True

  process.siPixelClusterDigisCUDA = siPixelClusterDigisCUDA.clone()
#  process.siPixelDigisClustersFromSoA = siPixelDigisClustersFromSoA.clone()
#  process.siPixelDigisClustersPreSplitting = siPixelDigisClustersFromSoA.clone()
  from EventFilter.SiPixelRawToDigi.siPixelDigisSoAFromCUDA_cfi import siPixelDigisSoAFromCUDA as _siPixelDigisSoAFromCUDA
   
  process.siPixelDigisSoA = _siPixelDigisSoAFromCUDA.clone(
    src = "siPixelClusterDigisCUDA",
    #Upgrade = True
)

  process.siPixelClustersPreSplitting = siPixelDigisClustersFromSoA.clone()
  process.siPixelClustersPreSplitting.src = "siPixelDigisSoA"
  process.siPixelClustersPreSplitting.Upgrade = True
#  process.siPixelRecHitFromSOA = siPixelRecHitFromSOA.clone()
#  process.siPixelRecHitFromSOA.pixelRecHitSrc = 'siPixelRecHitCUDA'
  process.siPixelRecHitsPreSplitting = siPixelRecHitFromSOA.clone()
  process.siPixelRecHitsPreSplitting.pixelRecHitSrc = 'siPixelRecHitCUDA'

#  process.siPixelClustersPreSplitting = siPixelRecHitFromSOA.clone()
#  process.siPixelClustersPreSplitting.pixelRecHitSrc = 'siPixelRecHitCUDA'
   
  process.siPixelRecHitCUDA = siPixelRecHitCUDA.clone()
  process.siPixelRecHitCUDA.src = 'siPixelClusterDigisCUDA'
  
  process.siPixelClustersPreSplittingTask_gpu = cms.Task(
    process.siPixelClusterDigisCUDA,
    process.siPixelDigisSoA,
    process.siPixelClustersPreSplitting #siPixelDigisClustersFromSoA
  )

  process.siPixelRecHitsPreSplittingTask_gpu = cms.Task(
    process.siPixelRecHitCUDA,
    process.siPixelRecHitsPreSplitting #siPixelRecHitFromSOA
  )

  process.PixelCPEFastESProducer.Upgrade = True
  
  #process.pixeltrackerlocalrecoTask = cms.Task(process.siPixelClustersPreSplittingTask,process.siPixelRecHitsPreSplittingTask)
  process.reconstruction_step += process.siPixelClusterDigisCUDA + process.siPixelDigisSoA + process.siPixelRecHitCUDA +process.offlineBeamSpotCUDA + process.pixelTrackCUDA + process.pixelTrackSoA + process.pixelVertexSoA
  #process.pixeltrackerlocalrecoTask = cms.Task(process.siPixelClustersPreSplittingTask_gpu,process.siPixelRecHitsPreSplittingTask_gpu)
  
  return process

process = cms.Process('RECO2',Phase2C9)#,pixelNtupleFit)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')

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


options = VarParsing.VarParsing('analysis')
options.register ('pixelVal',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "Pixel Validation On/Off")
options.register ('soa',
                  True, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "SoAs")
options.register ('debug',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "debug")
options.register ('n',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "n")
options.register ('threads',
                  8, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "threads")
options.register ('skip',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "events to skip")
options.register ('gpu',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "gpu")
options.register ('triplets',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "triplets")
options.register ('fullcontent',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "fullcontent")
options.register ('note',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "noting")
options.register ('eos',
                  True, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "eos")
options.register ('nopu',
                  True, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "nopu")
options.register ('timing',
                  False, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.bool,          # string, int, or float
                  "timing")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.n),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.MessageLogger = cms.Service("MessageLogger",
       destinations      = cms.untracked.vstring('myDebugOutputFile'),
       myDebugOutputFile = cms.untracked.PSet(
                                threshold = cms.untracked.string('DEBUG'),
                                default = cms.untracked.PSet(limit = cms.untracked.int32(-1))),
       debugModules      = cms.untracked.vstring('*')                               #7
)

if options.eos:
   ttbar = [
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/1E594011-12B6-1E4A-A56D-B59B357E97FE.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280001/08643AB5-6B23-C845-9B31-F7E0DE8CCF31.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/68486F17-8281-C14F-BD96-45A4E52DCB82.root"]

["/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FC47CF76-E9D0-B140-9C3E-AD994236A741.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FC56902D-DB9B-8844-ABB3-6E5F78B53E86.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FC589844-A73C-954F-BB0E-FA5FC095B1F4.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FCAA527A-329A-364E-83C3-A51122C545FD.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FCACFB78-AF68-5A48-9FEC-A323FD8EEE2E.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FCCA1ABA-C564-D74E-9F43-D41529C8EAEB.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FCDDAE03-8A9D-B44C-B42B-8446EDBB5236.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FCFDFCC2-F905-C246-8827-E5FED5204905.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FE3E90BC-C4F4-4040-BFB6-868C48E88215.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FEA85932-B228-F243-BE4C-3311AE475A4A.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FEAF20C5-8D1A-954E-A081-632FBE5745B1.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FEC64627-0B7B-B841-9667-10C13141B0E5.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FF5230B3-138E-5345-9C29-23945BBC0519.root",
"/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/280000/FFAF8045-404D-464C-9BDB-73B0AF032A55.root"]

if options.nopu:
   ttbar = ["/store/mc/Phase2HLTTDRSummer20ReRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/FEVT/NoPU_111X_mcRun4_realistic_T15_v1-v1/100000/DAF55EAB-0B6F-C646-B7DE-2D54C8A62073.root",
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

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(ttbar),
    secondaryFileNames = cms.untracked.vstring(),
    skipEvents=cms.untracked.uint32(options.skip)
)


if True and options.pixelVal:
    pixrechit = "siPixelRecHitsPreSplitting@cpu"
    process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('file:2C5C22E5-A92E-C64D-9BEC-7AE84777A41F.root'))


if options.pixelVal:

    if options.soa:
            pixrechit = "siPixelRecHitsPreSplitting"

    process.ReadLocalMeasurement = cms.EDAnalyzer("Phase2PixelNtuple",
       trackProducer = cms.InputTag("generalTracks"),
       siPixelRecHits = cms.InputTag(pixrechit),
       #verbose = cms.untracked.bool(True),
       #picky = cms.untracked.bool(False),
       ### for using track hit association
       associatePixel = cms.bool(True),
       associateStrip = cms.bool(False),
       associateRecoTracks = cms.bool(False),
       ROUList = cms.vstring('TrackerHitsPixelBarrelLowTof',
                             'TrackerHitsPixelBarrelHighTof',
                             'TrackerHitsPixelEndcapLowTof',
                             'TrackerHitsPixelEndcapHighTof'),
       usePhase2Tracker = cms.bool(True),
       pixelSimLinkSrc = cms.InputTag("simSiPixelDigis", "Pixel"),
       phase2TrackerSimLinkSrc = cms.InputTag("simSiPixelDigis", "Tracker")
    )

    process.pixel_val = cms.Path(process.ReadLocalMeasurement)

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
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
reconame = 'file:step3'
dqmname = 'file:step3_inDQM'
if options.soa:
    reconame = 'file:step3_pata'
    dqmname  = 'file:step3_inDQM_pata'

suff = "_" + str(options.n) + "_" + str(options.skip)

if options.triplets:
    suff = suff + "_triplets"
if options.gpu:
    suff = suff + "_gpu"
suff = suff + "_" + options.note
reconame = reconame + suff + ".root"
dqmname  = dqmname  + suff + ".root"

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(reconame),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(dqmname),
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


process.trackerphase2DQMSource = cms.Sequence( pixDigiMon 
                                       +rechitMonitorIT)
process.trackerphase2ValidationSource = cms.Sequence(pixDigiValid  
                                             + rechitValidIT)

process.globalValidationPixelTrackingOnly +=process.trackerphase2ValidationSource
process.DQMOfflinePixelTracking += process.trackerphase2DQMSource

process.rechitValidIT.rechitsSrc = "siPixelRecHitsPreSplitting"
process.rechitMonitorIT.rechitsSrc = "siPixelRecHitsPreSplitting" 
process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dumper = cms.Path(process.dump)

# Schedule definition

process.schedule = cms.Schedule(process.raw2digi_step)

if options.pixelVal and not options.timing:
    process.load('Configuration.StandardSequences.Digi_cff')

    process.digitisation_step = cms.Path(process.pdigi_valid)

    process.schedule = cms.Schedule([process.digitisation_step])

process.schedule.extend([process.reconstruction_step])

if options.debug:
    process.schedule.extend([process.dumper])

if not options.timing:
	process.schedule.extend([process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step])
	if options.pixelVal:
    		process.schedule.extend([process.pixel_val])
    		process.schedule.extend([process.DQMoutput_step])
	elif options.fullcontent:
    		process.schedule.extend([process.RECOSIMoutput_step,process.DQMoutput_step])
	else:
    		process.schedule.extend([process.DQMoutput_step])
else:
	process.consumer = cms.EDAnalyzer("GenericConsumer",
   		 eventProducts = cms.untracked.vstring('pixelVertices','pixelTracks'))	

	process.consume_step = cms.EndPath(process.consumer)

	process.schedule.append(process.consume_step)


from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
if options.soa:
    if options.gpu:
        customizePixelTracksSoAonGPU(process)
    else:
        customizePixelTracksSoAonCPU(process)

    if options.triplets:
        process.pixelTrackSoA.minHitsPerNtuplet = 3
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

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

if options.pixelVal:
    process.TFileService = cms.Service('TFileService',
    fileName = cms.string("pixelntuple.root")
    )
