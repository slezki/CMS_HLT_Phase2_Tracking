# CMS_HLT_Phase2_Tracking with L1 Tracks

### CMSSW_11_1_0 or CMSSW_11_2_0_pre2

##### L1 Hitless Seeding Tracking 
You would need to add L1Tracking either thourgh merging the dedicated PR

- 11_2_X : https://github.com/cms-sw/cmssw/pull/30342 
- 11_1_X : https://github.com/cms-sw/cmssw/pull/30574

and following instructions here (depending if L1 Tracking PR has already been integrated)

https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware

##### Running the Tracking Reco

In step3.py the different configurations are listed. Running as

```cmsRun step3.py n=N```

will run the baseline configuration (v6.1) which includes the following steps:

- Pixel Tracks ( Quadruplets Seeding)
- Initial Step Tracks Seeded by Pixel Tracks
- HighPt Triplet Tracks (running from pixel triplet seeds to full tracks) with cluster & trajectory masking from InitialStep tracks

different customisation are listed in step3.py. Running as

```cmsRun step3.py n=N wf=7```

will run the l1 traking before the baseline configuration (v6.1).

If you with to test the usage of pixelTriplets for initial step seeding:

```cmsRun step3.py n=N wf=W pixtrip=True```


