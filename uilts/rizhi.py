import logging
import time
def login():
    t = time.strftime('%Y%m%d%H%M%S', time.localtime())
    name='login'+t+"log.txt"
    logging.basicConfig(filename=r"D:\专高六\atee\Auto_mall\web_mall\login\log.txt",
                        filemode='w',level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s'
                        )