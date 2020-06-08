import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Reconstruction_cff import *

############# ordered setup

ecalUncalibRecHitSequence = cms.Sequence(
    bunchSpacingProducer +
    ecalMultiFitUncalibRecHit +
    ecalDetIdToBeRecovered
)

caloLocalReco = cms.Sequence(
    ecalUncalibRecHitSequence +
    ecalRecHit +
    hbhereco +
    hfprereco +
    hfreco + #uses hfprereco
    horeco 
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
