import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import *
from validation_modules import *
from prevalidation_modules import *

                             hltPhase2TrackValidatorFromPVAllTPStandalone)

validation_original = cms.Path( hltTPClusterProducer +
                                hltTrackAssociatorByHits +
                                hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidator +
                                hltPhase2TrackValidatorTPPtLess09Standalone + hltPhase2TrackValidatorFromPVStandalone +
                                hltPhase2TrackValidatorFromPVAllTPStandalone +
                                trackingParticlesBHadron + hltPhase2TrackValidatorBHadronTrackingOnly)

validation_purel1 = cms.Path(hltPhase2TrackValidatorL1)

validation_l1initial = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidator + hltPhase2TrackValidatorL1)

validation_l1trip = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidator + hltPhase2TrackValidatorL1)

validation_pixel = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly)

validation_all = cms.Path(hltPhase2TrackValidatorPixelTrackingOnly + hltPhase2TrackValidator + hltPhase2TrackValidatorL1)
