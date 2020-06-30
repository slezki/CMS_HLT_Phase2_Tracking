# CMS_HLT_Phase2_Tracking with L1 Tracks

### CMSSW_11_1_0_pre6

You would need to add L1Tracking either thourgh merging the dedicated PR or following instructions here

https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware

############
step3.py shows the different configurations

needs:
- step2.root
- raw2digi_step_cff.py
- tracking_sequences.py
- prevalidation_sequences.py
- validation_sequences.py
- dqm_sequencese.py

Once these modules are loaded. One of the customization functions may be used. The latest version (l1Tracking + v6.1) is turned on with 

process = l1_pixel_recovery_triplets(process)

If you with to test the usage of pixelTriplets for initial step seeding:

process = pixelTriplets(process)


