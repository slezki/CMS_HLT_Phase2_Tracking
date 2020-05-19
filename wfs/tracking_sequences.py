import FWCore.ParameterSet.Config as cms
from tracking_modules import *
from generic_modules import *

####################################################
########################## Basic V/ setup
#############

hltPhase2PixelTracksSequence = cms.Sequence(
    hltPhase2PixelTrackFilterByKinematics +
    hltPhase2PixelFitterByHelixProjections +
    hltPhase2PixelTracksTrackingRegions +  # = hlt
    hltPhase2PixelTracksSeedLayers +
    hltPhase2PixelTracksHitDoublets +
    hltPhase2PixelTracksHitQuadruplets +
    hltPhase2PixelTracks
)

hltPhase2PixelVerticesSequence = cms.Sequence( # pixelVertices
    hltPhase2PixelVertices +
    hltPhase2TrimmedPixelVertices
)


hltPhase2InitialStepPVSequence = cms.Sequence(
    hltPhase2FirstStepPrimaryVerticesUnsorted +
    hltPhase2InitialStepTrackRefsForJets +
    caloTowerForTrk + # uses hbhereco, hfreco, horeco, ecalRecHit
    hltPhase2Ak4CaloJetsForTrk +  # uses caloTowerForTrk
    hltPhase2FirstStepPrimaryVertices
)



hltPhase2InitialStepSequence = cms.Sequence(
    #hltPhase2InitialStepSeedLayers +
    #hltPhase2InitialStepTrackingRegions +
    #hltPhase2InitialStepHitDoublets +
    #hltPhase2InitialStepHitQuadruplets +
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    #hltPhase2InitialStepPVSequence + # use pixelVertices
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTrackSelectionHighPurity
)

hltPhase2InitialStepSequenceL1 = cms.Sequence(
    #hltPhase2InitialStepSeedLayers +
    #hltPhase2InitialStepTrackingRegions +
    #hltPhase2InitialStepHitDoublets +
    #hltPhase2InitialStepHitQuadruplets +
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    #hltPhase2InitialStepPVSequence + # use pixelVertices
    hltPhase2InitialStepSelector
    #hltPhase2InitialStepTrackCutClassifier +
    #hltPhase2InitialStepTrackSelectionHighPurity
)

hltPhase2HighPtTripletStepSequence = cms.Sequence(
    hltPhase2HighPtTripletStepClusters +
    hltPhase2HighPtTripletStepSeedLayers +
    hltPhase2HighPtTripletStepTrackingRegions +
    hltPhase2HighPtTripletStepHitDoublets +
    hltPhase2HighPtTripletStepHitTriplets +
    hltPhase2HighPtTripletStepSeeds +
    hltPhase2HighPtTripletStepTrackCandidates +
    hltPhase2HighPtTripletStepTracks +
    hltPhase2HighPtTripletStepTrackCutClassifier +
    hltPhase2HighPtTripletStepTrackSelectionHighPurity
)

vertexReco = cms.Sequence(
    hltPhase2InitialStepPVSequence + # pixelVertices moved to here, for now still keeping it
    hltPhase2Ak4CaloJetsForTrk + # uses caloTowerForTrk
    hltPhase2UnsortedOfflinePrimaryVertices +
    hltPhase2TrackWithVertexRefSelectorBeforeSorting +
    hltPhase2TrackRefsForJetsBeforeSorting +
    hltPhase2OfflinePrimaryVertices +
    hltPhase2OfflinePrimaryVerticesWithBS +
    hltPhase2InclusiveVertexFinder +
    hltPhase2VertexMerger +
    hltPhase2TrackVertexArbitrator +
    hltPhase2InclusiveSecondaryVertices
)

hltPhase2L1TracksSequence = cms.Sequence(
    hltPhase2L1TrackStepClusters +
    hltPhase2L1TrackSeedsFromL1Tracks +
    #L1TrackCandidates +
    hltPhase2L1TrackCandidates +
    hltPhase2L1CtfTracks +
    #L1StepPVSequence +
    hltPhase2L1StepSelector# +
    #hltPhase2L1TrackCutClassifier #+
    #L1TrackSelectionHighPurity
)

original_v7 = cms.Path(
    itLocalReco +
    offlineBeamSpot + #cmssw_10_6
    otLocalReco +
    #caloLocalReco +
    trackerClusterCheck +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2HighPtTripletStepSequence +
##############################################
    hltPhase2GeneralTracks
)


MC_Tracking_v7_L1_v1 = cms.Path(
    itLocalReco +
    offlineBeamSpot + #cmssw_10_6
    hltPhase2TTTracksFromTracklet +
    otLocalReco +
    #caloLocalReco +
    trackerClusterCheck +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequenceL1 +
    hltPhase2L1TracksSequence +
    #hltPhase2HighPtTripletStepSequence +
##############################################
    hltPhase2GeneralTracks
)


MC_Vertexing = cms.Path(
    caloLocalReco +
    vertexReco
)
