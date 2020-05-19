import FWCore.ParameterSet.Config as cms

"""
################################# list of actually needed modules that are in a cms.Path (here for bookkeeping)
from Configuration.StandardSequences.Reconstruction_cff import TrackProducer
# TTRHBuilder = cms.string('WithAngleAndTemplate'), # this will be changed in the main file for now to "WithTrackAngle" Currently all the rest TTRHBuilder are WithTrackAngle
from Configuration.StandardSequences.Reconstruction_cff import SiStripClusterChargeCutNone, SiStripClusterChargeCutLoose, SiStripClusterChargeCutTight ###added for cmssw_10_6
from Configuration.StandardSequences.Reconstruction_cff import CkfBaseTrajectoryFilter_block, offlineBeamSpot, trackerClusterCheck
###################### caloLocalReco
from Configuration.StandardSequences.Reconstruction_cff import bunchSpacingProducer,ecalDetIdToBeRecovered, ecalMultiFitUncalibRecHit
from Configuration.StandardSequences.Reconstruction_cff import ecalRecHit, hbhereco, hfreco # changes in cmssw_11_1
from Configuration.StandardSequences.Reconstruction_cff import hfprereco, horeco
###################### itlocalreco
from Configuration.StandardSequences.Reconstruction_cff import siPhase2Clusters, siPixelClusterShapeCache
from Configuration.StandardSequences.Reconstruction_cff import siPixelClusters, siPixelRecHits # changes in cmssw_11_1
##################### vertexReco
from Configuration.StandardSequences.Reconstruction_cff import  caloTowerForTrk
"""

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

