!cd yolact
# run yolact
!python eval.py --trained_model=weights/yolact_resnet50_54_800000.pth --score_threshold=0.15 --top_k=1 --images="../inputs":"../outputs"
!cd ..
