#!/usr/bin/env python
# coding: utf-8

__author__ = "Ryan W Null"
__copyright__ = "Copyright 2019-2020, The Ozpolat Lab (http://bduyguozpolat.org/)"
__credits__ = ["B. Duygu Ozpolat"]
__license__ = "GPL 3.0"
__version__ = "2020_2.0"




# Step 1: Create a name for your sequence


name=str(input("What is the gene name? (ex. PduVasa) "))




# Step 2: Input the anti-sense (reverse complement) sequence of your transcript of interest
    #To create reverse complements use this tool - https://www.bioinformatics.org/sms/rev_comp.html
    #Provided Example sequence
        #>Platynereis vasa cDNA reverse complement
        #CCAATCTATGGAGAGTGCCTCCACCAATATCTGGAGAGTGCAATTAACAAGTTTTACCTCAGATTTCCTTTTTTGGCATTTTAAGATGTTAATCACTAACACATAACGGACAACAGATTAACCACAGAGCAATTTCCAAGGAAAGCCCCCAGTACTGATAGAGACAACTGGAGAGCTTGCAGAACAGAGGCGTAGCACAGATTACACTCGAGCGAGTTTGTGTTTTACGCCCGCCCCATCAGCACCAGATTACACTTAAACTCCCTGTAGAATATCCTAGACATGCCACAAATCCAGTTGATATGAACATTCTGAAATATCTAATGAACTTTCCTTCTATGTTCCACTTAACTTCAAAATTCTAAGTACACTTTCCCCGAAGAGTATTTTAAGTATCAGCTGTACAACGCCCTAACATCTGAAGAGACATTACAGCCTTCTTCCGGCTGCCTCTTACAGTCAGCGGTTCTTTCCAACCCAAGGACGGATCTGGAATTCCTTGATAAAGATAAAACTACGCAATATAACTTTCCATGGAATGAGATCAGACTACACTAGTTCAGGCACTTAAACGATCACACGTAATCAGTAGCAAAAGGACTTCATTTGATCACGAATCAACGGCTAGCAAATATTTCATTTATATATAAAGTTATCAAAATCAAAGACTACCTGAGTAAATCATTTAATTCCAACACATCAAACTAGTTACTTGATGTACGGAATGAAGAAGATGAACACATATGTTTGTGAAAAATTGAGCAAGACTAGCTACTGTAGGAGGGAGAATAAACAATAAACCGACGGATTGCTTATCTTTACACGGAGAAACAATTGTGAAATTGAAGACAATTAGTCCAACCCTGAATGGCGACACATATGTACATAATAATGGCTTTAACCTCCCGCCTAAAACAGAATTCGGTATGGAGATATTTACATAAGAAATCTTAACATGAACCAGCGTGTCAAATGTACGAAAGATGAGATTTAAAATGGAATGGGGAAGCAGCTTGAGGTTATCAGAAAGGCACTTTAGAACAAGCGCCCTTCATTCATGAAATGCAAGGCAAGATGTTCCGAGGTAAAAGTCTGCATATAAGACCGTAACCTACCACTCAAGTCACTGACTCCGTGCTTTTTAATAACGTGGATGAGAAGAGACCAGCTTACTCTCAATTAGCGACATAAATGAGCATTTTTCTTTCCTAGTCCCTAATTTCCGACAGTCGATTCATCACTGAATGGTTGATTACAGCTGCATATATGTTTAACGTCAAGAAAACTAGAAATTAACATGATTAAATGAGATATACAAAGCTATAGAGCTAAAATAAATGCGGTTACAACTGATAAAATCTAACAATGTTAGCCAACATGCCGCAAGTGACTCATATTATACATAACATTCAAAAACATTTCATTGAGATACATAATCTAAATTTACACATGTTGTAGGTCACTCGCAACTTTCTCTTTAACCAACTGTACAGTTCTACATAGGCACCGTTTAGCACCAAAGAGAATAATAGCACATCCGGTACAATCATTGTACTCTACTAGCCAAGAATCAAGATGGTTTCAGAAACTGGTCCAGCCCAGCTGGCTAACAAAAGAACTACTTAAAAGAATGGGAGTAAATGAACCAAAGAGCGCAATTACAAGTTCAAGCATTAATCTACTTGGTTTGTCTGGAGATTTAATCCCAGTCCTCGTCATCACCACCGCCAGCATCGCCTCCGAATCCATTGGAACTTCCGCCGAATCCAGCATCTTCTGTGGTTTTCCTCATTCCTCTACGGGTGTCCTTGGCGCCAAATCTGTCGCCTCCCTGGAATCCACTAGAAATGGCTCCCTCCGCGATCTCCTCAAGCCATGGTGGGACAACTTGTTGTGCGTCGCCGAGAGTTTTGACGAGGGATCGAGCAAGTTCTTTGTCTTGGTTAACATCCGGATCGAAGAATGATGTGGCCTTTCCAAGATTACCGCAACGACCGGTTCGACCAATTCTGTGGACGTACTCATCAATGCCACTGGGGAGATCGTAGTTTATGACGTGCTTGACGCCAGGAATATCAAGACCTCTGGCAGCCACtGAGGTAGCAATCAAGATCGGAGCTCGGCCTGTTTTGAAGTCCAACAAGGCCTCTTCTCTTTCCCTCTGCAAACGATCTCCGTGAATACTTGTGGCAGGGTACTGTTCTTGGGACAGATACGCAGCAAGGAAATCAGCACTGCGCTTGGTTTCCAGGAATACCAGGGTTCTGTCGGTTCCTGCTTGGTTCAAGATCTCCACGAGCTTCTCCCTCTTCTCGTACTTGGTGACTTGGTGGACTTCCTGAGTAATGTCGGAGTTGGCACCACCCACTCGTCCGACAGTCACAAACACATACTCGCTCAAGAACTCCTTGGCAAGCTGCTGGATCTCGGCAGCGAAGGTTGCGCTGAACATGAGGGTCTGTCTCTGGCCTTTCTCGGGCATATCGAAGGTTGTGACGAGCTTTCTGATCTCGGGCTCGAAACCCATGTCCAACATACGATCGGCTTCATCCAGGATGAGGTACTTCACCTTCGACAAGTTAATCTTGCCCTTTCCAATGAAGTCGAGCAATCGACCGGGGGTACCAACGACAACGTGGGCGCCCTTCTCCAGTTCTCTGGCTTGGTATCCAACTGAAGTTCCACCGTAAACGACGACTGGTCTGACGCAAGTTGAAGAAGCAAACTTCCTTGCTTCGAGATAGATCTGGTTGACCAACTCTCTGGTGGGTCCAACGATAATAGCGGCAGGGTATTGGGGTCCTCCAAAACCAGAACCTCCTTCGATGAGATCATTCTTGATAATTCCAGTCAGCACGGGTAGCAAGAAAGCAGCTGTTTTTCCGGATCCTGTTTGAGCACAGCCCATCAAGTCTTTGCCTGAGAGGACGATAGGGATAGCCCACTTCTGGATAGGGGTCGGCCGATCGTACTTGGCTTTACGTACATTGGAGCGGACAGTTTCCGATAGGTCTGCTTGATCAAAATTTAAAATGCCGTTCTTTGGTGCATTAGTGCCTGACACTTCAACAGGAATAGACTCGTATTTGTCAAAGTTGATTCCGGCTGTGATGGACTGGAACATTTCTTCTTCACTCTCCGGGGGAGGCGGGGGAACATAGATCTCAGTTTTCTTTTCGCCATCTCCTCCTTCATTATTCGGGCATTCTCGTGAAAAGTGCCCTTCCTCTCCGCACTTGAAACATCCTTTTCCCTTATTTGAATCTCCGGAGTTACCACCGGAATCACCACCGCCATTAGGGCATTCACGAGAGAAATGTCCCTCTTCCCCACACTTGAAGCATCCCTTGCCTCCTCCACTGCCGCCGCCTCCAAATCCACCACCACCGCCAGAGCTTCCGAATCCACCGCCTCTGGAACCACCAAATCCACCACCGCCTCCGGAACTTCCTCCGTTGGGACATTCGCGGGAGAAATGGCCCTCCTCTCCACACTTGAAACATGCCCTACTGCCACCTCCTCCGCCGCCGCCTCCACTGCCTCCAGCATCCGGGCAATCACGGGCTATGTGACCCTCGCCACCACATTTGTAACAACCGCTGCTGCCACCGCCACCACCTCCTCGCTTTCCTCCGAATCCACCACCCCTTGGCTCATCATCTCCTCCAGCACCTCTTGATCCAAATCCGTTACTACGACCGCCAAATCCTCCACTCTCATTTGAATTCTCATCCCGGGAGCCAAATTTGCTGCCAAATCCACTGCTCTTGCTTCCGAAGCCCCCTTGCGAGTCGTCACCGCCTTTCGCCATGCCACGGCCTCTTCCAAAGTTGAAATTCCCATTTGTCGTGCCCCCAAATCCATTGGTCGTCCCCTCATCATCACTCCAGTCTGAcatTTTGGATGGTAAGATTCAGGATAACTATAACAACTCCTCAACCACAGACAACTTGCAACCAACTACAACCACGAGGAAGCTGATCTCGGGCGAAGTTTTAGTC

fullseq=str(input("Enter the antisense sequence of your cDNA (the reverse complement) without spaces or returns. "))


# Step 3: What amplifier hairpin will you use to detect probes? We've built in the probes sold by Molecular Instruments B1-B4.



amplifier=str(input("What is the amplifier to be used with this probe set? B1,B2,B3, or B4 ").upper())
def amp(ampl): 
    if ampl == "B1":
        upspc= "aa"
        dnspc= "ta"
        up = "GAGGAGGGCAGCAAACGG"
        dn = "GAAGAGTCTTCCTTTACG"
    elif ampl == "B2":
        upspc= "aa"
        dnspc= "aa"
        up = "CCTCGTAAATCCTCATCA"
        dn = "ATCATCCAGTAAACCGCC"
    elif ampl == "B3":
        upspc= "tt"
        dnspc= "tt"
        up = "GTCCCTGCCTCTATATCT"
        dn = "CCACTCAACTTTAACCCG"
    elif ampl == "B4":
        upspc= "aa"
        dnspc= "at"
        up = "CCTCAACCTACCTCCAAC"
        dn = "TCTCACCATATTCGCTTC"
    else:
        print( "Please try again")
    return([upspc,dnspc,up,dn])

test=amp(amplifier)
uspc=test[0]
dspc=test[1]
upinit=test[2]
dninit=test[3]



# Step 4: Tuning/printing output of probes


pause=int(input("How many bases from 5' end of the Sense RNA before starting to hybridize? ex. 100 "))
cdna=len(fullseq)
count=(int(input("How many pairs of probes do you want? This will be the maximum number if mRNA will accomodate. ")))
print( "")
print( "")
print( "UpSeq     DownSeq     Pair#")

position=cdna-pause     ### this controls how far from the 5'end of the mRNA probes begin 
pair=1
pairlib={}
idtlibu={}
idtlibd={}
while position>52: #52 is the cutoff for fitting an entire pair at the end of the gene. the program will cycle back over the RNA if not limited like this
    downstream=upinit+uspc+str(fullseq[position-25:position])
    upstream=str(fullseq[position-52:position-27])+dspc+dninit
    pairlib[pair]=str(str(cdna-position)+"     "+str(fullseq[position-25:position])+"     "+str(fullseq[position-52:position-27])+"     "+str(cdna-position+52))
    idtlibu[pair]=str(amplifier+"_"+str(name)+"_"+str(count)+"     "+upstream)
    idtlibd[pair]=str(amplifier+"_"+str(name)+"_"+str(count)+"     "+downstream)
    position-=54      ### 54 is the number of bases covered by one probe set, in the HCRv3 paper each hyb pair,52bp in length, was given 56bp of space, or ~1 hybridizing pair length 
    print( upstream+"     "+downstream+"     "+str(pair))
    if pair<count:
        pair+=1
    else:
        break

print( " ")
print( " ")
print( "These are the probe sequences:")
print( "StartPos     UpSeq     DownSeq     EndPos")
i=1
while i <= pair:
    print( pairlib[i])
    i+=1

    
print( " ")
print( " ")
print( "This is in IDT oPool submission format")
print( "Pool name     sequence")
i=1
while i <= pair:
    print( str(idtlibu[i]))
    print( str(idtlibd[i]))
    i+=1

    
print( "")
print( "")
print( "end")      
