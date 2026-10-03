## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 03 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-03-replicability.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
mcmc <- c("data/beads-0.csv", "data/beads-1.csv", "data/beads-2.csv", "data/beads-3.csv", "data/beads-4.csv")  ## LLMR-PATH: placeholders "/path/to/beads-N.csv" -> "data/beads-N.csv"; NOT EXECUTED (beads-0,2,3,4 unavailable, HTTP 404)
pos <- c("UB-4964 (Cod30)","UB-4960 (BuD391B)","UB-6476 (BuD339)","UB-4734 (MH105c)","UB-4732 (MH094)","UB-4890 (MelSG075)","UB-4728 (MH064)","UB-6041 (CasD182)","UB-6038 (CasD183)","UB-4959 (BuD391A)","UB-4511 (EH090)","UB-4512 (EH091)","MelSG077","UB-4885 (MelSG078)","UB-4884 (MelSG079)","UB-4882 (MelSG080)","UB-4733 (MH095)","UB-6473 (BuD250)","UB-4735 (Ber022)","UB-4739 (Ber134/1)","UB-4836 (WG27)","UB-6472 (BuD222)","UB-6037 (CasD134)","UB-4888 (MelSG089)","UB-6040 (CasD053)","UB-4707 (EH079)","UB-6035 (CasD096)","UB-4975 (AstCli12)","UB-4984 (Lec018)","UB-4835 (ApD134)","UB-4729 (MH068)","UB-6034 (CasD120)","UB-4705 (WHes123)","UB-6033 (WHes113)","UB-4709 (EH014)","UB-4708 (EH083)","UB-5208 (ApD107)","UB-4077 (But4275)","UB-4965 (ApD117)","UB-4889 (MelSG069)","UB-4963 (SPTip208)","UB-6032 (SPTip073)","UB-6036 (CasD013)","UB-4887 (MelSG082)","UB-4883 (MelSG095)","UB-4042 (But1674)","UB-4552 (MaDE3)","UB-4507 (Lec187)","UB-4706 (WHes118)","UB-4502 (Lec138)","UB-4504 (Lec179)","UB-4910 (BloodH22)","UB-4506 (Lec172/2)","UB-4551 (MaDE1 & E2)","UB-4554 (MaDF2)","UB-4549 (MaDC7)","UB-4553 (MaDD10)","UB-6042 (CasD088)","UB-4501 (Lec014)","UB-4503 (Lec148)","SUERC-51539 (ERL G353)","SUERC-51548 (ERL G210)","SUERC-51553 (ERL G116)","SUERC-39108 ERLK G322","SUERC-39109 ERL G362","SUERC-39112 ERL G405","SUERC-51560 ERL G038","SUERC-39091 (ERL G003)","SUERC-39092 (ERL G005)","SUERC-39113 (ERL G417)","SUERC-51549 (ERL G195)","SUERC-51543 (ERL G281)","SUERC-51551 (ERL G193)","SUERC-51552 (ERL G107)","SUERC-39100 (ERL G266)","SUERC-51550 (ERL G254)","SUERC-39096 (ERL G112)")
foo <- estimate_range(mcmc=mcmc, position=pos, app='oxcal')
foo$range_table
