# 🚀 Jobstronaut™ Application System (v1)

Created by **Alise McNiel**
[https://jobstronaut.dev](https://jobstronaut.dev)

---

## 📄 Overview

The **Jobstronaut Application System v1** is a plug-and-play job application platform that:

* Hosts a clean, dark-mode HTML application form
* Accepts name, email, job interest, and resume upload
* Submits applications via Python backend
* Logs submissions to CSV
* Sends email notifications upon success or failure
* Displays a "Thank you" confirmation message on successful submit ✅

Great for job-seekers, freelance recruiters, or teams that want to automate resume intake.

---

## 🔧 How to Use

### 1. 🏠 Backend Setup

Run locally or host on Render.com

```
git clone https://github.com/yourusername/jobstronaut_v1.git
cd jobstronaut_v1
pip install -r requirements.txt
python3 server.py
```

Visit `http://localhost:5000` or your deployed URL.

### 2. 🔍 Preview Form (static view)

Open `templates/index.html` in browser or visit the deployed frontend at:
👉 [https://buildwithalise.github.io/jobstronaut-frontend/](https://buildwithalise.github.io/jobstronaut-frontend/)

Note: Some styles may take a moment to update due to GitHub Pages caching.

---

## 🗓 Submit Applications Automatically

Customize `autofill_profile.json`:

```json
{
  "name": "Alise McNiel",
  "email": "alise@example.com",
  "interest": "Frontend Developer"
}
```

Run submission script:

```bash
python3 submit_application.py
```

This will:

* Upload `resume.pdf`
* Log submission to `application_log.csv`
* Send email confirmation
* Display a thank you confirmation on frontend

---

## 📍 Deployment Tips

Use [Render](https://render.com) to deploy for free:

* Add your files
* Connect to `render.yaml`
* Redeploy on HTML/CSS changes

Or host the frontend on GitHub Pages for easy previewing.

---

## 🚪 Suggested Upgrades (v2 Roadmap)

* ✅ Show a "Thank you for applying!" popup on submission
* ✅ Add a landing page with a button to launch this form
* Embed the form in a personal portfolio or dashboard
* Publish to a custom domain (e.g., `apply.jobstronaut.dev`)
* Auto-fill & submit real job apps (Indeed, LinkedIn, etc.)

---

## 💼 License

MIT License (included in `LICENSE.txt`)
Feel free to remix, resell, and expand.

Credit appreciated: **Built with Jobstronaut™**

---

## 🌟 Created By

**Alise McNiel**
jobstronaut.dev
"I see your future… and it's bright." ✨

