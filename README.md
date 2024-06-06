# WrestleAI

## Repository Structure
```bash
├── .streamlit
│   ├── config.toml
│   ├── secrets.toml
├── assets
│   ├── terms
│   ├── images
│   │   ├── general
│   │   ├── logo
│   │   ├── umich
│   │   ├── qrcodes
│   ├── docs
│   │   ├── pdf
│   │   ├── text
│   │   ├── markdown
├── classes
│   ├── clsSessionState.py
│   ├── clsPageSetup.py
│   ├── cls
├── app
│   ├── userstate
│   │   ├── appUserState.py
│   │   ├── components
│   │   │   ├── appRender.py
│   │   │   ├── appInfo.py
│   │   │   ├── appPayment.py
│   │   │   ├── appLogin.py
│   │   │   ├── appWelcome.py
│   ├── homepage
│   │   ├── appHomePage.py
│   │   ├── components
│   │   │   ├── appAthlete.py
│   │   │   ├── appCoach.py
│   │   │   ├── appSupporter.py
│   ├── assistant
│   │   ├── appAssistant.py
│   │   ├── components
│   │   │   ├── appUserAssistant.py
│   │   │   ├── appGuestAssistant.py
│   │   │   ├── appAssistantPreWork.py
│   ├── account
│   │   ├── appAccount.py
│   │   ├── components
│   │   │   ├── appCreateAccount.py
│   │   │   ├── appLoginAccount.py
├── styles
│   ├── style.css
├── pages
│   ├── 1_Home.py
│   ├── 1_AI_Assistant.py
│   ├── 3_Video_Upload.py
│   ├── 4_Settings.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

```

## UserState

### Overview
- The UserState goes through **_five_** different states, which represents the **_new user path_** and is the most complex.
- Steps in the UserState **_may be skipped or bypassed_** for existing users. 
- The user is considered **_new_** until they have **_completed Payment_** step in which they are considered existing users to simplify the experience of returning from payment
- The following outlines the UserState flow:
    > **1. Render:** The initial view when the user comes to WrestleAI. They will be considered a **_guest_ usertype** at this point. They will have options to interact with the **_Guest Assistant_**, **_sign in as an existing user_**, or **_register as a new user_**. 

    >**2. Info:** Info refers to the new user information needed to create an account. Once this information is captured, the user will proceed to payment

    >**3. Payment:** The user will be required to submit payment, which navigates them out of the current app session via a stripe payment link button to another tab. Upon successful completion, the user will be redirected back to the app with information stored in query params

    >**4. Login:** At this step, all users are considered **_existing_** and will be asked to provide username and password to authenticate. This is the default step for existing users and users returning from payment

    >**5. Welcome:** Welcome is simply ensuring all attributes are captured in the session state and navigation to Home Page (pages/1_Home.py). The user will never be brought back to the original UserState screen again during their session.