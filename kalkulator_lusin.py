class DozenEntry:
    def __init__(self, lusin, sisa):
        self.lusin = lusin
        self.sisa = sisa

    def count_piece_total(self):
        return self.lusin * 12 + self.sisa

    def __str__(self):
        return "{:5d} | {:4d} | {:5d}".format(self.lusin, self.sisa, self.count_piece_total())

def count_total(entry_lst):
    dash_line = "-------------------------------"
    print("No. | Lusin | Sisa |  Total (piece)")
    print(dash_line)
    total_piece = 0
    i = 0
    for dozen_entry in entry_lst:
        i += 1
        print("{:3d} | {}".format(i, dozen_entry))
        total_piece += dozen_entry.count_piece_total()
        if not (i % 5): print(dash_line)
    print(dash_line + " +")
    print("              Total: {:5d} piece(s)".format(total_piece))

    total_dozen = total_piece//12
    total_residual = total_piece%12
    print("     Total in dozen: {:5d} dozen(s) and {} piece(s)".format(total_dozen, total_residual))
    # total_validation = total_dozen * 12 + total_residual
    validation_str = "{:5d} * 12 + {}".format(total_dozen, total_residual)
    print("         Validation: {} = {} piece(s)".format(validation_str, eval(validation_str)))

def delete_last(lst, num):
    if (len(lst) == 0):
        print("Dozen List is empty!")
        return
    if (not num):
        print("Undo zero is useless!")
        return
    for i in range(num):
        dozen_entry = lst[-1]
        print("Removed {} {}.".format(dozen_entry.lusin, dozen_entry.sisa))
        lst.remove(dozen_entry)

def dozen_calc_runner():
    print("""=====================================
** Welcome to Konveksi Dozen Calculator! **

* Type 'help' and Enter to show available commands.
* Type 'exit' or 'quit' and Enter to exit..
=====================================""")
    keep_asking = True
    dozen_entry_list = list()
    session_name = ""
    while keep_asking:
        row = input(">>> ")
        row = row.split()
        if (row[0] in ['exit', 'quit', 'e', 'q']):
            dozen_entry_list = list()
            keep_asking = False
        elif (row[0] in ['undo', 'u']):
            try:
                num = int(row[1])
                delete_last(dozen_entry_list, num)
            except(IndexError):
                print("Undo needs lst and num arguments!")
        elif (row[0] in ['total', 't']):
            print("Nama: {}".format(session_name))
            count_total(dozen_entry_list)
        elif (row[0] in ['reset', 'r']):
            dozen_entry_list = list()
            session_name = ""
            print("============RESET============")
        elif (row[0] in ['name', 'nama', 'n']):
            session_name = " ".join(row[1:])
        elif (len(row) == 2):
            lusin = int(row[0])
            sisa = int(row[1])
            row_entry = DozenEntry(lusin, sisa)
            dozen_entry_list.append(row_entry)
        elif (len(row) == 1):
            lusin = int(row[0])
            sisa = 0
            row_entry = DozenEntry(lusin, sisa)
            dozen_entry_list.append(row_entry)
        else:
            print("Format masukan salah. Masukkan dengan format yang benar.")