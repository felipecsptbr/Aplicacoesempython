import requests
import json
import tkinter as tk
from tkinter import messagebox, font as tkFont
from PIL import Image, ImageTk
import io

API_KEY = "API KEY"


def requisicao(titulo):
    try:
        req = requests.get(
            "http://www.omdbapi.com/", params={"apikey": API_KEY, "t": titulo}
        )
        return req.json()
    except:
        messagebox.showerror("Erro", "Erro na conexão")
        return None


def get_movie_poster(url):
    response = requests.get(url)
    return Image.open(io.BytesIO(response.content))


def display_movie_details(movie):
    details_window = tk.Toplevel()
    details_window.title("Detalhes do Filme")
    details_window.geometry("500x680")

    if "Poster" in movie and movie["Poster"] != "N/A":
        poster_image = get_movie_poster(movie["Poster"])
        poster_photo = ImageTk.PhotoImage(poster_image)
        tk.Label(details_window, image=poster_photo).pack(pady=10)
        details_window.poster_photo = poster_photo

    tk.Label(
        details_window, text=f'Título: {movie.get("Title", "N/A")}', font=default_font
    ).pack(pady=5)
    tk.Label(
        details_window, text=f'Ano: {movie.get("Year", "N/A")}', font=default_font
    ).pack(pady=5)
    tk.Label(
        details_window,
        text=f'Diretor: {movie.get("Director", "N/A")}',
        font=default_font,
    ).pack(pady=5)
    tk.Label(
        details_window, text=f'Atores: {movie.get("Actors", "N/A")}', font=default_font
    ).pack(pady=5)
    tk.Label(
        details_window,
        text=f'Nota: {movie.get("imdbRating", "N/A")}',
        font=default_font,
    ).pack(pady=5)


def search_movie():
    movie_name = movie_name_entry.get()
    if not movie_name:
        messagebox.showinfo("Info", "Por favor, insira o nome do filme")
        return

    movie = requisicao(movie_name)
    if movie and movie["Response"] != "False":
        display_movie_details(movie)
    else:
        messagebox.showerror("Erro", "Filme não encontrado")


def show_movie_search_window():
    global movie_name_entry, default_font

    movie_window = tk.Tk()
    movie_window.title(
        "CineSearcher - Consulte informações como: Título, Ano, Diretor, Atores e Nota"
    )
    movie_window.geometry("450x400")

    # Definindo uma fonte padrão para a GUI após a criação da janela raiz
    default_font = tkFont.Font(family="Helvetica", size=11)

    # Carregando e exibindo a imagem de fundo
    image = Image.open("images-removebg-preview.png")
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(movie_window, image=photo)
    background_label.place(relwidth=1, relheight=1)

    tk.Label(movie_window, text="Nome do Filme:", font=default_font).pack(pady=10)
    movie_name_entry = tk.Entry(movie_window, font=default_font)
    movie_name_entry.pack(pady=10)

    tk.Button(
        movie_window, text="Buscar", command=search_movie, font=default_font
    ).pack(pady=10)

    movie_window.mainloop()


# Iniciando diretamente a janela de consulta de filmes
show_movie_search_window()
