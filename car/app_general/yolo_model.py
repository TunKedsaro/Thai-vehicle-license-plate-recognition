# # import torch
# from ultralytics import YOLOv10
# # from torchvision import transforms
# # from PIL import Image
# import matplotlib.pyplot as plt
# from operator import itemgetter
# import os


# def check_lib():
#     try:
#         import matplotlib.pyplot as plt
#         print("plt /")
#     except ImportError as e:
#         print(f"plt x {e}")

#     try:
#         import os
#         print("os /")
#     except ImportError as e:
#         print(f"os x {e}")

#     try:
#         from operator import itemgetter
#         print("itemgetter /")
#     except ImportError as e:
#         print(f"itemgetter x {e}")

#     try:
#         import torch
#         print("torch /")
#     except ImportError as e:
#         print(f"Error importing torch: {e}")

#     try:
#         from torchvision import transforms
#         print("transforms /")
#     except ImportError as e:
#         print("transforms x")

#     # pip install git+https://github.com/THU-MIG/yolov10.git
#     # pip install huggingface_hub
#     try:
#         from ultralytics import YOLOv10
#         print("YOLOv10 /")
#     except ImportError as e:
#         print(f"YOLOv10 x {e}")


# print("Hey this is check lib")
# check_lib()

# def predict_label(image_path):
#     img = plt.imread(image_path)
#     return img.shape

# # Load your model
# model_path = os.path.join(os.path.dirname(__file__), 'models/best.pt')
# model = YOLOv10(model_path)

# def predict_label(image_path):
#     img = plt.imread(image_path)
#     results = model(source=img, conf=0.35)
#     for result in results:
#         if result.boxes:
#             boxes = result.boxes.xywh.tolist()
#             clases = [int(cls) for cls in result.boxes.cls.tolist()]
#             bc = []
#             for b, c in zip(boxes, clases):
#                 bc.append([c, b[0]])
#             ls = sorted(bc, key=itemgetter(1))
#             q = [i[0] for i in ls]
#             result_label = convert2label(q)
#             return result_label
#     print("There are no box")
#     return None



# ################################################################################
import matplotlib.pyplot as plt
from ultralytics import YOLOv10
import os

# print("YOLO_Test_01")
# model_path = os.path.join("/home/TunKed05/car/app_general/models","best.pt")
# model = YOLOv10(model_path)
# img = plt.imread("/home/TunKed05/car/media/dGVfMjAyNy5qcGc.jpg")
# results = model(source=img, conf=0.35)
# print("result:",results)

from operator import itemgetter


print("YOLOv10_Test_02")
model_path = os.path.join("/home/TunKed05/car/app_general/models","best.pt")
model = YOLOv10(model_path)
thaichar = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'ก', 11: 'ข', 12: 'ฃ', 13: 'ค', 14: 'ฅ', 15: 'ฆ', 16: 'ง', 17: 'จ', 18: 'ฉ', 19: 'ช', 20: 'ซ', 21: 'ฌ', 22: 'ญ', 23: 'ฎ', 24: 'ฏ', 25: 'ฐ', 26: 'ฑ', 27: 'ฒ', 28: 'ณ', 29: 'ด', 30: 'ต', 31: 'ถ', 32: 'ท', 33: 'ธ', 34: 'น', 35: 'บ', 36: 'ป', 37: 'ผ', 38: 'ฝ', 39: 'พ', 40: 'ฟ', 41: 'ภ', 42: 'ม', 43: 'ย', 44: 'ร', 45: 'ล', 46: 'ว', 47: 'ศ', 48: 'ษ', 49: 'ส', 50: 'ห', 51: 'ฬ', 52: 'อ', 53: 'ฮ'}
junwat = {54: 'กรุงเทพมหานคร', 55: 'กระบี่', 56: 'กาญจนบุรี', 57: 'กาฬสินธุ์', 58: 'กำแพงเพชร', 59: 'ขอนแก่น', 60: 'จันทบุรี', 61: 'ฉะเชิงเทรา', 62: 'ชลบุรี', 63: 'ชัยนาท', 64: 'ชัยภูมิ', 65: 'ชุมพร', 66: 'เชียงราย', 67: 'เชียงใหม่', 68: 'ตรัง', 69: 'ตราด', 70: 'ตาก', 71: 'นครนายก', 72: 'นครปฐม', 73: 'นครพนม', 74: 'นครราชสีมา', 75: 'นครศรีธรรมราช', 76: 'นครสวรรค์', 77: 'นนทบุรี', 78: 'นราธิวาส', 79: 'น่าน', 80: 'บึงกาฬ', 81: 'บุรีรัมย์', 82: 'ปทุมธานี', 83: 'ประจวบคีรีขันธ์', 84: 'ปราจีนบุรี', 85: 'ปัตตานี', 86: 'พระนครศรีอยุธยา', 87: 'พังงา', 88: 'พัทลุง', 89: 'พิจิตร', 90: 'พิษณุโลก', 91: 'เพชรบุรี', 92: 'เพชรบูรณ์', 93: 'แพร่', 94: 'พะเยา', 95: 'ภูเก็ต', 96: 'มหาสารคาม', 97: 'มุกดาหาร', 98: 'แม่ฮ่องสอน', 99: 'ยะลา', 100: 'ยโสธร', 101: 'ร้อยเอ็ด', 102: 'ระนอง', 103: 'ระยอง', 104: 'ราชบุรี', 105: 'ลพบุรี', 106: 'ลำปาง', 107: 'ลำพูน', 108: 'เลย', 109: 'ศรีสะเกษ', 110: 'สกลนคร', 111: 'สงขลา', 112: 'สตูล', 113: 'สมุทรปราการ', 114: 'สมุทรสงคราม', 115: 'สมุทรสาคร', 116: 'สระแก้ว', 117: 'สระบุรี', 118: 'สิงห์บุรี', 119: 'สุโขทัย', 120: 'สุพรรณบุรี', 121: 'สุราษฎร์ธานี', 122: 'สุรินทร์', 123: 'หนองคาย', 124: 'หนองบัวลำภู', 125: 'อ่างทอง', 126: 'อุดรธานี', 127: 'อุทัยธานี', 128: 'อุตรดิตถ์', 129: 'อุบลราชธานี', 130: 'อำนาจเจริญ'}

def convert2label(clases):
    label = ''
    for i in clases:
        if i in junwat.keys():
            if i == 54:
                label = '0'
            else:
                label = '1'
    for j in clases:
        if j in thaichar.keys():
            label = label + thaichar[j]
    return label

def predict_label(image_path):
    img = plt.imread(image_path)
    results = model(source=img, conf=0.35)
    for result in results:
        if result.boxes:
            boxes = result.boxes.xywh.tolist()
            clases = [int(cls) for cls in result.boxes.cls.tolist()]
            bc = []
            for b, c in zip(boxes, clases):
                bc.append([c, b[0]])
            ls = sorted(bc, key=itemgetter(1))
            q = [i[0] for i in ls]
            result_label = convert2label(q)
            return result_label
    print("There are no box")
    return None


# r = predict_label(r"/home/TunKed05/car/media/dGVfMjAyNy5qcGc.jpg")
# print(r)