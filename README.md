# 💍 Islamic Wedding Invitation — Streamlit

A personalized, mobile-friendly Islamic wedding invitation.

## Project structure

```text
wedding_invitation_streamlit/
├── app.py
├── wedding_invitation.html
├── requirements.txt
└── assets/
    └── wedding-music.mp3   # optional
```

## Customize

Open `wedding_invitation.html` and edit the `WEDDING` object near the bottom:

- bride
- groom
- countdownDate
- mainDate
- mainDetails
- Mehndi details
- Nikah details
- Walima details
- RSVP URL
- location URL
- calendar details

## Add music

Put your MP3 here:

```text
assets/wedding-music.mp3
```

No code change is needed. `app.py` embeds the MP3 into the invitation at runtime.

The guest must tap the music button; the site does not autoplay audio.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy

Upload the project to GitHub and deploy the repository on Streamlit Community Cloud.

Guests only need the public Streamlit URL. They do not need any project files.

## Important

The invitation asks for the guest's name first. Wedding content remains hidden until the guest submits a valid name.
