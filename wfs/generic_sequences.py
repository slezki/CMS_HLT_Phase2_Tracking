import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Reconstruction_cff import *
from RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi import *
from RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi import *


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

TrackerRecoGeometryESProducer.trackerGeometryLabel = cms.untracked.string("")

trackerGeoTask = cms.Task(TrackerRecoGeometryESProducer)
trackerMeaTask = cms.Task(MeasurementTracker)

trackerGeo = cms.Sequence(trackerGeoTask)
trackerMea = cms.Sequence(trackerMeaTask)

otLocalReco = cms.Sequence(
    trackerGeo+
    trackerMea+
    MeasurementTrackerEvent
)
