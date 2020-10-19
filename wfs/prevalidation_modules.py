import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import quickTrackAssociatorByHits, quickTrackAssociatorByHits, tpClusterProducer
from  Configuration.StandardSequences.Validation_cff import trackingParticlesBHadron, simHitTPAssocProducer, trackingParticlesConversion
from  Configuration.StandardSequences.Validation_cff import trackingParticleNumberOfLayersProducer

####################################################
########################## Pixel Tracks
#############

hltPhase2PixelVertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation")
)

hltPhase2VertexAssociatorByPositionAndTracks = hltPhase2PixelVertexAssociatorByPositionAndTracks.clone(
    trackAssociation = cms.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation")
)

hltPhase2VertexAssociatorByPositionAndL1Tracks = hltPhase2PixelVertexAssociatorByPositionAndTracks.clone(
    trackAssociation = cms.InputTag("hltPhase2TrackingParticleL1TrackAsssociation")
)

##Tracks selectors
from CommonTools.RecoAlgos.recoTrackViewRefSelector_cfi import recoTrackViewRefSelector

hltPhase2CutsRecoTracksHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(9),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-9),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9), # previous 0.1
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(120),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2CutsRecoTracksBtvLike = hltPhase2CutsRecoTracksHp.clone(
    lip = cms.double(17.0),
    maxChi2 = cms.double(5.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(9),
    minLayer = cms.int32(0),
    minPixelHit = cms.int32(1),
    ptMin = cms.double(0.9),
    quality = cms.vstring(''),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    tip = cms.double(0.2),
    usePV = cms.bool(True),
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)


hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)

hltPhase2CutsRecoTracksFromPVHp = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)


hltPhase2CutsRecoTracksFromPVInitialStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)


hltPhase2CutsRecoTracksFromPVInitialStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)

hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
)


hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
)

hltPhase2CutsRecoTracksFromPVPt09Hp = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
)

hltPhase2CutsRecoTracksFromPVPt09InitialStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
)


hltPhase2CutsRecoTracksFromPVPt09InitialStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
)


hltPhase2CutsRecoTracksHighPtTripletStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
)


hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
)


hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
)

hltPhase2CutsRecoTracksL1StepByOriginalAlgo  = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(''),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('hltIter0'),
    quality = cms.vstring(''),
)

hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(""),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('hltIter0'),
    quality = cms.vstring('highPurity'),
)


hltPhase2CutsRecoTracksHighPtTripletStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
)


hltPhase2CutsRecoTracksInitialStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
)


hltPhase2CutsRecoTracksL1 = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('hltIter0'),
)

hltPhase2CutsRecoTracksInitialStepByAlgoMask = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
)


hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgo = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('initialStep'),
)


hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    originalAlgorithm = cms.vstring('initialStep'),
)


hltPhase2CutsRecoTracksInitialStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    quality = cms.vstring('highPurity'),
)

hltPhase2L1CtfTracksPt09 = hltPhase2CutsRecoTracksHp.clone(
    src = cms.InputTag("hltPhase2L1CtfTracks"),
)

hltPhase2CutsRecoTracksL1Step = hltPhase2CutsRecoTracksHp.clone(
    maxRapidity = cms.double(2),
    minRapidity = cms.double(-2),
    ptMin = cms.double(2.0), # previous 0.1
    src = cms.InputTag("hltPhase2L1CtfTracks"),
)

hltPhase2CutsRecoTracksL1StepHp = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2L1CtfTracks"),
)

hltPhase2CutsRecoTracksPt09L1StepHp = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2L1CtfTracksPt09"),
)

hltPhase2CutsRecoTracksPt09HighPtTripletStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
)


hltPhase2CutsRecoTracksPt09HighPtTripletStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('highPtTripletStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
)

hltPhase2CutsRecoTracksPt09Hp = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
)


hltPhase2CutsRecoTracksPt09InitialStep = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
)


hltPhase2CutsRecoTracksPt09InitialStepHp = hltPhase2CutsRecoTracksHp.clone(
    algorithm = cms.vstring('initialStep'),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("hltPhase2GeneralTracksPt09"),
)

hltPhase2GeneralTracksFromPVPt09 = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
)


hltPhase2GeneralTracksPt09 = hltPhase2CutsRecoTracksHp.clone(
    quality = cms.vstring('loose'),
    src = cms.InputTag("hltPhase2GeneralTracks"),
)

## Track From Vertex
hltPhase2GeneralTracksFromPV = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5),
    etaMin = cms.double(-5),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(1),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    ptErrorCut = cms.double(10000000000.0),
    ptMax = cms.double(10000000000.0),
    ptMin = cms.double(0.9), # previous 0
    quality = cms.string('loose'),
    rhoVtx = cms.double(10000000000.0),
    src = cms.InputTag("hltPhase2GeneralTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("hltPhase2PixelVertices"), #("hltPhase2OfflinePrimaryVertices"),
    vtxFallback = cms.bool(False),
    zetaVtx = cms.double(0.1)
)

##Track From Seed
hltPhase2SeedTrackshighPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2HighPtTripletStepSeeds")
)


hltPhase2SeedTracksinitialStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("hltPhase2InitialStepSeeds")
)

##Track Associators
hltPhase2TrackingParticleRecoTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("hltPhase2GeneralTracks")
)

hltPhase2TrackingParticlePixelTrackAsssociation = hltPhase2TrackingParticleRecoTrackAsssociation.clone(
    label_tr = cms.InputTag("hltPhase2PixelTracks")
)

hltPhase2TrackingParticleL1TrackAsssociation = hltPhase2TrackingParticleRecoTrackAsssociation.clone(
    label_tr = cms.InputTag("hltPhase2L1CtfTracks")
)

##TP Selection
hltPhase2TrackingParticlesSignal = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(False),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False), #cmssw_11_1
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), #10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), #-10
    pdgId = cms.vint32(),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(True),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

hltPhase2TrackingParticlesElectron = hltPhase2TrackingParticlesSignal.clone(
    pdgId = cms.vint32(-11, 11),
)

from Validation.RecoVertex.v0validator_cfi import v0Validator

hltPhase2V0Validator = v0Validator.clone(
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    vertexCollection = cms.untracked.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVertices","","RECO") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2SelectedOfflinePrimaryVerticesWithBS = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2OfflinePrimaryVerticesWithBS")
)

hltPhase2SelectedPixelVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("hltPhase2PixelVertices")
)

from Validation.RecoVertex.PrimaryVertexAnalyzer4PUSlimmed_cfi import vertexAnalysis

hltPhase2VertexAnalysisTrackingOnly = vertexAnalysis.clone(
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2OfflinePrimaryVertices", "hltPhase2OfflinePrimaryVerticesWithBS", "hltPhase2SelectedOfflinePrimaryVertices", "hltPhase2SelectedOfflinePrimaryVerticesWithBS")#, "hltPhase2FirstStepPrimaryVertices")
)

hltPhase2VertexAnalysisL1 = vertexAnalysis.clone(
    trackAssociatorMafp = cms.untracked.InputTag("hltPhase2TrackingParticleL1TrackAsssociation"),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndL1Tracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex")#
)

hltPhase2V0ValidatorL1 = v0Validator.clone(
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleL1TrackAsssociation"),
    vertexCollection = cms.untracked.InputTag("hltPhase2L1PrimaryVertex") #("hltPhase2OfflinePrimaryVertices")
)

hltPhase2PixelVertexAnalysisTrackingOnly = vertexAnalysis.clone(
    trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
    do_generic_sim_plots = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices")#,"hltPhase2TrimmedPixelVertices")#,"offlinePrimaryVertices")
)
