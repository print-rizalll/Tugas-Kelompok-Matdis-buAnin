"""
Program Kalkulator Permutasi & Kombinasi Interaktif
Dilengkapi dengan penampil seluruh susunan / kombinasi lengkap menggunakan library 'rich'.
"""

import math
import itertools
import sys
from typing import List, Any

# Memastikan encoding terminal mendukung UTF-8 di Windows
if sys.platform == "win32":
    try:
        if sys.stdout.encoding.lower() != "utf-8":
            sys.stdout.reconfigure(encoding="utf-8")
        if sys.stderr.encoding.lower() != "utf-8":
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt, IntPrompt, Confirm
    from rich import box
except ImportError:
    print("[ERROR] Library 'rich' belum terpasang.")
    print("Silakan jalankan perintah: pip install rich")
    sys.exit(1)

console = Console()

def print_header():
    """Menampilkan header / judul aplikasi."""
    title_text = Text("KALKULATOR PERMUTASI & KOMBINASI", style="bold cyan")
    subtitle_text = Text("Hitung Rumus + Tampilkan Seluruh Susunan Lengkap", style="italic yellow")
    panel = Panel(
        Text.assemble(title_text, "\n", subtitle_text, justify="center"),
        box=box.DOUBLE_EDGE,
        border_style="bright_blue",
        padding=(1, 2),
    )
    console.print(panel)

def input_elements() -> List[str]:
    """Mendapatkan daftar elemen dari pengguna."""
    console.print("\n[bold green]Pilihan Input Elemen:[/bold green]")
    console.print("  [1] Masukkan nama / simbol elemen sendiri (contoh: A, B, C atau Apel, Jeruk, Mangga)")
    console.print("  [2] Masukkan jumlah elemen n saja (otomatis: 1, 2, 3, ... atau A, B, C, ...)")

    choice = Prompt.ask("Pilih metode input", choices=["1", "2"], default="1")

    if choice == "1":
        raw_input = Prompt.ask(
            "[bold]Masukkan elemen[/bold] (pisahkan dengan koma atau spasi)"
        )
        # Pisahkan berdasarkan koma jika ada, atau spasi
        if "," in raw_input:
            elements = [item.strip() for item in raw_input.split(",") if item.strip()]
        else:
            elements = [item.strip() for item in raw_input.split() if item.strip()]

        if not elements:
            console.print("[red]Input tidak boleh kosong! Menggunakan default [A, B, C].[/red]")
            elements = ["A", "B", "C"]
        return elements
    else:
        n = IntPrompt.ask("[bold]Masukkan nilai n (jumlah elemen)[/bold]", default=4)
        while n <= 0:
            console.print("[red]Nilai n harus lebih besar dari 0.[/red]")
            n = IntPrompt.ask("[bold]Masukkan nilai n[/bold]", default=4)

        if n <= 26:
            # Gunakan alfabet A, B, C, ...
            elements = [chr(65 + i) for i in range(n)]
        else:
            # Gunakan angka 1, 2, 3, ...
            elements = [str(i + 1) for i in range(n)]
        return elements

def display_arrangements(title: str, items: List[tuple], max_display: int = 200):
    """Menampilkan daftar kemungkinan susunan dalam bentuk tabel/grid yang rapi."""
    total = len(items)
    
    if total == 0:
        console.print("[yellow]Tidak ada susunan yang dihasilkan.[/yellow]")
        return

    # Jika item sangat banyak, beri opsi untuk membatasi tampilan agar terminal tidak membeku
    display_items = items
    is_truncated = False
    if total > max_display:
        show_all = Confirm.ask(
            f"[yellow]Jumlah kemungkinan sangat besar ({total:,} susunan). Tampilkan semua?[/yellow]",
            default=False
        )
        if not show_all:
            display_items = items[:max_display]
            is_truncated = True

    # Hitung lebar rata-rata item agar tata letak kolom proporsional
    sample_items = [", ".join(map(str, x)) for x in display_items[:50]]
    max_item_len = max((len(s) for s in sample_items), default=6) + 4
    unit_width = max(max_item_len + 8, 18)
    term_width = console.width if console.width else 80
    num_columns = max(1, min(4, term_width // unit_width))

    table = Table(
        title=f"[bold green]{title} (Total: {total:,})[/bold green]",
        box=box.ROUNDED,
        border_style="magenta",
        header_style="bold cyan",
        show_lines=False,
    )

    for col_idx in range(num_columns):
        table.add_column("No.", justify="right", style="dim", no_wrap=True)
        table.add_column("Susunan", justify="center", style="bold white", no_wrap=True)

    # Siapkan baris-baris data
    rows = []
    current_row = []
    for idx, item in enumerate(display_items, start=1):
        formatted_item = ", ".join(map(str, item))
        current_row.extend([f"{idx}.", f"({formatted_item})"])
        if len(current_row) == num_columns * 2:
            rows.append(current_row)
            current_row = []

    if current_row:
        # Isi sisa kolom yang kosong
        while len(current_row) < num_columns * 2:
            current_row.extend(["", ""])
        rows.append(current_row)

    for row in rows:
        table.add_row(*row)

    console.print(table)

    if is_truncated:
        console.print(
            f"[dim italic]* Menampilkan {max_display} dari {total:,} susunan. Selebihnya disembunyikan untuk menjaga performa terminal.[/dim italic]\n"
        )

def process_permutation(elements: List[str], r: int):
    """Menghitung dan menampilkan permutasi."""
    n = len(elements)
    total_perm = math.perm(n, r)

    # Panel Ringkasan
    summary_text = (
        f"[bold cyan]Definisi:[/bold cyan] Urutan [italic]diperhatikan[/italic] (AB != BA)\n"
        f"[bold cyan]Himpunan Elemen (n={n}):[/bold cyan] {{{', '.join(elements)}}}\n"
        f"[bold cyan]Ukuran Susunan (r):[/bold cyan] {r}\n"
        f"[bold cyan]Rumus:[/bold cyan] P(n, r) = n! / (n - r)!\n"
        f"[bold cyan]Perhitungan:[/bold cyan] P({n}, {r}) = {n}! / ({n} - {r})! = [bold green]{total_perm:,}[/bold green] cara"
    )
    console.print(Panel(summary_text, title="[bold]Ringkasan Permutasi P(n, r)[/bold]", border_style="cyan"))

    # Generate kemungkinan
    arrangements = list(itertools.permutations(elements, r))
    display_arrangements(f"Daftar Seluruh Kemungkinan Permutasi P({n}, {r})", arrangements)

def process_combination(elements: List[str], r: int):
    """Menghitung dan menampilkan kombinasi."""
    n = len(elements)
    total_comb = math.comb(n, r)

    # Panel Ringkasan
    summary_text = (
        f"[bold yellow]Definisi:[/bold yellow] Urutan [italic]TIDAK diperhatikan[/italic] (AB = BA)\n"
        f"[bold yellow]Himpunan Elemen (n={n}):[/bold yellow] {{{', '.join(elements)}}}\n"
        f"[bold yellow]Ukuran Pilihan (r):[/bold yellow] {r}\n"
        f"[bold yellow]Rumus:[/bold yellow] C(n, r) = n! / (r! x (n - r)!)\n"
        f"[bold yellow]Perhitungan:[/bold yellow] C({n}, {r}) = {n}! / ({r}! x ({n} - {r})!) = [bold green]{total_comb:,}[/bold green] cara"
    )
    console.print(Panel(summary_text, title="[bold]Ringkasan Kombinasi C(n, r)[/bold]", border_style="yellow"))

    # Generate kemungkinan
    arrangements = list(itertools.combinations(elements, r))
    display_arrangements(f"Daftar Seluruh Kemungkinan Kombinasi C({n}, {r})", arrangements)

def main():
    while True:
        console.clear()
        print_header()

        console.print("[bold]Menu Utama:[/bold]")
        console.print("  [1] Hitung [cyan]Permutasi P(n, r)[/cyan]")
        console.print("  [2] Hitung [yellow]Kombinasi C(n, r)[/yellow]")
        console.print("  [3] Hitung [magenta]Keduanya Sekaligus (Komparasi)[/magenta]")
        console.print("  [4] Keluar")

        choice = Prompt.ask("\nPilih opsi", choices=["1", "2", "3", "4"], default="1")

        if choice == "4":
            console.print("\n[bold cyan]Terima kasih telah menggunakan program ini! Sampai jumpa![/bold cyan]")
            break

        elements = input_elements()
        n = len(elements)
        console.print(f"\n[green]Elemen yang digunakan (n = {n}):[/green] [bold]{elements}[/bold]")

        r = IntPrompt.ask(f"Masukkan nilai r (1 sampai {n})", default=min(2, n))
        while r < 1 or r > n:
            console.print(f"[red]Nilai r harus antara 1 dan {n}.[/red]")
            r = IntPrompt.ask(f"Masukkan nilai r (1 sampai {n})", default=min(2, n))

        console.print()
        if choice == "1":
            process_permutation(elements, r)
        elif choice == "2":
            process_combination(elements, r)
        elif choice == "3":
            process_permutation(elements, r)
            console.print()
            process_combination(elements, r)

        console.print("\n" + "=" * 60)
        ulang = Confirm.ask("Apakah Anda ingin melakukan perhitungan lagi?", default=True)
        if not ulang:
            console.print("\n[bold cyan]Terima kasih telah menggunakan program ini! Sampai jumpa![/bold cyan]")
            break

if __name__ == "__main__":
    main()
