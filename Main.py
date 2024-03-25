from lzma import MODE_FAST
import os
os.system("color")
import Function as MODULEF
first = open("dook.bin", "a")
first.close()

class Main:
    def __init__(self):
        self.info_user_position_active = 0

    def create_databases_all_foundation(self, input_user_name_database_key):
        final_name = MODULEF.room_filter_one(input_user_name_database_key)
        if final_name == "": return

        if len(final_name) > 0 or final_name != 0:
            os.mkdir(f"D:/dev/z - project/databases/{final_name}.pkg")
            file_opener = open("dook.bin", "a")
            file_opener.write(f"{MODULEF.writeBin(final_name)}\n")
            file_opener.close()
        
        os.mkdir(f"D:/dev/z - project/databases/{final_name}.pkg/data")

    
    def show_databases_from_dook(self, hide):
        head = "Database"
        right_space = len(head) + 1
        file_opener = open("dook.bin", "a")
        file_opener.close()
        file_opener = open("dook.bin", "r")
        check = file_opener.readline()
        file_opener.close()
        if len(check) == 0:
            print("+-" + "-"*(len(head) + 1) + "+")
            print("| " + head + " "*(right_space - len(head))+ "|")
            print("+-" + "-"*(len(head) + 1) + "+")
            return

        file_opener = open("dook.bin", "r")
        file_contens = file_opener.readlines()
        file_opener.close()
    
        for i in range(0, len(file_contens)):
            if len(MODULEF.readBin(file_contens[i])) >= right_space:
                right_space = len(MODULEF.readBin(file_contens[i]))

        print("+-" + "-"*(right_space) + "+")
        print("| " + head + " "*(right_space - len(head)) + "|")
        print("+-" + "-"*(right_space) + "+")

        for i in range(0, len(file_contens)):
            data_filter = ""
            data = MODULEF.readBin(file_contens[i])
            for o in range(0, len(data) - 1):
                data_filter += data[o]

            print("| " + data_filter + " "*(right_space - len(data_filter)) + "|")

        print("+-" + "-"*(right_space) + "+")

    def use_database(self, input_user_database_will_be_used_key):
        database_will_be_used = MODULEF.room_filter_one(input_user_database_will_be_used_key)
        if database_will_be_used == "": return

        file_opener = open("dook.bin", "r")
        shilter_temp = "empty"
        while len(shilter_temp) != 0:      
            shilter_temp = MODULEF.readBin(file_opener.readline())
            if len(shilter_temp) == 0: break
            if database_will_be_used in shilter_temp and (len(database_will_be_used) + 1) == len(shilter_temp):
                self.info_user_position_active = database_will_be_used
                file_opener.close()
                return
          
        print("database tidak ditemukan\n")
        file_opener.close()

    def create_head_plus_next(self, input_user_will_be_head_name_key):
        shilter_temp_for_head_name = ""
        if self.info_user_position_active == 0:
            print("tidak terkait dengan database manapun\n")
        else:
            if input_user_will_be_head_name_key[-1] != "]":
                print("kesalahan penulisan\n")
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()

                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                get_contents = file_opener.readlines()
                file_opener.close()

                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                heads = MODULEF.room_filter_coma(input_user_will_be_head_name_key)
                for i in range(0, len(heads)):
                    file_opener.write(MODULEF.writeBin(heads[i]) + "\n")
                file_opener.close()

                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "a")
                file_opener.close()
                
                if len(get_contents) != 0:
                    file = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                    get = file.readlines()
                    file.close()
                    file = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                    length = file.readlines()
                    file.close()
                    index = 0
                    for i in range(len(get) - len(heads) + 1, len(get) + 1):
                        file = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "a")
                        for o in range(0, len(length)):
                            file.write(MODULEF.writeBin("-") + "\n")
                        file.close()
                        index += 1
                    return

                for i in range(1, (len(heads) + 1)):
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "a")
                    file_opener.close()

    # PART PALING BIKIN MALES DAN NGESELIN. BUAT SIAAPAUN YNG BACA DIMASA DEPAN -
    # NANTI TOLONG DIPERBAIKI PROGRAMNYA YA, BUAT LEBIH EFISIEN :) kalo bisa semuanya diperbaiki hehe...
    def add_data(self, input_user_data):    
        if self.info_user_position_active == 0:
            print("tidak terkait database manapun\n")
        else:
            if input_user_data[-1] != "]":
                print("kesalahan penulisan\n")
                return
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()

                # NOTIF KALO USER BELUM BUAT HEAD
                check_status = "empty"
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                check_status = file_opener.read()
                if len(check_status) == 0:
                    print("anda belum membuat ruang-head\n")
                    return
                file_opener.close()
                # PROGRAM NOTIF BERAKHIR DISINI

                # MENGAMBIL DATA DARI HEAD FILE UNTUK MENJADI TITIK PENENTUAN PANJANG DARI JUMLAH DATA
                # YANG DIMASUKKAN OLEH USER
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                file_contents = file_opener.readlines() 
                file_opener.close()

                # FILTERISASI
                datas = MODULEF.room_filter_coma(input_user_data)
               
                if len(datas) == len(file_contents):
                    for i in range(0, len(datas)):
                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "a")
                        file_opener.write(MODULEF.writeBin(datas[i]) + "\n")
                        file_opener.close()
                    print(f"berhasil menambahkan data\n")
                    
                else:
                    print(f"\'data tidak tepat'. Jumlah ruang-head yang anda buat berjumlah \'{len(file_contents)}\'")
                    print(f"sedangkan data yang anda masukkan berjumlah \'{len(datas)}\'")

    def show_all_data(self, hide):
        if self.info_user_position_active == 0:
            print("tidak terkait database manapun\n")
        else:
            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
            file_opener.close()
            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
            check = file_opener.readline()
            file_opener.close()
            if len(check) == 0:
                print(f"belum ada data dimasukkan\n")
            else:
                heads = []
                right_space = []
                heads_visual = "| ID | "
                data_visual = "| "
                close_visual = "+----+"

                final_head = "empty"
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                while len(final_head) != 0:
                    final_head1 = ""
                    final_head = MODULEF.readBin(file_opener.readline())
                    if len(final_head) <= 0 : break
                    close_visual += "-"*(len(final_head) + 1) + "+"

                    for i in range(0, (len(final_head) - 1)):
                        final_head1 += final_head[i]

                    heads_visual += final_head1 + " | "
                    heads.append(final_head1)
                    right_space.append(len(final_head1) + 1)
                    
                file_opener.close()
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                check_status = file_opener.readline()
                file_opener.close()

                if len(check_status) == 0:
                    print(close_visual)
                    print(heads_visual)
                    print(close_visual)
                    # print(len(heads))
                else:
                    heads_visual = "ID"
                    i_d = 0
                    shilter_data_from_file_z = "empty"
                    for i in range(1, (len(heads) + 1)):
                        i_d = 0
                        shilter_data_from_file_z = "empty"
                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "r")
                        while len(shilter_data_from_file_z) != 0:
                            if len(shilter_data_from_file_z) <= 0 :
                                file_opener.close()
                                break
                            i_d += 1
                            shilter_data_from_file_z = MODULEF.readBin(file_opener.readline())
                            if len(shilter_data_from_file_z) >= right_space[i - 1]:
                                right_space[i - 1] = len(shilter_data_from_file_z)
                        file_opener.close()

                    # HEAD VISUAL AREA
                    i_d -= 1
                    closer = "+"

                    heads_visual = "| " + heads_visual + " "*(len(str(i_d)) - len(heads_visual) + 2) + "| "
                    closer += "-"*(len(str(i_d)) + 3) + "+"

                    for i in range(0, len(heads)):
                        closer += "-"*right_space[i] + "-+"
                        heads_visual += heads[i] + " "*(right_space[i] - len(heads[i])) + "| "

                    print(closer)
                    print(heads_visual)
                    # on / of
                    print(closer)
                    
                    # DATA VISUAL AREA
                    i_d_addres_file_to_file = 1
                    while i_d_addres_file_to_file <= i_d:
                        data_visual += str(i_d_addres_file_to_file) + " "*((len(str(i_d)) - len(str(i_d_addres_file_to_file))) + 2) + "| "
                        for i in range(1, (len(heads) + 1)):
                            data_final = ""
                            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "r")
                            data = MODULEF.readBin(file_opener.readlines()[i_d_addres_file_to_file - 1])
                            
                            for ind in range(0, (len(data) - 1)):
                                data_final += data[ind]

                            data_visual += data_final + " "*(right_space[i - 1] - len(data_final)) + "| " 

                        # print(closer)
                        print(data_visual)
                        data_visual = "| "                            
                        i_d_addres_file_to_file += 1

                    print(closer)
                    
                   
                    # beres nih yang diatas. tapi coba nanti dicek lagi deh siapa tahu ada yang bolong bolong atau kesalahan yg gk di sadari+
                    # ==========+================================================================
                    # ============================================
                    # =======================
                    # =============
                    # = oh iya, entah kenapa di terminal vscode itu jadi aneh tabelnya padahal kalo di terminal biasa sih aman aman aja
                    # coba nanti cari tahu itu masalahnya dimana dan kenapa +++++++++++++=========
                    #==========================
                    #===============
                    # masalah terminal aneh udah di fix ya tinggal di cek cek lagi aja deh :) 
                    # =============
                    # =====================================
                    # ===============================
                    # oke udah aku periksa sejauh ini aman aman aja, mungkin lanjut ke method selanjutnya ya :)

    def delete_line(self, input_key):
        if input_key[-1] != "]":
            print("terjadi kesalahan penulisan\n")
        else:
            if self.info_user_position_active == 0:
                print("tidak terkait dengan database manapun\n")
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                check = file_opener.readline()
                file_opener.close()
                
                if len(check) == 0:
                    print("\'tidak memiliki data apapun\'.\ntidak dapat melakukan penghapusan\n")
                else:
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "a")
                    file_opener.close()
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                    check = file_opener.readline()
                    file_opener.close()
                    
                    if len(check) == 0:
                        print("\'tidak ada data dimasukkan\'.\ntidak dapat melakukan penghapusan\n")
                    else:
                        from_input_key = MODULEF.room_filter_one(input_key)
                        filt = MODULEF.checking_error_if_int_has_string(from_input_key)
                        if filt == "no":
                            print("[argument] tidak valid\n")
                        else:
                            deleted_number = int(from_input_key)
                            get_value_from_file = "empty"
                            length_value_from_file = 0
                            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                            while get_value_from_file != "":
                                get_value_from_file = file_opener.readline()
                                length_value_from_file += 1

                            length_value_from_file -= 1
                            data_on_files = []
                            for i in range(1, (length_value_from_file + 1)):
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "r")
                                data_on_files.append(file_opener.readlines())
                                file_opener.close()
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "w")
                                file_opener.close()

                            for i in range(1, (length_value_from_file + 1)):
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i}Z.bin", "a")
                                for o in range(0, len(data_on_files[i - 1])):
                                    if o == (deleted_number - 1) : continue
                                    file_opener.write(data_on_files[i - 1][o]) 
                                
                                file_opener.close()

                

                        # print(deleted_number)
                        # print(length_value_from_file)
                # ni delete method. Udah dapet input user tinggal logika ngehapus datanya aja.
                # itu deleted number cuma buat ngetes ⌓‿⌓

    def d2582006(self, inp):
        v = MODULEF.room_filter_one(inp)
        f = open("dook.bin", "r")
        g = f.readlines()
        f.close()
        f = open("dook.bin", "w")
        f.close()
        f = open("dook.bin", "a")
        b = False
        for i in range(0, len(g)):
            g2 = ""
            for o in range(0, len(MODULEF.readBin(g[i])) - 1):
                g2 += MODULEF.readBin(g[i])[o]
            if v == g2:
                import shutil
                shutil.rmtree(f"databases\\{v}.pkg")
                print("database berhasil dihapus\n")
                b = True
                continue
            f.write(MODULEF.writeBin(g2) + "\n")
        f.close()
        if b == True: 
            self.info_user_position_active = 0
            return
        else: print("database tidak ditemukan\n")

    def delete_head(self,input):
        if input[-1] != "]":
            print("terjadi kesalahan penulisan\n")
        else:
            if self.info_user_position_active == 0:
                print("tidak terkait database manapun\n")
            else:
                f = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                g = f.readlines()
                f.close()
                v_input = MODULEF.room_filter_one(input)
                if len(g) == 0:
                    print("anda belum membuat ruan-head\n")
                    return
                else:
                    f = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                    heads = f.readlines()
                    f.close()
                    datas = []    
                    for i in range(0, len(heads)):
                        file = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "r")
                        datas.append(file.readlines())
                        file.close()
                        file = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "w")
                        file.close()
                    print(datas)

                    f = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "w")
                    f.close()

                    f = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                    determinant_f = 0
                    for i in range(0, len(g)):
                        v_g = MODULEF.readBin_newVersion_valid(g[i])
                        if v_g == v_input:
                            print("head berhasil dihapus\n")
                            determinant_f = i
                            i += 1
                            continue
                        f.write(MODULEF.writeBin(v_g) + "\n")
                    f.close()

                    index = 1
                    for i in range(0, len(heads)):
                        file = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{index}Z.bin", "a")
                        if i == determinant_f : 
                            i += 1
                            continue

                        for o in range(0, len(datas[i])):
                            file.write(datas[i][o])
                        file.close()
                        index += 1

                    file.close()
                    os.remove(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{len(heads)}Z.bin")

    def update_line(self, key):
        if key[-1] != "]":
            print("terjadi kesalahan penulisan\n")
        else:
            if self.info_user_position_active == 0:
                print("tidak terkait database manapun\n")
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                get = file_opener.readline()
                file_opener.close()

                if len(get) != 0:
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "a")
                    file_opener.close()
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                    dtrmnt = file_opener.readline()
                    file_opener.close()

                    if len(dtrmnt) != 0:
                        key_coma = ""
                        line = MODULEF.room_filter_one(key)
                        int_scanning = MODULEF.checking_error_if_int_has_string(line)
                        if int_scanning == "yes":
                            for i in range(0, len(key)):
                                if key[i] == "]": break
                            for o in range(i + 1, len(key)):
                                key_coma += key[o]

                            shilter_new_data = MODULEF.room_filter_coma(key_coma)
                            line_point = int(line)

                            heads = []
                            datas = []
                            x = ""

                            for i in range(0, len(shilter_new_data)):
                                for o in range(0, len(shilter_new_data[i])):
                                    if shilter_new_data[i][o] == ":":
                                        heads.append(x)
                                        x = ""
                                        continue
                                    x += shilter_new_data[i][o]
                                datas.append(x)
                                x = ""

                            print(heads)
                            print(datas)

                            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                            get_file_opener = file_opener.readlines()
                            file_opener.close()

                            for i in range(0, len(heads)):
                                for o in range(0, len(get_file_opener)):
                                    if heads[i] == MODULEF.readBin_newVersion_valid(get_file_opener[o]):
                                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{o + 1}Z.bin", "r")
                                        g = file_opener.readlines()
                                        file_opener.close()
                                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{o + 1}Z.bin", "w")
                                        file_opener.close()
                                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{o + 1}Z.bin", "a")
                                        for altI in range(0, len(g)):
                                            if altI == (line_point - 1):
                                                file_opener.write(MODULEF.writeBin(datas[i]) + "\n")
                                                continue
                                            file_opener.write(g[altI])
                                        file_opener.close()
                        
                        else:
                            print(f"argument line \'[{line}]\' bukan integer\n")

                    else:
                        print("tidak ada data untuk di update\n")

                else:
                    print("anda belum membuat ruang-head\n")

    
    def add_before_after(self, key):
        if key[-1] != "]" :
            print("terjadi kesalahan penulisan\n")
        else:
            if self.info_user_position_active == 0:
                print("tidak terkait database manapun\n")
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                get = file_opener.readline()
                file_opener.close()

                if len(get) == 0:
                    print("anda belum membuat ruang-head\n")
                else:
                    scanning_int = MODULEF.checking_error_if_int_has_string(MODULEF.room_filter_one(key))
                    if scanning_int == "no":
                        print(f"argument line \'[{MODULEF.room_filter_coma(key)}]\' bukan integer\n")
                    else:

                        for i in range(0, len(key)):
                            if key[i] == "]": break
                        key2 = ""
                        for o in range(i + 1, len(key)):
                            key2 += key[o]

                        line_point = int(MODULEF.room_filter_one(key))
                        file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                        g = file_opener.readlines()
                        file_opener.close()

                        if len(g) < line_point:
                            self.add_data(key2)
                        
                        else:
                            datas_input = MODULEF.room_filter_coma(key2)
                            datas_output = []

                            file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                            heads = file_opener.readlines()
                            file_opener.close

                            for i in range(0, len(heads)):
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "r")
                                datas_output.append(file_opener.readlines())
                                file_opener.close()
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "w")
                                file_opener.close()
                            
                            befaf_point = ""
                            if "before" in key:
                                befaf_point = (line_point - 1) - 1
                            elif "after" in key:
                                befaf_point = (line_point - 1) + 1

                            for i in range(0, len(datas_output)):
                                for o in range(0, len(datas_output[i])):
                                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "a")
                                    if o == befaf_point:
                                        file_opener.write(MODULEF.writeBin(datas_input[i]) + "\n")
                                    file_opener.write(datas_output[i][o])
                            print("berhasil menambahkan data\n")

    def see_limitStarting(self, key):
        if key[-1] != "]":
            print("terjadi kesalahan penulisan\n")
        else:
            if self.info_user_position_active == 0:
                print("tidak terkait databases manapun\n")
            else:
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "a")
                file_opener.close()
                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\head.bin", "r")
                heads = file_opener.readlines()
                file_opener.close()
                if len(heads) == 0:
                    print("anda belum membuat ruang-head\n")
                else:
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "a")
                    file_opener.close()
                    file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#1Z.bin", "r")
                    get_file = file_opener.readline()
                    file_opener.close()
                    if len(get_file) == 0:
                        print("belum ada data dimasukkan\n")
                    else:

                        vrfy_key = "no"
                        linePoint_start = 0
                        linePoint_end = 0
                        if "see but starting from [" in key:
                            chk = MODULEF.room_filter_coma(key)
                            if len(chk) > 2 :
                                print("[argument] tidak valid\n")
                                return
                            for i in range(0, 2):
                                vrfy = MODULEF.checking_error_if_int_has_string(chk[i])
                                if vrfy == "no":
                                    print("[argument] tidak valid\n")
                                    return
                            linePoint_start += int(chk[0]) - 1
                            linePoint_end += int(chk[1])
                            vrfy_key = "yes"
                        else:
                            vrfy_key = MODULEF.checking_error_if_int_has_string(MODULEF.room_filter_one(key))
                            if vrfy_key == "yes":
                                linePoint_end = int(MODULEF.room_filter_one(key))

                            
                        if vrfy_key == "no":
                            print("[argument] tidak valid")

                        else:
                            filesData_bin = []
                            rightSpcs = []
                            closingan = "+"

                            for i in range(0, len(heads)):
                                file_opener = open(f"databases\\{self.info_user_position_active}.pkg\\data\\25-8#{i + 1}Z.bin", "r")
                                filesData_bin.append(file_opener.readlines())
                                file_opener.close()
                                rightSpcs.append(len(MODULEF.readBin_newVersion_valid(heads[i])))

                            if linePoint_end > len(filesData_bin[0]):
                                print("jumlah data tidak mencukupi..\n")
                            else:

                                for i in range(0, len(rightSpcs)):
                                    for o in range(linePoint_start, linePoint_end):
                                        if len(MODULEF.readBin_newVersion_valid(filesData_bin[i][o])) > rightSpcs[i]:
                                            rightSpcs[i] = len(MODULEF.readBin_newVersion_valid(filesData_bin[i][o]))
                                
                                if len(str(linePoint_end)) > rightSpcs[0]:
                                    rightSpcs[0] = len(str(linePoint_end))

                                headsVsl = "| ID" + " "*(len(str(len(filesData_bin)))) + "| "
                                closingan += "-"*3 + "-"*(len(str(len(filesData_bin)))) + "+"

                                for i in range(0, len(heads)):
                                    vsld = MODULEF.readBin_newVersion_valid(heads[i])
                                    headsVsl += vsld + " "*((rightSpcs[i] - len(vsld)) + 1) + "| "
                                    closingan += "-"*len(vsld) + "-"*(rightSpcs[i] - (len(vsld)) + 2) + "+" 

                                print(closingan)
                                print(headsVsl)
                                print(closingan)
                                
                                idSpc = 3
                                if len(str(linePoint_end)) >= 3:
                                    idSpc = len(str(linePoint_end))

                                for i in range(linePoint_start, linePoint_end):
                                    datasVsl = "| " + str(i + 1) + " "*(idSpc - len(str(i + 1))) + "| "
                                    for o in range(0, len(heads)):
                                        dvsl = MODULEF.readBin_newVersion_valid(filesData_bin[o][i])
                                        datasVsl += dvsl + " "*(rightSpcs[o] - (len(dvsl)) + 1) + "| "
                                    print(datasVsl)
                                
                                print(closingan)

    def rename_databases(self, key):
        file_opener = open("dook.bin", "r")
        get_file = file_opener.readlines()
        file_opener.close()
        for i in range(0, len(get_file)):
            if MODULEF.room_filter_one(key) == MODULEF.readBin_newVersion_valid(get_file[i]):
                pass









Do = Main()





set_key = [ "create database [",
            "show databases",
            "use [",
            "create head [",
            "add [",
            "see all",
            "delete line [",
            "d2582006 [",
            "delete head [",
            "update line [",
            "add before line [",
            "add after line [",
            "see but limit [",
            "see but starting from ["
            # next
]


connection_key_to_main = [Do.create_databases_all_foundation,
                          Do.show_databases_from_dook,
                          Do.use_database,
                          Do.create_head_plus_next,
                          Do.add_data,
                          Do.show_all_data,
                          Do.delete_line,
                          Do.d2582006,
                          Do.delete_head,
                          Do.update_line,
                          Do.add_before_after,
                          Do.add_before_after,
                          Do.see_limitStarting,
                          Do.see_limitStarting
                          # next


]












# LOGIC 
active = '\033[32m'
reset = '\033[0m'


command = f"<active [{Do.info_user_position_active}]> "


key_input = input(command)

while key_input != "quit":
    for i in range(0, len(set_key)):
        if set_key[i] in key_input:
            connection_key_to_main[i](key_input)
            key_input = "fined"
            
    if key_input != "fined":
        print("Kata kuci tidak tersedia\n")

    if Do.info_user_position_active != 0:
        command = f"<active [\033[32m{Do.info_user_position_active}\033[0m]> "
    else:
        command = f"<active [{Do.info_user_position_active}]> "
    key_input = input(command)


