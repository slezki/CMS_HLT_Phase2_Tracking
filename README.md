## CMS_HLT_Phase2_Tracking 

### CMSSW_11_1_0, CMSSW_11_1_0_patch2 CMSSW_11_2_0_pre2

##### L1 Hitless Seeding Tracking 
In case you are working on a release wich has not included the L1 Hitless Seeding you would need to add L1Tracking thourgh merging the dedicated PR:

- 11_2_X : https://github.com/cms-sw/cmssw/pull/30342 
- 11_1_X : https://github.com/cms-sw/cmssw/pull/30574

e.g.
```
cmsrel CMSSW_11_1_0
cd CMSSW_11_1_0/src/
git cms-init
git cms-merge-topic 30342
scram b -j 8
```

and eventyally following instructions here (depending if L1 Tracking PR has already been integrated, who knows)

https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware

##### Running the Tracking Reco

In step3.py the different configurations are listed. Running as

```cmsRun step3.py n=N```

will run the baseline configuration (v6.1) which includes the following steps:

- Pixel Tracks (Quadruplets Seeding)
- Initial Step Tracks Seeded by Pixel Tracks
- HighPt Triplet Tracks (running from pixel triplet seeds to full tracks) with cluster & trajectory masking from InitialStep tracks

different customisation are listed in step3.py. Running as

```cmsRun step3.py n=N wf=7```

will run the l1 traking before the baseline configuration (v6.1).

If you with to test the usage of pixelTriplets for initial step seeding:

```cmsRun step3.py n=N wf=W pixtrip=True```

##### Patatrack Pixel Tracks Customizer

To run Patatrack pixel Tracks inplace of legacy PixelTracks

```cmsRun step3.py n=N patatrack=True```

This works in CMSSW_11_1_0_pre7_Patatrack with https://github.com/AdrianoDee/cmssw/tree/phase2_pixel merged

##### Trimming

To run the default trimming 

```cmsRun step3.py n=N zsep=25 wf=-4 frac=10 nvtx=20 ```
