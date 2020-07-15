import FWCore.ParameterSet.Config as cms
from tracking_modules import *
from generic_sequences import *
from Configuration.StandardSequences.Reconstruction_cff import *

####################################################
########################## Commonssoriginal_v7
#############

hltPhase2StartUp = cms.Sequence(
    offlineBeamSpot +
    itLocalReco +
     #cmssw_10_6
    otLocalReco +
    #caloLocalReco +
    trackerClusterCheck
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

####################################################
########################## Basic V7 setup
#############

hltPhase2PixelTracksSequence = cms.Sequence(
    hltPhase2PixelTrackFilterByKinematics +
    hltPhase2PixelFitterByHelixProjections +
    hltPhase2PixelTracksTrackingRegions +
    hltPhase2PixelTracksSeedLayers +
    hltPhase2PixelTracksHitDoublets +
    hltPhase2PixelTracksHitSeeds +
    hltPhase2PixelTracks
)

hltPhase2PixelVerticesSequence = cms.Sequence(
    hltPhase2PixelVertices +
    hltPhase2TrimmedPixelVertices
)


hltPhase2InitialStepSequenceFromPixelTracks = cms.Sequence(
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTrackSelectionHighPurity
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

original_v6 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2HighPtTripletStepSequence +
##############################################
    hltPhase2GeneralTracks
)

vertexing = cms.Path(
    caloLocalReco +
    vertexReco
)
