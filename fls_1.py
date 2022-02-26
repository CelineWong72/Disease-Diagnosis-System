from pyit2fls import trapezoid_mf, T1FS, T1FS_plot, T1Mamdani
from numpy import linspace


def calculate_FLS(fever_inp, headache_inp, rrate_inp, cough_inp, sthroat_inp, flu_inp, vomit_inp, diarr_inp):
    d_fever = linspace(98, 104, 1001)
    Fever_low = T1FS(d_fever, trapezoid_mf, [97.999, 98, 98.5, 99, 1])
    Fever_med = T1FS(d_fever, trapezoid_mf, [98.5, 99, 101.5, 102, 1])
    Fever_high = T1FS(d_fever, trapezoid_mf, [101.5, 102, 104, 104.001, 1])

    d_cough = linspace(0, 10, 1001)
    Cough_low = T1FS(d_cough, trapezoid_mf, [-0.001, 0, 3.5, 5, 1])
    Cough_med = T1FS(d_cough, trapezoid_mf, [3.5, 4.5, 6.5, 8, 1])
    Cough_high = T1FS(d_cough, trapezoid_mf, [6.5, 8, 10, 10.001, 1])

    d_rrate = linspace(30, 40, 1001)
    Rr_low = T1FS(d_rrate, trapezoid_mf, [29.999, 30, 32, 34, 1])
    Rr_med = T1FS(d_rrate, trapezoid_mf, [32, 34, 37, 39, 1])
    Rr_high = T1FS(d_rrate, trapezoid_mf, [37, 39, 40, 40.001, 1])

    d_headache = linspace(0, 10, 1001)
    Headache_mod = T1FS(d_headache, trapezoid_mf, [-0.001, 0, 4, 7, 1])
    Headache_sev = T1FS(d_headache, trapezoid_mf, [4, 7, 10, 10.001, 1])

    d_sthroat = linspace(0, 1, 1001)
    Sthroat_low = T1FS(d_sthroat, trapezoid_mf, [-0.001, 0, 0.05, 0.1, 1])
    Sthroat_med = T1FS(d_sthroat, trapezoid_mf, [0.05, 0.1, 0.45, 0.5, 1])
    Sthroat_high = T1FS(d_sthroat, trapezoid_mf, [0.45, 0.5, 1, 1.001, 1])

    d_flu = linspace(0, 1, 1001)
    Flu_no = T1FS(d_flu, trapezoid_mf, [0.001, 0, 0.4, 0.5, 1])
    Flu_yes = T1FS(d_flu, trapezoid_mf, [0.4, 0.5, 1, 1.001, 1])

    d_vomit = linspace(0, 1, 1001)
    Vomit_no = T1FS(d_vomit, trapezoid_mf, [-0.001, 0, 0.4, 0.5, 1])
    Vomit_yes = T1FS(d_vomit, trapezoid_mf, [0.4, 0.5, 1, 1.001, 1])

    d_diarr = linspace(0, 1, 1001)
    Diarr_no = T1FS(d_diarr, trapezoid_mf, [-0.001, 0, 0.4, 0.5, 1])
    Diarr_yes = T1FS(d_diarr, trapezoid_mf, [0.4, 0.5, 1, 1.001, 1])

    d_disease = linspace(0, 100, 1001)
    Di_normal = T1FS(d_disease, trapezoid_mf, [-0.001, 0, 15, 20, 1])
    Di_corona = T1FS(d_disease, trapezoid_mf, [15, 20, 35, 40, 1])
    Di_pneumo = T1FS(d_disease, trapezoid_mf, [35, 40, 55, 60, 1])
    Di_typhoid = T1FS(d_disease, trapezoid_mf, [55, 60, 75, 80, 1])
    Di_malaria = T1FS(d_disease, trapezoid_mf, [75, 80, 100, 100.001, 1])

    def plot_fever_mf():
        T1FS_plot(Fever_low, Fever_med, Fever_high,
                   title="Fever",
                   legends=["Low", "Medium", "High"],
                   )

    def plot_cough_mf():
        T1FS_plot(Cough_low, Cough_med, Cough_high,
                  title="Cough",
                  legends=["Low", "Medium", "High"],
                  )

    def plot_rr_mf():
        T1FS_plot(Rr_low, Rr_med, Rr_high,
                  title="Respiratory Rate",
                  legends=["Low", "Medium", "High"],
                  )

    def plot_headache_mf():
        T1FS_plot(Headache_mod, Headache_sev,
                  title="Headache",
                  legends=["Moderate", "Severe"],
                  )

    def plot_sthroat_mf():
        T1FS_plot(Sthroat_low, Sthroat_med, Sthroat_high,
                  title="Sorethroat",
                  legends=["Low", "Medium", "High"],
                  )

    def plot_flu_mf():
        T1FS_plot(Flu_no, Flu_yes,
                  title="Flu",
                  legends=["No", "Yes"],
                  )

    def plot_vomit_mf():
        T1FS_plot(Vomit_no, Vomit_yes,
                  title="Vomit",
                  legends=["No", "Yes"],
                  )

    def plot_diarr_mf():
        T1FS_plot(Diarr_no, Diarr_yes,
                  title="Diarrhea",
                  legends=["No", "Yes"],
                  )

    def plot_disease_mf():
        T1FS_plot(Di_normal, Di_corona, Di_pneumo, Di_typhoid, Di_malaria,
                  title="Disease",
                  legends=["Normal", "Coronavirus", "Pneumonia", "Typhoid", "Malaria"],
                  )

    # PLOT
    plot_fever_mf()
    plot_cough_mf()
    plot_rr_mf()
    plot_headache_mf()
    plot_sthroat_mf()
    plot_flu_mf()
    plot_vomit_mf()
    plot_diarr_mf()

    plot_disease_mf()

    SYS = T1Mamdani()

    SYS.add_input_variable("Fever")
    SYS.add_input_variable("Cough")
    SYS.add_input_variable("Respiratory Rate")
    SYS.add_input_variable("Headache")
    SYS.add_input_variable("Sore Throat")
    SYS.add_input_variable("Flu")
    SYS.add_input_variable("Vomit")
    SYS.add_input_variable("Diarrhea")
    SYS.add_output_variable("Disease")

    # NORMAL
    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                       ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                      [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_yes)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_yes), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_med), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_high), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_med), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_sev), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_med), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    SYS.add_rule([("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_low),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_normal)])

    # PNEUMONIA ( NO SORE THROAT, FLU, DIARRHEA, VOMIT - HEADACHE MOD - FEVER MOD HIGH) - BATUK2
    SYS.add_rule(
        [("Fever", Fever_med), ("Headache", Headache_mod), ("Respiratory Rate", Rr_med), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
        [("Disease", Di_pneumo)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_med), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
        [("Disease", Di_pneumo)])

    SYS.add_rule([("Fever", Fever_med), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
                  ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
                 [("Disease", Di_pneumo)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no), ("Diarrhea", Diarr_no)],
        [("Disease", Di_pneumo)])

    # MALARIA (FEVER, HEADACHE, VOMITTING, DIARRHEA - SORE THROUGH, COUGH LOW) - NYAMUK
    SYS.add_rule(
        [("Fever", Fever_med), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_malaria)])

    SYS.add_rule(
        [("Fever", Fever_med), ("Headache", Headache_sev), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_malaria)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_malaria)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_low), ("Cough", Cough_low),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_malaria)])

    # TYPHOID (HIGH FEVER, DIARRHEA, HEADACHE - NO FLU) - BACTERIA
    SYS.add_rule(
        [("Fever", Fever_low), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    SYS.add_rule(
        [("Fever", Fever_low), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    SYS.add_rule(
        [("Fever", Fever_med), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    SYS.add_rule(
        [("Fever", Fever_med), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_typhoid)])

    # CORONAVIRUS (HIGH FEVER, COUGH - SORE THROAT, DIARRHEA)
    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_no)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_yes), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_no)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_high), ("Flu", Flu_no), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_no)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_mod), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_high), ("Flu", Flu_yes), ("Vomit", Vomit_no),
         ("Diarrhea", Diarr_no)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_low), ("Flu", Flu_yes), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_corona)])

    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_high), ("Flu", Flu_no), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_corona)])

    # SYS.add_rule(
    #     [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
    #      ("Sore Throat", Sthroat_low), ("Flu", Flu_yes), ("Vomit", Vomit_yes),
    #      ("Diarrhea", Diarr_yes)],
    #     [("Disease", Di_corona)])
    #
    SYS.add_rule(
        [("Fever", Fever_high), ("Headache", Headache_sev), ("Respiratory Rate", Rr_high), ("Cough", Cough_high),
         ("Sore Throat", Sthroat_high), ("Flu", Flu_yes), ("Vomit", Vomit_yes),
         ("Diarrhea", Diarr_yes)],
        [("Disease", Di_corona)])

    # EVALUATION ######################################################################################################
    it2out, tr = SYS.evaluate(
        {"Fever": fever_inp, "Headache": headache_inp, "Respiratory Rate": rrate_inp, "Cough": cough_inp,
         "Sore Throat": sthroat_inp, "Flu": flu_inp, "Vomit": vomit_inp, "Diarrhea": diarr_inp})

    print(tr)

    num = tr["Disease"]
    if num > 0 and num < 20:
        label = "Normal"
    elif num >= 20 and num < 40:
        label = "Coronavirus"
    elif num >= 40 and num < 60:
        label = "Pneumonia"
    elif num >= 60 and num < 80:
        label = "Typhoid"
    elif num >= 80 and num < 100:
        label = "Malaria"
    else:
        label = "Unknown"

    print(label)
    return label


# # TEST DATA
# if __name__ == '__main__':
#     # HEALTHY DATA
#     calculate_FLS(98, 1, 31, 1, 0.05, 0, 0, 0.1)
#     # PNEUMONIA DATA
#     calculate_FLS(100, 3, 39, 8, 0.05, 0.1, 0.1, 0.1)
#     # MALARIA DATA
#     calculate_FLS(101, 1, 31, 2, 0.05, 0.1, 0.7, 0.7)
#     # THYPOID DATA
#     calculate_FLS(98.5, 1, 39, 8, 0.05, 0.1, 0.1, 0.8)
#     # COVID DATA
#     calculate_FLS(98.5, 2.56, 35.3, 6.02, 0, 0.119, 0.831, 0.907)