import tkinter as tk
import webbrowser

episodes = {
    "Film 1": {
        "Episode 1": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view",
        "Episode 2": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view",
        "Episode 3": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view"
    },
    "Film 2": {
        "Episode 1": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view",
        "Episode 2": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view",
        "Episode 3": "https://drive.google.com/file/d/1l27RRPsbQWAwp2iz4PBBcxmQmxrhuM_0/view"
    }

}

def show_episodes(film):

    episode_list.delete(0, tk.END)
    for episode, video_url in episodes[film].items():
        episode_list.insert(tk.END, f"{episode}: {video_url}")

def play_video(video_url):

    webbrowser.open(video_url)

def go_back():

    episode_list.delete(0, tk.END)
    film_list.pack()
    back_button.pack_forget()

window = tk.Tk()
window.geometry("1280x720")  

film_list = tk.Listbox(window)
for film in episodes.keys():
    film_list.insert(tk.END, film)
film_list.pack()

episode_list = tk.Listbox(window)
episode_list.pack()


back_button = tk.Button(window, text="Back", command=go_back)

video_frame = tk.Frame(window, width=1280, height=720)
video_frame.pack_propagate(0) 
video_frame.pack()

film_list.bind("<<ListboxSelect>>", lambda event: show_episodes(film_list.get(tk.ACTIVE)))

episode_list.bind("<<ListboxSelect>>", lambda event: play_video(episode_list.get(tk.ACTIVE).split(": ")[1]))

window.mainloop()
