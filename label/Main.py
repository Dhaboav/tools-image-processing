import tkinter.messagebox as msg
from frontend.Interface import ChoiceDialog
from backend.TrainRatio import TrainRatio
from backend.Convert import ConvertXML2YOLO
from backend.LabelXml import LabelCheckXML
from backend.LabelYolo import LabelCheckYOLO


if __name__ == "__main__":
    tester = ChoiceDialog()
    tester.root.wait_window(tester.popup)
    choice = tester.choice
    folder_path = tester.input_path

    # Data Class sesuai urutan label!
    class_name = ["ROBOT", "BOLA", "PENGHALANG", "GAWANG"]
    class_color = [(0, 255, 0), (0, 140, 255), (0, 0, 255), (128, 128, 128)]
    class_count = [0, 0, 0, 0]

    if choice == 'Cek Label XML':
        if folder_path:
            excute = LabelCheckXML(dataset_path=folder_path, folder_name='labelXML')
            # train_boolean --> True: Train, False: Val
            excute.run(train_boolean=True, class_name=class_name, class_color=class_color, class_counter=class_count)
        else:
            msg.showerror('Error', 'No Folder Path!')

    elif choice == 'Cek Label YOLO':
        if folder_path:
            excute = LabelCheckYOLO(dataset_path=folder_path, folder_name='labelYOLO')
            # train_boolean --> True: Train, False: Val
            excute.run(train_boolean=True, class_name=class_name, class_color=class_color, class_counter=class_count)
        else:
            msg.showerror('Error', 'No Folder Path!')

    elif choice == 'Konversi XML ke YOLO':
        if folder_path:
            class_mapping = {"0": "ROBOT", "1": "BOLA", "2": "PENGHALANG", "3": "GAWANG"}
            excute = ConvertXML2YOLO(folder_path=folder_path, class_mapping=class_mapping)
            excute.run()
        else:
            msg.showerror('Error', 'No Folder Path!')

    elif choice == 'Train Rasio SSD Mobilenet':
        if folder_path:
            excute = TrainRatio(folder_path=folder_path)
            excute.run()
        else:
            msg.showerror('Error', 'No Folder Path!')