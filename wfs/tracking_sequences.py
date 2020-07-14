import FWCore.ParameterSet.Config as cms
from tracking_modules import *
from generic_sequences import *
from L1Trigger.TrackFindingTracklet.Tracklet_cfi import *
from Configuration.StandardSequences.Reconstruction_cff import *

####################################################
########################## Commonssoriginal_v7
#############

hltPhase2L1TTTracksEmulation = TTTracksFromTrackletEmulation.clone()

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

hltPhase2PixelTracksSequenceL1 = cms.Sequence(
    hltPhase2PixelTrackClusters +
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

original_v6 = cms.Path(
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

original_v7 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    hltPhase2InitialStepSequenceFromPixelTracks +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks
)

####################################################
########################## Pure L1 setup (\w vertexing)
#############

hltPhase2L1TracksStepPrimaryVerticesUnsorted = hltPhase2FirstStepPrimaryVerticesUnsorted.clone()
hltPhase2L1TracksStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")

hltPhase2L1TracksStepTrackRefsForJets = hltPhase2InitialStepTrackRefsForJets.clone()
hltPhase2L1TracksStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

hltPhase2Ak4CaloJetsForTrkL1 = hltPhase2Ak4CaloJetsForTrk.clone()
hltPhase2Ak4CaloJetsForTrkL1.srcPVs = cms.InputTag("hltPhase2L1TracksStepPrimaryVerticesUnsorted")

hltPhase2L1TracksStepPrimaryVertices = hltPhase2FirstStepPrimaryVertices.clone()
hltPhase2L1TracksStepPrimaryVertices.jets = cms.InputTag("hltPhase2Ak4CaloJetsForTrkL1")
hltPhase2L1TracksStepPrimaryVertices.particles = cms.InputTag("hltPhase2L1TracksStepTrackRefsForJets")

hltPhase2L1PVSequence = cms.Sequence(
    hltPhase2L1TracksStepPrimaryVerticesUnsorted +
    hltPhase2L1TracksStepTrackRefsForJets +
    caloTowerForTrk + # uses hbhereco, hfreco, horeco, ecalRecHit
    hltPhase2Ak4CaloJetsForTrkL1 +  # uses caloTowerForTrk
    hltPhase2L1TracksStepPrimaryVertices
)


hltPhase2L1TracksTaskSeed = cms.Task(
            hltPhase2L1TrackSeedsFromL1Tracks
)
hltPhase2L1TracksSeqSeed = cms.Sequence(hltPhase2L1TracksTaskSeed) ##need this strange syntax to add mkFit steps

hltPhase2L1TracksSeqPattern = cms.Sequence(
            hltPhase2L1TracksSeqSeed +
            hltPhase2L1TrackCandidates +
            hltPhase2L1CtfTracks
)

hltPhase2L1TracksSequenceClassifiation = cms.Sequence(
            # hltPhase2L1PVSequence +
            hltPhase2L1TracksCutClassifier +#+
            hltPhase2L1TracksSelectionHighPurity)

hltPhase2L1TracksSequence = cms.Sequence(
    hltPhase2L1TracksSeqSeed +
    hltPhase2L1TracksSeqPattern +
    hltPhase2L1TracksSequenceClassifiation
)

pure_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)




hltPhase2InitialStepSequenceL1 = cms.Sequence(
    #hltPhase2InitialStepSeedLayers +
    #hltPhase2InitialStepTrackingRegions +
    #hltPhase2InitialStepHitDoublets +
    #hltPhase2InitialStepHitQuadruplets +
    hltPhase2InitialStepClusters +
    hltPhase2InitialStepSeeds +
    hltPhase2InitialStepTrackCandidates +
    hltPhase2InitialStepTracks +
    #hltPhase2InitialStepPVSequence + # use pixelVertices
    #hltPhase2InitialStepSelector
    hltPhase2InitialStepTrackCutClassifier +
    hltPhase2InitialStepTrackSelectionHighPurity
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

initial_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    TTTracksFromTrackletEmulation +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)

initial_l1tracks_mask = cms.Path(
    hltPhase2StartUp +
    TTTracksFromTrackletEmulation +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
    hltPhase2L1TracksSequence +
    hltPhase2GeneralTracks
)

triplet_l1tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks

)

pixeltriplet_l1 = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence +
    hltPhase2PixelVerticesSequence +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSequence +
    hltPhase2InitialStepSequenceL1 +
    hltPhase2GeneralTracks

)



l1_pixel_reco = cms.Path(
    hltPhase2StartUp +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSeqSeed +
    hltPhase2L1TracksSeqPattern +
    hltPhase2PixelTracksSequenceL1 +
    hltPhase2PixelVerticesSequence +
    hltPhase2L1TracksSequenceClassifiation +
    hltPhase2InitialStepSequence +
    hltPhase2GeneralTracks

)

l1_pixel_reco_triplets = cms.Path(
    hltPhase2StartUp +
    TTTracksFromTrackletEmulation +
    hltPhase2L1TracksSeqSeed +
    hltPhase2L1TracksSeqPattern +
    hltPhase2PixelTracksSequenceL1 +
    hltPhase2PixelVerticesSequence +
    hltPhase2L1TracksSequenceClassifiation +
    hltPhase2InitialStepSequence +
    hltPhase2HighPtTripletStepSequence +
    hltPhase2GeneralTracks

)

l1emulation = cms.Path
(
TTTracksFromTrackletEmulation
)
vertexing = cms.Path(
    caloLocalReco +
    vertexReco
)



#
#
#
#
# MC_Tracking_v7_L1_v1 = cms.Path(
#     itLocalReco +
#     offlineBeamSpot + #cmssw_10_6
#     hltPhase2TTTracksFromTracklet +
#     otLocalReco +
#     #caloLocalReco +
#     trackerClusterCheck +
#     hltPhase2PixelTracksSequence + # pixeltracks
#     hltPhase2PixelVerticesSequence + # pixelvertices
# ##############################################
#     hltPhase2InitialStepSequenceL1 +
#     hltPhase2L1TracksSequence +
#     #hltPhase2HighPtTripletStepSequence +
# ##############################################
#     hltPhase2GeneralTracks
# )
