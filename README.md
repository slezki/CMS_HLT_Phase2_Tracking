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


#### Adding tracking sequence to your process

All the required modules are in `/wfs/` directory. First you need the raw2digi, tracking, validation, prevalidation, dqm sequences to be loaded
```
process.load('raw2digi_step_cff')
process.load("tracking_sequences_nol1")
process.load('validation_sequences')
process.load('prevalidation_sequences')
process.load('dqm_sequences')
```

then to run the various tracking sequence import the customization functions

```from customize_steps import *```

### Patatrack configurations

If you want to run a configuration including Patatrack pixel tracks (see (the wiki)[https://patatrack.web.cern.ch/patatrack/wiki/]), you would need to set up your release to be 11_1_3_Patatrack adding on top of that what is needed to run with Phase2 tracker.

```
cmsrel CMSSW_11_1_3_Patatrack
cd CMSSW_11_1_3/src/
cmsenv
git cms-init -x cms-patatrack
git branch CMSSW_11_1_X_Patatrack --track cms-patatrack/CMSSW_11_1_X_Patatrack

git cms-merge-topic AdrianoDee:patatrack_hlt_phase2

scram b -j 8
```


## Tracking configurations

### V6s

#### V6_1 (baseline)

The __v6_1__ configuration is the __baseline__ configuration consisting of two main iterations running after pixel tracks building.

1. PixelTracks and PixelVertices (Run2 like set up to have high PV tagging) production; 
2. initialStep iteration: seeded from pixel tracks, BS constrained; 
3. highPtTripletStep iteration: seeded with pixel triplet seeds, BS constrained; 

The final products are:

4. hltPhase2GeneralTracks: from the merge of initialStepTracks and highPtTripletStepTracks;
5. hltPhase2UnsortedOfflinePrimaryVertices: vertices with Deterministic Annealing built from hltPhase2GeneralTracks;

To run this configuration use

```cmsRun step3.py n=N ```

or use

```customizeOriginal_v6(process,timing)```

on your process. Note that this will overwrite your schedule and you would need to add your futher reco in the schedule after this. The `timing` variable is set to `False` by default. If set to `True` it basically drops prevalidation, validation and dqm steps.

#### V6_2 (baseline with patatrack pixel tracks)

The __v6_2__ configuration has the same iterations as the __baseline__ configuration with the difference the pixel tracks, used as seeding for InitialStep, are reconstructed with Patatrack pixel tracks. Once the Patatrack CMSSW environment is set up you would need only to run:

```cmsRun step3.py n=N patatrack=True```

Or to use the 

```customizePixelTracksSoAonCPU(process,vertex=False)```

where the vertex flag indicates if the vertices has to be Patatrack-like (not the default option).

#### V6_3 (baseline with seeding only from patatrack pixel tracks)

The __v6_3__ configuration has the same iterations as the __baseline__ configuration with the difference the pixel tracks are reconstructed with Patatrack pixel tracks and the further used both to seed the initial step iteration (being filtered to have > 3 hits) and the high pT triplet (being filtered to have exactly 3 hits)

```cmsRun step3.py allpata=True patatrack=True pixtrip=True```

### V7s

#### V7_1 (trimmed)

The __v7_2__ configuration is the configuration __trimmed__ around the vertices reconstructed as pixel vertices with pixel tracks. It consists of two main iterations running after pixel tracks building.

1. PixelTracks and PixelVertices (Run2 like set up to have high PV tagging) production; 
2. Pixel Vertices Trimming with: max number of vertices==10, min SumPt2 fraction w.r.t. leading = 0.1 and min SumPt2==10GeV;
2. initialStep iteration: seeded from pixel tracks, constrained to the trimmed PVs; 
3. highPtTripletStep iteration: seeded with pixel triplet seeds, constrained to the trimmed PVs; 

The final products are:

4. hltPhase2GeneralTracks: from the merge of initialStepTracks and highPtTripletStepTracks;
5. hltPhase2UnsortedOfflinePrimaryVertices: vertices with Deterministic Annealing built from hltPhase2GeneralTracks;

To run this configuration use

```cmsRun step3.py n=N wf=-4```

or either use 

```
customizeOriginalTrimmingInitial_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
customizeOriginalTrimmingTriplet_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
```

on your process where the suggested cuts are the above mentioned:

- `FRAC = 10` 
- `NVTX = 10`
- `SUMPT2 = 10`


#### V7_2 (baseline with patatrack pixel tracks)

The __v7_2__ configuration has the same iterations as the __trimmed__ configuration with the difference the pixel tracks, used as seeding for InitialStep, are reconstructed with Patatrack pixel tracks. Once the Patatrack CMSSW environment is set up you would need only to run:

```cmsRun step3.py n=N patatrack=True wf=-4```

Or to use the 

```customizePixelTracksSoAonCPU(process,vertex=False)```

where the vertex flag indicates if the vertices has to be Patatrack-like (not the default option).

#### V7_3 (baseline with seeding only from patatrack pixel tracks)

The __v7_3__ configuration has the same iterations as the __trimmed__ configuration with the difference the pixel tracks are reconstructed with Patatrack pixel tracks and the further used both to seed the initial step iteration (being filtered to have > 3 hits) and the high pT triplet (being filtered to have exactly 3 hits)

```cmsRun step3.py allpata=True patatrack=True pixtrip=True wf=-4```

### V8 (Single Iteration - WIP)

The __v8__ is a configuration with a single iteration seeded by Patatrack pixel tracks [WIP]


