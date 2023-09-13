from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
from loguru import logger
import tqdm
tqdm.tqdm.get_lock().locks = []
import nest_asyncio
nest_asyncio.apply()
logger.info("YO! Upload!")
gauth = GoogleAuth()
auth.authenticate_user()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
logger.info("Auth DONE!")


import os
import json
import glob
import time
import fire

def get_tqdm(*args, **kwargs) -> tqdm.std.tqdm:
    import tqdm.auto
    tqdm.tqdm.get_lock().locks = []
    return tqdm.auto.tqdm(*args, **kwargs)

def upload(file_path, target_folder_id):
    title = os.path.basename(file_path)
    logger.debug(f"uploading {title}")
    file1 = drive.CreateFile({
        "title": title,
        "parents": [{"kind": "drive#fileLink", "id": target_folder_id}]})
    file1.SetContentFile(file_path)
    file1.Upload()
    logger.debug(f"uploading {title} DONE!")


def upload_files(folder_path: str = '/active/upload', cooldown_time: int = 30, target_folder_id: str = '1CK0eVCxJ5zuco_f43n5G6_rCMwkcN7eh'):
    current_time = time.time()

    all_files = sorted(glob.glob(os.path.join(folder_path, '*')), key=os.path.getctime)
    all_files = [f for f in all_files if current_time - os.path.getmtime(f) > cooldown_time]

    logger.info(f"files:\n{json.dumps(all_files, indent=1)}")

    for file_path in get_tqdm(all_files):
        upload(file_path, target_folder_id)
        os.remove(file_path)
        logger.debug(f"<DEL> {file_path}")

if __name__ == '__main__':
    fire.Fire(upload_files)
