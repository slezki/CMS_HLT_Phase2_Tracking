import FWCore.ParameterSet.Config as cms
from prevalidation_modules import *


#########################################################################

prevalidation_commons =  cms.Task(
                                quickTrackAssociatorByHits,quickTrackAssociatorByHits,
                                tpClusterProducer,trackingParticlesBHadron,simHitTPAssocProducer,
                                trackingParticlesConversion,trackingParticleNumberOfLayersProducer,

                                hltPhase2TrackingParticlesSignal,hltPhase2TrackingParticlesElectron)

prevalidation_highpt = cms.Task(hltPhase2CutsRecoTracksFromPVHighPtTripletStep,hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp,hltPhase2SeedTrackshighPtTripletStepSeeds,
                                          hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep,hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp,
                                          hltPhase2CutsRecoTracksHighPtTripletStep,hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask,
                                          hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp,hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo,
                                          hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp,hltPhase2CutsRecoTracksHighPtTripletStepHp,
                                          hltPhase2CutsRecoTracksPt09HighPtTripletStep, hltPhase2CutsRecoTracksPt09HighPtTripletStepHp)

prevalidation_associators = cms.Task(hltPhase2TrackingParticleRecoTrackAsssociation,
                                     hltPhase2VertexAssociatorByPositionAndTracks,
                                     hltPhase2PixelVertexAssociatorByPositionAndTracks,
                                     hltPhase2TrackingParticlePixelTrackAsssociation,
                                     )

prevalidation_initial = cms.Task(hltPhase2CutsRecoTracksInitialStep,hltPhase2CutsRecoTracksFromPVPt09InitialStepHp,hltPhase2SeedTracksinitialStepSeeds,
                                           hltPhase2CutsRecoTracksInitialStepByAlgoMask,hltPhase2CutsRecoTracksInitialStepByOriginalAlgo,
                                           hltPhase2CutsRecoTracksInitialStepHp,hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp,
                                           hltPhase2CutsRecoTracksPt09InitialStep,hltPhase2CutsRecoTracksFromPVInitialStepHp,
                                           hltPhase2CutsRecoTracksFromPVInitialStep,hltPhase2CutsRecoTracksFromPVPt09InitialStep,
                                           hltPhase2CutsRecoTracksPt09InitialStepHp,hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp)

prevalidation_general = cms.Task(hltPhase2CutsRecoTracksFromPVHp,hltPhase2GeneralTracksFromPV,
                                hltPhase2CutsRecoTracksFromPVPt09Hp,hltPhase2GeneralTracksFromPVPt09,
                                hltPhase2CutsRecoTracksPt09Hp,hltPhase2CutsRecoTracksBtvLike,
                                hltPhase2GeneralTracksPt09,hltPhase2CutsRecoTracksHp)

prevalidation_vertex = cms.Task(hltPhase2SelectedOfflinePrimaryVertices,
                                hltPhase2SelectedOfflinePrimaryVerticesWithBS,
                                hltPhase2VertexAnalysisTrackingOnly,
                                hltPhase2SelectedPixelVertices,
                                hltPhase2PixelVertexAnalysisTrackingOnly)

prevalidation_l1 = cms.Task(hltPhase2TrackingParticleL1TrackAsssociation,hltPhase2CutsRecoTracksL1Step,hltPhase2CutsRecoTracksL1,hltPhase2CutsRecoTracksL1StepByOriginalAlgo,hltPhase2CutsRecoTracksL1StepByOriginalAlgoHp)

prevalidation_v0 = cms.Task(hltPhase2V0Validator)

####################################################
########################## Pixel Tracks
#############

prevalidation_startup = cms.Task(prevalidation_commons,prevalidation_associators)##,prevalidation_vertex)

prevalidation_original = cms.Path(prevalidation_startup,
                                  prevalidation_v0,
                                  prevalidation_initial,
                                  prevalidation_highpt,
                                  prevalidation_general)

prevalidation_purel1 = cms.Path(prevalidation_startup,
                                 prevalidation_l1,
                                 prevalidation_general)

prevalidation_l1initial = cms.Path(prevalidation_startup,
                                  prevalidation_l1,
                                  prevalidation_initial,
                                  prevalidation_general)

prevalidation_l1trip= cms.Path(prevalidation_startup,
                                  prevalidation_l1,
                                  prevalidation_highpt,
                                  prevalidation_general)
