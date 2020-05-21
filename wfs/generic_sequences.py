import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Reconstruction_cff import *

############# ordered setup

ecalUncalibRecHitSequence = cms.Sequence(
    bunchSpacingProducer +
    ecalMultiFitUncalibRecHit +
    ecalDetIdToBeRecovered
)

caloLocalReco = cms.Sequence(
    hbhereco +
    hfprereco +
    hfreco + #uses hfprereco
    horeco +
    ecalUncalibRecHitSequence +
    ecalRecHit
)

itLocalReco = cms.Sequence(
    siPhase2Clusters +
    siPixelClusters +
    siPixelClusterShapeCache +
    siPixelRecHits
)
otLocalReco = cms.Sequence(
    MeasurementTrackerEvent
)
