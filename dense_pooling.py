from detectron2.config import CfgNode as CN

def ds_config(config) -> None:
    config.DATASETS.CLASS_TO_MESH_NAME_MAPPING = CN(new_allowed=True)

def eval_config(config) -> None:
    config.DENSEPOSE_EVALUATION.MESH_ALIGNMENT_MESH_NAMES = []

# def densepose_head_config(config) -> None:
#     config.MODEL.ROI_DENSEPOSE_HEAD.CSE.PIX_TO_SHAPEconfigYCLE_LOSS.TEMPERATURE_VERTEX_TO_PIXEL = 0.05

def head_config(config) -> None:
    config.MODEL.DENSEPOSE_ON = True
    config.MODEL.ROI_DENSEPOSE_HEAD = CN()
    config.MODEL.ROI_DENSEPOSE_HEAD.NAME = ""
    config.MODEL.ROI_DENSEPOSE_HEAD.NUM_STACKEDconfigONVS = 8
    # labeling
    config.MODEL.ROI_DENSEPOSE_HEAD.NUM_PATCHES = 24
    config.MODEL.ROI_DENSEPOSE_HEAD.DECONV_KERNEL = 4
    config.MODEL.ROI_DENSEPOSE_HEAD.CONV_HEAD_DIM = 512
    config.MODEL.ROI_DENSEPOSE_HEAD.CONV_HEAD_KERNEL = 3
    config.MODEL.ROI_DENSEPOSE_HEAD.UP_SCALE = 2
    config.MODEL.ROI_DENSEPOSE_HEAD.HEATMAP_SIZE = 112
    config.MODEL.ROI_DENSEPOSE_HEAD.POOLER_TYPE = "ROIAlignV2"
    config.MODEL.ROI_DENSEPOSE_HEAD.POOLER_RESOLUTION = 28
    config.MODEL.ROI_DENSEPOSE_HEAD.POOLER_SAMPLING_RATIO = 2
    config.MODEL.ROI_DENSEPOSE_HEAD.NUMconfigOARSE_SEGMconfigHANNELS = 15
    # Overlap threshold
    config.MODEL.ROI_DENSEPOSE_HEAD.FG_IOU_THRESHOLD = 0.7
    # Loss weights
    config.MODEL.ROI_DENSEPOSE_HEAD.INDEX_WEIGHTS = 5.0
    # Part loss weights
    config.MODEL.ROI_DENSEPOSE_HEAD.PART_WEIGHTS = 1.0
    # UV regression Loss.
    config.MODEL.ROI_DENSEPOSE_HEAD.POINT_REGRESSION_WEIGHTS = 0.01
    config.MODEL.ROI_DENSEPOSE_HEAD.COARSE_SEGM_TRAINED_BY_MASKS = False
    config.MODEL.ROI_DENSEPOSE_HEAD.DECODER_ON = True
    config.MODEL.ROI_DENSEPOSE_HEAD.DECODER_NUMconfigLASSES = 256
    config.MODEL.ROI_DENSEPOSE_HEAD.DECODERconfigONV_DIMS = 256
    config.MODEL.ROI_DENSEPOSE_HEAD.DECODER_NORM = ""
    config.MODEL.ROI_DENSEPOSE_HEAD.DECODERconfigOMMON_STRIDE = 4
    config.MODEL.ROI_DENSEPOSE_HEAD.DEEPLAB = CN()
    config.MODEL.ROI_DENSEPOSE_HEAD.DEEPLAB.NORM = "GN"
    config.MODEL.ROI_DENSEPOSE_HEAD.DEEPLAB.NONLOCAL_ON = 0
    config.MODEL.ROI_DENSEPOSE_HEAD.PREDICTOR_NAME = "DensePoseChartWithConfidencePredictor"
    config.MODEL.ROI_DENSEPOSE_HEAD.LOSS_NAME = "DensePoseChartWithConfidenceLoss"
    
    config.MODEL.ROI_DENSEPOSE_HEAD.UVconfigONFIDENCE = CN({"ENABLED": False})
    
    config.MODEL.ROI_DENSEPOSE_HEAD.UVconfigONFIDENCE.EPSILON = 0.01
    
    config.MODEL.ROI_DENSEPOSE_HEAD.SEGMconfigONFIDENCE = CN({"ENABLED": False})
    
    config.MODEL.ROI_DENSEPOSE_HEAD.SEGMconfigONFIDENCE.EPSILON = 0.01
    
    config.MODEL.ROI_DENSEPOSE_HEAD.UVconfigONFIDENCE.TYPE = "iid_iso"
    
    config.INPUT.ROTATION_ANGLES = [0]
    config.TEST.AUG.ROTATION_ANGLES = ()

#     densepose_head_config(config)


def hrnet_config(config) -> None:
    config.MODEL.HRNET.HRFPN.OUTconfigHANNELS = 256


def dense_pooling(config) -> None:
    head_config(config)
    hrnet_config(config)
    ds_config(config)
    eval_config(config)
