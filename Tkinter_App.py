import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time

class MysticProdiApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.setup_layout()
        self.add_mystical_effects()
        
    def setup_window(self):
        """Setup window with mystical theme"""
        self.root.title("🔮 Ramalan Nasib Program Studi - Crystal Ball Predictor")
        self.root.geometry("700x900")
        
        # Dark mystical gradient background
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(True, True)
        
        # Center window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def setup_styles(self):
        """Setup mystical styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Mystical button style
        self.style.configure('Mystical.TButton',
                           font=('Papyrus', 14, 'bold'),
                           padding=(25, 15),
                           background='#4a148c',
                           foreground='#ffd700',
                           borderwidth=2,
                           relief='raised')
        
        # Magical entry style
        self.style.configure('Magic.TEntry',
                           font=('Georgia', 11),
                           padding=8,
                           fieldbackground='#2e1065',
                           foreground='#e1bee7',
                           borderwidth=2,
                           relief='groove')
                           
        # Mystical title style
        self.style.configure('MysticTitle.TLabel',
                           font=('Papyrus', 20, 'bold'),
                           background='#1a1a2e',
                           foreground='#ffd700')
                           
        # Oracle subtitle style
        self.style.configure('Oracle.TLabel',
                           font=('Georgia', 12, 'italic'),
                           background='#1a1a2e',
                           foreground='#e1bee7')
                           
        # Crystal result style
        self.style.configure('Crystal.TLabel',
                           font=('Papyrus', 16, 'bold'),
                           background='#4a148c',
                           foreground='#ffd700',
                           padding=20,
                           relief='raised',
                           borderwidth=3)

    def create_widgets(self):
        """Create mystical widgets"""
        # Main mystical frame
        self.main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=40, pady=30)
        
        # Mystical title with crystal ball
        self.title_label = ttk.Label(
            self.main_frame, 
            text="🔮 RAMALAN NASIB PROGRAM STUDI 🔮",
            style='MysticTitle.TLabel'
        )
        
        # Oracle subtitle
        self.subtitle_label = ttk.Label(
            self.main_frame,
            text="✨ Masukkan nilai spiritual mata pelajaranmu, wahai pencari ilmu ✨\n🌟 Kristal ajaib akan meramal masa depan akademikmu 🌟",
            style='Oracle.TLabel',
            justify='center'
        )
        
        # Mystical input frame with gradient effect
        self.input_frame = tk.Frame(self.main_frame, bg='#16213e', 
                                   relief='ridge', bd=4, padx=30, pady=25)
        
        # Add mystical border
        border_frame = tk.Frame(self.input_frame, bg='#4a148c', height=3)
        border_frame.pack(fill='x', pady=(0, 15))
        
        # Subject names with mystical theme
        self.subjects = [
            "🔢 Matematika Mistik", "⚛️ Fisika Gaib", "🧪 Kimia Alkemis", 
            "🌿 Biologi Herbal", "📜 Bahasa Nusantara",
            "🗣️ Bahasa Asing", "⏳ Sejarah Kuno", "🗺️ Geografi Mistis", 
            "💰 Ekonomi Ramalan", "👥 Sosiologi Spiritual"
        ]
        
        self.entries = {}
        self.create_mystical_inputs()
        
        # Mystical predict button
        self.predict_button = ttk.Button(
            self.main_frame,
            text="🔮 RAMALKAN NASIBKU! 🔮",
            command=self.divine_prediction,
            style='Mystical.TButton'
        )
        
        # Fortune telling area
        self.fortune_frame = tk.Frame(self.main_frame, bg='#1a1a2e')
        
        # Mystical loading label
        self.loading_label = ttk.Label(
            self.fortune_frame,
            text="",
            style='Oracle.TLabel'
        )
        
    def create_mystical_inputs(self):
        """Create mystical input fields"""
        for i, subject in enumerate(self.subjects):
            # Mystical subject frame
            subject_frame = tk.Frame(self.input_frame, bg='#16213e')
            
            # Glowing subject label
            subject_label = tk.Label(
                subject_frame,
                text=subject,
                font=('Georgia', 11, 'bold'),
                bg='#16213e',
                fg='#e1bee7',
                width=25,
                anchor='w'
            )
            
            # Magical entry
            entry_var = tk.StringVar()
            entry = ttk.Entry(
                subject_frame,
                textvariable=entry_var,
                style='Magic.TEntry',
                width=12,
                justify='center'
            )
            
            # Add mystical validation
            entry.configure(validate='key', 
                          validatecommand=(self.root.register(self.validate_mystical_input), '%P'))
            
            # Store in mystical grimoire
            self.entries[subject] = entry_var
            
            # Enchanted layout
            subject_label.pack(side='left', padx=(0, 15))
            entry.pack(side='right', padx=5)
            subject_frame.pack(fill='x', pady=5)
            
    def validate_mystical_input(self, value):
        """Validate mystical input"""
        if value == "":
            return True
        try:
            mystical_val = float(value)
            return 0 <= mystical_val <= 100
        except ValueError:
            return False
    
    def setup_layout(self):
        """Setup mystical layout"""
        self.main_frame.pack(fill='both', expand=True)
        
        self.title_label.pack(pady=(0, 15))
        self.subtitle_label.pack(pady=(0, 25))
        
        self.input_frame.pack(fill='x', pady=(0, 30))
        
        self.predict_button.pack(pady=20)
        
        self.fortune_frame.pack(fill='x', pady=(15, 0))
        self.loading_label.pack(fill='x')
        
    def add_mystical_effects(self):
        """Add mystical background effects"""
        # Create floating mystical symbols
        self.create_floating_symbols()
        
    def create_floating_symbols(self):
        """Create floating mystical symbols"""
        symbols = ["✨", "🌟", "⭐", "💫", "🔮", "🌙", "⚡"]
        
        def animate_symbol():
            symbol = random.choice(symbols)
            x = random.randint(50, 650)
            y = random.randint(100, 800)
            
            symbol_label = tk.Label(
                self.root, 
                text=symbol, 
                bg='#1a1a2e', 
                fg='#ffd700',
                font=('Arial', random.randint(12, 20))
            )
            symbol_label.place(x=x, y=y)
            
            # Animate floating
            def float_up(current_y, alpha=1.0):
                if current_y > -50 and alpha > 0:
                    symbol_label.place(y=current_y - 2)
                    self.root.after(100, lambda: float_up(current_y - 2, alpha - 0.02))
                else:
                    symbol_label.destroy()
            
            float_up(y)
            
        # Schedule next symbol
        self.root.after(random.randint(2000, 5000), animate_symbol)
        animate_symbol()  # Start first symbol
    
    def divine_prediction(self):
        """Divine the mystical prediction"""
        # Check mystical energy levels
        filled_fields = sum(1 for entry_var in self.entries.values() if entry_var.get().strip())
        
        if filled_fields == 0:
            self.show_mystical_warning()
            return
        
        # Begin mystical ritual
        self.mystical_loading_ritual()
    
    def show_mystical_warning(self):
        """Show mystical warning"""
        warning_window = tk.Toplevel(self.root)
        warning_window.title("🔮 Peringatan Spiritual")
        warning_window.geometry("400x200")
        warning_window.configure(bg='#4a148c')
        warning_window.transient(self.root)
        warning_window.grab_set()
        
        # Center warning
        warning_window.update_idletasks()
        x = (warning_window.winfo_screenwidth() // 2) - (400 // 2)
        y = (warning_window.winfo_screenheight() // 2) - (200 // 2)
        warning_window.geometry(f"400x200+{x}+{y}")
        
        warning_label = tk.Label(
            warning_window,
            text="⚠️ ENERGI SPIRITUAL KURANG! ⚠️\n\n🔮 Masukkan setidaknya satu nilai\nagar kristal dapat meramal nasibmu\n\n✨ Tanpa energi, ramalan tak dapat dimulai ✨",
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 12, 'bold'),
            justify='center'
        )
        warning_label.pack(expand=True)
        
        ok_button = tk.Button(
            warning_window,
            text="🙏 SAYA MENGERTI",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 10, 'bold'),
            command=warning_window.destroy,
            padx=20,
            pady=5
        )
        ok_button.pack(pady=10)
    
    def mystical_loading_ritual(self):
        """Perform mystical loading ritual"""
        ritual_texts = [
            "🔮 Menghubungi roh peramal kuno...",
            "✨ Mengaktifkan kristal ajaib...",
            "🌟 Membaca garis takdir...",
            "🌙 Menganalisis energi spiritual...",
            "⚡ Memanggil oracle digital...",
            "💫 Menenun benang nasib..."
        ]
        
        def ritual_animation(index=0, dot_count=0):
            if index < len(ritual_texts):
                dots = "." * (dot_count % 4)
                text = ritual_texts[index] + dots
                self.loading_label.configure(text=text)
                
                if dot_count < 6:
                    self.root.after(300, lambda: ritual_animation(index, dot_count + 1))
                else:
                    self.root.after(500, lambda: ritual_animation(index + 1, 0))
            else:
                self.root.after(1000, self.reveal_mystical_destiny)
        
        ritual_animation()
    
    def reveal_mystical_destiny(self):
        """Reveal the mystical destiny with sweet alert popup"""
        self.loading_label.configure(text="")
        
        # Calculate mystical average
        total = sum(float(entry_var.get()) for entry_var in self.entries.values() 
                   if entry_var.get().strip())
        count = sum(1 for entry_var in self.entries.values() if entry_var.get().strip())
        average = total / count if count > 0 else 0
        
        # Create mystical popup
        self.create_mystical_popup(average, count)
    
    def create_mystical_popup(self, average, count):
        """Create beautiful mystical popup like sweet alert"""
        popup = tk.Toplevel(self.root)
        popup.title("🔮 Ramalan Takdir Terungkap")
        popup.geometry("500x600")
        popup.configure(bg='#1a1a2e')
        popup.transient(self.root)
        popup.grab_set()
        popup.resizable(False, False)
        
        # Center popup
        popup.update_idletasks()
        x = (popup.winfo_screenwidth() // 2) - (500 // 2)
        y = (popup.winfo_screenheight() // 2) - (600 // 2)
        popup.geometry(f"500x600+{x}+{y}")
        
        # Mystical border
        border_frame = tk.Frame(popup, bg='#ffd700', height=5)
        border_frame.pack(fill='x')
        
        # Main content frame
        content_frame = tk.Frame(popup, bg='#1a1a2e', padx=30, pady=30)
        content_frame.pack(fill='both', expand=True)
        
        # Animated crystal ball
        crystal_label = tk.Label(
            content_frame,
            text="🔮",
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Arial', 60)
        )
        crystal_label.pack(pady=(0, 20))
        
        # Destiny revealed title
        title_label = tk.Label(
            content_frame,
            text="✨ TAKDIR TERUNGKAP! ✨",
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Papyrus', 18, 'bold')
        )
        title_label.pack(pady=(0, 15))
        
        # Mystical result frame
        result_frame = tk.Frame(content_frame, bg='#4a148c', relief='raised', bd=3, padx=20, pady=20)
        result_frame.pack(fill='x', pady=(0, 20))
        
        # Main prediction
        prediction_label = tk.Label(
            result_frame,
            text="🎯 PROGRAM STUDI TAKDIRMU:\n\n💻 TEKNOLOGI INFORMASI 💻",
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 16, 'bold'),
            justify='center'
        )
        prediction_label.pack()
        
        # Mystical details
        details_text = f"🌟 Energi Spiritual: {average:.1f}/100\n"
        details_text += f"📊 Mata Pelajaran Teraktivasi: {count}/10\n"
        details_text += f"🔮 Tingkat Kepercayaan: 99.9%\n\n"
        details_text += "💫 RAMALAN ORACLE:\n"
        details_text += '"Bintang-bintang berbisik tentang masa\n'
        details_text += 'depanmu di dunia digital. Teknologi akan\n'
        details_text += 'menjadi tongkat sihirmu untuk mengubah dunia!"'
        
        details_label = tk.Label(
            content_frame,
            text=details_text,
            bg='#1a1a2e',
            fg='#e1bee7',
            font=('Georgia', 11),
            justify='center'
        )
        details_label.pack(pady=(0, 20))
        
        # Action buttons frame
        button_frame = tk.Frame(content_frame, bg='#1a1a2e')
        button_frame.pack(fill='x')
        
        # Accept destiny button
        accept_button = tk.Button(
            button_frame,
            text="🙏 TERIMA TAKDIR",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 12, 'bold'),
            command=popup.destroy,
            padx=20,
            pady=8,
            relief='raised',
            bd=2
        )
        accept_button.pack(side='left', padx=(0, 10), expand=True, fill='x')
        
        # Ramal again button
        again_button = tk.Button(
            button_frame,
            text="🔮 RAMAL LAGI",
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 12, 'bold'),
            command=lambda: [popup.destroy(), self.clear_mystical_inputs()],
            padx=20,
            pady=8,
            relief='raised',
            bd=2
        )
        again_button.pack(side='right', expand=True, fill='x')
        
        # Add sparkle animation to crystal ball
        self.animate_crystal(crystal_label)
        
        # Play mystical sound effect (visual representation)
        self.mystical_sound_effect(popup)
    
    def animate_crystal(self, crystal_label):
        """Animate the crystal ball"""
        crystals = ["🔮", "💎", "🌟", "✨"]
        current = 0
        
        def rotate_crystal():
            nonlocal current
            crystal_label.configure(text=crystals[current % len(crystals)])
            current += 1
            crystal_label.after(500, rotate_crystal)
        
        rotate_crystal()
    
    def mystical_sound_effect(self, popup):
        """Visual sound effect"""
        sound_frame = tk.Frame(popup, bg='#1a1a2e')
        sound_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        sound_label = tk.Label(
            sound_frame,
            text="🎵 ♪ ♫ ♪ ♫ ♪ 🎵",
            bg='#1a1a2e',
            fg='#ffd700',
            font=('Arial', 14)
        )
        sound_label.pack(expand=True)
        
        def fade_sound():
            sound_frame.destroy()
        
        popup.after(2000, fade_sound)
    
    def clear_mystical_inputs(self):
        """Clear all mystical inputs"""
        for entry_var in self.entries.values():
            entry_var.set("")

def main():
    """Summon the mystical application"""
    root = tk.Tk()
    app = MysticProdiApp(root)
    
    # Mystical shortcuts
    root.bind('<Return>', lambda e: app.predict_button.invoke())
    root.bind('<Control-q>', lambda e: root.quit())
    root.bind('<Escape>', lambda e: root.quit())
    
    # Mystical welcome
    def show_mystical_welcome():
        welcome = tk.Toplevel(root)
        welcome.title("🔮 Selamat Datang ke Dunia Mistis")
        welcome.geometry("450x300")
        welcome.configure(bg='#4a148c')
        welcome.transient(root)
        welcome.grab_set()
        
        # Center welcome
        welcome.update_idletasks()
        x = (welcome.winfo_screenwidth() // 2) - (450 // 2)
        y = (welcome.winfo_screenheight() // 2) - (300 // 2)
        welcome.geometry(f"450x300+{x}+{y}")
        
        welcome_text = """🔮 SELAMAT DATANG, PENCARI TAKDIR! 🔮

✨ Aplikasi ramalan ini akan mengungkap
program studi yang ditakdirkan untukmu ✨

🌟 PANDUAN MYSTIS:
• Masukkan nilai spiritual (0-100)
• Tekan Enter untuk ramalan instan
• ESC untuk meninggalkan dunia mistis

🔥 Bersiaplah untuk menyaksikan keajaiban! 🔥"""
        
        label = tk.Label(
            welcome,
            text=welcome_text,
            bg='#4a148c',
            fg='#ffd700',
            font=('Papyrus', 11, 'bold'),
            justify='center'
        )
        label.pack(expand=True)
        
        ok_btn = tk.Button(
            welcome,
            text="🚀 MULAI PERJALANAN MISTIS!",
            bg='#ffd700',
            fg='#4a148c',
            font=('Papyrus', 10, 'bold'),
            command=welcome.destroy,
            pady=5
        )
        ok_btn.pack(pady=10)
    
    root.after(800, show_mystical_welcome)
    root.mainloop()

if __name__ == "__main__":
    main()