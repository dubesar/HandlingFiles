c=[]
from tqdm import tqdm
import cv2
for i in tqdm(os.listdir('../input/train/train/')):
    img = cv2.imread(os.path.join('../input/train/train/',i),cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(96,96))
    c.append(img)
