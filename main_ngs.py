import sys
import argparse
import os
from bs4 import BeautifulSoup
from requests import Request, Session
from time import sleep
from tqdm import tqdm
import logging
from utils.loggerinitializer import *
from distutils.dir_util import mkpath
from utils.read_config import open_json
import brotlicffi


mkpath(os.getcwd() + "/logs/")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
initialize_logger(os.getcwd() + "/logs/", logger)


def ngs_scraper(config1,config2):

    '''This function receives two config files and returns a html with all
    results from NGS-QC'''

    pages = int(config1['pages'])
    uid = config1['uid']

    for page in tqdm(range(1,pages+1)):
        print("Getting page", str(page))
        s = Session()
        s.verify = False

        headers = config2

        payload={'uid': uid, 'order': '0', 'page': str(page)}
        req=Request('POST', 'https://ngsqc.org/get_page.php', data=payload, headers=headers)
        prepped=req.prepare()
        resp = s.send(prepped)
        data = brotlicffi.decompress(resp.content)

        with open (args.output, "a+") as f:
            f.write(str(data))
    
        sleep(2)

    f.close()

    return f 



def main():

    logger.info("############### STARTING " + sys.argv[0] + " ###############")

    first_config = open_json(args.config)
    headers_config = open_json(args.headers)
    ngs_scraper(first_config,headers_config)
   

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description = 'A tool to perform a web scraper of NGS-QC result(s) page(s)'
    )
    
    parser.add_argument('-c', '--config', action='store',
                        help='The absolut path to the config.ini file. You should update the template with the required information',
                        required=True)
    parser.add_argument('-hed', '--headers', action='store',
                        help='The absolut path to the headers_config.ini file. You should update the template with the required information',
                        required=True)

    parser.add_argument('-o', '--output', action='store',
                        help='The absolut path to save the htm file',
                        required=True)

    args = parser.parse_args()
    main()

