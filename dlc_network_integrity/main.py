import os
from models.rawdlc import Rawdlc


def main():
    # TODO: Make config file with the constants as variables, configurable per project
    filename = '/home/jovyan/work/dlc_network_integrity/data/7061_20190830_CC1_02_R01DLC_resnet50_leftPP_CenterFeb13shuffle1_950000.h5'
    
    nose = 'nose'
    leftpaw = 'leftPaw'
    pellet = 'pellet'
    rightpaw = 'rightPaw'

    sess = Rawdlc(filename)
    leftpaw_frame_idx = sess.get_low_p_frames(leftpaw)
    rightpaw_frame_idx = sess.get_low_p_frames(rightpaw)
    nose_frame_idx = sess.get_low_p_frames(nose)
    pellet_frame_idx = sess.get_low_p_frames(pellet)
    
    all_idx = set(np.concatenate([leftpaw_frame_idx, rightpaw_frame_idx, nose_frame_idx, pellet_frame_idx]))
    
    for idx in all_idx:
        print('Here is where I need to implement a new set of functions, a new section to the app, that will save the frames with the necesary plotted points.')



main()