from models.rawdlc import Rawdlc


filename = './data/7061_20190830_CC1_02_R01DLC_resnet50_leftPP_CenterFeb13shuffle1_950000.h5'
sess = Rawdlc(filename)

for bodypart in sess.bodyparts: break
sess.get_loc(bodypart)
