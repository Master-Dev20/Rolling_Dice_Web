# 🎲 Flask Dice Rolling Game  

A simple Flask-based web application that simulates rolling a dice. When the user clicks the **"Roll Dice"** button, a randomly generated number (1-6) determines the displayed dice image.  

## 📌 Features  
- Backend powered by **Flask**.  
- **JavaScript** dynamically updates the dice image.  
- **Responsive UI** built with HTML, CSS, and JavaScript.  
- Dice images change **in real time** based on the rolled number.  

## 📁 Project Structure  
```
📂 project-directory  
│-- 📂 static  
│   │-- 📂 Dice  
│   │   │-- Dice1.jpeg  
│   │   │-- Dice2.jpeg  
│   │   │-- Dice3.jpeg  
│   │   │-- Dice4.jpeg  
│   │   │-- Dice5.jpeg  
│   │   │-- Dice6.jpeg  
│   │-- style.css  
│   │-- script.js  
│-- 📂 templates  
│   │-- index.html  
│-- app.py  
│-- README.md  
```  

## 🚀 How to Run  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Master-Dev20/Rolling_Dice.git  
cd Rolling_Dice_Web 
```  
### 2️⃣ Install Dependencies  
```bash
pip install flask  
```  
### 3️⃣ Run the Flask App  
```bash
python app.py  
```  
### 4️⃣ Open in Browser  
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and start rolling the dice!  

## 🔧 How It Works  
- The backend (`app.py`) generates a **random number (1-6)** when the user clicks **"Roll Dice"**.  
- The corresponding dice image (**Dice1.jpeg** to **Dice6.jpeg**) is sent to the frontend.  
- JavaScript updates the image **dynamically** without refreshing the page.  

## 🎯 Future Enhancements  
✅ Add a dice rolling **animation**.  
✅ Improve the **UI design**.  
✅ Implement a **multiplayer mode**.  

**Happy coding! 🚀🎲**  
