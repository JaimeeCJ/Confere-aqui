import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import sqlite3
import leitura
from PIL import Image, ImageTk
from tkinter import Label, Button, Text, Toplevel, messagebox, ttk


class ConfereAqui:
    def __init__(self, root):
        self.root = root
        self.root.title("Confere Aqui!")
        self.root.iconbitmap(default="assets/logo/logo.ico")
        self.root.geometry("1280x768+36+-5")
        self.root.resizable(0, 0)

        self.load_images()
        self.create_main_screen()

    def load_images(self):
        self.background_img = tkinter.PhotoImage(file="assets/images/paginaresults.png")
        self.btn_return = tkinter.PhotoImage(file="assets/images/btnvoltarrs.png")
        self.img_btn_send = tkinter.PhotoImage(file="assets/images/enviarfotoimg.png")
        self.img_btn_send2 = tkinter.PhotoImage(file="assets/images/enviar2fotoimg.png")
        self.img_btn_result = tkinter.PhotoImage(file="assets/images/resultadofotoimg.png")
        self.backgroundimg = tkinter.PhotoImage(file="assets/images/fundotliinicio.png")
        self.fundo = tkinter.PhotoImage(file="assets/images/fundo.png")
        self.selectimagept2 = tkinter.PhotoImage(file="assets/images/enviarfotoimgpt2.png")
        self.resultadoimgpt2 = tkinter.PhotoImage(file="assets/images/resultadofotoimgpt2.png")
        self.camponomeimg = tkinter.PhotoImage(file="assets/images/camponome.png")
        self.btnsalvarimg = tkinter.PhotoImage(file="assets/images/salvarbtn.png")
        self.btnexcluirimg = tkinter.PhotoImage(file="assets/images/excluirbtn.png")
        self.letraax = tkinter.PhotoImage(file="assets/images/letraacerta.png")
        self.letrabx = tkinter.PhotoImage(file="assets/images/letrabcerta.png")
        self.letracx = tkinter.PhotoImage(file="assets/images/letraccerta.png")
        self.letradx = tkinter.PhotoImage(file="assets/images/letradcerta.png")
        self.letraex = tkinter.PhotoImage(file="assets/images/letraecerta.png")
        self.letraaass = tkinter.PhotoImage(file="assets/images/aass.png")
        self.letrabass = tkinter.PhotoImage(file="assets/images/bass.png")
        self.letracass = tkinter.PhotoImage(file="assets/images/cass.png")
        self.letradass = tkinter.PhotoImage(file="assets/images/dass.png")
        self.letraeass = tkinter.PhotoImage(file="assets/images/eass.png")
        self.letraa = tkinter.PhotoImage(file="assets/images/a.png")
        self.letrab = tkinter.PhotoImage(file="assets/images/b.png")
        self.letrac = tkinter.PhotoImage(file="assets/images/c.png")
        self.letrad = tkinter.PhotoImage(file="assets/images/d.png")
        self.letrae = tkinter.PhotoImage(file="assets/images/e.png")


    def create_main_screen(self):
        background_label = Label(self.root, image=self.backgroundimg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        btn_send_img = Button(self.root, image=self.img_btn_send, borderwidth=0, highlightthickness=0, bd=0,
                              activebackground="#145b98", cursor="hand2",
                              command=lambda: self.select_image(btn_send_img, btn_img_result))
        btn_send_img.place(x=390, y=310)

        btn_img_result = Button(self.root, image=self.img_btn_result, borderwidth=0, highlightthickness=0, bd=0,
                                  activebackground="#145b98", cursor="hand2", command=self.page_results)
        btn_img_result.place(x=445, y=430)

    def page_results(self):
        master3 = Toplevel(self.root)
        master3.title("Confere Aqui!")
        master3.iconbitmap(default="assets/logo/logo.ico")
        master3.geometry("1280x768+36+-5")
        master3.resizable(0, 0)
        master3.focus_force()

        background_label = Label(master3, image=self.background_img)
        background_label.image = self.background_img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        Button(master3, image=self.btn_return, activebackground="#6d8192", highlightthickness=0, bd=0,
               cursor="hand2", command=master3.destroy).place(x=1030, y=640)

        self.load_results(master3)

    def load_results(self, master):
        # Configura o estilo para Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        font=("Arial", 12),  # Define a fonte das células
                        rowheight=25,  # Altura das linhas
                        background="#f2f2f2",
                        fieldbackground="#f2f2f2")  # Cor de fundo
        style.configure("Treeview.Heading",
                        font=("Arial", 13, "bold"),  # Fonte dos cabeçalhos
                        background="#357ABD",
                        foreground="black")  # Cor do texto do cabeçalho
        style.map("Treeview.Heading",
                  background=[("active", "#1c6db1")])  # Cor ao passar o mouse no cabeçalho

        # Conecta ao banco de dados e busca os dados
        conn = sqlite3.connect('dbcorretor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id_result, nm_student, qty_score, qty_question, dt_result FROM tab_result")
        rows = cursor.fetchall()
        conn.close()

        # Cria o Treeview com as colunas
        tree = ttk.Treeview(master, columns=("ID", "Nome", "Qtd. correct_question", "Qtd. questões", "Data correção"),
                            show="headings", style="Treeview")

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Qtd. correct_question", text="Qtd. correct_question")
        tree.heading("Qtd. questões", text="Qtd. questões")
        tree.heading("Data correção", text="Data correção")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=200, anchor="w")
        tree.column("Qtd. correct_question", width=100, anchor="center")
        tree.column("Qtd. questões", width=100, anchor="center")
        tree.column("Data correção", width=100, anchor="center")

        # Configura alternância de cores nas linhas
        tree.tag_configure("oddrow", background="#ffffff")
        tree.tag_configure("evenrow", background="#d3d3d3")

        # Insere os dados com tags alternadas
        for i, row in enumerate(rows):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=row, tags=(tag,))

        # Adiciona a barra de rolagem ao Treeview
        scrollbar = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=1180, y=100, height=500)

        tree.place(x=100, y=100, width=1080, height=500)
    def select_image(self, btn_select, btn_result):
        global filename
        filename = askopenfilename()
        img = Image.open(filename)
        if img:
            self.display_image_preview(filename, img, btn_select, btn_result)

    def display_image_preview(self, filename, img, btn_select, btn_result):
        label_img_path = Label(self.root, text=f"{filename} Selecionada", bg="#88a3ba", fg="white",
                               borderwidth=7, highlightthickness=0)
        label_img_path.place(x=810, y=270)

        btn_select.config(image=self.selectimagept2)
        btn_result.config(image=self.resultadoimgpt2)
        btn_select.place(x=60, y=300)
        btn_result.place(x=60, y=450)

        resized_image = img.resize((400, 405), Image.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)
        label_preview = Label(self.root, image=new_image)
        label_preview.image = new_image
        label_preview.place(x=810, y=300)

        Button(self.root, image=self.img_btn_send2, borderwidth=0, highlightthickness=0, bd=0,
               activebackground="#145b98", cursor="hand2", command=self.load_result_window).place(x=695, y=670)

    def load_result_window(self):
        def return_window():
            result_window.destroy()
        def save_db(correct_question, questions, nm_student):
            return_window()
            #nm_student = camponome.get("1.0", "end-1c")
            self.save_result(nm_student, correct_question, questions)
        # Configuração inicial da janela
        result_window = Toplevel(self.root)
        result_window.title("Resultado")
        result_window.geometry("1280x768+36+-5")
        result_window.resizable(0, 0)

        # Background
        background_label = Label(result_window, image=self.fundo)
        background_label.image = self.fundo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Definindo valores
        total_question = 25
        answer = [0, 2, 1, 2, 0, 0, 2, 1, 3, 3, 2, 2, 1, 1, 2, 2, 1, 3, 4, 2, 1, 2, 1, 1, 2]
        global myindex
        myindex = leitura.start_reading(filename)
        score = [1 if answer[x] == myindex[x] else 0 for x in range(total_question)]
        scoreporcent = (sum(score) / total_question) * 100
        correct_question = sum(score)

        # Configuração de Labels e botões principais
        self.create_label(result_window, '{0}{1}'.format(scoreporcent, '%'), (510, 595), "#51728b", "Cambria 30")
        self.create_label(result_window, '{0}{1}'.format(correct_question, '/25'), (520, 505), "#6d8192", "Cambria 25")

        self.create_button(result_window, image=self.btnexcluirimg, pos=(450, 290), command=return_window)
        self.create_button(result_window, image=self.btnsalvarimg, pos=(450, 180),
                      command=lambda: save_db(correct_question, total_question, txt_name.get("1.0", "end-1c")))

        # Campo de texto
        txt_name = Text(result_window, height=1, width=43, bg="#88a3ba", font="Cambria 25", fg="white")
        txt_name.place(x=452, y=60)

        # Função para criar botões de resposta
        buttons = []
        for i in range(total_question):
            self.create_response_buttons(result_window, i, answer, buttons)
            self.create_question_number_label(result_window, i)

    def create_label(self, window, text, pos, bg, font):
        label = Label(window, text=text, bg=bg, fg="white", font=font)
        label.place(x=pos[0], y=pos[1])
        return label

    def create_button(self, window, image, pos, command):
        button = Button(window, image=image, borderwidth=0, highlightthickness=0, cursor="hand2", command=command)
        button.image = image
        button.place(x=pos[0], y=pos[1])
        return button

    def create_question_number_label(self, window, index):
        lbl_number = Label(window, text=f'{index + 1} -', bg="#1b6baf", fg="white", font="Cambria")
        lbl_number.grid(row=index + 1, column=1, padx=(10, 0))

    def create_response_buttons(self, window, index, answer, buttons):
        x = 0
        row = index
        options = [self.letraa, self.letrab, self.letrac, self.letrad, self.letrae]
        selected_options = [self.letraax, self.letrabx, self.letracx, self.letradx, self.letraex]
        student_options = [self.letraaass, self.letrabass, self.letracass, self.letradass, self.letraeass]


        for i, option in enumerate(options):
            is_selected = (answer[row] == i)
            image = selected_options[i] if is_selected else option
            button = Button(
                window, image=image, activebackground="#1b6aae", highlightthickness=0, bd=0, cursor="hand2",
                command=lambda count=len(buttons), row=row, x=i: self.change_answer(count, row, x, answer, buttons)
            )
            button.grid(row=row + 1, column=x + 1, padx=(80 if i == 0 else 0, 0))
            buttons.append(button)

            if answer[row] != myindex[row] and myindex[row] == i:
                button_student = Button(window, image=student_options[i], activebackground="#1b6aae", highlightthickness=0, bd=0,
                                     cursor="hand2")
                button_student.image = student_options[i]
                button_student.grid(row=row + 1, column=x + 1)

            x += 1

    def change_answer(self, v, row, x, answer, buttons):
        # Atualiza a resposta do aluno
        answer[row] = x
        k = row * 5
        # Reseta as imagens dos botões de opções
        for i in range(5):
            buttons[k + i].configure(image=[self.letraa, self.letrab, self.letrac, self.letrad, self.letrae][i])
        # Define a imagem do botão selecionado
        buttons[v].configure(image=[self.letraax, self.letrabx, self.letracx, self.letradx, self.letraex][x])

    def save_result(self, nm_student, correct_question, total_question):
        try:
            conn = sqlite3.connect('dbcorretor.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO tab_result (nm_student, qty_score, qty_question) VALUES (?, ?, ?)",
                           (nm_student, correct_question, total_question))
            conn.commit()
            conn.close()

            messagebox.showinfo("Sucesso", f"Resultado salvo com sucesso! \nEstudante:{nm_student} ")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {e}")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = ConfereAqui(root)
    root.mainloop()