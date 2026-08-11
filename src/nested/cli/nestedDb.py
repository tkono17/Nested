import os
import fire
import dotenv
import logging
from ..service import NestedDbService
from appbasics import DbApp

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(name)-20s %(levelname)-8s %(message)s')
    dotenv.load_dotenv()
    dbApp = DbApp()
    dbApp.init(NestedDbService())

    fire.Fire(dbApp)
