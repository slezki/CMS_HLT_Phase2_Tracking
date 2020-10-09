import FWCore.ParameterSet.Config as cms
from tracking_modules import *
from generic_sequences import *
from Configuration.StandardSequences.Reconstruction_cff import *

####################################################
####### CPE Fix For Template When Track Angle
'''
PixelCPEGenericESProducer = cms.ESProducer('PixelCPEGenericESProducer',
  LoadTemplatesFromDB = cms.bool(True),
  Alpha2Order = cms.bool(True),
  ClusterProbComputationFlag = cms.int32(0),
  useLAWidthFromDB = cms.bool(True),
  lAOffset = cms.double(0),
  lAWidthBPix = cms.double(0),
  lAWidthFPix = cms.double(0),
  eff_charge_cut_highX = cms.double(1),
  eff_charge_cut_highY = cms.double(1),
  eff_charge_cut_lowX = cms.double(0),
  eff_charge_cut_lowY = cms.double(0),
  size_cutX = cms.double(3),
  size_cutY = cms.double(3),
  EdgeClusterErrorX = cms.double(50),
  EdgeClusterErrorY = cms.double(85),
  inflate_errors = cms.bool(False),
  inflate_all_errors_no_trk_angle = cms.bool(False),
  NoTemplateErrorsWhenNoTrkAngles = cms.bool(True),
  UseErrorsFromTemplates = cms.bool(True),
  TruncatePixelCharge = cms.bool(False),
  IrradiationBiasCorrection = cms.bool(False),
  DoCosmics = cms.bool(False),
  Upgrade = cms.bool(True),
  SmallPitch = cms.bool(False),
  ComponentName = cms.string('PixelCPEGeneric'),
  MagneticFieldRecord = cms.ESInputTag('', ''),
  useLAAlignmentOffsets = cms.bool(False),
  DoLorentz = cms.bool(False),
  appendToDataLabel = cms.string('')
)
'''
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
    hltPhase2InitialStepTracksSelectionHighPurity
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
    hltPhase2InitialStepTracksSelectionHighPurity
)

hltPhase2HighPtTripletStepSeeding = cms.Sequence(
            hltPhase2HighPtTripletStepClusters +
            hltPhase2HighPtTripletStepSeedLayers +
            hltPhase2HighPtTripletStepTrackingRegions +
            hltPhase2HighPtTripletStepHitDoublets +
            hltPhase2HighPtTripletStepHitTriplets +
            hltPhase2HighPtTripletStepSeeds
)


hltPhase2HighPtTripletStepSequence = cms.Sequence(
    hltPhase2HighPtTripletStepSeeding +
    hltPhase2HighPtTripletStepTrackCandidates +
    hltPhase2HighPtTripletStepTracks +
    hltPhase2HighPtTripletStepTrackCutClassifier +
    hltPhase2HighPtTripletStepTracksSelectionHighPurity
)

vertexReco = cms.Sequence(
    hltPhase2UnsortedOfflinePrimaryVertices +
    hltPhase2TrackWithVertexRefSelectorBeforeSorting +
    hltPhase2TrackRefsForJetsBeforeSorting +
    caloTowerForTrk +
    hltPhase2Ak4CaloJetsForTrk + # uses caloTowerForTrk
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


single_it = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence + # pixelvertices
##############################################
    hltPhase2InitialStepSequence +
    hltPhase2GeneralTracks
)


pixel_tracks = cms.Path(
    hltPhase2StartUp +
    hltPhase2PixelTracksSequence + # pixeltracks
    hltPhase2PixelVerticesSequence)
