import FWCore.ParameterSet.Config as cms
#from tracking_modules import *
#from generic_sequences import *
########################################################
############################ Customisers
##############
import RecoTracker.MkFit.mkFitInputConverter_cfi as mkFitInputConverter_cfi
import RecoTracker.MkFit.mkFitProducer_cfi as mkFitProducer_cfi
import RecoTracker.MkFit.mkFitOutputConverter_cfi as mkFitOutputConverter_cfi


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

def customizeGeneralTracksToPureL1TracksStep(process):

    process.trackAlgoPriorityOrder.algoOrder = cms.vstring('ctf')
    process.hltPhase2GeneralTracks.TrackProducers = cms.VInputTag("hltPhase2L1CtfTracks")
    process.hltPhase2GeneralTracks.hasSelector = cms.vint32(0)
    process.hltPhase2GeneralTracks.indivShareFrac = cms.vdouble(1.0)
    process.hltPhase2GeneralTracks.selectedTrackQuals= cms.VInputTag(cms.InputTag("hltPhase2L1TracksSelectionHighPurity"))
    process.hltPhase2GeneralTracks.setsToMerge.tLists = cms.vint32(0)

    process.hltPhase2FirstStepPrimaryVerticesUnsorted.TrackLabel = cms.InputTag("hltPhase2L1CtfTracks")
    process.hltPhase2InitialStepTrackRefsForJets.src = cms.InputTag("hltPhase2L1CtfTracks")

    return process
