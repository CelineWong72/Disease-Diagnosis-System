import tkinter
from tkinter import *
from tkinter import ttk
import fls_1
import fls_2


class DetectionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Disease Diagnosis System with Fuzzy Inference System")
        master.geometry("500x750")
        master.resizable(False, False)
        master['background'] = '#e9ecef'
        tabControl = ttk.Notebook(root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Type-1')
        tabControl.add(tab2, text='Type-2')
        tabControl.pack(expand=1, fill="both")

        self.tabSwitch(tab1, "Type-1 Disease Detection System")
        self.tabSwitch(tab2, "Type-2 Disease Detection System")

    def tabSwitch(self, tab, text):
        root = tab
        line0 = Label(root, text=text).pack()
        line1 = Label(root, text="This program will diagnose diseases such as").pack()
        line2 = Label(root, text="Malaria, Pneumonia, Typhoid and Coronavirus based on your symptoms.").pack()
        line3 = Label(root, text="Scale your symptoms using the intensity scale below.").pack()

        fever, headache, rrate, cough, sthroat, flu, vomit, diarr = DoubleVar(), DoubleVar(), DoubleVar(), DoubleVar(),\
                                                                    DoubleVar(), DoubleVar(), DoubleVar(), DoubleVar()

        fever_label = Label(root, text="Intensity of fever (F).").pack()
        fever_slider = Scale(root, from_=98, to=104, orient=HORIZONTAL, resolution=0.05, variable=fever)
        fever_slider.pack()

        headache_label = Label(root, text="Intensity of headache.").pack()
        headache_slider = Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=0.05, variable=headache)
        headache_slider.pack()

        rrate_label = Label(root, text="Respiratory rate.").pack()
        rrate_slider = Scale(root, from_=30, to=40, orient=HORIZONTAL, resolution=0.05, variable=rrate)
        rrate_slider.pack()

        cough_label = Label(root, text="Intensity of coughing.").pack()
        cough_slider = Scale(root, from_=0, to=10, orient=HORIZONTAL, resolution=0.05, variable=cough)
        cough_slider.pack()

        sthroat_label = Label(root, text="Intensity of sore throat.").pack()
        sthroat_slider = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.05, variable=sthroat)
        sthroat_slider.pack()

        flu_label = Label(root, text="Intensity of flu.").pack()
        flu_slider = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.05, variable=flu)
        flu_slider.pack()

        vomit_label = Label(root, text="Intensity of vomit.").pack()
        vomit_slider = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.05, variable=vomit)
        vomit_slider.pack()

        diarr_label = Label(root, text="Intensity of diarrhea.").pack()
        diarr_slider = Scale(root, from_=0, to=1, orient=HORIZONTAL, resolution=0.05, variable=diarr)
        diarr_slider.pack()


        def Click():
            output_label = Label(root, text=("Inputs:", cough_slider.get(),
                                             fever_slider.get(),
                                             headache_slider.get(),
                                             rrate_slider.get(),
                                             sthroat_slider.get(),
                                             flu_slider.get(),
                                             vomit_slider.get(),
                                             diarr_slider.get())).pack()
            if text == "Type-1 Disease Detection System":
                chance = fls_1.calculate_FLS(fever_slider.get(), headache_slider.get(), rrate_slider.get(), cough.get(),
                                             sthroat.get(), flu.get(), vomit.get(), diarr.get())
            else:
                chance = fls_2.calculate_FLS(fever_slider.get(), headache_slider.get(), rrate_slider.get(), cough.get(),
                                             sthroat.get(), flu.get(), vomit.get(), diarr.get())
            output_label = Label(root, text=("Disease: ", chance)).pack()

        calc_button = tkinter.Button(root, text="Check", command=Click).pack()

root = Tk()
gui = DetectionGUI(root)
root.mainloop()
