# 69080ebc9cf4715778881890cbd1e30586e69162 for full format without process.hltPhase2*
import FWCore.ParameterSet.Config as cms
from phase2_tracking import *

def customise_prevalidation_common(process):

    process.hltPhase2PixelVertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
        absT = cms.double(-1),
        absZ = cms.double(0.1),
        maxRecoT = cms.double(-1),
        maxRecoZ = cms.double(1000),
        sharedTrackFraction = cms.double(-1),
        sigmaT = cms.double(-1),
        sigmaZ = cms.double(3),
        trackAssociation = cms.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation")
    )

    process.hltPhase2VertexAssociatorByPositionAndTracks = process.hltPhase2PixelVertexAssociatorByPositionAndTracks.clone(
        trackAssociation = cms.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation")
    )

    process.hltPhase2VertexAssociatorByPositionAndL1Tracks = process.hltPhase2PixelVertexAssociatorByPositionAndTracks.clone(
        trackAssociation = cms.InputTag("hltPhase2TrackingParticleL1TrackAsssociation")
    )

    ##Tracks selectors
    from CommonTools.RecoAlgos.recoTrackViewRefSelector_cfi import recoTrackViewRefSelector

    process.hltPhase2CutsRecoTracksHp = cms.EDProducer("RecoTrackViewRefSelector",
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

    process.hltPhase2CutsRecoTracksBtvLike = process.hltPhase2CutsRecoTracksHp.clone(
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


    process.hltPhase2CutsRecoTracksFromPVHighPtTripletStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )


    process.hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )

    process.hltPhase2CutsRecoTracksFromPVHp = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )


    process.hltPhase2CutsRecoTracksFromPVInitialStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )


    process.hltPhase2CutsRecoTracksFromPVInitialStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )

    process.hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    )


    process.hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    )

    process.hltPhase2CutsRecoTracksFromPVPt09Hp = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    )

    process.hltPhase2CutsRecoTracksFromPVPt09InitialStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    )


    process.hltPhase2CutsRecoTracksFromPVPt09InitialStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPVPt09"),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(''),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
    )

    process.hltPhase2CutsRecoTracksL1StepByOriginalAlgo  = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(''),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('hltIter0'),
        quality = cms.vstring(''),
    )

    process.hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(""),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('hltIter0'),
        quality = cms.vstring('highPurity'),
    )


    process.hltPhase2CutsRecoTracksHighPtTripletStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
    )


    process.hltPhase2CutsRecoTracksInitialStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
    )


    process.hltPhase2CutsRecoTracksL1 = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('hltIter0'),
    )

    process.hltPhase2CutsRecoTracksInitialStepByAlgoMask = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring('initialStep'),
    )


    process.hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring('initialStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracks"),
    )


    process.hltPhase2CutsRecoTracksInitialStepByOriginalAlgo = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('initialStep'),
    )


    process.hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring(),
        algorithmMaskContains = cms.vstring(),
        originalAlgorithm = cms.vstring('initialStep'),
    )


    process.hltPhase2CutsRecoTracksInitialStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        algorithmMaskContains = cms.vstring(),
        quality = cms.vstring('highPurity'),
    )

    process.hltPhase2L1CtfTracksPt09 = process.hltPhase2CutsRecoTracksHp.clone(
        src = cms.InputTag("hltPhase2L1CtfTracks"),
    )

    process.hltPhase2CutsRecoTracksL1Step = process.hltPhase2CutsRecoTracksHp.clone(
        maxRapidity = cms.double(2),
        minRapidity = cms.double(-2),
        ptMin = cms.double(2.0), # previous 0.1
        src = cms.InputTag("hltPhase2L1CtfTracks"),
    )

    process.hltPhase2CutsRecoTracksL1StepHp = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2L1CtfTracks"),
    )

    process.hltPhase2CutsRecoTracksPt09L1StepHp = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2L1CtfTracksPt09"),
    )

    process.hltPhase2CutsRecoTracksPt09HighPtTripletStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    )


    process.hltPhase2CutsRecoTracksPt09HighPtTripletStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('highPtTripletStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    )

    process.hltPhase2CutsRecoTracksPt09Hp = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    )


    process.hltPhase2CutsRecoTracksPt09InitialStep = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    )


    process.hltPhase2CutsRecoTracksPt09InitialStepHp = process.hltPhase2CutsRecoTracksHp.clone(
        algorithm = cms.vstring('initialStep'),
        quality = cms.vstring('highPurity'),
        src = cms.InputTag("hltPhase2GeneralTracksPt09"),
    )

    process.hltPhase2GeneralTracksFromPVPt09 = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    )


    process.hltPhase2GeneralTracksPt09 = process.hltPhase2CutsRecoTracksHp.clone(
        quality = cms.vstring('loose'),
        src = cms.InputTag("hltPhase2GeneralTracks"),
    )

    ## Track From Vertex
    process.hltPhase2GeneralTracksFromPV = cms.EDProducer("TrackWithVertexRefSelector",
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
    process.hltPhase2SeedTrackshighPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
        TTRHBuilder = cms.string('WithoutRefit'),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        src = cms.InputTag("hltPhase2HighPtTripletStepSeeds")
    )


    process.hltPhase2SeedTracksinitialStepSeeds = cms.EDProducer("TrackFromSeedProducer",
        TTRHBuilder = cms.string('WithoutRefit'),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        src = cms.InputTag("hltPhase2InitialStepSeeds")
    )

    ##Track Associators
    process.hltPhase2TrackingParticleRecoTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
        associator = cms.InputTag("quickTrackAssociatorByHits"),
        ignoremissingtrackcollection = cms.untracked.bool(False),
        label_tp = cms.InputTag("mix","MergedTrackTruth"),
        label_tr = cms.InputTag("hltPhase2GeneralTracks")
    )

    process.hltPhase2TrackingParticlePixelTrackAsssociation = process.hltPhase2TrackingParticleRecoTrackAsssociation.clone(
        label_tr = cms.InputTag("hltPhase2PixelTracks")
    )

    process.hltPhase2TrackingParticleL1TrackAsssociation = process.hltPhase2TrackingParticleRecoTrackAsssociation.clone(
        label_tr = cms.InputTag("hltPhase2L1CtfTracks")
    )

    ##TP Selection
    process.hltPhase2TrackingParticlesSignal = cms.EDFilter("TrackingParticleRefSelector",
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

    process.hltPhase2TrackingParticlesElectron = process.hltPhase2TrackingParticlesSignal.clone(
        pdgId = cms.vint32(-11, 11),
    )

    from Validation.RecoVertex.v0validator_cfi import v0Validator

    process.hltPhase2V0Validator = v0Validator.clone(
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
        vertexCollection = cms.untracked.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
    )

    process.hltPhase2SelectedOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
        cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2OfflinePrimaryVertices","","RECO") #("hltPhase2OfflinePrimaryVertices")
    )

    process.hltPhase2SelectedOfflinePrimaryVerticesWithBS = cms.EDFilter("VertexSelector",
        cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2OfflinePrimaryVerticesWithBS")
    )

    process.hltPhase2SelectedPixelVertices = cms.EDFilter("VertexSelector",
        cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2PixelVertices")
    )

    from Validation.RecoVertex.PrimaryVertexAnalyzer4PUSlimmed_cfi import vertexAnalysis

    process.hltPhase2VertexAnalysisTrackingOnly = vertexAnalysis.clone(
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
        vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
        vertexRecoCollections = cms.VInputTag("hltPhase2OfflinePrimaryVertices", "hltPhase2OfflinePrimaryVerticesWithBS", "hltPhase2SelectedOfflinePrimaryVertices", "hltPhase2SelectedOfflinePrimaryVerticesWithBS")#, "hltPhase2FirstStepPrimaryVertices")
    )

    process.hltPhase2VertexAnalysisL1 = vertexAnalysis.clone(
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
        vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
        vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex")#
    )

    process.hltPhase2PixelVertexAnalysisTrackingOnly = vertexAnalysis.clone(
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
        do_generic_sim_plots = cms.untracked.bool(False),
        vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
        vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices")#,"hltPhase2TrimmedPixelVertices")#,"offlinePrimaryVertices")
    )

    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")# import quickTrackAssociatorByHits
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")# import tpClusterProducer
    process.load("Validation.RecoTrack.TrackValidation_cff")# import trackingParticlesBHadron,trackingParticlesConversion,trackingParticleNumberOfLayersProducer
    process.load("SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi")# import simHitTPAssocProducer

    process.prevalidation_commons = cms.Task(
                                    process.quickTrackAssociatorByHits,
                                    process.tpClusterProducer,process.trackingParticlesBHadron,process.simHitTPAssocProducer,
                                    process.trackingParticlesConversion,process.trackingParticleNumberOfLayersProducer,
                                    process.hltPhase2TrackingParticlesSignal,process.hltPhase2TrackingParticlesElectron)

    process.prevalidation_highpt = cms.Task(process.hltPhase2CutsRecoTracksFromPVHighPtTripletStep,process.hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp,process.hltPhase2SeedTrackshighPtTripletStepSeeds,
                                              process.hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep,process.hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp,
                                              process.hltPhase2CutsRecoTracksHighPtTripletStep,process.hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask,
                                              process.hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp,process.hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo,
                                              process.hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp,process.hltPhase2CutsRecoTracksHighPtTripletStepHp,
                                              process.hltPhase2CutsRecoTracksPt09HighPtTripletStep, process.hltPhase2CutsRecoTracksPt09HighPtTripletStepHp)

    process.prevalidation_associators = cms.Task(process.hltPhase2TrackingParticleRecoTrackAsssociation,
                                         process.hltPhase2VertexAssociatorByPositionAndTracks,
                                         process.hltPhase2PixelVertexAssociatorByPositionAndTracks,
                                         process.hltPhase2TrackingParticlePixelTrackAsssociation,
                                         )

    process.prevalidation_associators_pixel = cms.Task(
                                         process.hltPhase2PixelVertexAssociatorByPositionAndTracks,
                                         process.hltPhase2TrackingParticlePixelTrackAsssociation
                                         )

    process.prevalidation_initial = cms.Task(process.hltPhase2CutsRecoTracksInitialStep,process.hltPhase2CutsRecoTracksFromPVPt09InitialStepHp,process.hltPhase2SeedTracksinitialStepSeeds,
                                               process.hltPhase2CutsRecoTracksInitialStepByAlgoMask,process.hltPhase2CutsRecoTracksInitialStepByOriginalAlgo,
                                               process.hltPhase2CutsRecoTracksInitialStepHp,process.hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp,
                                               process.hltPhase2CutsRecoTracksPt09InitialStep,process.hltPhase2CutsRecoTracksFromPVInitialStepHp,
                                               process.hltPhase2CutsRecoTracksFromPVInitialStep,process.hltPhase2CutsRecoTracksFromPVPt09InitialStep,
                                               process.hltPhase2CutsRecoTracksPt09InitialStepHp,process.hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp)

    process.prevalidation_general = cms.Task(process.hltPhase2CutsRecoTracksFromPVHp,process.hltPhase2GeneralTracksFromPV,
                                    process.hltPhase2CutsRecoTracksFromPVPt09Hp,process.hltPhase2GeneralTracksFromPVPt09,
                                    process.hltPhase2CutsRecoTracksPt09Hp,process.hltPhase2CutsRecoTracksBtvLike,
                                    process.hltPhase2GeneralTracksPt09,process.hltPhase2CutsRecoTracksHp)

    process.prevalidation_vertex = cms.Task(process.hltPhase2SelectedOfflinePrimaryVertices,
                                    process.hltPhase2SelectedOfflinePrimaryVerticesWithBS,
                                    process.hltPhase2VertexAnalysisTrackingOnly)

    process.prevalidation_pixelvertex = cms.Task(
                                    process.hltPhase2SelectedPixelVertices,
                                    process.hltPhase2PixelVertexAnalysisTrackingOnly)

    process.prevalidation_v0 = cms.Task(process.hltPhase2V0Validator)

    process.prevalidation_startup = cms.Task(process.prevalidation_commons,process.prevalidation_associators,process.prevalidation_associators_pixel,process.prevalidation_pixelvertex)

    return process

def customise_validation_common(process):

    process.hltPhase2HistoProducer = cms.PSet(
    mindrj = cms.double(0.001), #cmssw_10_6
        maxdrj = cms.double(0.1), #cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9), # previous 0.05
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(30.0)
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0)
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9), # previous 0.05
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1), # logscale
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4',
            'BPix1+BPix2+BPix3+FPix1_pos',
            'BPix1+BPix2+BPix3+FPix1_neg',
            'BPix1+BPix2+FPix1_pos+FPix2_pos',
            'BPix1+BPix2+FPix1_neg+FPix2_neg',
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg',
            'BPix1+BPix2+BPix3',
            'BPix2+BPix3+BPix4',
            'BPix1+BPix3+BPix4',
            'BPix1+BPix2+BPix4',
            'BPix2+BPix3+FPix1_pos',
            'BPix2+BPix3+FPix1_neg',
            'BPix1+BPix2+FPix1_pos',
            'BPix1+BPix2+FPix1_neg',
            'BPix2+FPix1_pos+FPix2_pos',
            'BPix2+FPix1_neg+FPix2_neg',
            'BPix1+FPix1_pos+FPix2_pos',
            'BPix1+FPix1_neg+FPix2_neg',
            'FPix1_pos+FPix2_pos+FPix3_pos',
            'FPix1_neg+FPix2_neg+FPix3_neg',
            'BPix1+FPix2_pos+FPix3_pos',
            'BPix1+FPix2_neg+FPix3_neg',
            'FPix2_pos+FPix3_pos+FPix4_pos',
            'FPix2_neg+FPix3_neg+FPix4_neg',
            'FPix3_pos+FPix4_pos+FPix5_pos',
            'FPix3_neg+FPix4_neg+FPix5_neg',
            'FPix4_pos+FPix5_pos+FPix6_pos',
            'FPix4_neg+FPix5_neg+FPix6_neg',
            'FPix5_pos+FPix6_pos+FPix7_pos',
            'FPix5_neg+FPix6_neg+FPix7_neg',
            'FPix6_pos+FPix7_pos+FPix8_pos',
            'FPix6_neg+FPix7_neg+FPix8_neg',
            'BPix1+BPix2',
            'BPix1+BPix3',
            'BPix2+BPix3',
            'BPix1+FPix1_pos',
            'BPix1+FPix1_neg',
            'BPix2+FPix1_pos',
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    )

    process.hltPhase2TrackValidator = cms.EDProducer("MultiTrackValidator",
        cores = cms.InputTag("highPtJetsForTrk"),
        UseAssociators = cms.bool(False),
        associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        calculateDrSingleCollection = cms.untracked.bool(True),
        chargedOnlyTP = cms.bool(True),
        dEdx1Tag = cms.InputTag("dedxHarmonic2"),
        dEdx2Tag = cms.InputTag("dedxTruncated40"),
        dirName = cms.string('Tracking/Track/'),
        doMVAPlots = cms.untracked.bool(False),
        doPVAssociationPlots = cms.untracked.bool(True),
        doPlotsOnlyForTruePV = cms.untracked.bool(False),
        doRecoTrackPlots = cms.untracked.bool(True),
        doResolutionPlotsForLabels = cms.VInputTag(),
        doSeedPlots = cms.untracked.bool(False),
        doSimPlots = cms.untracked.bool(True),
        doSimTrackPlots = cms.untracked.bool(True),
        doSummaryPlots = cms.untracked.bool(True),
        dodEdxPlots = cms.untracked.bool(False),
        histoProducerAlgoBlock = process.hltPhase2HistoProducer,
        ignoremissingtrackcollection = cms.untracked.bool(False),
        intimeOnlyTP = cms.bool(True),
        invertRapidityCutTP = cms.bool(False), # cmssw_11_1
        label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksInitialStep",
        "hltPhase2CutsRecoTracksHighPtTripletStep","hltPhase2CutsRecoTracksInitialStepHp",
        "hltPhase2CutsRecoTracksHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo",
        "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
        "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp",
        "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp",
        "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
        "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
        "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp",
        "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
        "hltPhase2CutsRecoTracksPt09InitialStep",
        "hltPhase2CutsRecoTracksPt09HighPtTripletStep",
        "hltPhase2CutsRecoTracksPt09InitialStepHp",
        "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp"),
        label_pileupinfo = cms.InputTag("addPileupInfo"),
        label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
        label_tp_effic_refvector = cms.bool(False),
        label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
        label_tp_fake_refvector = cms.bool(False),
        label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
        label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
        label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
        label_tv = cms.InputTag("mix","MergedTrackTruth"),
        label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices"),
        lipTP = cms.double(30.0),
        maxRapidityTP = cms.double(4.5),
        minHitTP = cms.int32(0),
        minRapidityTP = cms.double(-4.5),
        mvaLabels = cms.untracked.PSet(),
        parametersDefiner = cms.string('LhcParametersDefinerForTP'),
        pdgIdTP = cms.vint32(),
        ptMaxTP = cms.double(1e+100),
        ptMinTP = cms.double(0.005),
        signalOnlyTP = cms.bool(False),
        sim = cms.VInputTag(
            cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
            cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
            cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
        ),
        simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
        simPVMaxZ = cms.untracked.double(-1),
        stableOnlyTP = cms.bool(False),
        tipTP = cms.double(60.0),
        trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
        useGsf = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
    )

    process.hltPhase2TrackValidatorPixelTrackingOnly = process.hltPhase2TrackValidator.clone(
        associators = cms.untracked.VInputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
        dirName = cms.string('Tracking/PixelTrack/'),
        label = cms.VInputTag("hltPhase2PixelTracks"),
        label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices"),
        trackCollectionForDrCalculation = cms.InputTag("hltPhase2PixelTracks"),
        vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
    )

    process.hltPhase2TrackValidatorL1 = process.hltPhase2TrackValidator.clone(
        cores = cms.InputTag("highPtJetsForTrk"),
        associators = cms.untracked.VInputTag("hltPhase2TrackingParticleL1TrackAsssociation"),
        dirName = cms.string('Tracking/Track/'),
        label = cms.VInputTag("hltPhase2L1CtfTracks"),
        label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices"),
        trackCollectionForDrCalculation = cms.InputTag("hltPhase2L1CtfTracks"),
        vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
        doSeedPlots = cms.untracked.bool(False),
        maxRapidityTP = cms.double(4.5),
        minRapidityTP = cms.double(-4.5),
        ptMinTP = cms.double(0.005),
        )

    process.hltPhase2TrackValidatorTPPtLess09Standalone = process.hltPhase2TrackValidator.clone(
        ptMaxTP = cms.double(0.9),
        ptMinTP = cms.double(0.0),
    )

    process.hltPhase2TrackValidatorFromPVStandalone = process.hltPhase2TrackValidator.clone(
        label_tp_effic = cms.InputTag("hltPhase2TrackingParticlesSignal"),
        label_tp_effic_refvector = cms.bool(True),
        label_tp_fake = cms.InputTag("hltPhase2TrackingParticlesSignal"),
        label_tp_fake_refvector = cms.bool(True),
        label = cms.VInputTag(
            "hltPhase2GeneralTracksFromPV", "hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep",
            "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp",
            "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep",
            "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp",
        ),
     )

    process.hltPhase2TrackValidatorFromPVAllTPStandalone = process.hltPhase2TrackValidator.clone(
         label = cms.VInputTag(
             "hltPhase2GeneralTracksFromPV", "hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep",
             "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp",
             "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep",
             "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp",
         ),
      )

    process.hltPhase2TrackValidatorBHadronTrackingOnly = process.hltPhase2TrackValidator.clone(
        label_tp_effic = cms.InputTag("trackingParticlesBHadron"),
        label_tp_effic_refvector = cms.bool(True)
      )

    process.hltPhase2TrackValidatorSeedingTrackingOnly = process.hltPhase2TrackValidator.clone(
        doSeedPlots = cms.untracked.bool(True),
        label = cms.VInputTag(
            "hltPhase2SeedTracksinitialStepSeeds", "hltPhase2SeedTrackshighPtTripletStepSeeds" ### v2
        ),
      )

    process.load("Validation.RecoTrack.associators_cff")# import hltTPClusterProducer,hltTrackAssociatorByHits

    process.hltMultiTrackValidation = cms.Sequence(
           process.hltTPClusterProducer
         + process.hltTrackAssociatorByHits
         + process.hltPhase2TrackValidator
     )

    process.validation_baselineTask = cms.Task(process.hltPhase2TrackValidatorPixelTrackingOnly,process.hltPhase2TrackValidator,
                                     process.hltPhase2TrackValidatorTPPtLess09Standalone,process.hltPhase2TrackValidatorFromPVStandalone,
                                     process.hltPhase2TrackValidatorFromPVAllTPStandalone)

    process.validation_baseline = cms.Sequence(process.validation_baselineTask)

    return process

def customise_dqm_common(process):

    from CommonTools.RecoAlgos.TrackWithVertexSelector_cfi import trackWithVertexSelector

    #Track Selector Vtx
    process.hltPhase2PV0p1 = trackWithVertexSelector.clone(
        numberOfValidPixelHits = cms.uint32(0),
        ptErrorCut = cms.double(9999999.0),
        etaMax = cms.double(5.0),
        etaMin = cms.double(-5.0),
        ptMax = cms.double(100000.0),
        ptMin = cms.double(0.8),
        quality = cms.string(''),
        rhoVtx = cms.double(999.0),
        src = cms.InputTag("hltPhase2GeneralTracks"),
        vertexTag = cms.InputTag("hltPhase2TrackingDQMgoodOfflinePrimaryVertices"),
        zetaVtx = cms.double(0.1)
    )

    process.hltPhase2HighPurityPV0p1 = process.hltPhase2PV0p1.clone(
        quality = cms.string('highPurity'),
    )

    #Eff monitor
    process.hltPhase2TrackMon_ckf = cms.EDProducer("TrackEfficiencyMonitor",
        AlgoName = cms.string('CKFTk'),
        FolderName = cms.string('Tracking/TrackParameters'),
        OutputFileName = cms.string('MonitorTrackEfficiency.root'),
        OutputMEsInRootFile = cms.bool(False),
        STATrackCollection = cms.InputTag("cosmicMuons"),
        TKTrackCollection = cms.InputTag("hltPhase2GeneralTracks"),
        deltaXBin = cms.int32(50),
        deltaXMax = cms.double(100),
        deltaXMin = cms.double(-100),
        deltaYBin = cms.int32(50),
        deltaYMax = cms.double(100),
        deltaYMin = cms.double(-100),
        isBFieldOff = cms.bool(False),
        muonCompatibleLayersBin = cms.int32(10),
        muonCompatibleLayersMax = cms.double(30),
        muonCompatibleLayersMin = cms.double(0),
        muonD0Bin = cms.int32(50),
        muonD0Max = cms.double(100),
        muonD0Min = cms.double(-100),
        muonEtaBin = cms.int32(50),
        muonEtaMax = cms.double(3.2),
        muonEtaMin = cms.double(-3.2),
        muonPhiBin = cms.int32(50),
        muonPhiMax = cms.double(0.0),
        muonPhiMin = cms.double(-3.2),
        muonXBin = cms.int32(50),
        muonXMax = cms.double(100),
        muonXMin = cms.double(-100),
        muonYBin = cms.int32(50),
        muonYMax = cms.double(100),
        muonYMin = cms.double(-100),
        muonZBin = cms.int32(50),
        muonZMax = cms.double(500),
        muonZMin = cms.double(-500),
        muoncoll = cms.InputTag("muons"),
        signDeltaXBin = cms.int32(50),
        signDeltaXMax = cms.double(5),
        signDeltaXMin = cms.double(-5),
        signDeltaYBin = cms.int32(50),
        signDeltaYMax = cms.double(5),
        signDeltaYMin = cms.double(-5),
        theMaxZ = cms.double(110.0),
        theRadius = cms.double(85.0),
        trackCompatibleLayersBin = cms.int32(10),
        trackCompatibleLayersMax = cms.double(30),
        trackCompatibleLayersMin = cms.double(0),
        trackD0Bin = cms.int32(50),
        trackD0Max = cms.double(100),
        trackD0Min = cms.double(-100),
        trackEfficiency = cms.bool(True),
        trackEtaBin = cms.int32(50),
        trackEtaMax = cms.double(3.2),
        trackEtaMin = cms.double(-3.2),
        trackPhiBin = cms.int32(50),
        trackPhiMax = cms.double(0.0),
        trackPhiMin = cms.double(-3.2),
        trackXBin = cms.int32(50),
        trackXMax = cms.double(100),
        trackXMin = cms.double(-100),
        trackYBin = cms.int32(50),
        trackYMax = cms.double(100),
        trackYMin = cms.double(-100),
        trackZBin = cms.int32(50),
        trackZMax = cms.double(500),
        trackZMin = cms.double(-500)
    )

    #Track monitors
    process.hltPhase2TrackSeedMonHighPtTripletStep = cms.EDProducer("TrackingMonitor",
    **dict(
        [
            ("AbsDxyBin" , cms.int32(120) ),
            ("AbsDxyMax" , cms.double(60.0) ),
            ("AbsDxyMin" , cms.double(0.0) ),
            ("AlgoName" , cms.string('highPtTripletStep') ),
            ("BSFolderName" , cms.string('Tracking/TrackParameters/BeamSpotParameters') ),
            ("BXlumiSetup" , cms.PSet(
            BXlumiBin = cms.int32(400),
            BXlumiMax = cms.double(6000),
            BXlumiMin = cms.double(2000),
            lumi = cms.InputTag("lumiProducer"),
            lumiScale = cms.double(6.37)
        ) ),
            ("Chi2Bin" , cms.int32(50) ),
            ("Chi2Max" , cms.double(199.5) ),
            ("Chi2Min" , cms.double(-0.5) ),
            ("Chi2NDFBin" , cms.int32(50) ),
            ("Chi2NDFMax" , cms.double(19.5) ),
            ("Chi2NDFMin" , cms.double(-0.5) ),
            ("Chi2ProbBin" , cms.int32(100) ),
            ("Chi2ProbMax" , cms.double(1.0) ),
            ("Chi2ProbMin" , cms.double(0.0) ),
            ("ClusterLabels" , cms.vstring(
            'Tot',
            'Strip',
            'Pix'
        ) ),
            ("DxyBin" , cms.int32(100) ),
            ("DxyErrBin" , cms.int32(200) ),
            ("DxyErrMax" , cms.double(0.1) ),
            ("DxyMax" , cms.double(0.5) ),
            ("DxyMin" , cms.double(-0.5) ),
            ("Eta2DBin" , cms.int32(26) ),
            ("EtaBin" , cms.int32(46) ),
            ("EtaMax" , cms.double(4.5) ),
            ("EtaMin" , cms.double(-4.5) ),
            ("FolderName" , cms.string('Tracking/TrackParameters/hltPhase2GeneralTracks') ),
            ("GoodPVtxBin" , cms.int32(200) ),
            ("GoodPVtxMax" , cms.double(200.0) ),
            ("GoodPVtxMin" , cms.double(0.0) ),
            ("LSBin" , cms.int32(2000) ),
            ("LSMax" , cms.double(2000.0) ),
            ("LSMin" , cms.double(0) ),
            ("LUMIBin" , cms.int32(700) ),
            ("LUMIMax" , cms.double(70000.0) ),
            ("LUMIMin" , cms.double(0.0) ),
            ("LongDCABins" , cms.int32(100) ),
            ("LongDCAMax" , cms.double(8.0) ),
            ("LongDCAMin" , cms.double(-8.0) ),
            ("MVABin" , cms.int32(100) ),
            ("MVAMax" , cms.double(1) ),
            ("MVAMin" , cms.double(-1) ),
            ("MVAProducers" , cms.vstring(
            'initialStepClassifier1',
            'initialStepClassifier2'
        ) ),
            ("MeanHitBin" , cms.int32(30) ),
            ("MeanHitMax" , cms.double(29.5) ),
            ("MeanHitMin" , cms.double(-0.5) ),
            ("MeanLayBin" , cms.int32(25) ),
            ("MeanLayMax" , cms.double(24.5) ),
            ("MeanLayMin" , cms.double(-0.5) ),
            ("MeasurementState" , cms.string('ImpactPoint') ),
            ("NClusPxBin" , cms.int32(500) ),
            ("NClusPxMax" , cms.double(150000) ),
            ("NClusPxMin" , cms.double(-0.5) ),
            ("NClusStrBin" , cms.int32(500) ),
            ("NClusStrMax" , cms.double(199999.5) ),
            ("NClusStrMin" , cms.double(-0.5) ),
            ("NTrk2DBin" , cms.int32(50) ),
            ("NTrk2DMax" , cms.double(1999.5) ),
            ("NTrk2DMin" , cms.double(-0.5) ),
            ("PVBin" , cms.int32(125) ),
            ("PVFolderName" , cms.string('Tracking/PrimaryVertices') ),
            ("PVMax" , cms.double(249.5) ),
            ("PVMin" , cms.double(-0.5) ),
            ("PXBLayBin" , cms.int32(6) ),
            ("PXBLayMax" , cms.double(5.5) ),
            ("PXBLayMin" , cms.double(-0.5) ),
            ("PXFLayBin" , cms.int32(6) ),
            ("PXFLayMax" , cms.double(5.5) ),
            ("PXFLayMin" , cms.double(-0.5) ),
            ("Phi2DBin" , cms.int32(32) ),
            ("PhiBin" , cms.int32(32) ),
            ("PhiMax" , cms.double(3.141592654) ),
            ("PhiMin" , cms.double(-3.141592654) ),
            ("Quality" , cms.string('') ),
            ("RecHitBin" , cms.int32(40) ),
            ("RecHitMax" , cms.double(39.5) ),
            ("RecHitMin" , cms.double(-0.5) ),
            ("RecLayBin" , cms.int32(25) ),
            ("RecLayMax" , cms.double(24.5) ),
            ("RecLayMin" , cms.double(-0.5) ),
            ("RecLostBin" , cms.int32(10) ),
            ("RecLostMax" , cms.double(9.5) ),
            ("RecLostMin" , cms.double(-0.5) ),
            ("RegionCandidatePtBin" , cms.int32(100) ),
            ("RegionCandidatePtMax" , cms.double(1000) ),
            ("RegionCandidatePtMin" , cms.double(0) ),
            ("RegionCandidates" , cms.InputTag("") ),
            ("RegionProducer" , cms.InputTag("") ),
            ("RegionSeedingLayersProducer" , cms.InputTag("") ),
            ("RegionSizeBin" , cms.int32(20) ),
            ("RegionSizeMax" , cms.double(19.5) ),
            ("RegionSizeMin" , cms.double(-0.5) ),
            ("SeedCandBin" , cms.int32(20) ),
            ("SeedCandMax" , cms.double(19.5) ),
            ("SeedCandMin" , cms.double(-0.5) ),
            ("SeedDxyBin" , cms.int32(100) ),
            ("SeedDxyMax" , cms.double(0.5) ),
            ("SeedDxyMin" , cms.double(-0.5) ),
            ("SeedDzBin" , cms.int32(120) ),
            ("SeedDzMax" , cms.double(30.0) ),
            ("SeedDzMin" , cms.double(-30.0) ),
            ("SeedHitBin" , cms.int32(6) ),
            ("SeedHitMax" , cms.double(5.5) ),
            ("SeedHitMin" , cms.double(-0.5) ),
            ("SeedProducer" , cms.InputTag("hltPhase2HighPtTripletStepSeeds") ),
            ("TCDxyBin" , cms.int32(100) ),
            ("TCDxyMax" , cms.double(100.0) ),
            ("TCDxyMin" , cms.double(-100.0) ),
            ("TCDzBin" , cms.int32(100) ),
            ("TCDzMax" , cms.double(400.0) ),
            ("TCDzMin" , cms.double(-400.0) ),
            ("TCHitBin" , cms.int32(40) ),
            ("TCHitMax" , cms.double(39.5) ),
            ("TCHitMin" , cms.double(-0.5) ),
            ("TCProducer" , cms.InputTag("hltPhase2HighPtTripletStepTrackCandidates") ),
            ("TCSizeBin" , cms.int32(200) ),
            ("TCSizeMax" , cms.double(999.5) ),
            ("TCSizeMin" , cms.double(-0.5) ),
            ("TECLayBin" , cms.int32(15) ),
            ("TECLayMax" , cms.double(14.5) ),
            ("TECLayMin" , cms.double(-0.5) ),
            ("TIBLayBin" , cms.int32(6) ),
            ("TIBLayMax" , cms.double(5.5) ),
            ("TIBLayMin" , cms.double(-0.5) ),
            ("TIDLayBin" , cms.int32(6) ),
            ("TIDLayMax" , cms.double(5.5) ),
            ("TIDLayMin" , cms.double(-0.5) ),
            ("TOBLayBin" , cms.int32(10) ),
            ("TOBLayMax" , cms.double(9.5) ),
            ("TOBLayMin" , cms.double(-0.5) ),
            ("TTRHBuilder" , cms.string('WithTrackAngle') ),
            ("ThetaBin" , cms.int32(32) ),
            ("ThetaMax" , cms.double(3.2) ),
            ("ThetaMin" , cms.double(0.0) ),
            ("TkSeedSizeBin" , cms.int32(100) ),
            ("TkSeedSizeMax" , cms.double(5000) ),
            ("TkSeedSizeMin" , cms.double(-0.5) ),
            ("TkSizeBin" , cms.int32(1000) ),
            ("TkSizeMax" , cms.double(999.5) ),
            ("TkSizeMin" , cms.double(-0.5) ),
            ("TrackPBin" , cms.int32(100) ),
            ("TrackPMax" , cms.double(100.0) ),
            ("TrackPMin" , cms.double(0.0) ),
            ("TrackProducer" , cms.InputTag("hltPhase2GeneralTracks") ),
            ("TrackProducerForMVA" , cms.InputTag("hltPhase2InitialStepTracks") ),
            ("TrackPt2DBin" , cms.int32(100) ),
            ("TrackPtBin" , cms.int32(100) ),
            ("TrackPtMax" , cms.double(100.0) ),
            ("TrackPtMin" , cms.double(0.1) ),
            ("TrackPxBin" , cms.int32(50) ),
            ("TrackPxMax" , cms.double(50.0) ),
            ("TrackPxMin" , cms.double(-50.0) ),
            ("TrackPyBin" , cms.int32(50) ),
            ("TrackPyMax" , cms.double(50.0) ),
            ("TrackPyMin" , cms.double(-50.0) ),
            ("TrackPzBin" , cms.int32(50) ),
            ("TrackPzMax" , cms.double(50.0) ),
            ("TrackPzMin" , cms.double(-50.0) ),
            ("TrackQBin" , cms.int32(8) ),
            ("TrackQMax" , cms.double(2.5) ),
            ("TrackQMin" , cms.double(-2.5) ),
            ("TransDCABins" , cms.int32(100) ),
            ("TransDCAMax" , cms.double(8.0) ),
            ("TransDCAMin" , cms.double(-8.0) ),
            ("VXBin" , cms.int32(100) ),
            ("VXMax" , cms.double(0.5) ),
            ("VXMin" , cms.double(-0.5) ),
            ("VYBin" , cms.int32(100) ),
            ("VYMax" , cms.double(0.5) ),
            ("VYMin" , cms.double(-0.5) ),
            ("VZBin" , cms.int32(100) ),
            ("VZBinProf" , cms.int32(100) ),
            ("VZMax" , cms.double(30.0) ),
            ("VZMaxProf" , cms.double(0.2) ),
            ("VZMin" , cms.double(-30.0) ),
            ("VZMinProf" , cms.double(-0.2) ),
            ("X0Bin" , cms.int32(100) ),
            ("X0Max" , cms.double(0.5) ),
            ("X0Min" , cms.double(-0.5) ),
            ("Y0Bin" , cms.int32(100) ),
            ("Y0Max" , cms.double(0.5) ),
            ("Y0Min" , cms.double(-0.5) ),
            ("Z0Bin" , cms.int32(120) ),
            ("Z0Max" , cms.double(60.0) ),
            ("Z0Min" , cms.double(-60.0) ),
            ("allTrackProducer" , cms.InputTag("hltPhase2GeneralTracks") ),
            ("beamSpot" , cms.InputTag("offlineBeamSpot") ),
            ("denCut" , cms.string(' pt >= 1 ') ),
            ("doAllPlots" , cms.bool(False) ),
            ("doAllTrackCandHistos" , cms.bool(False) ),
            ("doBeamSpotPlots" , cms.bool(False) ),
            ("doDCAPlots" , cms.bool(False) ),
            ("doDCAwrt000Plots" , cms.bool(False) ),
            ("doDCAwrtPVPlots" , cms.bool(False) ),
            ("doEffFromHitPatternVsBX" , cms.bool(False) ),
            ("doEffFromHitPatternVsLUMI" , cms.bool(False) ),
            ("doEffFromHitPatternVsPU" , cms.bool(False) ),
            ("doGeneralPropertiesPlots" , cms.bool(False) ),
            ("doHIPlots" , cms.bool(False) ),
            ("doHitPropertiesPlots" , cms.bool(False) ),
            ("doLayersVsPhiVsEtaPerTrack" , cms.bool(False) ),
        ] +
        [
            ("doLumiAnalysis" , cms.bool(False) ),
            ("doMVAPlots" , cms.bool(False) ),
            ("doMeasurementStatePlots" , cms.bool(False) ),
            ("doPUmonitoring" , cms.bool(False) ),
            ("doPlotsVsBX" , cms.bool(False) ),
            ("doPlotsVsBXlumi" , cms.bool(False) ),
            ("doPlotsVsGoodPVtx" , cms.bool(True) ),
            ("doPlotsVsLUMI" , cms.bool(False) ),
            ("doPrimaryVertexPlots" , cms.bool(False) ),
            ("doProfilesVsLS" , cms.bool(False) ),
            ("doRecHitVsPhiVsEtaPerTrack" , cms.bool(False) ),
            ("doRecHitVsPtVsEtaPerTrack" , cms.bool(False) ),
            ("doRecHitsPerTrackProfile" , cms.bool(False) ),
            ("doRegionCandidatePlots" , cms.bool(False) ),
            ("doRegionPlots" , cms.bool(False) ),
            ("doSIPPlots" , cms.bool(False) ),
            ("doSeedDxyHisto" , cms.bool(False) ),
            ("doSeedDzHisto" , cms.bool(False) ),
            ("doSeedETAHisto" , cms.bool(True) ),
            ("doSeedLumiAnalysis" , cms.bool(True) ),
            ("doSeedNRecHitsHisto" , cms.bool(False) ),
            ("doSeedNVsEtaProf" , cms.bool(False) ),
            ("doSeedNVsPhiProf" , cms.bool(False) ),
            ("doSeedNumberHisto" , cms.bool(True) ),
            ("doSeedPHIHisto" , cms.bool(True) ),
            ("doSeedPHIVsETAHisto" , cms.bool(True) ),
            ("doSeedPTHisto" , cms.bool(True) ),
            ("doSeedParameterHistos" , cms.bool(False) ),
            ("doSeedQHisto" , cms.bool(False) ),
            ("doSeedThetaHisto" , cms.bool(False) ),
            ("doSeedVsClusterHisto" , cms.bool(True) ),
            ("doStopSource" , cms.bool(True) ),
            ("doTestPlots" , cms.bool(False) ),
            ("doThetaPlots" , cms.bool(False) ),
            ("doTrackCandHistos" , cms.bool(True) ),
            ("doTrackPxPyPlots" , cms.bool(False) ),
            ("doTrackerSpecific" , cms.bool(False) ),
            ("etaErrBin" , cms.int32(50) ),
            ("etaErrMax" , cms.double(0.1) ),
            ("etaErrMin" , cms.double(0.0) ),
            ("genericTriggerEventPSet" , cms.PSet(

        ) ),
            ("minNumberOfPixelsPerCluster" , cms.int32(2) ),
            ("minPixelClusterCharge" , cms.double(15000.0) ),
            ("numCut" , cms.string(" pt >= 1 & quality(\'highPurity\') ") ),
            ("pErrBin" , cms.int32(50) ),
            ("pErrMax" , cms.double(1.0) ),
            ("pErrMin" , cms.double(0.0) ),
            ("phiErrBin" , cms.int32(50) ),
            ("phiErrMax" , cms.double(0.1) ),
            ("phiErrMin" , cms.double(0.0) ),
            ("pixelCluster" , cms.InputTag("siPixelClusters") ),
            ("pixelCluster4lumi" , cms.InputTag("siPixelClustersPreSplitting") ),
            ("primaryVertex" , cms.InputTag("hltPhase2OfflinePrimaryVertices") ),
            ("primaryVertexInputTags" , cms.VInputTag() ),
            ("ptErrBin" , cms.int32(50) ),
            ("ptErrMax" , cms.double(1.0) ),
            ("ptErrMin" , cms.double(0.0) ),
            ("pvLabels" , cms.vstring() ),
            ("pvNDOF" , cms.int32(4) ),
            ("pxErrBin" , cms.int32(50) ),
            ("pxErrMax" , cms.double(1.0) ),
            ("pxErrMin" , cms.double(0.0) ),
            ("pyErrBin" , cms.int32(50) ),
            ("pyErrMax" , cms.double(1.0) ),
            ("pyErrMin" , cms.double(0.0) ),
            ("pzErrBin" , cms.int32(50) ),
            ("pzErrMax" , cms.double(1.0) ),
            ("pzErrMin" , cms.double(0.0) ),
            ("qualityString" , cms.string('highPurity') ),
            ("scal" , cms.InputTag("scalersRawToDigi") ),
            ("selPrimaryVertexInputTags" , cms.VInputTag() ),
            ("stripCluster" , cms.InputTag("siStripClusters") ),
            ("subdetectorBin" , cms.int32(25) ),
            ("subdetectors" , cms.vstring(
            'TIB',
            'TOB',
            'TID',
            'TEC',
            'PixBarrel',
            'PixEndcap',
            'Pixel',
            'Strip'
        ) ),
            ("useBPixLayer1" , cms.bool(False) ),
            ]
        )
    )

    process.hltPhase2TrackSeedMonInitialStep = process.hltPhase2TrackSeedMonHighPtTripletStep.clone(
            AlgoName = cms.string('initialStep'),
            BSFolderName = cms.string('Tracking/TrackParameters/BeamSpotParameters'),
            MVAProducers=cms.vstring('hltPhase2InitialStepTrackCutClassifier'),
            FolderName = cms.string('Tracking/TrackParameters/hltPhase2GeneralTracks'),
            PVFolderName = cms.string('Tracking/PrimaryVertices'),
            SeedProducer = cms.InputTag("hltPhase2InitialStepSeeds"),
            TCProducer = cms.InputTag("hltPhase2InitialStepTrackCandidates"),
            TrackProducer = cms.InputTag("hltPhase2GeneralTracks"),
            TrackProducerForMVA = cms.InputTag("hltPhase2InitialStepTracks"),
            denCut = cms.string(' pt >= 1 '),
            genericTriggerEventPSet = cms.PSet(),
            numCut = cms.string(" pt >= 1 & quality(\'highPurity\') "),
            primaryVertexInputTags = cms.VInputTag(),
            selPrimaryVertexInputTags = cms.VInputTag()
            )


    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks = process.hltPhase2TrackSeedMonHighPtTripletStep.clone(
           AlgoName=cms.string('GenTk'),
           BSFolderName=cms.string('Tracking/ParametersVsBeamSpot'),
           FolderName=cms.string('Tracking/TrackParameters/hltPhase2GeneralTracks'),
           MVAProducers=cms.vstring('hltPhase2InitialStepTrackCutClassifier'),
           MeasurementState=cms.string('ImpactPoint'),
           PVFolderName=cms.string('Tracking/PrimaryVertices/hltPhase2GeneralTracks'),
           RegionCandidates=cms.InputTag(""),
           RegionProducer=cms.InputTag(""),
           RegionSeedingLayersProducer=cms.InputTag(""),
           SeedProducer=cms.InputTag("hltPhase2InitialStepSeeds"),
           TCProducer=cms.InputTag("hltPhase2InitialStepTrackCandidates"),
           TTRHBuilder=cms.string('WithTrackAngle'),
           TrackProducer=cms.InputTag("hltPhase2GeneralTracks"),
           TrackProducerForMVA=cms.InputTag("hltPhase2InitialStepTracks"),
           allTrackProducer=cms.InputTag("hltPhase2GeneralTracks"),
           beamSpot=cms.InputTag("offlineBeamSpot"),
           denCut=cms.string(''),
           genericTriggerEventPSet=cms.PSet(
            andOr = cms.bool(False),
            andOrDcs = cms.bool(False),
            dcsInputTag = cms.InputTag("scalersRawToDigi"),
            dcsPartitions = cms.vint32(
                24, 25, 26, 27, 28,
                29
            ),
            errorReplyDcs = cms.bool(True)),
           numCut=cms.string("quality(\'highPurity\')"),
           pixelCluster=cms.InputTag("siPixelClusters"),
           pixelCluster4lumi=cms.InputTag("siPixelClustersPreSplitting"),
           primaryVertex=cms.InputTag("hltPhase2OfflinePrimaryVertices"),
           primaryVertexInputTags=cms.VInputTag(cms.InputTag("hltPhase2OfflinePrimaryVertices")),
           qualityString=cms.string('highPurity'),
           scal=cms.InputTag("scalersRawToDigi"),
           selPrimaryVertexInputTags=cms.VInputTag(cms.InputTag("goodOfflinePrimaryVertices")),
           stripCluster=cms.InputTag("siStripClusters")
    )

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1 = process.hltPhase2TrackSeedMonHighPtTripletStep.clone(

           AlgoName=cms.string('GenTk'),
           BSFolderName=cms.string('Tracking/ParametersVsBeamSpot'),
           FolderName=cms.string('Tracking/TrackParameters/HighPurityTracks/dzPV0p1'),
           MVAProducers=cms.vstring('hltPhase2InitialStepTrackCutClassifier'),
           MeasurementState=cms.string('ImpactPoint'),
           PVFolderName=cms.string('Tracking/PrimaryVertices/HighPurityTracks/dzPV0p1'),
           RegionCandidates=cms.InputTag(""),
           RegionProducer=cms.InputTag(""),
           RegionSeedingLayersProducer=cms.InputTag(""),
           SeedProducer=cms.InputTag("hltPhase2InitialStepSeeds"),
           TCProducer=cms.InputTag("hltPhase2InitialStepTrackCandidates"),
           TTRHBuilder=cms.string('WithTrackAngle'),
           TrackProducer=cms.InputTag("hltPhase2HighPurityPV0p1"),
           TrackProducerForMVA=cms.InputTag("hltPhase2InitialStepTracks"),
           allTrackProducer=cms.InputTag("hltPhase2PV0p1"),
           beamSpot=cms.InputTag("offlineBeamSpot"),
           denCut=cms.string(''),
           genericTriggerEventPSet=cms.PSet(
            andOr = cms.bool(False),
            andOrDcs = cms.bool(False),
            dcsInputTag = cms.InputTag("scalersRawToDigi"),
            dcsPartitions = cms.vint32(
                24, 25, 26, 27, 28,
                29),
            errorReplyDcs = cms.bool(True)),
           numCut=cms.string("quality(\'highPurity\')"),
           pixelCluster=cms.InputTag("siPixelClusters"),
           pixelCluster4lumi=cms.InputTag("siPixelClustersPreSplitting"),
           primaryVertex=cms.InputTag("hltPhase2OfflinePrimaryVertices"),
           primaryVertexInputTags=cms.VInputTag(cms.InputTag("hltPhase2OfflinePrimaryVertices")),
           qualityString=cms.string('highPurity'),
           scal=cms.InputTag("scalersRawToDigi"),
           selPrimaryVertexInputTags=cms.VInputTag(cms.InputTag("goodOfflinePrimaryVertices")),
           stripCluster=cms.InputTag("siStripClusters"),

        )

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity = process.hltPhase2TrackSeedMonHighPtTripletStep.clone(
           AlgoName=cms.string('GenTk'),
           BSFolderName=cms.string('Tracking/ParametersVsBeamSpot'),
           FolderName=cms.string('Tracking/TrackParameters/HighPurityTracks/pt_1'),
           MVAProducers=cms.vstring('hltPhase2InitialStepTrackCutClassifier'),
           MeasurementState=cms.string('ImpactPoint'),
           PVFolderName=cms.string('Tracking/PrimaryVertices/HighPurityTracks/pt_1'),
           RegionSeedingLayersProducer=cms.InputTag(""),
           SeedProducer=cms.InputTag("hltPhase2InitialStepSeeds"),
           TCProducer=cms.InputTag("hltPhase2InitialStepTrackCandidates"),
           TTRHBuilder=cms.string('WithTrackAngle'),
           TrackProducer=cms.InputTag("hltPhase2HighPurity"),
           TrackProducerForMVA=cms.InputTag("hltPhase2InitialStepTracks"),
           allTrackProducer=cms.InputTag("hltPhase2GeneralTracks"),
           beamSpot=cms.InputTag("offlineBeamSpot"),
           denCut=cms.string(' pt >= 1 '),
           genericTriggerEventPSet=cms.PSet(
            andOr = cms.bool(False),
            andOrDcs = cms.bool(False),
            dcsInputTag = cms.InputTag("scalersRawToDigi"),
            dcsPartitions = cms.vint32(
                24, 25, 26, 27, 28,
                29
            ),
            errorReplyDcs = cms.bool(True)
        ),
           numCut=cms.string(" pt >= 1 & quality(\'highPurity\')"),
           pixelCluster=cms.InputTag("siPixelClusters"),
           pixelCluster4lumi=cms.InputTag("siPixelClustersPreSplitting"),
           primaryVertex=cms.InputTag("hltPhase2OfflinePrimaryVertices"),
           primaryVertexInputTags=cms.VInputTag(cms.InputTag("hltPhase2OfflinePrimaryVertices")),
           qualityString=cms.string('highPurity'),
           scal=cms.InputTag("scalersRawToDigi"),
           selPrimaryVertexInputTags=cms.VInputTag(cms.InputTag("goodOfflinePrimaryVertices")),
           stripCluster=cms.InputTag("siStripClusters"),

        )


    #Track selector
    process.hltPhase2HighPurity = cms.EDFilter("TrackSelector",
        cut = cms.string("quality(\'highPurity\')"),
        src = cms.InputTag("hltPhase2GeneralTracks")
    )

    #PV resol
    process.hltPhase2PrimaryVertexResolution = cms.EDProducer("PrimaryVertexResolution",
        beamspotSrc = cms.untracked.InputTag("offlineBeamSpot"),
        binsNtracks = cms.untracked.int32(60),
        binsNvertices = cms.untracked.int32(100),
        binsPull = cms.untracked.int32(100),
        binsResol = cms.untracked.int32(100),
        lumiScalersSrc = cms.untracked.InputTag("scalersRawToDigi"),
        maxLumi = cms.untracked.double(20000),
        maxNtracks = cms.untracked.double(119.5),
        maxNvertices = cms.untracked.double(199.5),
        maxPt = cms.untracked.double(1000),
        maxPull = cms.untracked.double(5),
        maxResol = cms.untracked.double(0.02),
        minLumi = cms.untracked.double(200),
        minNtracks = cms.untracked.double(-0.5),
        minNvertices = cms.untracked.double(-0.5),
        minPt = cms.untracked.double(1),
        rootFolder = cms.untracked.string('OfflinePV/Resolution'),
        transientTrackBuilder = cms.untracked.string('TransientTrackBuilder'),
        vertexSrc = cms.untracked.InputTag("hltPhase2TrackingDQMgoodOfflinePrimaryVertices")
    )

    process.hltPhase2PvMonitor = cms.EDProducer("PrimaryVertexMonitor",
        AlignmentLabel = cms.string('Alignment'),
        DxyBin = cms.int32(100),
        DxyMax = cms.double(5000.0),
        DxyMin = cms.double(-5000.0),
        DzBin = cms.int32(100),
        DzMax = cms.double(2000.0),
        DzMin = cms.double(-2000.0),
        EtaBin = cms.int32(41),
        EtaMax = cms.double(4.0),
        EtaMin = cms.double(-4.0),
        PhiBin = cms.int32(32),
        PhiMax = cms.double(3.141592654),
        PhiMin = cms.double(-3.141592654),
        TkSizeBin = cms.int32(100),
        TkSizeMax = cms.double(499.5),
        TkSizeMin = cms.double(-0.5),
        TopFolderName = cms.string('OfflinePV'),
        Xpos = cms.double(0.1),
        Ypos = cms.double(0.0),
        beamSpotLabel = cms.InputTag("offlineBeamSpot"),
        ndof = cms.int32(4),
        vertexLabel = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
    )

    #Vertex Selector
    process.hltPhase2TrackingDQMgoodPixelVertices = cms.EDFilter("VertexSelector",
        cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")
    )

    process.hltPhase2TrackingDQMgoodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
        cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2OfflinePrimaryVertices") #("hltPhase2OfflinePrimaryVertices")
    )

    process.hltPhase2TrackingDQMgoodTrimmedPixelVertices = cms.EDFilter("VertexSelector",
        cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
        filter = cms.bool(False),
        src = cms.InputTag("hltPhase2TrimmedPixelVertices") #("hltPhase2OfflinePrimaryVertices")
    )

    #############################################
    ##### Release updates from 11_1_0_pre6

    ##11_1_0_pre7

    gooppvtx_60 = cms.PSet(GoodPVtxBin = cms.int32(60),GoodPVtxMax = cms.double(60.0),GoodPVtxMin = cms.double(0.0))
    gooppvtx_200 = cms.PSet(GoodPVtxBin = cms.int32(200),GoodPVtxMax = cms.double(200.0),GoodPVtxMin = cms.double(0.0))
    npvtx = cms.PSet(NTrkPVtxBin = cms.int32(200), NTrkPVtxMin = cms.double( 0.), NTrkPVtxMax = cms.double(200.))
    sumptvtx = cms.PSet(SumPtPVtxBin = cms.int32(200), SumPtPVtxMin = cms.double( 0.), SumPtPVtxMax = cms.double(1000.))

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackSeedMonHighPtTripletStep.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackSeedMonInitialStep.GoodPVtx = gooppvtx_200
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.GoodPVtx = gooppvtx_60
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.GoodPVtx = gooppvtx_60

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.SumPtPVtx = sumptvtx
    process.hltPhase2TrackSeedMonHighPtTripletStep.SumPtPVtx = sumptvtx
    process.hltPhase2TrackSeedMonInitialStep.SumPtPVtx = sumptvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.SumPtPVtx = sumptvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.SumPtPVtx = sumptvtx

    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.NTrkPVtx = npvtx
    process.hltPhase2TrackSeedMonHighPtTripletStep.NTrkPVtx = npvtx
    process.hltPhase2TrackSeedMonInitialStep.NTrkPVtx = npvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.NTrkPVtx = npvtx
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.NTrkPVtx = npvtx


    ##11_1_0

    ntrk2d = cms.PSet(NTrk2DBin = cms.int32(50), NTrk2DMax = cms.double(1999.5), NTrk2DMin = cms.double(-0.5))

    process.hltPhase2TrackSeedMonHighPtTripletStep.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.NTrk2D = ntrk2d
    process.hltPhase2TrackSeedMonInitialStep.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.NTrk2D = ntrk2d
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.NTrk2D = ntrk2d

    process.hltPhase2TrackSeedMonHighPtTripletStep.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.forceSCAL = cms.bool(True)
    process.hltPhase2TrackSeedMonInitialStep.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.forceSCAL = cms.bool(True)
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.forceSCAL = cms.bool(True)

    process.hltPhase2TrackSeedMonHighPtTripletStep.metadata = cms.InputTag('onlineMetaDataDigis')
    process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks.metadata = cms.InputTag('onlineMetaDataDigis')
    process.hltPhase2TrackSeedMonInitialStep.metadata = cms.InputTag('onlineMetaDataDigis')
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1.metadata = cms.InputTag('onlineMetaDataDigis')
    process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity.metadata = cms.InputTag('onlineMetaDataDigis')

    process.load("DQM.TrackingMonitor.TrackSplittingMonitor_cfi")# import TrackSplitMonitor
    process.load("DQM.TrackingMonitorSource.TrackingSourceConfig_Tier0_cff")# import dqmInfoTracking

    process.dqm_commons = cms.Task(process.TrackSplitMonitor,process.dqmInfoTracking)

    process.dqm_initial = cms.Task(process.hltPhase2TrackSeedMonInitialStep)

    process.dqm_highpt = cms.Task(process.hltPhase2TrackSeedMonHighPtTripletStep)

    process.dqm_vertex = cms.Task(process.hltPhase2PvMonitor,process.hltPhase2PrimaryVertexResolution,process.hltPhase2TrackingDQMgoodOfflinePrimaryVertices)

    process.dqm_pixelvertex = cms.Task(process.hltPhase2TrackingDQMgoodPixelVertices,process.hltPhase2TrackingDQMgoodPixelVertices)

    process.dqm_general = cms.Task(process.hltPhase2TrackerCollisionSelectedTrackMonCommongeneralTracks,
                           ##High Purity & Selectors
                           process.hltPhase2PV0p1, process.hltPhase2HighPurityPV0p1, #PV
                           process.hltPhase2HighPurity, #HP
                           #Monitors
                           process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurityPV0p1,
                           process.hltPhase2TrackerCollisionSelectedTrackMonCommonHighPurity,
                           #Eff Mon
                           process.hltPhase2TrackMon_ckf)
    process.dqm_original = cms.EndPath(process.dqm_commons,process.dqm_vertex,process.dqm_pixelvertex,process.dqm_initial,process.dqm_highpt,process.dqm_general)

    return process

def deletions(process):

    if 'trackingDQMgoodOfflinePrimaryVertices' in process.__dict__:
        del process.trackingDQMgoodOfflinePrimaryVertices
    if 'dedxDQMHarm2SP' in process.__dict__:
        del process.dedxDQMHarm2SP
    if 'dedxDQMHarm2SO' in process.__dict__:
        del process.dedxDQMHarm2SO
    if 'dedxDQMHarm2PO' in process.__dict__:
        del process.dedxDQMHarm2PO

    return process

def customise_hltPhase2_TRKv06_1_val(process):

    process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterChargeCut_cfi")
    process.load("RecoPixelVertexing.PixelLowPtUtilities.ClusterShapeTrajectoryFilter_cfi")
    process.load('RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi')
    process.load('Geometry.CaloEventSetup.CaloTowerConstituents_cfi')

    process = customise_hltPhase2_TRKv06_1(process)
    process = customise_prevalidation_common(process)
    process = customise_validation_common(process)
    process = customise_dqm_common(process)

    del process.schedule[:]

    process.reconstruction_step = cms.Path(process.reconstruction)
    process.prevalidation_step= cms.Path(process.prevalidation_startup,process.prevalidation_v0,process.prevalidation_initial,process.prevalidation_highpt,process.prevalidation_general)
    process.validation_step = cms.EndPath(process.validation_baseline)
    process.mydqm = cms.Sequence(process.dqm_commons,process.dqm_vertex,process.dqm_pixelvertex,process.dqm_initial,process.dqm_highpt,process.dqm_general)
    process.dqm_step = cms.EndPath(process.mydqm)
    process.dqmoffline_step = cms.EndPath()
    process = deletions(process)

    process.schedule = cms.Schedule(process.raw2digi_step, process.reconstruction_step, process.prevalidation_step, process.validation_step, process.dqm_step, process.endjob_step, process.DQMoutput_step)

    return process

def customise_hltPhase2_TRKv07_withvalidation(process):

    process = customise_hltPhase2_TRKv07(process)
    process = customise_prevalidation_common(process)
    process = customise_validation_common(process)

    process.reconstruction_step = cms.Path(process.reconstruction)
    process.prevalidation_step= cms.Path(process.prevalidation_startup,process.prevalidation_v0,process.prevalidation_initial,process.prevalidation_highpt,process.prevalidation_general)
    process.validation_step = cms.EndPath(process.validation_baseline)

    process.DQMOfflineTracking = cms.Sequence(process.dqm_commons,process.dqm_vertex,process.dqm_pixelvertex,process.dqm_initial,process.dqm_highpt,process.dqm_general)
    process.dqm_step = cms.EndPath(process.DQMOfflineTracking)
    process.schedule = cms.Schedule(*[ process.raw2digi_step, process.reconstruction_step, process.prevalidation_step, process.validation_step, process.dqm_step, process.endjob_step, process.DQMoutput_step])

    return process
