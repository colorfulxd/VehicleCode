export PYTHONPATH=$PYTHONPATH:C:/Work/05_Learning/01_Stage2_Record/检测/research:C:/Work/05_Learning/01_Stage2_Record/检测/research/slim

set PYTHONPATH=%PYTHONPATH%;C:/Work/05_Learning/01_Stage2_Record/检测/research

set PYTHONPATH=%PYTHONPATH%;C:/Work/05_Learning/01_Stage2_Record/检测/research/slim
python C:/Work/05_Learning/01_Stage2_Record/检测/research/object_detection/train.py --train_dir=C:/Work/05_Learning/01_Stage2_Record/DetectionData/Train --pipeline_config_path=C:/Work/05_Learning/01_Stage2_Record/检测/research/ssd_mobilenet_v1_pets.config