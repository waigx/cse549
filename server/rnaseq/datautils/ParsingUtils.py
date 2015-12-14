import pandas as pd

def readRSEMTruth(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', skiprows=1,
                     names=['Name', 'Gene{}'.format(suffix),
                            'Length{}'.format(suffix),
                            'EffLength{}'.format(suffix),
                            'NumReads{}'.format(suffix),
                            'TPM{}'.format(suffix),
                            'FPKM{}'.format(suffix),
                            'IsoPct{}'.format(suffix)])
    df.set_index('Name', inplace=True)
    return df


def readExpress(fn, suffix=""):
    df = pd.read_csv(fn, sep="\t", skiprows=1,
                     names=["bundle_id{}".format(suffix),
                            "Name",
                            "Length{}".format(suffix),
                            "eff_length{}".format(suffix),
                            "tot_counts{}".format(suffix),
                            "uniq_counts{}".format(suffix),
                            "NumReads{}".format(suffix),
                            "NumReadsEffective{}".format(suffix),
                            "ambig_distr_alpha{}".format(suffix),
                            "ambig_distr_beta{}".format(suffix),
                            "fpkm{}".format(suffix),
                            "fpkm_conf_low{}".format(suffix),
                            "fpkm_conf_high{}".format(suffix),
                            "solvable{}".format(suffix),
                            "TPM{}".format(suffix)])
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df


def readSailfishQuasi(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', comment='#',
                     names=['Name',
                            'Length{}'.format(suffix),
                            'TPM{}'.format(suffix),
                            'NumReads{}'.format(suffix)])
    df.dropna(how='all', inplace=True)
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df

def readTigar(fn, suffix=""):
    df = pd.read_table(fn, sep='\t', skiprows=1,
                     names=['Name',
                            'Length{}'.format(suffix),
                            'NumReads{}'.format(suffix),
                            'FPKM{}'.format(suffix),
                            'Theta{}'.format(suffix)])
    df.dropna(how='all', inplace=True)
    df['TPM_{}'.format(suffix)] = df['Theta{}'.format(suffix)] * 1000000.0
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df



def readSalmon(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', comment='#',
                     names=['Name',
                            'Length{}'.format(suffix),
                            'TPM{}'.format(suffix),
                            'NumReads{}'.format(suffix)])
    df.dropna(how='all', inplace=True)
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df

def readSailfish_orig(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', comment='#',
                     names=['Name',
                            'Length{}'.format(suffix),
                            'TPM{}'.format(suffix),
                            'RPKM{}'.format(suffix),
                            'KPKM{}'.format(suffix),
                            'NumKmers{}'.format(suffix),
                            'NumReads{}'.format(suffix)])
    df.dropna(how='all', inplace=True)
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df

def readSailfish(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', comment='#',
                     names=['Name',
                            'Length{}'.format(suffix),
                            'TPM{}'.format(suffix),
                            'NumReads{}'.format(suffix)])
    df.dropna(how='all', inplace=True)
    df.convert_objects(convert_numeric=True)
    df.set_index('Name', inplace=True)
    return df

def readKallisto(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t', skiprows=1,
                     names=['Name',
                            'Length{}'.format(suffix),
                            'EffLen{}'.format(suffix),
                            'NumReads{}'.format(suffix),
                            'TPM{}'.format(suffix)])
    df.set_index('Name', inplace=True)
    df.convert_objects(convert_numeric=True)
    return df

def readProFile(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t',
                     names=['Locus{}'.format(suffix),
                            'Name',
                            'Coding{}'.format(suffix),
                            'Length{}'.format(suffix),
                            'ExpFrac{}'.format(suffix),
                            'ExpNum{}'.format(suffix),
                            'LibFrac{}'.format(suffix),
                            'LibNum{}'.format(suffix),
                            'SeqFrac{}'.format(suffix),
                            'SeqNum{}'.format(suffix),
                            'CovFrac{}'.format(suffix),
                            'ChiSquare{}'.format(suffix),
                            'CV{}'.format(suffix)])
    df.set_index('Name', inplace=True)
    df.convert_objects(convert_numeric=True)
    return df

def readBitSeqFile(fn,suffix=""):
    df = pd.read_csv(fn, sep=' ',skiprows=6,
                     names = ['mean_theta{}'.format(suffix),
                              'alpha{}'.format(suffix),
                              'beta{}'.format(suffix)])
    #df.set_index('Name', inplace=True)
    df.convert_objects(convert_numeric=True)
    return df


def readResFile(fn, suffix=""):
    df = pd.read_csv(fn, sep='\t',
                     names=['Name',
                            'Length{}'.format(suffix),
                            'Abund{}'.format(suffix)])
    df.set_index('Name', inplace=True)
    df.convert_objects(convert_numeric=True)
    return df

def readTranscriptRes(fn, suffix=""):
    df = pd.read_csv(fn, sep = '\t', skiprows=1,
                     names = ['Name',
                              'Length',
                              'GC_Cont',
                              'A_Cont',
                              'T_Cont',
                              'C_Cont',
                              'G_Cont'])
    df.set_index('Name', inplace=True)
    df.convert_objects(convert_numeric=True)
    return df