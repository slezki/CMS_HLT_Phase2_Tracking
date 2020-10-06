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

In [step3.py](https://github.com/AdrianoDee/CMS_HLT_Phase2_Tracking/blob/master/wfs/step3.py) the different configurations are listed. Running as

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

To run the default trimming (v_7_2)

```cmsRun step3.py n=N zsep=25 wf=-4 frac=10 nvtx=20 ```

#### Adding tracking sequence to your process

All the required modules are in `/wfs/` directory. First you need the raw2digi, tracking, validation, prevalidation, dqm sequences to be loaded
```
process.load('raw2digi_step_cff')
process.load("tracking_sequences_nol1")
process.load('validation_sequences')
process.load('prevalidation_sequences')
process.load('dqm_sequences')
```

then to run the __original__ (namely the v6_1) tracking sequence import the customization functions

```from customize_steps import *```

and use

```customizeOriginal_v6(process,timing)```

on your process. Note that this will overwrite your schedule and you would need to add your futher reco in the schedule after this. The `timing` variable is set to `False` by default. It set to `True` it basically drops prevalidation, validation and dqm steps. To run the __trimmed__ version (where regions are defined around trimmed vertices for both Initial and HighPtTriplet steps) *after* the `customizeOriginal_v6(process,timing)` insert

```
customizeOriginalTrimmingInitial_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
customizeOriginalTrimmingTriplet_v6(process,timing,fraction=FRAC,numVertex=NVTX,minSumPt2=SUMPT2)
```
where the suggested cuts are 

- `FRAC = 10` = 10% of minimun sum_pt_2 fraction w.r.t. leading PV 
- `NVTX = 20`
- `SUMPT2 = 20` = 20 GeV of minimun sum_pt_2 for each trimmed vtx

##### Customizing your workflows

Two customizers are available in order to run the __original v6_1__ and the __trimmed v_7_1__ tracking reconstruction configuration. 


```
cmsrel CMSSW_11_1_3
cd CMSSW_11_1_3/src
git clone git@github.com:AdrianoDee/CMS_HLT_Phase2_Tracking.git -b configs
scram b -j 4
```

Then you can run and customise your own step 

```
cmsDriver.py step3 --geometry Extended2026D49 --era Phase2C9 --conditions auto:phase2_realistic_T15 \
--processName RECO2 --step RAW2DIGI,RECO --eventcontent RECO --datatier RECO \
--dasquery="file dataset=/TT_TuneCP5_14TeV-powheg-pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v2/FEVT" 
--mc --nThreads 4 --nStreams 4 --no_exec -n 10 \
--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring \
--customise CMS_HLT_Phase2_Tracking/Configs/phase2_tracking.customise_hltPhase2_TRKv06_1 \
--no_exec --python_filename hlt_phase2_tracking_v6p1.py  ```
```

for __v6_1__ and with 

```--customise CMS_HLT_Phase2_Tracking/Configs/phase2_tracking.customise_hltPhase2_TRKv07```

for __v7_1__. Note that these customizer will add to the process new modules named with the scheme *hltPhase2ModuleName* and will ovverwrite the __globalreco_tracking__ Task.  
