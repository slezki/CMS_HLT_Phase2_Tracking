import FWCore.ParameterSet.Config as cms
from  Configuration.StandardSequences.Validation_cff import *
from prevalidation_modules import *
from SimGeneral.TrackingAnalysis.trackingParticleNumberOfLayersProducer_cfi import *
from Validation.RecoTrack.HLTmultiTrackValidator_cff import *
from SimTracker.VertexAssociation.VertexAssociatorByPositionAndTracks_cfi import *
from SimTracker.VertexAssociation.VertexAssociatorByPositionAndTracks_cfi import *

hltPhase2HistoProducer = cms.PSet(
mindrj = cms.double(0.001), #cmssw_10_6
    maxdrj = cms.double(0.1), #cmssw_10_6
    nintdrj = cms.int32(100), #cmssw_10_6
    GpSelectorForEfficiencyVsEta = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9),
        status = cms.int32(1),
        tip = cms.double(2.5) #previous 3.5
    ),
    GpSelectorForEfficiencyVsPhi = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9),
        status = cms.int32(1),
        tip = cms.double(2.5) #previous 3.5
    ),
    GpSelectorForEfficiencyVsPt = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9), # previous 0.05
        status = cms.int32(1),
        tip = cms.double(2.5) #previous 3.5
    ),
    GpSelectorForEfficiencyVsVTXR = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9),
        status = cms.int32(1),
        tip = cms.double(30.0)
    ),
    GpSelectorForEfficiencyVsVTXZ = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(35.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9),
        status = cms.int32(1),
        tip = cms.double(2.5) #previous 3.5
    ),
    TpSelectorForEfficiencyVsEta = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9), # previous 0.05
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(2.5) #previous 3.5
    ),
    TpSelectorForEfficiencyVsPhi = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9), # previous 0.05
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(2.5) #previous 3.5
    ),
    TpSelectorForEfficiencyVsPt = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9), # previous 0.05
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(2.5) #previous 3.5
    ),
    TpSelectorForEfficiencyVsVTXR = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9), # previous 0.05
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(60.0)
    ),
    TpSelectorForEfficiencyVsVTXZ = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9), # previous 0.05
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(2.5) #previous 3.5
    ),
    cotThetaRes_nbin = cms.int32(300),
    cotThetaRes_rangeMax = cms.double(0.02),
    cotThetaRes_rangeMin = cms.double(-0.02),
    doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
    dxyDzZoom = cms.double(25),
    dxyRes_nbin = cms.int32(500),
    dxyRes_rangeMax = cms.double(0.1),
    dxyRes_rangeMin = cms.double(-0.1),
    dzRes_nbin = cms.int32(150),
    dzRes_rangeMax = cms.double(0.05),
    dzRes_rangeMin = cms.double(-0.05),
    generalGpSelector = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2), # cmssw_11_1
        minPhi = cms.double(-3.2), # cmssw_11_1
        maxRapidity = cms.double(4.5), #previous 2.5
        minRapidity = cms.double(-4.5), #previous -2.5
        pdgId = cms.vint32(),
        ptMin = cms.double(0.9),
        status = cms.int32(1),
        tip = cms.double(2.5) #previous 3.5
    ),
    generalTpSelector = cms.PSet(
        chargedOnly = cms.bool(True),
        invertRapidityCut = cms.bool(False), # cmssw_11_1
        intimeOnly = cms.bool(False),
        lip = cms.double(30.0),
        maxPhi = cms.double(3.2),
        maxRapidity = cms.double(4.5),
        minHit = cms.int32(0),
        minPhi = cms.double(-3.2),
        minRapidity = cms.double(-4.5),
        pdgId = cms.vint32(),
        ptMax = cms.double(1e+100),
        ptMin = cms.double(0.9),
        signalOnly = cms.bool(True),
        stableOnly = cms.bool(False),
        tip = cms.double(2.5) #previous 3.5
    ),
    maxChi2 = cms.double(20),
    maxDeDx = cms.double(10.0),
    maxDxy = cms.double(25),
    maxDz = cms.double(30),
    maxDzpvCumulative = cms.double(0.6),
    maxDzpvsigCumulative = cms.double(10),
    maxEta = cms.double(4.5),
    maxHit = cms.double(80.5),
    maxLayers = cms.double(25.5),
    maxMVA = cms.double(1),
    maxPVz = cms.double(60),
    maxPhi = cms.double(3.1416),
    maxPt = cms.double(1000),
    maxPu = cms.double(259.5),
    maxTracks = cms.double(2000),
    maxVertcount = cms.double(160.5),
    maxVertpos = cms.double(100),
    maxZpos = cms.double(30),
    maxdr = cms.double(1),
    minChi2 = cms.double(0),
    minDeDx = cms.double(0.0),
    minDxy = cms.double(-25),
    minDz = cms.double(-30),
    minEta = cms.double(-4.5),
    minHit = cms.double(-0.5),
    minLayers = cms.double(-0.5),
    minMVA = cms.double(-1),
    minPVz = cms.double(-60),
    minPhi = cms.double(-3.1416),
    minPt = cms.double(0.1), # logscale
    minPu = cms.double(-0.5),
    minTracks = cms.double(0),
    minVertcount = cms.double(-0.5),
    minVertpos = cms.double(0.01),
    minZpos = cms.double(-30),
    mindr = cms.double(0.001),
    nintChi2 = cms.int32(40),
    nintDeDx = cms.int32(40),
    nintDxy = cms.int32(100),
    nintDz = cms.int32(60),
    nintDzpvCumulative = cms.int32(240),
    nintDzpvsigCumulative = cms.int32(200),
    nintEta = cms.int32(90),
    nintHit = cms.int32(81),
    nintLayers = cms.int32(26),
    nintMVA = cms.int32(100),
    nintPVz = cms.int32(120),
    nintPhi = cms.int32(36),
    nintPt = cms.int32(40),
    nintPu = cms.int32(130),
    nintTracks = cms.int32(200),
    nintVertcount = cms.int32(161),
    nintVertpos = cms.int32(40),
    nintZpos = cms.int32(60),
    nintdr = cms.int32(100),
    phiRes_nbin = cms.int32(300),
    phiRes_rangeMax = cms.double(0.01),
    phiRes_rangeMin = cms.double(-0.01),
    ptRes_nbin = cms.int32(100),
    ptRes_rangeMax = cms.double(0.1),
    ptRes_rangeMin = cms.double(-0.1),
    seedingLayerSets = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4',
        'BPix1+BPix2+BPix3+FPix1_pos',
        'BPix1+BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos+FPix2_pos',
        'BPix1+BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg',
        'BPix1+BPix2+BPix3',
        'BPix2+BPix3+BPix4',
        'BPix1+BPix3+BPix4',
        'BPix1+BPix2+BPix4',
        'BPix2+BPix3+FPix1_pos',
        'BPix2+BPix3+FPix1_neg',
        'BPix1+BPix2+FPix1_pos',
        'BPix1+BPix2+FPix1_neg',
        'BPix2+FPix1_pos+FPix2_pos',
        'BPix2+FPix1_neg+FPix2_neg',
        'BPix1+FPix1_pos+FPix2_pos',
        'BPix1+FPix1_neg+FPix2_neg',
        'FPix1_pos+FPix2_pos+FPix3_pos',
        'FPix1_neg+FPix2_neg+FPix3_neg',
        'BPix1+FPix2_pos+FPix3_pos',
        'BPix1+FPix2_neg+FPix3_neg',
        'FPix2_pos+FPix3_pos+FPix4_pos',
        'FPix2_neg+FPix3_neg+FPix4_neg',
        'FPix3_pos+FPix4_pos+FPix5_pos',
        'FPix3_neg+FPix4_neg+FPix5_neg',
        'FPix4_pos+FPix5_pos+FPix6_pos',
        'FPix4_neg+FPix5_neg+FPix6_neg',
        'FPix5_pos+FPix6_pos+FPix7_pos',
        'FPix5_neg+FPix6_neg+FPix7_neg',
        'FPix6_pos+FPix7_pos+FPix8_pos',
        'FPix6_neg+FPix7_neg+FPix8_neg',
        'BPix1+BPix2',
        'BPix1+BPix3',
        'BPix2+BPix3',
        'BPix1+FPix1_pos',
        'BPix1+FPix1_neg',
        'BPix2+FPix1_pos',
        'BPix2+FPix1_neg'
    ),
    useFabsEta = cms.bool(False),
    useInvPt = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    useLogVertpos = cms.untracked.bool(True)
)

#
hltPhase2TrackValidator = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag(""), #cmssw_10_6
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/Track/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(""),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag(""),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag(""),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("")
)

#hltPhase2TrackValidator = hltTrackValidator.clone()
#hltPhase2TrackValidator.label = []
#hltPhase2TrackValidator.cores = cms.InputTag("")

hltPhase2TrackValidatorL1 = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag(""), #cmssw_10_6
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag(""),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/Track/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(True),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(2.5),
            minRapidity = cms.double(-2.5),
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5), #previous 2.5
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(60.0)
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
	doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            lip = cms.double(30.0),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(30.0)
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.0),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.0),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4',
            'BPix1+BPix2+BPix3+FPix1_pos',
            'BPix1+BPix2+BPix3+FPix1_neg',
            'BPix1+BPix2+FPix1_pos+FPix2_pos',
            'BPix1+BPix2+FPix1_neg+FPix2_neg',
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg',
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos',
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg',
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos',
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg',
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos',
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg',
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos',
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg',
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos',
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg',
            #'BPix1+BPix2+BPix3',
            #'BPix2+BPix3+BPix4',
            #'BPix1+BPix3+BPix4',
            #'BPix1+BPix2+BPix4',
            #'BPix2+BPix3+FPix1_pos',
            #'BPix2+BPix3+FPix1_neg',
            #'BPix1+BPix2+FPix1_pos',
            #'BPix1+BPix2+FPix1_neg',
            #'BPix2+FPix1_pos+FPix2_pos',
            #'BPix2+FPix1_neg+FPix2_neg',
            #'BPix1+FPix1_pos+FPix2_pos',
            #'BPix1+FPix1_neg+FPix2_neg',
            #'FPix1_pos+FPix2_pos+FPix3_pos',
            #'FPix1_neg+FPix2_neg+FPix3_neg',
            #'BPix1+FPix2_pos+FPix3_pos',
            #'BPix1+FPix2_neg+FPix3_neg',
            #'FPix2_pos+FPix3_pos+FPix4_pos',
            #'FPix2_neg+FPix3_neg+FPix4_neg',
            #'FPix3_pos+FPix4_pos+FPix5_pos',
            #'FPix3_neg+FPix4_neg+FPix5_neg',
            #'FPix4_pos+FPix5_pos+FPix6_pos',
            #'FPix4_neg+FPix5_neg+FPix6_neg',
            #'FPix5_pos+FPix6_pos+FPix7_pos',
            #'FPix5_neg+FPix6_neg+FPix7_neg',
            #'FPix6_pos+FPix7_pos+FPix8_pos',
            #'FPix6_neg+FPix7_neg+FPix8_neg',
            #'BPix1+BPix2',
            #'BPix1+BPix3',
            #'BPix2+BPix3',
            #'BPix1+FPix1_pos',
            #'BPix1+FPix1_neg',
            #'BPix2+FPix1_pos',
            #'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(""),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag(""),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.0),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.0),
    mvaLabels = cms.untracked.PSet(),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag(""),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("")
)

hltPhase2TrackValidatorPixelTrackingOnly = hltPhase2TrackValidator.clone()
hltPhase2TrackValidatorPixelTrackingOnly.associators = cms.untracked.VInputTag("hltPhase2TrackingParticlePixelTrackAsssociation")
hltPhase2TrackValidatorPixelTrackingOnly.dirName = cms.string('Tracking/PixelTrack/')
hltPhase2TrackValidatorPixelTrackingOnly.label = cms.VInputTag("hltPhase2PixelTracks")
hltPhase2TrackValidatorPixelTrackingOnly.label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices")
hltPhase2TrackValidatorPixelTrackingOnly.trackCollectionForDrCalculation = cms.InputTag("hltPhase2PixelTracks")
hltPhase2TrackValidatorPixelTrackingOnly.vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks")

# hltPhase2TrackValidatorL1 = hltPhase2TrackValidatorPixelTrackingOnly.clone()
hltPhase2TrackValidatorL1.cores = cms.InputTag("highPtJetsForTrk")
hltPhase2TrackValidatorL1.associators = cms.untracked.VInputTag("hltPhase2TrackingParticleL1TrackAsssociation")
hltPhase2TrackValidatorL1.dirName = cms.string('Tracking/Track/')
hltPhase2TrackValidatorL1.label = cms.VInputTag("hltPhase2L1CtfTracks")
hltPhase2TrackValidatorL1.label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices")
hltPhase2TrackValidatorL1.trackCollectionForDrCalculation = cms.InputTag("hltPhase2PixelTracks")
hltPhase2TrackValidatorL1.trackCollectionForDrCalculation = cms.InputTag("hltPhase2L1CtfTracks")
hltPhase2TrackValidatorL1.vertexAssociator = cms.untracked.InputTag("hltPhase2PixelVertexAssociatorByPositionAndTracks")
hltPhase2TrackValidatorL1.doSeedPlots = cms.untracked.bool(False)

hltPhase2TrackValidatorTrackingOnly = hltPhase2TrackValidatorPixelTrackingOnly.clone()
hltPhase2TrackValidatorTrackingOnly.cores = cms.InputTag("highPtJetsForTrk")
hltPhase2TrackValidatorTrackingOnly.associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation")
hltPhase2TrackValidatorTrackingOnly.dirName = cms.string('Tracking/Track/')
hltPhase2TrackValidatorTrackingOnly.label = cms.VInputTag(
"hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep",   		"hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",
"hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",   	"hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp","hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp",
"hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp", "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
"hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",  "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
"hltPhase2CutsRecoTracksPt09InitialStep", "hltPhase2CutsRecoTracksPt09HighPtTripletStep", "hltPhase2CutsRecoTracksPt09InitialStepHp", "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp")
hltPhase2TrackValidatorTrackingOnly.trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks")
hltPhase2TrackValidatorTrackingOnly.vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
hltPhase2TrackValidatorTrackingOnly.label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices") #("hltPhase2OfflinePrimaryVertices")

# hltPhase2TrackValidatorFromPVStandalone = hltPhase2TrackValidator.clone()
# hltPhase2TrackValidatorFromPVStandalone.associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
# hltPhase2TrackValidatorFromPVStandalone.dirName = cms.string('Tracking/TrackFromPV/'),
# hltPhase2TrackValidatorFromPVStandalone.doPlotsOnlyForTruePV = cms.untracked.bool(True),

hltPhase2TrackValidatorTPPtLess09Standalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackTPPtLess09/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(False),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep",
        "hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",   	"hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp",
        "hltPhase2CutsRecoTracksInitialStepByAlgoMask", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
        "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp", "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
        "hltPhase2CutsRecoTracksPt09InitialStep",
        "hltPhase2CutsRecoTracksPt09HighPtTripletStep", "hltPhase2CutsRecoTracksPt09InitialStepHp", "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2SelectedPixelVertices"), #("hltPhase2OfflinePrimaryVertices")
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(0.9),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2TrackValidatorFromPVStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPV/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
         "hltPhase2GeneralTracksFromPV", #"hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep",
        # "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp",
        # "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep",
        # "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp",
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("hltPhase2TrackingParticlesSignal"),
    label_tp_effic_refvector = cms.bool(True),
    label_tp_fake = cms.InputTag("hltPhase2TrackingParticlesSignal"),
    label_tp_fake_refvector = cms.bool(True),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2PixelVertices"), #("hltPhase2OfflinePrimaryVertices")
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2TrackValidatorFromPVAllTPStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPVAllTP/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(False),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracksFromPV", "hltPhase2CutsRecoTracksFromPVHp", "hltPhase2GeneralTracksFromPVPt09", "hltPhase2CutsRecoTracksFromPVPt09Hp", "hltPhase2CutsRecoTracksFromPVInitialStep",
        "hltPhase2CutsRecoTracksFromPVHighPtTripletStep", "hltPhase2CutsRecoTracksFromPVInitialStepHp", "hltPhase2CutsRecoTracksFromPVHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksFromPVPt09InitialStep", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStep",
        "hltPhase2CutsRecoTracksFromPVPt09InitialStepHp", "hltPhase2CutsRecoTracksFromPVPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2SelectedPixelVertices"), #("hltPhase2OfflinePrimaryVertices")
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2TrackValidatorAllTPEfficStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("hltPhase2TrackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackAllTPEffic/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksHp", "hltPhase2CutsRecoTracksInitialStep", "hltPhase2CutsRecoTracksHighPtTripletStep",
        "hltPhase2CutsRecoTracksInitialStepHp", "hltPhase2CutsRecoTracksHighPtTripletStepHp",
        "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",  "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp", "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp",
        #"hltPhase2L1CtfTracks",
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2SelectedPixelVertices"), #("hltPhase2OfflinePrimaryVertices")
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)

hltPhase2TrackValidatorBHadronTrackingOnly = hltPhase2TrackValidatorTrackingOnly.clone(
    label_tp_effic = cms.InputTag("trackingParticlesBHadron"),
    label_tp_effic_refvector = cms.bool(True),
    label = cms.VInputTag(
    "hltPhase2GeneralTracks", "hltPhase2CutsRecoTracksInitialStep",
    "hltPhase2CutsRecoTracksHighPtTripletStep","hltPhase2CutsRecoTracksInitialStepHp",
    "hltPhase2CutsRecoTracksHighPtTripletStepHp",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgo",
    "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgo",
    "hltPhase2CutsRecoTracksInitialStepByOriginalAlgoHp",
    "hltPhase2CutsRecoTracksHighPtTripletStepByOriginalAlgoHp",
    "hltPhase2GeneralTracksPt09", "hltPhase2CutsRecoTracksPt09Hp",
    "hltPhase2CutsRecoTracksBtvLike", "hltPhase2CutsRecoTracksInitialStepByAlgoMask",
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMask",
    "hltPhase2CutsRecoTracksInitialStepByAlgoMaskHp",
    "hltPhase2CutsRecoTracksHighPtTripletStepByAlgoMaskHp",
    "hltPhase2CutsRecoTracksPt09InitialStep",
    "hltPhase2CutsRecoTracksPt09HighPtTripletStep",
    "hltPhase2CutsRecoTracksPt09InitialStepHp",
    "hltPhase2CutsRecoTracksPt09HighPtTripletStepHp"),
    dirName = cms.string('Tracking/TrackBHadron/')
  )

hltPhase2TrackValidatorSeedingTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHits"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackSeeding/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(True),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = hltPhase2HistoProducer,
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "hltPhase2SeedTracksinitialStepSeeds", "hltPhase2SeedTrackshighPtTripletStepSeeds" ### v2
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("hltPhase2SelectedPixelVertices"), #("hltPhase2OfflinePrimaryVertices")
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.9), # previous 0.005
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"),
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"),
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(60.0),
    trackCollectionForDrCalculation = cms.InputTag("hltPhase2GeneralTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("hltPhase2VertexAssociatorByPositionAndTracks")
)


# MC_validation_v6 = cms.Path(hltPhase2TrackValidatorL1TrackingOnly  +
#                              hltPhase2TrackValidatorPixelTrackingOnly +
#                              hltPhase2TrackValidatorTrackingOnly
#                              #hltPhase2TrackValidatorTPPtLess09Standalone+
#                              #hltPhase2TrackValidatorFromPVStandalone +
#                              #hltPhase2TrackValidatorFromPVAllTPStandalone +
#                              #hltPhase2TrackValidatorAllTPEfficStandalone +
#                              #hltPhase2TrackValidatorBHadronTrackingOnly +
#                              #hltPhase2TrackValidatorSeedingTrackingOnly
# )
