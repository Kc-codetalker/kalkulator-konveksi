class JobEntry:
    def __init__(self, lusin, sisa, nominal):
        self.lusin = lusin
        self.sisa = sisa
        self.nominal = nominal
        self.subtotal = self.count_subtotal()
    
    def count_subtotal(self):
        float_lusin = self.lusin + (self.sisa / 12)
        return float_lusin*self.nominal
    
    def __str__(self):
        return "{:5d} | {:4d} | {:>7s} | {:>10s}".format(self.lusin, self.sisa, format_currency(self.nominal), format_currency(self.subtotal))

def format_currency(amount):
    amount = str(int(amount))
    formatted = ""
    for i in range(len(amount)):
        if (i % 3 == 0):
            formatted = "," + formatted
        formatted = amount[len(amount)-i-1] + formatted
    return formatted[:-1]

def count_total(lst):
    dash_line = "------------------------------------------"
    print("No. | Lusin | Sisa |  Biaya  |  Subtotal")
    print(dash_line)
    total = 0
    i = 0
    for job in lst:
        i += 1
        print("{:3d} | {}".format(i, job))
        total += job.subtotal
        if not (i % 5): print(dash_line)
    print(dash_line + " +")
    print("                        Total: {:>10s}".format(format_currency(total)))

def delete_last(lst, num):
    if (len(lst) == 0):
        print("Job List is empty!")
        return
    if (not num):
        print("Undo zero is useless!")
        return
    for i in range(num):
        job = lst[-1]
        print("Removed {} {} {}.".format(job.lusin, job.sisa, job.nominal))
        lst.remove(job)

def main():
    print("""=====================================
** Welcome to Konveksi Calculator! **

* Type 'help' and Enter to show available commands.
* Type 'exit' or 'quit' and Enter to exit..
=====================================""")

    keep_asking = True
    job_list = list()
    worker_name = ""
    while keep_asking:
        row = input(">>> ")
        row = row.split()
        if (row[0] in ['exit', 'quit', 'e', 'q']):
            job_list = list()
            keep_asking = False
        elif (row[0] in ['undo', 'u']):
            try:
                num = int(row[1])
                delete_last(job_list, num)
            except(IndexError):
                print("Undo needs lst and num arguments!")
        elif (row[0] in ['total', 't']):
            print("Nama: {}".format(worker_name))
            count_total(job_list)
        elif (row[0] in ['reset', 'r']):
            job_list = list()
            worker_name = ""
            print("============RESET============")
        elif (row[0] in ['name', 'nama', 'n']):
            worker_name = " ".join(row[1:])
        elif (len(row) == 3):
            lusin = int(row[0])
            sisa = int(row[1])
            nominal = int(row[2])
            row_entry = JobEntry(lusin, sisa, nominal)
            job_list.append(row_entry)
        elif (len(row) == 2):
            lusin = int(row[0])
            sisa = 0
            nominal = int(row[1])
            row_entry = JobEntry(lusin, sisa, nominal)
            job_list.append(row_entry)
        else:
            print("Format masukan salah. Masukkan dengan format yang benar.")

if __name__ == '__main__':
    main()