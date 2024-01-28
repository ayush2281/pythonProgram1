import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.target_number = random.randint(1, 1000)
        self.guess_attempts = 0

        self.label = tk.Label(master, text="Enter your guess:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        user_guess = int(self.entry.get())
        self.guess_attempts += 1

        if user_guess == self.target_number:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.guess_attempts} attempts.")
            self.reset_game()
        elif user_guess < self.target_number:
            messagebox.showinfo("Incorrect", "Too low! Try again.")
        else:
            messagebox.showinfo("Incorrect", "Too high! Try again.")

    def reset_game(self):
        self.target_number = random.randint(1, 1000)
        self.guess_attempts = 0
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
