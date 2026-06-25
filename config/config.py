# ISTAT API
ISTAT_URL = 'https://esploradati.istat.it/SDMXWS/rest/data/41_983'
ISTAT_HEADERS = {'Accept': 'application/vnd.sdmx.data+csv;version=1.0.0'}

# SITUAS API
SITUAS_URL = 'https://situas.istat.it/ShibO2Module/api/Report/Spool/{anno}-12-31/74?&pdoctype=CSV'
SITUAS_COOKIE = 'rxVisitor=17823024965236V98Q9RG38MIGGGFKTR5GDCJ7UDA761E; dtSa=-; dtCookie=v_4_srv_8_sn_BOJED851GTSUKI3R96OSTBOQT022P6RT_perc_100000_ol_0_mul_1_app-3A5f9422794d4b081c_1; rxvt=1782307249186|1782304834351; dtPC=8$302496518_44h23vPPKDIRPBCQAKKWACIUBKRQRNDDPIOFKU-0e0'  
# update when expired

# File paths
RAW_PATH = '../raw/'
CLEAN_PATH = '../clean/'

# Years range
START_YEAR = 2001
END_YEAR = 2024