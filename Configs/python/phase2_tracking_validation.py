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

    process.highPtTripletStepTracksSelectionHighPurity = cms.EDProducer('TrackCollectionFilterCloner',
        copyExtras = cms.untracked.bool(True),
        copyTrajectories = cms.untracked.bool(False),
        minQuality = cms.string('highPurity'),
        originalMVAVals = cms.InputTag('highPtTripletStepTrackCutClassifier','MVAValues'),
        originalQualVals = cms.InputTag('highPtTripletStepTrackCutClassifier','QualityMasks'),
        originalSource = cms.InputTag('highPtTripletStepTracks')
    )

    process.trackAlgoPriorityOrder = cms.ESProducer('TrackAlgoPriorityOrderESProducer',
        ComponentName = cms.string('trackAlgoPriorityOrder'),
        algoOrder = cms.vstring(
            'initialStep',
            'highPtTripletStep'
        ),
        appendToDataLabel = cms.string('')
    )

    process.generalTracks = cms.EDProducer('TrackListMerger',
        Epsilon = cms.double(-0.001),
        FoundHitBonus = cms.double(5.0),
        LostHitPenalty = cms.double(5.0),
        MaxNormalizedChisq = cms.double(1000.0),
        MinFound = cms.int32(3),
        MinPT = cms.double(0.9),
        ShareFrac = cms.double(0.19),
        TrackProducers = cms.VInputTag('initialStepTracksSelectionHighPurity', 'highPtTripletStepTracksSelectionHighPurity'),
        allowFirstHitShare = cms.bool(True),
        copyExtras = cms.untracked.bool(True),
        copyMVA = cms.bool(False),
        hasSelector = cms.vint32(0, 0),
        indivShareFrac = cms.vdouble(1.0, 1.0),
        makeReKeyedSeeds = cms.untracked.bool(False),
        newQuality = cms.string('confirmed'),
        selectedTrackQuals = cms.VInputTag(cms.InputTag('initialStepTrackSelectionHightPurity'), cms.InputTag('highPtTripletStepTracksSelectionHighPurity')),
        setsToMerge = cms.VPSet(cms.PSet(
            pQual = cms.bool(True),
            tLists = cms.vint32(0, 1)
        )),
        trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
        writeOnlyTrkQuals = cms.bool(False)
    )

    process.unsortedOfflinePrimaryVertices = cms.EDProducer('PrimaryVertexProducer',
        TkClusParameters = cms.PSet(
            TkDAClusParameters = cms.PSet(
                Tmin = cms.double(2.0),
                Tpurge = cms.double(2.0),
                Tstop = cms.double(0.5),
                coolingFactor = cms.double(0.6),
                d0CutOff = cms.double(3.0),
                dzCutOff = cms.double(3.0),
                uniquetrkweight = cms.double(0.8),
                vertexSize = cms.double(0.006),
                zmerge = cms.double(0.01)
            ),
            algorithm = cms.string('DA_vect')
        ),
        TkFilterParameters = cms.PSet(
            algorithm = cms.string('filter'),
            maxD0Significance = cms.double(4.0),
            maxEta = cms.double(4.0),
            maxNormalizedChi2 = cms.double(10.0),
            minPixelLayersWithHits = cms.int32(2),
            minPt = cms.double(0.9),
            minSiliconLayersWithHits = cms.int32(5),
            trackQuality = cms.string('any')
        ),
        TrackLabel = cms.InputTag('generalTracks'),
        beamSpotLabel = cms.InputTag('offlineBeamSpot'),
        verbose = cms.untracked.bool(False),
        vertexCollections = cms.VPSet(
            cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string(''),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(0.0),
                useBeamConstraint = cms.bool(False)
            ),
            cms.PSet(
                algorithm = cms.string('AdaptiveVertexFitter'),
                chi2cutoff = cms.double(2.5),
                label = cms.string('WithBS'),
                maxDistanceToBeam = cms.double(1.0),
                minNdof = cms.double(2.0),
                useBeamConstraint = cms.bool(True)
            )
        )
    )

    process.trackWithVertexRefSelectorBeforeSorting = cms.EDProducer('TrackWithVertexRefSelector',
        copyExtras = cms.untracked.bool(False),
        copyTrajectories = cms.untracked.bool(False),
        d0Max = cms.double(999.0),
        dzMax = cms.double(999.0),
        etaMax = cms.double(5.0),
        etaMin = cms.double(0.0),
        nSigmaDtVertex = cms.double(0),
        nVertices = cms.uint32(0),
        normalizedChi2 = cms.double(999999.0),
        numberOfLostHits = cms.uint32(999),
        numberOfValidHits = cms.uint32(0),
        numberOfValidPixelHits = cms.uint32(0),
        ptErrorCut = cms.double(9e+99),
        ptMax = cms.double(9e+99),
        ptMin = cms.double(0.9),
        quality = cms.string('highPurity'),
        rhoVtx = cms.double(0.2),
        src = cms.InputTag('generalTracks'),
        timeResosTag = cms.InputTag(''),
        timesTag = cms.InputTag(''),
        useVtx = cms.bool(True),
        vertexTag = cms.InputTag('unsortedOfflinePrimaryVertices'),
        vtxFallback = cms.bool(True),
        zetaVtx = cms.double(1.0)
    )
>>>>>>> 69080ebc9cf4715778881890cbd1e30586e69162

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
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticleL1TrackAsssociationf"),
        vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks"),
        vertexRecoCollections = cms.VInputTag("hltPhase2L1PrimaryVertex")#
    )

    process.hltPhase2PixelVertexAnalysisTrackingOnly = vertexAnalysis.clone(
        trackAssociatorMap = cms.untracked.InputTag("hltPhase2TrackingParticlePixelTrackAsssociation"),
        do_generic_sim_plots = cms.untracked.bool(False),
        vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks"),
        vertexRecoCollections = cms.VInputTag("hltPhase2PixelVertices", "hltPhase2SelectedPixelVertices")#,"hltPhase2TrimmedPixelVertices")#,"offlinePrimaryVertices")
    )

    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
    process.load("Validation.RecoTrack.TrackValidation_cff")
    process.load("SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi")

    process.prevalidation_commons =  cms.Task(
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

    process.vertexReco = cms.Sequence(
            process.ak4CaloJetsForTrk
          + process.unsortedOfflinePrimaryVertices
          + process.trackWithVertexRefSelectorBeforeSorting
          + process.trackRefsForJetsBeforeSorting
          + process.offlinePrimaryVertices
          + process.offlinePrimaryVerticesWithBS
#          + process.inclusiveVertexFinder
#          + process.vertexMerger
#          + process.trackVertexArbitrator
#          + process.inclusiveSecondaryVertices
        )
>>>>>>> 69080ebc9cf4715778881890cbd1e30586e69162

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
        trackCollectionForDrCalculation = cms.InputTag(""),
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

    process.load("Validation.RecoTrack.associators_cff")

    process.hltMultiTrackValidation = cms.Sequence(
           process.hltTPClusterProducer
         + process.hltTrackAssociatorByHits
         + process.hltPhase2TrackValidator
     )

    process.validation_baseline= cms.Task(process.hltPhase2TrackValidatorPixelTrackingOnly,process.hltPhase2TrackValidator,
                                     process.hltPhase2TrackValidatorTPPtLess09Standalone,process.hltPhase2TrackValidatorFromPVStandalone,
                                     process.hltPhase2TrackValidatorFromPVAllTPStandalone)
    return process
     # process.validation_original = cms.Path( )
     #                               #+hltPhase2TrackValidatorAllTPEfficStandalone)
     #                              # +hltPhase2TrackValidatorBHadronTrackingOnly
     #                              # +hltPhase2TrackValidatorSeedingTrackingOnly)
     #
     # process.validation_purel1 = cms.Path(process.hltPhase2TrackValidatorL1)
     #
     # process.validation_l1initial = cms.Path(process.hltPhase2TrackValidatorPixelTrackingOnly + process.hltPhase2TrackValidatorTrackingOnly + process.hltPhase2TrackValidatorL1)
     #
     # process.validation_l1trip = cms.Path(process.hltPhase2TrackValidatorPixelTrackingOnly + process.hltPhase2TrackValidatorTrackingOnly + process.hltPhase2TrackValidatorL1)
     #
     # process.validation_base = cms.EndPath(process.hltMultiTrackValidation + process.hltTrackAssociatorByHits)
     #
     # process.validation_pixel = cms.Path(process.hltPhase2TrackValidatorPixelTrackingOnly)
     #
     # process.validation_all = cms.Path(process.hltPhase2TrackValidatorPixelTrackingOnly + process.hltPhase2TrackValidatorTrackingOnly + process.hltPhase2TrackValidatorL1)
