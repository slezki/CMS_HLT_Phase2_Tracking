import FWCore.ParameterSet.Config as cms
from Configuration.ProcessModifiers.l1tracking_cff import *

layerListForPhase2 = ['BPix1+BPix2+BPix3+BPix4',
                       'BPix1+BPix2+BPix3+FPix1_pos','BPix1+BPix2+BPix3+FPix1_neg',
                       'BPix1+BPix2+FPix1_pos+FPix2_pos', 'BPix1+BPix2+FPix1_neg+FPix2_neg',
                       'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
                       'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
                       'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
                       'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
                       'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
                       'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
                       ]
layerListForPhase2Eta4 = layerListForPhase2 + ['FPix5_pos+FPix6_pos+FPix7_pos+FPix9_pos', 'FPix5_neg+FPix6_neg+FPix7_neg+FPix9_neg',
'FPix6_pos+FPix7_pos+FPix8_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix8_neg+FPix9_neg',
'FPix8_pos+FPix9_pos+FPix10_pos+FPix11_pos', 'FPix8_neg+FPix9_neg+FPix10_neg+FPix11_neg',
 'FPix11_pos+FPix9_pos+FPix10_pos+FPix12_pos', 'FPix9_neg+FPix10_neg+FPix11_neg+FPix12_neg']

tripletsLayers = ['BPix1+BPix2+BPix3', 'BPix2+BPix3+BPix4',
                 'BPix1+BPix3+BPix4', 'BPix1+BPix2+BPix4',
                 'BPix2+BPix3+FPix1_pos', 'BPix2+BPix3+FPix1_neg',
                 'BPix1+BPix2+FPix1_pos', 'BPix1+BPix2+FPix1_neg',
                 'BPix2+FPix1_pos+FPix2_pos', 'BPix2+FPix1_neg+FPix2_neg',
                 'BPix1+FPix1_pos+FPix2_pos', 'BPix1+FPix1_neg+FPix2_neg',
#
                 'FPix1_pos+FPix2_pos+FPix3_pos', 'FPix1_neg+FPix2_neg+FPix3_neg',
                 'BPix1+FPix2_pos+FPix3_pos', 'BPix1+FPix2_neg+FPix3_neg',
#
                 'FPix2_pos+FPix3_pos+FPix4_pos', 'FPix2_neg+FPix3_neg+FPix4_neg',
                 'FPix3_pos+FPix4_pos+FPix5_pos', 'FPix3_neg+FPix4_neg+FPix5_neg',
                 'FPix4_pos+FPix5_pos+FPix6_pos', 'FPix4_neg+FPix5_neg+FPix6_neg',
                 'FPix5_pos+FPix6_pos+FPix7_pos', 'FPix5_neg+FPix6_neg+FPix7_neg',
                 'FPix6_pos+FPix7_pos+FPix8_pos', 'FPix6_neg+FPix7_neg+FPix8_neg',
#  removed as redunant and covering effectively only eta>4   (here for documentation, to be optimized after TDR)
#                 ]
     ]

tripletsLayersEta4 = tripletsLayers +  ['BPix1+BPix2+FPix2_pos', 'BPix1+BPix2+FPix2_neg','BPix1+FPix1_pos+FPix3_pos',
                            'BPix1+FPix1_neg+FPix3_neg','FPix6_pos+FPix7_pos+FPix9_pos', 'FPix6_neg+FPix7_neg+FPix9_neg']


########################################################
############################ Customisers
##############
import RecoTracker.MkFit.mkFitInputConverter_cfi as mkFitInputConverter_cfi
import RecoTracker.MkFit.mkFitProducer_cfi as mkFitProducer_cfi
import RecoTracker.MkFit.mkFitOutputConverter_cfi as mkFitOutputConverter_cfi

def customizePixelSeedsEta4(process):

    process.hltPhase2PixelTracksSeedLayers.layerList = cms.vstring(layerListForPhase2Eta4)

    return process

def customizeL1TracksStepToMkFit(process):

    process.hltPhase2L1TracksCandidatesMkFitInput = mkFitInputConverter_cfi.mkFitInputConverter.clone(
            seeds = "hltPhase2L1TrackSeedsFromL1Tracks",
        )

    process.hltPhase2L1TracksCandidatesMkFit = mkFitProducer_cfi.mkFitProducer.clone(
            hitsSeeds = "hltPhase2L1TracksCandidatesMkFitInput",
        )

    process.hltPhase2L1TracksCandidates = mkFitOutputConverter_cfi.mkFitOutputConverter.clone(
        seeds = "hltPhase2L1TrackSeedsFromL1Tracks",
        hitsSeeds = "hltPhase2L1TracksCandidatesMkFitInput",
        tracks = "initialStepTrackCandidatesMkFit",
    )


    # proccess.siPixelClusters =
    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TracksCandidatesMkFitInput,
                              process.hltPhase2L1TracksCandidatesMkFit)

    return process

def customizeGeneralTracksToInitialL1TracksStep(process,timing):

    #process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1TrackStepClusters)

    if timing:
        process.initial_l1tracks = 0
        process.pure_l1tracks = 0
        process.original_v7 = 0
        # process.initial_l1tracks_mask = 0
    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks,
                                      process.vertexing, process.prevalidation_l1initial,
                                      process.validation_l1initial, process.dqm_l1initial])

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTrackSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTrackSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp")

    return process

def customizeGeneralTracksToInitialL1TracksStepMasking(process):

    if timing:
        process.initial_l1tracks = 0
        process.pure_l1tracks = 0
        process.original_v7 = 0
        # process.initial_l1tracks_mask = 0
    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.initial_l1tracks,
                                      process.vertexing, process.prevalidation_l1initial,
                                      process.validation_l1initial, process.dqm_l1initial])


    process.hltPhase2L1TracksTaskSeed.add(process.hltPhase2L1StepSeedClusterMask)
    process.hltPhase2L1TracksCutClassifier.vertices = cms.InputTag("hltPhase2L1TracksStepPrimaryVertices")

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('initialStep','ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2InitialStepTrackSelectionHighPurity","hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2InitialStepTrackSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    #process.hltPhase2InitialStepTracks.clusterRemovalInfo = cms.InputTag("hltPhase2L1TrackStepClusters")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09InitialStepHp")

    process.hltPhase2PixelTracksSeedLayers.FPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")
    process.hltPhase2PixelTracksSeedLayers.BPix.skipClusters = cms.InputTag("hltPhase2L1StepSeedClusterMask")

    return process

def customizeOriginal(process,timing):

    # process.siPixelClusters.vertices = "hltPhase2PixelVertices"
    if not timing:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.original_v7,
                                           process.vertexing, process.prevalidation_original,
                                           process.validation_original, process.dqm_original])
    else:
        process.initial_l1tracks = 0
        process.pure_l1tracks = 0
        # process.original_v7 = 0
        process.initial_l1tracks_mask = 0

def customizeGeneralTracksToPixelL1TracksStep(process,timing):


    if timing:
        # process.initial_l1tracks = 0
        process.pure_l1tracks = 0
        process.original_v7 = 0
        process.initial_l1tracks_mask = 0

    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                      process.vertexing, process.prevalidation_purel1,
                                      process.validation_l1initial, process.dqm_purel1])

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf','hltPixel')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2PixelTracks")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2PixelTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks")

    return process

def customizeGeneralTracksToPixelTripletL1TracksStep(process,timing):

    process.hltPhase2PixelTracksHitSeeds = cms.EDProducer( "CAHitTripletEDProducer",
        CAHardPtCut = cms.double( 0.5 ),
        SeedComparitorPSet = cms.PSet(
          clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "siPixelClusterShapeCache") # pixelVertices
        ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        doublets = cms.InputTag( "hltPhase2PixelTracksHitDoublets" ),
        # fitFastCircle = cms.bool( True ),
        CAThetaCut = cms.double( 0.0012 ), # 0.002 ),
        maxChi2 = cms.PSet(
          value2 = cms.double( 50.0 ),
          value1 = cms.double( 200.0 ),
          pt1 = cms.double( 0.7 ),
          enabled = cms.bool( True ),
          pt2 = cms.double( 2.0 )
        ),
        CAPhiCut = cms.double( 0.18 ),
        useBendingCorrection = cms.bool( True ),
        # fitFastCircleChi2Cut = cms.bool( True )#,
    )

    process.hltPhase2PixelTracksHitDoublets.layerPairs = cms.vuint32( 0, 1 )
    process.hltPhase2PixelTracksSeedLayers.layerList = cms.vstring(tripletsLayers)

    if timing:
        # process.initial_l1tracks = 0
        process.pure_l1tracks = 0
        process.original_v7 = 0
        process.initial_l1tracks_mask = 0
    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                          process.vertexing, process.prevalidation_purel1,
                                          process.validation_l1initial, process.dqm_purel1])


    #l1tracking.toReplaceWith(process.hltPhase2PixelTracksHitQuadruplets,process.hltPhase2PixelTracksHitTriplets)

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf','hltPixel')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks","hltPhase2PixelTracks")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0,0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0,1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"),
                                                                     cms.InputTag("hltPhase2PixelTracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0,1)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks")

    return process

def customizeGeneralTracksToPureL1TracksStep(process):

    if timing:
        process.initial_l1tracks = 0
        # process.pure_l1tracks = 0
        process.original_v7 = 0
        process.initial_l1tracks_mask = 0
    else:
        process.schedule = cms.Schedule(*[ process.raw2digi_step,process.pure_l1tracks,
                                          process.vertexing, process.prevalidation_purel1,
                                          process.validation_purel1, process.dqm_purel1])



    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1TracksSelectionHighPurity")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    process.hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag("hltPhase2GeneralTracks")

    return process
